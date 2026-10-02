/**
 * Snake — ICSD Edition
 *
 * Classic snake game on canvas. Eat food, grow longer, don't hit yourself.
 */

(function () {
    'use strict';

    const GAME_SLUG = 'snake';
    const GRID = 20;        // 20×20 grid
    const TICK_MS = 110;    // initial speed (lower = faster)

    let canvas, ctx, scoreEl, overlayEl;
    let snake, dir, nextDir, food, score, gameOver, tickInterval, tickMs, waiting = false;
    let cellSize;

    // ==========================================
    // Init
    // ==========================================
    function init() {
        canvas = document.querySelector('.game-snake-canvas');
        if (!canvas) return;

        ctx = canvas.getContext('2d');
        scoreEl = document.querySelector('[data-game-score="snake"]');
        overlayEl = document.querySelector('[data-game-overlay="snake"]');

        // محاسبهٔ ابتدایی ابعاد canvas (بدون صدا زدن draw)
        const setupCanvas = () => {
            const rect = canvas.getBoundingClientRect();
            const dpr = window.devicePixelRatio || 1;
            canvas.width  = rect.width * dpr;
            canvas.height = rect.height * dpr;
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            cellSize = rect.width / GRID;
        };
        setupCanvas();

        // resize handler ‌— فقط وقتی snake تعریف شده باشه draw کن
        window.addEventListener('resize', () => {
            setupCanvas();
            if (snake) draw();
        });

        // restart button
        const restartBtn = document.querySelector('[data-game-restart="snake"]');
        if (restartBtn) restartBtn.addEventListener('click', startNew);

        // controls
        document.addEventListener('keydown', handleKey);
        attachTouch(canvas);
        attachMobileButtons();

        startNew();
    }

    // ==========================================
    // New game
    // ==========================================
    function startNew() {
        snake = [{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }];
        dir = { x: 1, y: 0 };       // moving right initially
        nextDir = dir;
        score = 0;
        gameOver = false;
        tickMs = TICK_MS;
        placeFood();
        updateScore();
        draw();

        if (overlayEl) overlayEl.classList.remove('is-active');
        if (tickInterval) clearInterval(tickInterval);
        tickInterval = null;
        waiting = true;   // تا اولین حرکت بازیکن صبر کن
        drawHint();
    }

    function begin() {
        if (!waiting || gameOver) return;
        waiting = false;
        tickInterval = setInterval(tick, tickMs);
    }

    function drawHint() {
        const rect = canvas.getBoundingClientRect();
        ctx.fillStyle = 'rgba(0,0,0,.45)';
        const hy = rect.height * 0.22;
        ctx.fillRect(0, hy - 30, rect.width, 60);
        ctx.fillStyle = '#fff';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.direction = 'rtl';
        ctx.font = '700 15px Vazirmatn, Tahoma, sans-serif';
        ctx.fillText('برای شروع، کلید جهت‌دار را بزنید یا روی صفحه بکشید', rect.width / 2, hy);
    }

    // ==========================================
    // Place food
    // ==========================================
    function placeFood() {
        while (true) {
            food = {
                x: Math.floor(Math.random() * GRID),
                y: Math.floor(Math.random() * GRID),
            };
            if (!snake.some(s => s.x === food.x && s.y === food.y)) break;
        }
    }

    // ==========================================
    // Tick
    // ==========================================
    function tick() {
        if (gameOver) return;
        dir = nextDir;
        const head = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };

        // wall collision
        if (head.x < 0 || head.x >= GRID || head.y < 0 || head.y >= GRID) {
            return endGame();
        }
        // self collision
        if (snake.some(s => s.x === head.x && s.y === head.y)) {
            return endGame();
        }

        snake.unshift(head);

        // food?
        if (head.x === food.x && head.y === food.y) {
            score += 10;
            updateScore();
            placeFood();
            // speed up slightly every 50 points
            if (score % 50 === 0 && tickMs > 50) {
                tickMs -= 5;
                clearInterval(tickInterval);
                tickInterval = setInterval(tick, tickMs);
            }
        } else {
            snake.pop();
        }

        draw();
    }

    // ==========================================
    // Draw
    // ==========================================
    function draw() {
        const rect = canvas.getBoundingClientRect();
        ctx.fillStyle = getComputedStyle(canvas).backgroundColor;
        ctx.fillRect(0, 0, rect.width, rect.height);

        // food (red apple)
        const fx = food.x * cellSize, fy = food.y * cellSize;
        ctx.fillStyle = '#E74C3C';
        ctx.beginPath();
        ctx.arc(fx + cellSize/2, fy + cellSize/2, cellSize/2 - 2, 0, Math.PI * 2);
        ctx.fill();

        // snake
        const color = getComputedStyle(document.documentElement).getPropertyValue('--icsd-primary').trim() || '#2CA180';
        snake.forEach((seg, i) => {
            const opacity = i === 0 ? 1 : Math.max(0.3, 1 - i * 0.04);
            ctx.fillStyle = color;
            ctx.globalAlpha = opacity;
            const x = seg.x * cellSize, y = seg.y * cellSize;
            const radius = i === 0 ? 4 : 3;
            roundRect(ctx, x + 1, y + 1, cellSize - 2, cellSize - 2, radius);
            ctx.fill();
        });
        ctx.globalAlpha = 1;
    }

    function roundRect(ctx, x, y, w, h, r) {
        ctx.beginPath();
        ctx.moveTo(x + r, y);
        ctx.lineTo(x + w - r, y);
        ctx.quadraticCurveTo(x + w, y, x + w, y + r);
        ctx.lineTo(x + w, y + h - r);
        ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
        ctx.lineTo(x + r, y + h);
        ctx.quadraticCurveTo(x, y + h, x, y + h - r);
        ctx.lineTo(x, y + r);
        ctx.quadraticCurveTo(x, y, x + r, y);
    }

    // ==========================================
    // Score
    // ==========================================
    function updateScore() {
        if (scoreEl) scoreEl.textContent = ICSDGames.faNum(score);
    }

    // ==========================================
    // End game
    // ==========================================
    function endGame() {
        gameOver = true;
        if (tickInterval) clearInterval(tickInterval);

        ICSDGames.showGameOverModal({
            overlayEl: overlayEl,
            score: score,
            gameSlug: GAME_SLUG,
            isWin: false,
            onRestart: startNew,
        });
    }

    // ==========================================
    // Direction setter (prevent 180° turn)
    // ==========================================
    function setDir(dx, dy) {
        if (waiting) { dir = { x: dx, y: dy }; nextDir = dir; begin(); return; }
        // can't reverse
        if (dx === -dir.x && dy === -dir.y) return;
        nextDir = { x: dx, y: dy };
        begin();
    }

    // ==========================================
    // Keyboard (RTL: visually right arrow → right on screen, but movement is in board coords)
    // ==========================================
    function handleKey(e) {
        if (e.target.tagName === 'INPUT') return;
        switch (e.key) {
            case 'ArrowUp':    case 'w': case 'W': setDir(0, -1); e.preventDefault(); break;
            case 'ArrowDown':  case 's': case 'S': setDir(0,  1); e.preventDefault(); break;
            case 'ArrowLeft':  case 'a': case 'A': setDir(-1, 0); e.preventDefault(); break;
            case 'ArrowRight': case 'd': case 'D': setDir(1,  0); e.preventDefault(); break;
        }
    }

    // ==========================================
    // Touch swipe
    // ==========================================
    function attachTouch(el) {
        let sx = 0, sy = 0, st = 0;
        const MIN = 20;

        el.addEventListener('touchstart', e => {
            const t = e.changedTouches[0];
            sx = t.screenX; sy = t.screenY; st = Date.now();
            e.preventDefault();
        }, { passive: false });

        el.addEventListener('touchend', e => {
            const t = e.changedTouches[0];
            const dx = t.screenX - sx, dy = t.screenY - sy;
            if (Date.now() - st > 600) return;
            if (Math.abs(dx) < MIN && Math.abs(dy) < MIN) return;

            if (Math.abs(dx) > Math.abs(dy)) {
                setDir(dx > 0 ? 1 : -1, 0);
            } else {
                setDir(0, dy > 0 ? 1 : -1);
            }
            e.preventDefault();
        }, { passive: false });
    }

    // ==========================================
    // Mobile touch buttons
    // ==========================================
    function attachMobileButtons() {
        const map = {
            'ctrl-up':    [0, -1],
            'ctrl-down':  [0,  1],
            'ctrl-left':  [-1, 0],
            'ctrl-right': [ 1, 0],
        };
        Object.entries(map).forEach(([cls, [dx, dy]]) => {
            const btn = document.querySelector('.game-snake-mobile-controls .' + cls);
            if (btn) btn.addEventListener('click', () => setDir(dx, dy));
        });
    }

    // ==========================================
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
