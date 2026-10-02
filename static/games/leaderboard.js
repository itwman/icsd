/**
 * ICSD Games — Leaderboard & Score Submission
 *
 * Shared utility functions for all games.
 * Provides:
 * - submitScore(gameSlug, playerName, score) → Promise
 * - getLeaderboard(gameSlug, limit) → Promise
 * - getPersonalBest(gameSlug) / setPersonalBest(gameSlug, score) → localStorage
 * - showGameOverModal(opts) → handles UX of submitting score after game over
 * - faNum(n) → Persian numerals
 */

(function () {
    'use strict';

    const ICSDGames = {

        // ==========================================
        // Persian numerals helper
        // ==========================================
        faNum: function (n) {
            const map = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
            return String(n).replace(/[0-9]/g, d => map[d]);
        },

        // ==========================================
        // localStorage: Personal Best
        // ==========================================
        getPersonalBest: function (gameSlug) {
            try {
                const v = localStorage.getItem('icsd_pb_' + gameSlug);
                return v ? parseInt(v, 10) : 0;
            } catch (e) { return 0; }
        },

        setPersonalBest: function (gameSlug, score) {
            try {
                const current = this.getPersonalBest(gameSlug);
                if (score > current) {
                    localStorage.setItem('icsd_pb_' + gameSlug, String(score));
                    return true; // new best!
                }
                return false;
            } catch (e) { return false; }
        },

        getPlayerName: function () {
            try {
                return localStorage.getItem('icsd_player_name') || '';
            } catch (e) { return ''; }
        },

        setPlayerName: function (name) {
            try {
                localStorage.setItem('icsd_player_name', name);
            } catch (e) { /* ignore */ }
        },

        // ==========================================
        // AJAX: Submit score
        // ==========================================
        submitScore: function (gameSlug, playerName, score) {
            const cfg = window.icsdGames || {};
            return fetch(cfg.submitUrl, {
                method: 'POST', credentials: 'same-origin',
                headers: { 'Content-Type': 'application/json', 'X-CSRFToken': cfg.csrf || '' },
                body: JSON.stringify({ player_name: playerName, score: score })
            }).then(r => r.json().then(d => { if (!r.ok) throw new Error(d.message || 'خطا'); return d; }));
        },

        getLeaderboard: function (gameSlug, limit) {
            const cfg = window.icsdGames || {};
            if (!cfg.boardUrl) return Promise.resolve([]);
            return fetch(cfg.boardUrl, { credentials: 'same-origin' })
                .then(r => r.json()).then(d => d.leaderboard || []).catch(() => []);
        },

        // ==========================================
        // Render leaderboard into a UL
        // ==========================================
        renderLeaderboard: function (listEl, items) {
            if (!listEl) return;
            if (!items || items.length === 0) {
                listEl.innerHTML = '<li class="icsd-leaderboard-empty">هنوز رکوردی ثبت نشده — اولین نفر باش!</li>';
                return;
            }
            const html = items.map((item, i) => {
                const rank = i + 1;
                const escapedName = String(item.player_name).replace(/[<>&"]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]));
                return `<li>
                    <span class="rank">${this.faNum(rank)}</span>
                    <span class="player">${escapedName}</span>
                    <span class="score">${this.faNum(item.score)}</span>
                </li>`;
            }).join('');
            listEl.innerHTML = html;
        },

        // ==========================================
        // Render personal best card
        // ==========================================
        renderPersonalBest: function (cardEl, gameSlug) {
            if (!cardEl) return;
            const pb = this.getPersonalBest(gameSlug);
            const valueEl = cardEl.querySelector('.pb-value');
            if (valueEl) valueEl.textContent = this.faNum(pb);
        },

        // ==========================================
        // Show game over modal with submit option
        // ==========================================
        showGameOverModal: function (opts) {
            // opts: { overlayEl, score, gameSlug, onRestart, isWin }
            const overlay = opts.overlayEl;
            if (!overlay) return;

            const isNewBest = this.setPersonalBest(opts.gameSlug, opts.score);
            const savedName = this.getPlayerName();

            overlay.innerHTML = `
                <div class="icsd-game-overlay-content">
                    <h2>${opts.isWin ? '🎉 برد!' : 'پایان بازی'}</h2>
                    <div class="final-score">${this.faNum(opts.score)}</div>
                    ${isNewBest ? '<div class="rank-info">🏆 <strong>رکورد شخصی جدید!</strong></div>' : ''}
                    ${opts.score > 0 ? `
                        <input type="text" class="player-name-input" placeholder="نام مستعار خود را وارد کنید"
                               value="${String(savedName).replace(/[<>&"]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]))}" maxlength="30" />
                        <div class="actions">
                            <button class="icsd-game-btn primary submit-score-btn">🏆 ثبت در لیدربورد</button>
                            <button class="icsd-game-btn restart-btn">🔄 شروع مجدد</button>
                        </div>
                        <button class="icsd-skip-submit">رد کردن و شروع مجدد</button>
                    ` : `
                        <div class="actions">
                            <button class="icsd-game-btn primary restart-btn">🔄 شروع مجدد</button>
                        </div>
                    `}
                </div>
            `;
            overlay.classList.add('is-active');

            const nameInput = overlay.querySelector('.player-name-input');
            const submitBtn = overlay.querySelector('.submit-score-btn');
            const restartBtns = overlay.querySelectorAll('.restart-btn, .icsd-skip-submit');

            if (submitBtn && nameInput) {
                submitBtn.addEventListener('click', () => {
                    const name = nameInput.value.trim();
                    if (!name) {
                        nameInput.focus();
                        return;
                    }
                    this.setPlayerName(name);
                    submitBtn.disabled = true;
                    submitBtn.textContent = 'در حال ثبت...';

                    this.submitScore(opts.gameSlug, name, opts.score)
                        .then(data => {
                            submitBtn.textContent = `✓ رتبه ${this.faNum(data.rank)}`;
                            // Update leaderboard list if visible
                            const lbList = document.querySelector('.icsd-leaderboard-list[data-game="' + opts.gameSlug + '"]');
                            if (lbList) this.renderLeaderboard(lbList, data.leaderboard);

                            setTimeout(() => {
                                overlay.classList.remove('is-active');
                                if (typeof opts.onRestart === 'function') opts.onRestart();
                            }, 1800);
                        })
                        .catch(err => {
                            submitBtn.textContent = '❌ ' + (err.message || 'خطا');
                            submitBtn.disabled = false;
                        });
                });

                nameInput.addEventListener('keydown', e => {
                    if (e.key === 'Enter') submitBtn.click();
                });
            }

            restartBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    overlay.classList.remove('is-active');
                    if (typeof opts.onRestart === 'function') opts.onRestart();
                });
            });
        },

        // ==========================================
        // Init: load leaderboard on page load
        // ==========================================
        initLeaderboards: function () {
            document.querySelectorAll('.icsd-leaderboard-list[data-game]').forEach(listEl => {
                const gameSlug = listEl.dataset.game;
                this.getLeaderboard(gameSlug, 10).then(items => {
                    this.renderLeaderboard(listEl, items);
                });
            });

            document.querySelectorAll('.icsd-personal-best[data-game]').forEach(cardEl => {
                const gameSlug = cardEl.dataset.game;
                this.renderPersonalBest(cardEl, gameSlug);
            });
        }
    };

    // Expose globally for game scripts
    window.ICSDGames = ICSDGames;

    // Auto-init on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => ICSDGames.initLeaderboards());
    } else {
        ICSDGames.initLeaderboards();
    }
})();
