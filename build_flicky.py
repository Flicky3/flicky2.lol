import json

with open(r'C:\Users\Flick\Downloads\vault\embedded_accounts.js', 'r', encoding='utf-8') as f:
    acc_js = f.read()

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FLICKY // VAULT</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    :root {
      --bg-body: #0a0a0c;
      --bg-surface: #121216;
      --bg-card: #17171d;
      --bg-card-hover: #1f1f27;
      --bg-bubble: #22222c;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-light: rgba(255, 255, 255, 0.16);
      --border-hover: rgba(255, 255, 255, 0.35);
      --text-main: #ffffff;
      --text-muted: #8e8e9f;
      --text-soft: #b5b5c4;
      --accent-white: #ffffff;
      --accent-pill: #2b2b36;
      --shadow-bubble: 0 10px 30px -10px rgba(0, 0, 0, 0.7), 0 4px 12px rgba(0, 0, 0, 0.5);
      --shadow-lift: 0 18px 40px -10px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(255, 255, 255, 0.18);
      --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --radius-pill: 9999px;
      --radius-bubble: 28px;
      --radius-bubble-sm: 20px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body {
      background-color: var(--bg-body);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }

    .bg-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .ambient-bubble {
      position: absolute;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, rgba(255, 255, 255, 0.04) 0%, rgba(255, 255, 255, 0.01) 60%, transparent 100%);
      border: 1px solid rgba(255, 255, 255, 0.04);
      filter: blur(1px);
      animation: floatBubble 22s infinite ease-in-out;
    }

    .bubble-1 { width: 550px; height: 550px; top: -100px; right: -50px; animation-duration: 26s; }
    .bubble-2 { width: 420px; height: 420px; bottom: 5%; left: -80px; animation-duration: 20s; animation-delay: -5s; }
    .bubble-3 { width: 300px; height: 300px; top: 40%; right: 15%; animation-duration: 18s; animation-delay: -10s; }

    @keyframes floatBubble {
      0%, 100% { transform: translateY(0) scale(1); }
      50% { transform: translateY(-30px) scale(1.04); }
    }

    .layout-wrapper {
      position: relative;
      z-index: 1;
      max-width: 1320px;
      margin: 0 auto;
      padding: 32px 24px 80px;
    }

    .bubble-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 12px 24px;
      background: rgba(23, 23, 29, 0.75);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      box-shadow: var(--shadow-bubble);
      margin-bottom: 40px;
    }

    .brand-cluster {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--text-main);
    }

    .brand-icon-bubble {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: #ffffff;
      color: #000000;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      font-weight: 800;
      box-shadow: 0 4px 14px rgba(255, 255, 255, 0.25);
    }

    .brand-title {
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }

    .brand-tag {
      font-size: 0.72rem;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      background: var(--accent-pill);
      color: var(--text-soft);
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .bubble-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 9px;
      padding: 10px 22px;
      border-radius: var(--radius-pill);
      font-size: 0.88rem;
      font-weight: 600;
      font-family: var(--font-body);
      text-decoration: none;
      cursor: pointer;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      border: 1px solid var(--border-subtle);
      background: var(--bg-card);
      color: var(--text-main);
    }

    .bubble-btn:hover {
      background: var(--bg-card-hover);
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }

    .bubble-btn-primary {
      background: #ffffff;
      color: #000000;
      border-color: #ffffff;
      box-shadow: 0 4px 16px rgba(255, 255, 255, 0.2);
    }

    .bubble-btn-primary:hover {
      background: #e8e8ed;
      color: #000000;
      box-shadow: 0 8px 24px rgba(255, 255, 255, 0.35);
      transform: translateY(-2px);
    }

    .hero-bubble {
      text-align: center;
      padding: 36px 24px 28px;
      margin-bottom: 24px;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-soft);
      margin-bottom: 18px;
    }

    .hero-title {
      font-size: clamp(2.3rem, 5vw, 3.6rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.1;
      margin-bottom: 14px;
      color: #ffffff;
    }

    .hero-subtitle {
      font-size: 1.05rem;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 28px;
      line-height: 1.6;
    }

    .stats-bubble-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 34px;
    }

    .stat-pill {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 22px;
      border-radius: var(--radius-pill);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-bubble);
    }

    .stat-num {
      font-size: 1.05rem;
      font-weight: 700;
      color: #ffffff;
      font-family: var(--font-mono);
    }

    .stat-lbl {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .gen-section-bubble {
      background: linear-gradient(135deg, #181820 0%, #111116 100%);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-bubble);
      padding: 32px 36px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-lift);
      position: relative;
      overflow: hidden;
    }

    .gen-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 24px;
    }

    .gen-title-block h2 {
      font-size: 1.45rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .gen-title-block p {
      font-size: 0.88rem;
      color: var(--text-muted);
    }

    .cooldown-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 18px;
      border-radius: var(--radius-pill);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
      font-size: 0.82rem;
      color: var(--text-soft);
    }

    .cooldown-pill.ready {
      border-color: rgba(255, 255, 255, 0.4);
      color: #ffffff;
    }

    .gen-buttons-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }

    .gen-trigger-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 20px 16px;
      border-radius: var(--radius-bubble-sm);
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: var(--font-body);
      font-weight: 700;
      box-shadow: var(--shadow-bubble);
    }

    .gen-trigger-btn i {
      font-size: 1.8rem;
      transition: transform 0.2s ease;
    }

    .gen-trigger-btn:hover:not(:disabled) {
      background: #ffffff;
      color: #000000;
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(255, 255, 255, 0.25);
    }

    .gen-trigger-btn:hover:not(:disabled) i {
      transform: scale(1.12);
    }

    .gen-trigger-btn:disabled {
      opacity: 0.45;
      cursor: not-allowed;
      filter: grayscale(1);
    }

    .gen-btn-count {
      font-size: 0.72rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-weight: 500;
    }

    .gen-trigger-btn:hover:not(:disabled) .gen-btn-count {
      color: #333333;
    }

    .gen-display-box {
      background: var(--bg-body);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-bubble-sm);
      padding: 18px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }

    .gen-result-text {
      font-family: var(--font-mono);
      font-size: 0.88rem;
      color: var(--text-main);
      word-break: break-all;
      flex: 1;
    }

    .gen-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .filter-bubble-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 32px;
      padding: 14px 20px;
      border-radius: var(--radius-bubble-sm);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
    }

    .search-input-pill {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      flex: 1;
      max-width: 440px;
      transition: all 0.2s ease;
    }

    .search-input-pill:focus-within {
      border-color: var(--border-hover);
      box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.08);
    }

    .search-input-pill i {
      color: var(--text-muted);
      font-size: 0.88rem;
    }

    .search-input-pill input {
      border: none;
      background: transparent;
      color: #ffffff;
      font-family: var(--font-body);
      font-size: 0.9rem;
      outline: none;
      width: 100%;
    }

    .search-input-pill input::placeholder {
      color: var(--text-muted);
    }

    .filter-pills {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-pill {
      border: 1px solid var(--border-subtle);
      background: transparent;
      color: var(--text-soft);
      padding: 7px 16px;
      border-radius: var(--radius-pill);
      font-size: 0.82rem;
      font-weight: 600;
      font-family: var(--font-body);
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .filter-pill .pill-count {
      padding: 2px 7px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.08);
      font-size: 0.72rem;
      font-family: var(--font-mono);
      font-weight: 700;
    }

    .filter-pill:hover, .filter-pill.active {
      background: #ffffff;
      color: #000000;
      border-color: #ffffff;
    }

    .filter-pill.active .pill-count {
      background: rgba(0, 0, 0, 0.15);
      color: #000000;
    }

    .vault-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 22px;
      margin-bottom: 60px;
    }

    .bubble-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-bubble);
      padding: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: var(--shadow-bubble);
      position: relative;
      overflow: hidden;
    }

    .bubble-card:hover {
      transform: translateY(-5px);
      background: var(--bg-card-hover);
      border-color: var(--border-hover);
      box-shadow: var(--shadow-lift);
    }

    .card-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 14px;
      margin-bottom: 18px;
    }

    .card-icon-bubble {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: var(--bg-bubble);
      border: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      color: #ffffff;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
      transition: transform 0.2s ease;
    }

    .bubble-card:hover .card-icon-bubble {
      transform: scale(1.08);
      background: #ffffff;
      color: #000000;
    }

    .card-badge-pill {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      color: var(--text-soft);
      font-family: var(--font-mono);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }

    .card-title {
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 8px;
      line-height: 1.3;
    }

    .card-desc {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 20px;
      flex-grow: 1;
    }

    .card-meta-pills {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 22px;
    }

    .meta-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.06);
      font-size: 0.76rem;
      font-weight: 500;
      color: var(--text-soft);
      font-family: var(--font-mono);
    }

    .card-footer {
      display: flex;
      align-items: center;
      gap: 10px;
      padding-top: 18px;
      border-top: 1px solid var(--border-subtle);
    }

    .card-btn {
      flex: 1;
      padding: 10px 16px;
      border-radius: var(--radius-pill);
      font-size: 0.84rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      border: 1px solid var(--border-subtle);
    }

    .card-btn-download {
      background: #ffffff;
      color: #000000;
      border-color: #ffffff;
    }

    .card-btn-download:hover {
      background: #e5e5ec;
      transform: translateY(-2px);
      box-shadow: 0 4px 14px rgba(255, 255, 255, 0.2);
    }

    .card-btn-inspect {
      background: var(--bg-bubble);
      color: var(--text-main);
      border-color: var(--border-subtle);
      max-width: 105px;
    }

    .card-btn-inspect:hover {
      background: #2f2f3d;
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }

    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 999;
      padding: 20px;
    }

    .modal-overlay.active {
      display: flex;
      animation: modalFadeIn 0.24s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modalFadeIn {
      from { opacity: 0; transform: scale(0.96); }
      to { opacity: 1; transform: scale(1); }
    }

    .modal-bubble {
      background: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-bubble);
      max-width: 640px;
      width: 100%;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(255, 255, 255, 0.15);
      overflow: hidden;
    }

    .modal-head {
      padding: 24px 28px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
    }

    .modal-head h4 {
      font-size: 1.2rem;
      font-weight: 800;
      color: #ffffff;
    }

    .modal-close-btn {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--bg-bubble);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .modal-close-btn:hover {
      background: #ffffff;
      color: #000000;
    }

    .modal-body {
      padding: 24px 28px;
      overflow-y: auto;
      flex: 1;
    }

    .file-tree-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .file-item-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 14px;
      border-radius: var(--radius-pill);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--text-soft);
    }

    .modal-foot {
      padding: 18px 28px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      justify-content: flex-end;
      gap: 12px;
    }

    .toast-pill {
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%) translateY(80px);
      background: #ffffff;
      color: #000000;
      padding: 12px 26px;
      border-radius: var(--radius-pill);
      font-size: 0.88rem;
      font-weight: 700;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 1000;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s;
      opacity: 0;
      pointer-events: none;
    }

    .toast-pill.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    @media (max-width: 768px) {
      .layout-wrapper { padding: 18px 16px 60px; }
      .bubble-nav { flex-direction: column; align-items: stretch; border-radius: var(--radius-bubble); }
      .nav-actions { justify-content: center; }
      .gen-buttons-row { grid-template-columns: 1fr; }
      .vault-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <div class="bg-canvas">
    <div class="ambient-bubble bubble-1"></div>
    <div class="ambient-bubble bubble-2"></div>
    <div class="ambient-bubble bubble-3"></div>
  </div>

  <div class="layout-wrapper">
    
    <header class="bubble-nav">
      <a href="/flicky" class="brand-cluster">
        <div class="brand-icon-bubble">
          <i class="fa-solid fa-cube"></i>
        </div>
        <div>
          <span class="brand-title">FLICKY</span>
          <span class="brand-tag">VAULT</span>
        </div>
      </a>

      <div class="nav-actions">
        <a href="vault/Flicky_Source_Vault_Complete.zip" class="bubble-btn bubble-btn-primary" download>
          <i class="fa-solid fa-file-zipper"></i>
          <span>Master Bundle (1.43 GB)</span>
        </a>
      </div>
    </header>

    <section class="hero-bubble">
      <div class="hero-badge">
        <i class="fa-solid fa-circle-dot"></i>
        <span>SOURCE PLATFORM • CRACKS • ACCOUNT GENERATOR</span>
      </div>
      <h1 class="hero-title">Flicky Source & Account Vault</h1>
      <p class="hero-subtitle">
        Unified distribution for gaming reverse-engineering frameworks, clean unpacked binary cracks, and an automated 5-minute cooldown credential dispenser.
      </p>

      <div class="stats-bubble-row">
        <div class="stat-pill">
          <span class="stat-num" id="statTotalArchives">21</span>
          <span class="stat-lbl">Total Archives</span>
        </div>
        <div class="stat-pill">
          <span class="stat-num">6,033+</span>
          <span class="stat-lbl">Packaged Files</span>
        </div>
        <div class="stat-pill">
          <span class="stat-num" id="statTotalAccounts">289</span>
          <span class="stat-lbl">Available Accounts</span>
        </div>
        <div class="stat-pill">
          <span class="stat-num">5m</span>
          <span class="stat-lbl">Cooldown Limit</span>
        </div>
      </div>
    </section>

    <!-- Account Generator Bubble Box with Discord Verification Gate -->
    <section class="gen-section-bubble">
      <div class="gen-header">
        <div class="gen-title-block">
          <h2><i class="fa-solid fa-id-card-clip"></i> Account Generator</h2>
          <p>Instant credential dispenser for Steam, Rockstar Games, and Discord. Requires Discord authorization & enforces a 5-minute cooldown.</p>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
          <div class="cooldown-pill ready" id="discordAuthBadge" style="cursor: pointer;" onclick="toggleDiscordModal()">
            <i class="fa-brands fa-discord"></i>
            <span id="discordAuthStatusText">Discord: Not Authorized</span>
          </div>
          <div class="cooldown-pill ready" id="cooldownBadge">
            <i class="fa-solid fa-clock"></i>
            <span id="cooldownTimerText">Status: Ready to Generate</span>
          </div>
        </div>
      </div>

      <!-- Discord Lock Overlay Banner (Visible when unauthorized) -->
      <div id="discordLockBanner" style="background: rgba(88, 101, 242, 0.08); border: 1px dashed rgba(88, 101, 242, 0.35); border-radius: var(--radius-bubble-sm); padding: 22px 26px; margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 16px;">
          <div style="width: 46px; height: 46px; border-radius: 50%; background: #5865F2; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 4px 14px rgba(88, 101, 242, 0.4);">
            <i class="fa-brands fa-discord"></i>
          </div>
          <div>
            <div style="font-size: 1rem; font-weight: 800; color: #ffffff;">Discord Authorization Required</div>
            <div style="font-size: 0.84rem; color: var(--text-muted);">Connect and authorize your Discord profile to unlock account generation privileges.</div>
          </div>
        </div>
        <button class="bubble-btn bubble-btn-primary" onclick="openDiscordAuthModal()" style="background: #5865F2; color: #fff; border-color: #5865F2; box-shadow: 0 4px 18px rgba(88, 101, 242, 0.35);">
          <i class="fa-brands fa-discord"></i>
          <span>Authorize Discord</span>
        </button>
      </div>

      <!-- Authorized User Pill Banner (Visible when authorized) -->
      <div id="discordActiveBanner" style="display: none; background: rgba(255, 255, 255, 0.04); border: 1px solid var(--border-subtle); border-radius: var(--radius-bubble-sm); padding: 14px 20px; margin-bottom: 24px; align-items: center; justify-content: space-between; gap: 14px; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <img id="discordUserAvatar" src="https://cdn.discordapp.com/embed/avatars/0.png" alt="Avatar" style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid var(--border-subtle);">
          <div>
            <div style="font-size: 0.88rem; font-weight: 700; color: #ffffff; display: flex; align-items: center; gap: 8px;">
              <span id="discordUsernameDisplay">User</span>
              <span style="font-size: 0.68rem; padding: 2px 8px; border-radius: var(--radius-pill); background: rgba(35, 165, 90, 0.2); color: #57F287; border: 1px solid rgba(87, 242, 135, 0.3); font-weight: 700;">AUTHORIZED</span>
            </div>
            <div style="font-size: 0.74rem; color: var(--text-muted); font-family: var(--font-mono);" id="discordIdDisplay">ID: 0000000000000000</div>
          </div>
        </div>
        <button class="bubble-btn" onclick="disconnectDiscord()" style="padding: 6px 14px; font-size: 0.75rem;">
          <i class="fa-solid fa-arrow-right-from-bracket"></i> <span>Disconnect</span>
        </button>
      </div>

      <div class="gen-buttons-row">
        <button class="gen-trigger-btn" id="btnGenSteam" onclick="generateAccount('steam')">
          <i class="fa-brands fa-steam"></i>
          <span>Steam Account</span>
          <span class="gen-btn-count" id="countSteam">149 Available</span>
        </button>
        <button class="gen-trigger-btn" id="btnGenRockstar" onclick="generateAccount('rockstar')">
          <i class="fa-solid fa-star"></i>
          <span>Rockstar Account</span>
          <span class="gen-btn-count" id="countRockstar">84 Available</span>
        </button>
        <button class="gen-trigger-btn" id="btnGenDiscord" onclick="generateAccount('discord')">
          <i class="fa-brands fa-discord"></i>
          <span>Discord Account</span>
          <span class="gen-btn-count" id="countDiscord">56 Available</span>
        </button>
      </div>

      <div class="gen-display-box">
        <div class="gen-result-text" id="genResultBox">
          <span style="color: var(--text-muted);">Authorize Discord and choose a platform above to dispense your credentials...</span>
        </div>
        <div class="gen-actions">
          <button class="bubble-btn" id="btnCopyAcc" onclick="copyAccountResult()" style="padding: 8px 16px; font-size: 0.8rem; display: none;">
            <i class="fa-regular fa-copy"></i> <span>Copy</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Filter Bar with Badge Counts -->
    <div class="filter-bubble-bar">
      <div class="search-input-pill">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" id="vaultSearch" placeholder="Search 21 archives by title or game..." oninput="handleFilter()">
      </div>

      <div class="filter-pills" id="categoryFilterContainer"></div>
    </div>

    <!-- Unified Cards Grid -->
    <main class="vault-grid" id="unifiedVaultGrid"></main>

  </div>

  <div class="modal-overlay" id="inspectModal" onclick="closeModalOnOverlay(event)">
    <div class="modal-bubble">
      <div class="modal-head">
        <h4 id="modalTitle">Archive Details</h4>
        <button class="modal-close-btn" onclick="closeModal()">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <p id="modalSub" style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 16px;"></p>
        <ul class="file-tree-list" id="modalFileList"></ul>
      </div>
      <div class="modal-foot">
        <button class="bubble-btn" onclick="closeModal()">Close</button>
        <a id="modalDownloadBtn" href="#" class="bubble-btn bubble-btn-primary" download>
          <i class="fa-solid fa-download"></i>
          <span>Download Zip</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Discord Authorization Modal -->
  <div class="modal-overlay" id="discordAuthModal" onclick="closeDiscordModalOnOverlay(event)">
    <div class="modal-bubble" style="max-width: 480px;">
      <div class="modal-head">
        <h4 style="display: flex; align-items: center; gap: 10px;">
          <i class="fa-brands fa-discord" style="color: #5865F2;"></i>
          <span>Discord Authorization</span>
        </h4>
        <button class="modal-close-btn" onclick="closeDiscordAuthModal()">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body" style="text-align: center; padding: 28px 24px;">
        <div style="width: 68px; height: 68px; border-radius: 50%; background: rgba(88, 101, 242, 0.12); border: 1px solid rgba(88, 101, 242, 0.4); color: #5865F2; display: inline-flex; align-items: center; justify-content: center; font-size: 2rem; margin-bottom: 18px;">
          <i class="fa-brands fa-discord"></i>
        </div>
        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">Link Your Discord Account</h3>
        <p style="font-size: 0.86rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 22px;">
          To prevent spam and enforce the 5-minute generator cooldown, please enter your Discord username or ID to authorize your browser session.
        </p>

        <div style="text-align: left; margin-bottom: 18px;">
          <label style="font-size: 0.78rem; font-weight: 700; color: var(--text-soft); text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 6px; display: block;">Discord Tag / Username</label>
          <div class="search-input-pill" style="max-width: 100%;">
            <i class="fa-solid fa-at"></i>
            <input type="text" id="discordAuthInput" placeholder="e.g. flicky or flicky#0001" onkeydown="if(event.key==='Enter') submitDiscordAuth()">
          </div>
        </div>

        <div style="font-size: 0.76rem; color: var(--text-muted); display: flex; align-items: center; justify-content: center; gap: 6px;">
          <i class="fa-solid fa-shield-halved"></i>
          <span>Official OAuth2 integration & local session verification</span>
        </div>
      </div>
      <div class="modal-foot" style="justify-content: space-between;">
        <button class="bubble-btn" onclick="closeDiscordAuthModal()">Cancel</button>
        <button class="bubble-btn bubble-btn-primary" onclick="submitDiscordAuth()" style="background: #5865F2; color: #fff; border-color: #5865F2;">
          <i class="fa-solid fa-check"></i>
          <span>Authorize Now</span>
        </button>
      </div>
    </div>
  </div>

  <div class="toast-pill" id="toastPill">
    <i class="fa-solid fa-check"></i>
    <span id="toastMsg">Ready</span>
  </div>

  <script>
""" + acc_js + """
    let accountsDB = embeddedAccounts;

    const allVaultItems = [
      // Roblox (2 items)
      {
        id: "roblox_external",
        title: "Roblox External",
        category: "Roblox",
        badge: "Roblox",
        desc: "Dedicated Roblox external multi-feature client with memory cache scanning and ESP overlay.",
        zip: "vault/new_adds/roblox_external.zip",
        size: "28.58 MB",
        files: 197,
        preview: ["roblox-ext.slnx", "roblox-ext/globals.h", "roblox-ext/offsets.h", "roblox-ext/cache/cache.cpp", "roblox-ext/stb_image.h"]
      },
      {
        id: "roblox_external_base",
        title: "Roblox External Base",
        category: "Roblox",
        badge: "Roblox",
        desc: "Offset probing toolkit and modular external base for automated updates and memory reads.",
        zip: "vault/new_adds/Roblox_external_base.zip",
        size: "26.11 MB",
        files: 333,
        preview: ["build_all.bat", "probe_offsets.py", "rbx-external.sln", "UPDATER_README.md", "UWLoader/Build"]
      },

      // Rust (2 items)
      {
        id: "cloak-rust",
        title: "Cloak-Rust",
        category: "Rust",
        badge: "Rust",
        desc: "Lightweight Rust external framework featuring memory routines and modular offsets.",
        zip: "vault/Cloak-Rust.zip",
        size: "11.2 MB",
        files: 108,
        preview: ["src/main.rs", "Cargo.toml", "offsets.hpp", "driver/communication.h", "gui/overlay.cpp"]
      },
      {
        id: "rust-external-paste-main",
        title: "Rust External Paste",
        category: "Rust",
        badge: "Rust",
        desc: "Clean Rust external template with driver communication headers and simple vector math.",
        zip: "vault/rust-external-paste-main.zip",
        size: "5.06 MB",
        files: 51,
        preview: ["rust-external.sln", "main.cpp", "driver.h", "math.h", "offsets.h", "render.cpp"]
      },

      // CS2 (1 item)
      {
        id: "cs2_cheat",
        title: "CS2 Internal Engine",
        category: "CS2",
        badge: "CS2",
        desc: "Complete Counter-Strike 2 source codebase with netvars, hooks, aimbot, and ESP modules.",
        zip: "vault/new_adds/Cs2.zip",
        size: "2.67 MB",
        files: 343,
        preview: ["CMakeLists.txt", "src/main.cpp", "src/core/globals.h", "src/core/hooks.cpp", "src/features/esp.cpp", "src/features/aimbot.cpp"]
      },

      // FiveM (4 items)
      {
        id: "robrun_source",
        title: "robrun source",
        category: "FiveM",
        badge: "FiveM",
        desc: "Full source suite including kernel memory driver, manual mapper, DirectX overlay, and ESP math.",
        zip: "vault/Ballout_AMZ_Full_Source.zip",
        size: "97.22 MB",
        files: 1249,
        preview: ["Ballout.sln", "amz.cpp", "driver/kernel_io.c", "mapper/kdmapper.cpp", "overlay/directx.cpp"]
      },
      {
        id: "fivem_external",
        title: "FiveM External",
        category: "FiveM",
        badge: "FiveM",
        desc: "Comprehensive FiveM external runtime codebase supporting native entity decryptions.",
        zip: "vault/Fivem_external.zip",
        size: "55.04 MB",
        files: 101,
        preview: ["Fivem external.sln", "entry.cpp", "sdk/world.hpp", "sdk/ped.hpp", "render/overlay.hpp"]
      },
      {
        id: "robrun_external",
        title: "Robrun External",
        category: "FiveM",
        badge: "FiveM",
        desc: "Feature-packed external platform built with robust game memory parsing routines.",
        zip: "vault/Robrun_external.zip",
        size: "37.67 MB",
        files: 1213,
        preview: ["Robrun.sln", "main.cpp", "features/visuals.cpp", "features/aim.cpp", "sdk/entity.hpp"]
      },
      {
        id: "fivem_imgui",
        title: "FiveM ImGui",
        category: "FiveM",
        badge: "FiveM",
        desc: "Compact ImGui GUI menu template tailored specifically for FiveM overlay injection.",
        zip: "vault/fivem_imgui.zip",
        size: "2.71 MB",
        files: 43,
        preview: ["fivem imgui.sln", "main.cpp", "menu/menu.cpp", "imgui/imgui_draw.cpp", "hook/dxgi.cpp"]
      },

      // Cracks (4 items)
      {
        id: "k3crack",
        title: "k3crack",
        category: "Cracks",
        badge: "Cracks",
        desc: "Standalone unpacked binary build for k3 loader authentication bypassing.",
        zip: "vault/cracks/k3crack.zip",
        size: "22.59 MB",
        files: 1,
        preview: ["k3crack.exe"]
      },
      {
        id: "sanity",
        title: "Sanity Loader Suite",
        category: "Cracks",
        badge: "Cracks",
        desc: "Complete Sanity crack package including SanityLoader.exe, DRM patch, and Capstone disassembler.",
        zip: "vault/cracks/Sanity.zip",
        size: "5.54 MB",
        files: 3,
        preview: ["SanityLoader.exe", "drm.dll", "capstone.dll"]
      },
      {
        id: "summit_external",
        title: "Summit External",
        category: "Cracks",
        badge: "Cracks",
        desc: "Summit external client binary with unpacked license authentication routines.",
        zip: "vault/cracks/Summit_External.zip",
        size: "7.53 MB",
        files: 1,
        preview: ["Summit External.exe"]
      },
      {
        id: "vain_bp_2",
        title: "Vain BP (2)",
        category: "Cracks",
        badge: "Cracks",
        desc: "Vain client binary patched for direct offline initialization and testing.",
        zip: "vault/cracks/vain_bp_2.zip",
        size: "4.13 MB",
        files: 1,
        preview: ["vain bp (2).exe"]
      },

      // External & Other (8 items)
      {
        id: "fn_external",
        title: "FN External",
        category: "External",
        badge: "Fortnite",
        desc: "Modern Fortnite external project featuring DirectX 11 overlay and memory config handling.",
        zip: "vault/new_adds/FN_external.zip",
        size: "18.58 MB",
        files: 211,
        preview: ["rage.slnx", "FN EXTERNAL2/main.cpp", "FN EXTERNAL2/rage.vcxproj", "FN EXTERNAL2/dependenices/configs/config.hpp"]
      },
      {
        id: "r6_internal_dx12",
        title: "R6 Internal DX12",
        category: "External",
        badge: "R6 Siege",
        desc: "Rainbow Six Siege DX12 internal hook engine with full game structures and offsets.",
        zip: "vault/new_adds/R6_Internal_dx12.zip",
        size: "331.14 MB",
        files: 205,
        preview: ["rb6.sln", "rb6/core/dx12_hook.cpp", "rb6/features/visuals.cpp", "rb6/sdk/offsets.h"]
      },
      {
        id: "bloodstrikepy",
        title: "BloodStrikePy",
        category: "External",
        badge: "BloodStrike",
        desc: "Python automated visual scripting and memory engine for BloodStrike.",
        zip: "vault/new_adds/BloodStrikePy.zip",
        size: "0.01 MB",
        files: 2,
        preview: ["new.py", "Run.bat"]
      },
      {
        id: "custom_external",
        title: "Custom External",
        category: "External",
        badge: "External",
        desc: "Complete external rendering solution with DirectX overlay hooks and math helpers.",
        zip: "vault/Custom_external.zip",
        size: "562.97 MB",
        files: 918,
        preview: ["Custom external.sln", "main.cpp", "render.cpp", "overlay.h", "math/vector.h", "driver/interface.cpp"]
      },
      {
        id: "new_era",
        title: "New Era",
        category: "External",
        badge: "External",
        desc: "Advanced multi-module external engine with customizable visual pipelines and entity tracking.",
        zip: "vault/New_Era.zip",
        size: "656.93 MB",
        files: 939,
        preview: ["New Era.sln", "src/core/main.cpp", "src/hooks/dx11.cpp", "src/features/esp.cpp", "sdk/offsets.h"]
      },
      {
        id: "imgui_loader",
        title: "ImGui Loader",
        category: "External",
        badge: "ImGui",
        desc: "Polished ImGui-based user authentication loader with custom styling and smooth animation ticks.",
        zip: "vault/Imgui_loader.zip",
        size: "9.11 MB",
        files: 47,
        preview: ["Imgui loader.sln", "main.cpp", "imgui/imgui.cpp", "auth/auth.hpp", "ui/design.cpp"]
      },
      {
        id: "ion-ai-cracked-main",
        title: "Ion AI Framework",
        category: "External",
        badge: "Neural AI",
        desc: "Neural / computer vision assisted targeting algorithms and color-detection engine.",
        zip: "vault/ion-ai-cracked-main.zip",
        size: "30.32 MB",
        files: 15,
        preview: ["main.py", "model/weights.onnx", "engine/capture.py", "gui/interface.py", "requirements.txt"]
      },
      {
        id: "nvdia_streamproof",
        title: "Nvidia Streamproof",
        category: "External",
        badge: "Bypass",
        desc: "Nvidia shadowplay / overlay bypass implementation for clean capture masking.",
        zip: "vault/Nvdia_streamproof.zip",
        size: "3.7 KB",
        files: 2,
        preview: ["streamproof.h", "streamproof.cpp"]
      }
    ];

    let currentCategory = 'all';

    function initAccountCounts() {
      const steamCount = (accountsDB.steam || []).length;
      const rockstarCount = (accountsDB.rockstar || []).length;
      const discordCount = (accountsDB.discord || []).length;
      const totalCount = steamCount + rockstarCount + discordCount;

      document.getElementById('countSteam').textContent = `${steamCount} Available`;
      document.getElementById('countRockstar').textContent = `${rockstarCount} Available`;
      document.getElementById('countDiscord').textContent = `${discordCount} Available`;
      document.getElementById('statTotalAccounts').textContent = totalCount;
    }

    // Discord Authorization Gate
    const DISCORD_AUTH_KEY = 'flicky_discord_auth_profile';

    function getDiscordProfile() {
      try {
        const raw = localStorage.getItem(DISCORD_AUTH_KEY);
        return raw ? JSON.parse(raw) : null;
      } catch (e) {
        return null;
      }
    }

    function isDiscordAuthorized() {
      const prof = getDiscordProfile();
      return !!(prof && prof.username);
    }

    function updateDiscordUI() {
      const profile = getDiscordProfile();
      const lockBanner = document.getElementById('discordLockBanner');
      const activeBanner = document.getElementById('discordActiveBanner');
      const authBadge = document.getElementById('discordAuthBadge');
      const authStatusText = document.getElementById('discordAuthStatusText');

      if (profile && profile.username) {
        lockBanner.style.display = 'none';
        activeBanner.style.display = 'flex';
        document.getElementById('discordUsernameDisplay').textContent = '@' + profile.username;
        document.getElementById('discordIdDisplay').textContent = 'ID: ' + profile.id;
        document.getElementById('discordUserAvatar').src = profile.avatar || 'https://cdn.discordapp.com/embed/avatars/0.png';
        authBadge.className = 'cooldown-pill ready';
        authBadge.style.borderColor = 'rgba(88, 101, 242, 0.4)';
        authStatusText.innerHTML = '<span style="color:#57F287;">●</span> Discord: @' + profile.username;
      } else {
        lockBanner.style.display = 'flex';
        activeBanner.style.display = 'none';
        authBadge.className = 'cooldown-pill';
        authBadge.style.borderColor = '';
        authStatusText.textContent = 'Discord: Not Authorized';
      }
    }

    function openDiscordAuthModal() {
      document.getElementById('discordAuthModal').classList.add('active');
      setTimeout(() => {
        const inp = document.getElementById('discordAuthInput');
        if (inp) { inp.focus(); }
      }, 100);
    }

    function closeDiscordAuthModal() {
      document.getElementById('discordAuthModal').classList.remove('active');
    }

    function closeDiscordModalOnOverlay(e) {
      if (e.target.id === 'discordAuthModal') closeDiscordAuthModal();
    }

    function toggleDiscordModal() {
      if (!isDiscordAuthorized()) openDiscordAuthModal();
    }

    function submitDiscordAuth() {
      const input = document.getElementById('discordAuthInput');
      const val = (input ? input.value : '').trim().replace(/^@/, '');
      if (!val) {
        showToast('Please enter your Discord username or tag.');
        return;
      }

      let hash = 0;
      for (let i = 0; i < val.length; i++) hash = ((hash << 5) - hash) + val.charCodeAt(i);
      const suffix = Math.abs(hash).toString().padEnd(14, '7').substring(0, 14);
      const mockId = '10' + suffix;
      const avatarIndex = Math.abs(hash) % 5;

      const profile = {
        username: val,
        id: mockId,
        avatar: 'https://cdn.discordapp.com/embed/avatars/' + avatarIndex + '.png',
        authorizedAt: Date.now()
      };

      localStorage.setItem(DISCORD_AUTH_KEY, JSON.stringify(profile));
      updateDiscordUI();
      closeDiscordAuthModal();
      showToast('Discord authorized as @' + val + '!');

      if (window.location.protocol !== 'file:') {
        fetch('/api/discord/link-demo', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username: val, discord_id: mockId, avatar: profile.avatar })
        }).catch(() => {});
      }
    }

    function disconnectDiscord() {
      localStorage.removeItem(DISCORD_AUTH_KEY);
      updateDiscordUI();
      showToast('Discord account disconnected.');
    }

    const COOLDOWN_KEY = 'flicky_acc_gen_timestamp';
    const COOLDOWN_MS = 5 * 60 * 1000;

    function checkCooldown() {
      const lastTimeStr = localStorage.getItem(COOLDOWN_KEY);
      if (!lastTimeStr) {
        setCooldownState(true, 0);
        return true;
      }
      const lastTime = parseInt(lastTimeStr, 10);
      const now = Date.now();
      const diff = now - lastTime;
      if (diff >= COOLDOWN_MS) {
        setCooldownState(true, 0);
        return true;
      } else {
        const remainingSec = Math.ceil((COOLDOWN_MS - diff) / 1000);
        setCooldownState(false, remainingSec);
        return false;
      }
    }

    function setCooldownState(isReady, remainingSec) {
      const badge = document.getElementById('cooldownBadge');
      const text = document.getElementById('cooldownTimerText');
      const btns = [document.getElementById('btnGenSteam'), document.getElementById('btnGenRockstar'), document.getElementById('btnGenDiscord')];

      if (isReady) {
        badge.className = 'cooldown-pill ready';
        text.innerHTML = '<i class="fa-solid fa-circle-check"></i> Status: Ready to Generate';
        btns.forEach(b => { if(b) b.disabled = false; });
      } else {
        badge.className = 'cooldown-pill';
        const mins = Math.floor(remainingSec / 60);
        const secs = remainingSec % 60;
        const fmt = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
        text.innerHTML = `<i class="fa-solid fa-hourglass-half"></i> Cooldown: ${fmt} left`;
        btns.forEach(b => { if(b) b.disabled = true; });
      }
    }

    setInterval(checkCooldown, 1000);

    function generateAccount(type) {
      // 1. Enforce Discord Authorization Gate
      if (!isDiscordAuthorized()) {
        showToast('You must authorize your Discord account before generating credentials.');
        openDiscordAuthModal();
        return;
      }

      // 2. Enforce 5-minute cooldown
      if (!checkCooldown()) {
        showToast('Please wait for the 5-minute cooldown to expire.');
        return;
      }

      const pool = accountsDB[type] || [];
      if (pool.length === 0) {
        showToast(`No accounts available for ${type}.`);
        return;
      }

      const randomIndex = Math.floor(Math.random() * pool.length);
      const chosen = pool[randomIndex];

      localStorage.setItem(COOLDOWN_KEY, Date.now().toString());
      checkCooldown();

      const resultBox = document.getElementById('genResultBox');
      const copyBtn = document.getElementById('btnCopyAcc');

      resultBox.innerHTML = `
        <div style="margin-bottom: 4px; font-weight: 700; color: #ffffff; text-transform: uppercase; font-size: 0.78rem; letter-spacing: 0.05em;">
          <i class="fa-solid fa-key"></i> Dispensed ${type} Account:
        </div>
        <div style="font-size: 0.95rem; color: #e8e8ed; background: rgba(255,255,255,0.06); padding: 8px 12px; border-radius: 8px;">
          ${escapeHtml(chosen)}
        </div>
      `;
      copyBtn.style.display = 'inline-flex';
      copyBtn.setAttribute('data-acc', chosen);

      showToast(`1 ${type.toUpperCase()} account generated!`);
    }

    function copyAccountResult() {
      const copyBtn = document.getElementById('btnCopyAcc');
      const text = copyBtn.getAttribute('data-acc');
      if (text) {
        navigator.clipboard.writeText(text).then(() => {
          showToast('Credentials copied to clipboard!');
        });
      }
    }

    function escapeHtml(str) {
      return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }

    function buildFilterPills() {
      const categories = [
        { id: 'all', name: 'All' },
        { id: 'Roblox', name: 'Roblox' },
        { id: 'Rust', name: 'Rust' },
        { id: 'CS2', name: 'CS2' },
        { id: 'FiveM', name: 'FiveM' },
        { id: 'Cracks', name: 'Cracks' },
        { id: 'External', name: 'External' }
      ];

      const container = document.getElementById('categoryFilterContainer');
      container.innerHTML = '';

      categories.forEach(cat => {
        const count = cat.id === 'all' 
          ? allVaultItems.length 
          : allVaultItems.filter(i => i.category.toLowerCase() === cat.id.toLowerCase()).length;

        const btn = document.createElement('button');
        btn.className = `filter-pill ${currentCategory.toLowerCase() === cat.id.toLowerCase() ? 'active' : ''}`;
        btn.innerHTML = `<span>${cat.name}</span> <span class="pill-count">${count}</span>`;
        btn.onclick = () => setCategory(cat.id, btn);
        container.appendChild(btn);
      });
    }

    function setCategory(cat, btn) {
      currentCategory = cat;
      document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderCards();
    }

    function handleFilter() {
      renderCards();
    }

    function renderCards() {
      const grid = document.getElementById('unifiedVaultGrid');
      const searchVal = document.getElementById('vaultSearch').value.toLowerCase().trim();

      grid.innerHTML = '';
      const filtered = allVaultItems.filter(item => {
        const matchesCategory = currentCategory === 'all' || item.category.toLowerCase() === currentCategory.toLowerCase();
        const matchesSearch = item.title.toLowerCase().includes(searchVal) || 
                              item.desc.toLowerCase().includes(searchVal) ||
                              item.category.toLowerCase().includes(searchVal) ||
                              (item.badge && item.badge.toLowerCase().includes(searchVal));
        return matchesCategory && matchesSearch;
      });

      if (filtered.length === 0) {
        grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; color: var(--text-muted); font-size: 1rem;">No archives found matching "${searchVal || currentCategory}".</div>`;
        return;
      }

      filtered.forEach(item => {
        const card = document.createElement('article');
        card.className = 'bubble-card';

        let iconClass = 'fa-code';
        if (item.category === 'Cracks') iconClass = 'fa-unlock-keyhole';
        else if (item.category === 'Rust') iconClass = 'fa-shield-halved';
        else if (item.category === 'Roblox') iconClass = 'fa-shapes';
        else if (item.category === 'CS2') iconClass = 'fa-crosshairs';
        else if (item.category === 'FiveM') iconClass = 'fa-car-side';

        card.innerHTML = `
          <div>
            <div class="card-top">
              <div class="card-icon-bubble">
                <i class="fa-solid ${iconClass}"></i>
              </div>
              <span class="card-badge-pill">${item.badge || item.category}</span>
            </div>
            <h3 class="card-title">${item.title}</h3>
            <p class="card-desc">${item.desc}</p>
            <div class="card-meta-pills">
              <span class="meta-pill"><i class="fa-solid fa-file-zipper"></i> ${item.size}</span>
              <span class="meta-pill"><i class="fa-solid fa-layer-group"></i> ${item.files} file${item.files > 1 ? 's' : ''}</span>
              <span class="meta-pill"><i class="fa-solid fa-check"></i> Available</span>
            </div>
          </div>
          <div class="card-footer">
            <button class="card-btn card-btn-inspect" onclick="openInspect('${item.id}')">
              <i class="fa-solid fa-folder-tree"></i> Files
            </button>
            <a href="${item.zip}" class="card-btn card-btn-download" download onclick="showToast('Downloading ${item.title}...')">
              <i class="fa-solid fa-download"></i> Download .zip
            </a>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function openInspect(itemId) {
      const item = allVaultItems.find(i => i.id === itemId);
      if (!item) return;

      document.getElementById('modalTitle').textContent = item.title;
      document.getElementById('modalSub').textContent = `${item.files} file(s) • ${item.size} compressed zip archive`;
      
      const fileListEl = document.getElementById('modalFileList');
      fileListEl.innerHTML = '';
      (item.preview || []).forEach(f => {
        const li = document.createElement('li');
        li.className = 'file-item-pill';
        li.innerHTML = `<i class="fa-solid fa-file-code"></i> <span>${f}</span>`;
        fileListEl.appendChild(li);
      });

      if ((item.files || 0) > (item.preview || []).length) {
        const extra = item.files - item.preview.length;
        const li = document.createElement('li');
        li.className = 'file-item-pill';
        li.style.color = 'var(--text-muted)';
        li.innerHTML = `<i class="fa-solid fa-ellipsis"></i> <span>+ ${extra} additional project files in zip</span>`;
        fileListEl.appendChild(li);
      }

      const dlBtn = document.getElementById('modalDownloadBtn');
      dlBtn.href = item.zip;
      dlBtn.onclick = () => showToast(`Downloading ${item.title}...`);

      document.getElementById('inspectModal').classList.add('active');
    }

    function closeModal() {
      document.getElementById('inspectModal').classList.remove('active');
    }

    function closeModalOnOverlay(e) {
      if (e.target.id === 'inspectModal') closeModal();
    }

    function showToast(msg) {
      const toast = document.getElementById('toastPill');
      document.getElementById('toastMsg').textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 3000);
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });

    initAccountCounts();
    updateDiscordUI();
    checkCooldown();
    buildFilterPills();
    renderCards();
  </script>
</body>
</html>"""

with open(r'C:\Users\Flick\Downloads\flicky.html', 'w', encoding='utf-8') as f:
    f.write(template)

print('Successfully generated C:\\Users\\Flick\\Downloads\\flicky.html')
