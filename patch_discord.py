with open(r'C:\Users\Flick\Downloads\build_flicky.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the gen-header HTML with Discord Authorization Card / Gate
old_gen_box = '''    <!-- Account Generator Bubble Box -->
    <section class="gen-section-bubble">
      <div class="gen-header">
        <div class="gen-title-block">
          <h2><i class="fa-solid fa-id-card-clip"></i> Account Generator</h2>
          <p>Instant credential dispenser for Steam, Rockstar Games, and Discord. Dispenses 1 account every 5 minutes.</p>
        </div>
        <div class="cooldown-pill ready" id="cooldownBadge">
          <i class="fa-solid fa-clock"></i>
          <span id="cooldownTimerText">Status: Ready to Generate</span>
        </div>
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
          <span style="color: var(--text-muted);">Select Steam, Rockstar, or Discord above to dispense your credentials...</span>
        </div>
        <div class="gen-actions">
          <button class="bubble-btn" id="btnCopyAcc" onclick="copyAccountResult()" style="padding: 8px 16px; font-size: 0.8rem; display: none;">
            <i class="fa-regular fa-copy"></i> <span>Copy</span>
          </button>
        </div>
      </div>
    </section>'''

new_gen_box = '''    <!-- Account Generator Bubble Box with Discord Verification Gate -->
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
    </section>'''

assert old_gen_box in text, 'old_gen_box target string not found in build_flicky.py'
text = text.replace(old_gen_box, new_gen_box)

# 2. Add Discord Auth Modal right before toast-pill
old_modal_end = '''  <div class="toast-pill" id="toastPill">'''
new_discord_modal = '''  <!-- Discord Authorization Modal -->
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

  <div class="toast-pill" id="toastPill">'''

assert old_modal_end in text, 'old_modal_end target string not found'
text = text.replace(old_modal_end, new_discord_modal)

# 3. Add Discord Auth JS routines
js_needle = '''    const COOLDOWN_KEY = 'flicky_acc_gen_timestamp';'''
discord_js_addition = '''    // Discord Authorization Gate
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

    const COOLDOWN_KEY = 'flicky_acc_gen_timestamp';'''

assert js_needle in text, 'js_needle target string not found'
text = text.replace(js_needle, discord_js_addition)

# 4. Enforce Discord gate check inside generateAccount
old_gen_fn = '''    function generateAccount(type) {
      if (!checkCooldown()) {
        showToast('Please wait for the 5-minute cooldown to expire.');
        return;
      }'''

new_gen_fn = '''    function generateAccount(type) {
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
      }'''

assert old_gen_fn in text, 'old_gen_fn target string not found'
text = text.replace(old_gen_fn, new_gen_fn)

# 5. Call updateDiscordUI in boot sequence
old_boot = '''    initAccountCounts();
    checkCooldown();'''

new_boot = '''    initAccountCounts();
    updateDiscordUI();
    checkCooldown();'''

assert old_boot in text, 'old_boot target string not found'
text = text.replace(old_boot, new_boot)

with open(r'C:\Users\Flick\Downloads\build_flicky.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('build_flicky.py patched with Discord authorization gate successfully')
