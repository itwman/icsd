/**
 * Wordle فارسی — حدس کلمه
 *
 * 6 chances to guess a 5-letter Persian word.
 * Score = remaining attempts × 100 + speed bonus
 */

(function () {
    'use strict';

    const GAME_SLUG = 'wordle-fa';
    const WORD_LEN = 5;
    const MAX_TRIES = 6;

    // فهرست کلمات از پنل مدیریت (بازی‌ها ← حدس کلمات ← فهرست کلمات) می‌آید
    const SRC = (window.icsdGames && Array.isArray(window.icsdGames.words)) ? window.icsdGames.words : [];
    const FALLBACK_WORDS = ['ایران', 'ستاره', 'فرهنگ', 'سلامت', 'تاریخ', 'ریاضی', 'سفارش', 'محصول', 'گزارش', 'تحلیل'];
    const CLEAN = SRC.map(w => String(w).trim().replace(/ي/g, 'ی').replace(/ك/g, 'ک').replace(/[آأإ]/g, 'ا'))
                     .filter(w => w.length === WORD_LEN && !/[\u200c\s]/.test(w));
    const POOL = CLEAN.length >= 3 ? CLEAN : FALLBACK_WORDS;

    let target = '';
    let currentRow = 0;
    let currentCol = 0;
    let guesses = [];      // array of strings
    let gameOver = false;
    let startTime = 0;

    let boardEl, keyboardEl, messageEl, scoreEl, overlayEl;

    // ==========================================
    // حروف الفبای فارسی برای کیبورد
    // ==========================================
    const KEYBOARD_LAYOUT = [
        ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ'],
        ['ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ'],
        ['ENTER', 'ظ', 'ط', 'ژ', 'ز', 'ر', 'ذ', 'د', 'پ', 'و', 'BACK'],
    ];

    // نرمال‌سازی حروف فارسی (مثلاً ي به ی، ك به ک)
    function normalize(ch) {
        return ch
            .replace(/ي/g, 'ی')
            .replace(/ك/g, 'ک')
            .replace(/أ/g, 'ا').replace(/إ/g, 'ا').replace(/آ/g, 'ا');
    }

    // ==========================================
    // Init
    // ==========================================
    function init() {
        boardEl    = document.querySelector('.game-wordle-board');
        keyboardEl = document.querySelector('.game-wordle-keyboard');
        messageEl  = document.querySelector('.game-wordle-message');
        scoreEl    = document.querySelector('[data-game-score="wordle-fa"]');
        overlayEl  = document.querySelector('[data-game-overlay="wordle-fa"]');

        if (!boardEl || !keyboardEl) return;

        buildBoard();
        buildKeyboard();

        document.addEventListener('keydown', handleKey);

        const restartBtn = document.querySelector('[data-game-restart="wordle-fa"]');
        if (restartBtn) restartBtn.addEventListener('click', startNew);

        startNew();
    }

    function buildBoard() {
        boardEl.innerHTML = '';
        for (let r = 0; r < MAX_TRIES; r++) {
            const row = document.createElement('div');
            row.className = 'game-wordle-row';
            row.dataset.row = r;
            for (let c = 0; c < WORD_LEN; c++) {
                const cell = document.createElement('div');
                cell.className = 'game-wordle-cell';
                cell.dataset.col = c;
                row.appendChild(cell);
            }
            boardEl.appendChild(row);
        }
    }

    function buildKeyboard() {
        keyboardEl.innerHTML = '';
        KEYBOARD_LAYOUT.forEach(row => {
            const rowEl = document.createElement('div');
            rowEl.className = 'game-wordle-keyboard-row';
            row.forEach(key => {
                const btn = document.createElement('button');
                btn.className = 'game-wordle-key';
                btn.dataset.key = key;
                if (key === 'ENTER') {
                    btn.textContent = 'تأیید';
                    btn.classList.add('wide');
                } else if (key === 'BACK') {
                    btn.textContent = '⌫';
                    btn.classList.add('wide');
                } else {
                    btn.textContent = key;
                }
                btn.addEventListener('click', () => onKey(key));
                rowEl.appendChild(btn);
            });
            keyboardEl.appendChild(rowEl);
        });
    }

    // ==========================================
    // Start new game
    // ==========================================
    function startNew() {
        target = POOL[Math.floor(Math.random() * POOL.length)];
        currentRow = 0;
        currentCol = 0;
        guesses = [];
        gameOver = false;
        startTime = Date.now();

        // reset board UI
        boardEl.querySelectorAll('.game-wordle-cell').forEach(cell => {
            cell.textContent = '';
            cell.className = 'game-wordle-cell';
        });
        boardEl.querySelectorAll('.game-wordle-row').forEach(row => row.classList.remove('is-revealing'));

        // reset keyboard
        keyboardEl.querySelectorAll('.game-wordle-key').forEach(k => {
            k.classList.remove('correct', 'present', 'absent');
        });

        showMessage('');
        if (scoreEl) scoreEl.textContent = '۰';
        if (overlayEl) overlayEl.classList.remove('is-active');
    }

    // ==========================================
    // Handle key (from keyboard or touch)
    // ==========================================
    function onKey(key) {
        if (gameOver) return;

        if (key === 'ENTER') return submitGuess();
        if (key === 'BACK')  return removeChar();
        if (key.length === 1) return addChar(key);
    }

    function handleKey(e) {
        if (e.target.tagName === 'INPUT') return;
        if (e.key === 'Enter')      return onKey('ENTER');
        if (e.key === 'Backspace')  return onKey('BACK');

        // فقط حروف فارسی
        const ch = normalize(e.key);
        if (/[\u0600-\u06FF]/.test(ch) && ch.length === 1) {
            onKey(ch);
        }
    }

    function addChar(ch) {
        if (currentCol >= WORD_LEN) return;
        const row = boardEl.querySelector(`[data-row="${currentRow}"]`);
        const cell = row.querySelector(`[data-col="${currentCol}"]`);
        cell.textContent = ch;
        cell.classList.add('filled');
        currentCol++;
    }

    function removeChar() {
        if (currentCol === 0) return;
        currentCol--;
        const row = boardEl.querySelector(`[data-row="${currentRow}"]`);
        const cell = row.querySelector(`[data-col="${currentCol}"]`);
        cell.textContent = '';
        cell.classList.remove('filled');
    }

    // ==========================================
    // Submit guess
    // ==========================================
    function submitGuess() {
        if (currentCol < WORD_LEN) {
            showMessage('کلمه باید ۵ حرف باشد', true);
            return;
        }

        const row = boardEl.querySelector(`[data-row="${currentRow}"]`);
        const cells = row.querySelectorAll('.game-wordle-cell');
        const guess = Array.from(cells).map(c => c.textContent).join('');

        // Reveal animation
        row.classList.add('is-revealing');

        // Compute results
        const results = computeResults(guess, target);
        cells.forEach((cell, i) => {
            setTimeout(() => {
                cell.classList.add(results[i]);
                updateKeyboardKey(guess[i], results[i]);
            }, i * 150 + 250);
        });

        currentRow++;
        currentCol = 0;

        // Check win/lose
        setTimeout(() => {
            if (guess === target) {
                gameOver = true;
                const remaining = MAX_TRIES - (currentRow - 1);
                const elapsed = Math.round((Date.now() - startTime) / 1000);
                const speedBonus = Math.max(0, 200 - elapsed);
                const score = remaining * 100 + speedBonus;
                if (scoreEl) scoreEl.textContent = ICSDGames.faNum(score);

                setTimeout(() => endGame(true, score), 600);
            } else if (currentRow >= MAX_TRIES) {
                gameOver = true;
                showMessage(`کلمه: ${target}`, false);
                setTimeout(() => endGame(false, 0), 1200);
            }
        }, WORD_LEN * 150 + 400);
    }

    // ==========================================
    // Compute results: each cell is 'correct' / 'present' / 'absent'
    // ==========================================
    function computeResults(guess, target) {
        const results = new Array(WORD_LEN).fill('absent');
        const targetChars = target.split('');
        const guessChars = guess.split('');

        // Pass 1: correct (exact match)
        for (let i = 0; i < WORD_LEN; i++) {
            if (guessChars[i] === targetChars[i]) {
                results[i] = 'correct';
                targetChars[i] = null;
            }
        }
        // Pass 2: present (in word but wrong position)
        for (let i = 0; i < WORD_LEN; i++) {
            if (results[i] === 'correct') continue;
            const idx = targetChars.indexOf(guessChars[i]);
            if (idx !== -1) {
                results[i] = 'present';
                targetChars[idx] = null;
            }
        }
        return results;
    }

    function updateKeyboardKey(ch, state) {
        const key = keyboardEl.querySelector(`[data-key="${ch}"]`);
        if (!key) return;
        // Don't downgrade: correct > present > absent
        if (key.classList.contains('correct')) return;
        if (key.classList.contains('present') && state === 'absent') return;
        key.classList.remove('correct', 'present', 'absent');
        key.classList.add(state);
    }

    function showMessage(text, isError) {
        if (!messageEl) return;
        messageEl.textContent = text;
        messageEl.classList.toggle('error', !!isError);
    }

    // ==========================================
    // End game
    // ==========================================
    function endGame(isWin, finalScore) {
        ICSDGames.showGameOverModal({
            overlayEl: overlayEl,
            score: finalScore,
            gameSlug: GAME_SLUG,
            isWin: isWin,
            onRestart: startNew,
        });
    }

    // ==========================================
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
