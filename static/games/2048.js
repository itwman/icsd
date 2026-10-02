/**
 * 2048 — ICSD Edition
 *
 * Classic 4×4 sliding tile puzzle game.
 * Features: keyboard + touch controls, smooth animations, persistent best score,
 * leaderboard integration via ICSDGames.
 */

(function () {
    'use strict';

    const GAME_SLUG = '2048';
    const SIZE = 4;
    const GAP = 10; // px - matches CSS

    let board = [];        // 2D array, 0 = empty, else tile id
    let score = 0;
    let won = false;
    let gameOver = false;
    let nextTileId = 1;
    let tileRegistry = {}; // {id: {value, row, col, el, isNew, isMerged}}

    let boardEl, gridEl, tilesEl, scoreEl, overlayEl;
    let cellSize = 0;       // pixel size of one cell (computed)

    // ==========================================
    // Init
    // ==========================================
    function init() {
        boardEl = document.querySelector('.game-2048-board');
        if (!boardEl) return;

        gridEl   = boardEl.querySelector('.game-2048-grid');
        tilesEl  = boardEl.querySelector('.game-2048-tiles');
        scoreEl  = document.querySelector('[data-game-score="2048"]');
        overlayEl = document.querySelector('[data-game-overlay="2048"]');

        // build empty grid cells (visible background)
        gridEl.innerHTML = '';
        for (let i = 0; i < SIZE * SIZE; i++) {
            const cell = document.createElement('div');
            cell.className = 'game-2048-cell';
            gridEl.appendChild(cell);
        }

        // محاسبه‌ی اولیه‌ی اندازه‌ی سلول
        computeCellSize();

        // resize handler
        window.addEventListener('resize', () => {
            computeCellSize();
            renderTiles();
        });

        // restart button
        const restartBtn = document.querySelector('[data-game-restart="2048"]');
        if (restartBtn) restartBtn.addEventListener('click', startNew);

        // controls
        document.addEventListener('keydown', handleKey);
        attachTouch(boardEl);

        startNew();
    }

    /**
     * محاسبه‌ی اندازه‌ی هر سلول بر اساس عرض فعلی tilesEl
     * (tilesEl همون منطقه‌ی داخلی board هست با inset برابر GAP)
     */
    function computeCellSize() {
        if (!tilesEl) return;
        const rect = tilesEl.getBoundingClientRect();
        // tilesEl حاوی SIZE سلول + (SIZE-1) gap هست
        cellSize = (rect.width - (SIZE - 1) * GAP) / SIZE;
    }

    // ==========================================
    // New game
    // ==========================================
    function startNew() {
        board = Array.from({ length: SIZE }, () => Array(SIZE).fill(0));
        tileRegistry = {};
        nextTileId = 1;
        score = 0;
        won = false;
        gameOver = false;
        tilesEl.innerHTML = '';
        addRandomTile();
        addRandomTile();
        computeCellSize();
        renderTiles();
        updateScore();
        if (overlayEl) overlayEl.classList.remove('is-active');
    }

    // ==========================================
    // Random tile
    // ==========================================
    function addRandomTile() {
        const empty = [];
        for (let r = 0; r < SIZE; r++) {
            for (let c = 0; c < SIZE; c++) {
                if (board[r][c] === 0) empty.push([r, c]);
            }
        }
        if (empty.length === 0) return null;

        const [r, c] = empty[Math.floor(Math.random() * empty.length)];
        const value = Math.random() < 0.9 ? 2 : 4;
        const id = nextTileId++;

        board[r][c] = id;
        tileRegistry[id] = { id, value, row: r, col: c, isNew: true, isMerged: false, el: null };
        return id;
    }

    // ==========================================
    // Render tiles (positioned absolutely in pixels)
    //
    // RTL: column 0 is RIGHTMOST visually
    // x position from RIGHT edge = col * (cellSize + GAP)
    // Since tilesEl has direction:rtl is NOT set, we use 'right' instead of 'left'
    // ==========================================
    function renderTiles() {
        if (cellSize === 0) computeCellSize();

        // remove tiles no longer in registry
        Array.from(tilesEl.children).forEach(el => {
            const id = parseInt(el.dataset.id, 10);
            if (!tileRegistry[id]) el.remove();
        });

        Object.values(tileRegistry).forEach(tile => {
            let el = tile.el;
            if (!el) {
                el = document.createElement('div');
                el.className = 'game-2048-tile';
                el.dataset.id = tile.id;
                el.style.position = 'absolute';
                el.style.top = '0';
                el.style.right = '0'; // anchor to right (RTL)
                tilesEl.appendChild(el);
                tile.el = el;
            }

            // اندازه دقیق در پیکسل
            el.style.width  = cellSize + 'px';
            el.style.height = cellSize + 'px';

            // RTL: col 0 = rightmost
            const xRight = tile.col * (cellSize + GAP);  // distance from right
            const yTop   = tile.row * (cellSize + GAP);  // distance from top

            el.style.transform = `translate(${-xRight}px, ${yTop}px)`;
            // نکته: چون anchor right هست و translate به سمت چپ منفیه،
            // 'right: 0' + 'translateX(-xRight)' یعنی تایل به اندازه xRight به چپ از لبه راست رفته.
            // در RTL این یعنی col 0 درست در لبه راست می‌ایسته.

            el.dataset.value = tile.value;
            el.textContent = ICSDGames.faNum(tile.value);

            el.classList.toggle('is-new', tile.isNew);
            el.classList.toggle('is-merged', tile.isMerged);
        });

        // clear flags after render
        requestAnimationFrame(() => {
            Object.values(tileRegistry).forEach(t => {
                t.isNew = false;
                t.isMerged = false;
                if (t.el) {
                    t.el.classList.remove('is-new', 'is-merged');
                }
            });
        });
    }

    // ==========================================
    // Update score display
    // ==========================================
    function updateScore() {
        if (scoreEl) scoreEl.textContent = ICSDGames.faNum(score);
    }

    // ==========================================
    // Move tiles in direction
    //
    // در سیستم گرید داخلی ما:
    //   col 0 = راست‌ترین (RTL)
    //   col SIZE-1 = چپ‌ترین
    //
    // کاربر کلید جهت‌نما رو فشار می‌ده — می‌بینه:
    //   ArrowRight = می‌خواد تایل‌ها به سمت راست بصری برن = به سمت col 0 (decrease col)
    //   ArrowLeft = به سمت چپ بصری = به سمت col SIZE-1 (increase col)
    //   ArrowUp = به بالا = به سمت row 0 (decrease row)
    //   ArrowDown = به پایین = به سمت row SIZE-1 (increase row)
    // ==========================================
    function move(dir) {
        if (gameOver) return;

        let moved = false;
        const merged = {};

        const traversals = getTraversals(dir);

        traversals.rows.forEach(r => {
            traversals.cols.forEach(c => {
                const id = board[r][c];
                if (!id) return;

                const { newR, newC, mergeId } = findFarthestPosition(r, c, dir, merged);

                if (mergeId) {
                    const tile = tileRegistry[id];
                    const mergeTile = tileRegistry[mergeId];
                    const newValue = tile.value * 2;

                    board[r][c] = 0;
                    delete tileRegistry[id];
                    if (tile.el) tile.el.remove();

                    mergeTile.value = newValue;
                    mergeTile.isMerged = true;
                    merged[mergeTile.id] = true;

                    score += newValue;
                    if (newValue === 2048 && !won) won = true;
                    moved = true;
                } else if (newR !== r || newC !== c) {
                    board[r][c] = 0;
                    board[newR][newC] = id;
                    tileRegistry[id].row = newR;
                    tileRegistry[id].col = newC;
                    moved = true;
                }
            });
        });

        if (moved) {
            addRandomTile();
            renderTiles();
            updateScore();

            if (!hasValidMoves()) {
                gameOver = true;
                setTimeout(() => endGame(false), 300);
            } else if (won === true) {
                won = 'celebrated';
                setTimeout(() => endGame(true), 300);
            }
        }
    }

    function getTraversals(dir) {
        const rows = [], cols = [];
        for (let i = 0; i < SIZE; i++) { rows.push(i); cols.push(i); }

        // باید تایل‌های نزدیک‌تر به مقصد رو اول پردازش کنیم
        // dir='down' = به سمت row SIZE-1 → از row بالا شروع کن (پیش‌فرض)، نه از row پایین
        // در واقع: تایل پایینی باید اول حرکت کنه چون فضای جلوش بازه
        // پس برای 'down' باید rows رو معکوس کنیم (شروع از SIZE-1)
        if (dir === 'down')  rows.reverse();
        if (dir === 'left')  cols.reverse(); // dir=left: cols increase, شروع از col SIZE-1

        return { rows, cols };
    }

    function findFarthestPosition(r, c, dir, merged) {
        // dr/dc: تغییر هر گام
        const dr = (dir === 'up')   ? -1 : (dir === 'down'  ? 1 : 0);
        const dc = (dir === 'right')? -1 : (dir === 'left'  ? 1 : 0);
        // dir='right' (بصری راست) = به سمت col 0 = decrease col

        let curR = r, curC = c;
        const sourceId = board[r][c];
        const sourceValue = tileRegistry[sourceId].value;

        while (true) {
            const nextR = curR + dr;
            const nextC = curC + dc;
            if (nextR < 0 || nextR >= SIZE || nextC < 0 || nextC >= SIZE) break;
            const targetId = board[nextR][nextC];
            if (!targetId) {
                curR = nextR;
                curC = nextC;
                continue;
            }
            // can merge?
            if (tileRegistry[targetId].value === sourceValue && !merged[targetId]) {
                return { newR: nextR, newC: nextC, mergeId: targetId };
            }
            break;
        }

        return { newR: curR, newC: curC, mergeId: null };
    }

    function hasValidMoves() {
        for (let r = 0; r < SIZE; r++) {
            for (let c = 0; c < SIZE; c++) {
                if (board[r][c] === 0) return true;
            }
        }
        for (let r = 0; r < SIZE; r++) {
            for (let c = 0; c < SIZE; c++) {
                const v = tileRegistry[board[r][c]].value;
                if (c < SIZE - 1 && tileRegistry[board[r][c + 1]].value === v) return true;
                if (r < SIZE - 1 && tileRegistry[board[r + 1][c]].value === v) return true;
            }
        }
        return false;
    }

    // ==========================================
    // End game / show modal
    // ==========================================
    function endGame(isWin) {
        ICSDGames.showGameOverModal({
            overlayEl: overlayEl,
            score: score,
            gameSlug: GAME_SLUG,
            isWin: isWin,
            onRestart: startNew,
        });
    }

    // ==========================================
    // Keyboard
    // ==========================================
    function handleKey(e) {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        if (!boardEl) return;

        const map = {
            'ArrowUp':    'up',
            'ArrowDown':  'down',
            'ArrowLeft':  'left',
            'ArrowRight': 'right',
            'w': 'up', 'W': 'up',
            's': 'down', 'S': 'down',
            'a': 'left', 'A': 'left',
            'd': 'right', 'D': 'right',
        };
        const dir = map[e.key];
        if (dir) {
            e.preventDefault();
            move(dir);
        }
    }

    // ==========================================
    // Touch / swipe
    // ==========================================
    function attachTouch(el) {
        let startX = 0, startY = 0, startT = 0;
        const MIN_SWIPE = 30;

        el.addEventListener('touchstart', e => {
            const t = e.changedTouches[0];
            startX = t.screenX;
            startY = t.screenY;
            startT = Date.now();
        }, { passive: true });

        el.addEventListener('touchend', e => {
            const t = e.changedTouches[0];
            const dx = t.screenX - startX;
            const dy = t.screenY - startY;
            const dt = Date.now() - startT;
            if (dt > 1000) return;

            if (Math.abs(dx) < MIN_SWIPE && Math.abs(dy) < MIN_SWIPE) return;

            if (Math.abs(dx) > Math.abs(dy)) {
                move(dx > 0 ? 'right' : 'left');
            } else {
                move(dy > 0 ? 'down' : 'up');
            }
        }, { passive: true });
    }

    // ==========================================
    // DOM ready
    // ==========================================
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
