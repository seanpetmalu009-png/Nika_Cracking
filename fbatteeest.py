#_____ TOOL : FACEBOOK AUTO CERATE 🎓

#___ OPEN SOURCE : KGF CYBER TEAM 

#____ OWNER : NIKA BREVOUR

#-----------------------( IMPORT )-----------------------#
import os,sys,time,requests,re,random,string,json,platform,subprocess,pyotp
from os import system
from io import BytesIO
from typing import Set,Optional
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from os import path
from urllib.request import Request,urlopen
from time import localtime as lt
from pip._vendor import requests
from datetime import datetime,timedelta
from bs4 import BeautifulSoup as sop
from random import randint as rr
from random import choice as rc
from string import digits as digits
#-----------------------( COLOR )-----------------------#
G="\033[1;92m";W="\x1b[38;5;15m";B="\033[1;34m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\33[1;91m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\x1b[10;95m"
white="\033[1;37m";yellow="\033[1;33m";green="\033[1;32m";gren="\033[38;5;49m";redd="\033[38;5;160m";red="\033[1;31m";cyan="\033[1;36m";bluee="\033[38;5;6m";blue="\033[1;34m";purple="\033[1;35m";orange="\033[38;5;208m";black="\033[1;30m";reset="\033[0m"
#______
os.system("xdg-open https://t.me/+ySgl6S0nEZwwYWFl")
#-----------------------( STYLE )-----------------------#
xp=f"{white}[{green}●{white}]{green}"
xp1=f"{white}[{green}1{white}]{green}"
xp2=f"{white}[{green}2{white}]{green}"
xp3=f"{white}[{green}3{white}]{green}"
xp4=f"{white}[{green}4{white}]{green}"
xp5=f"{white}[{green}5{white}]{green}"
xp6=f"{white}[{green}6{white}]{green}"
xp7=f"{white}[{green}7{white}]{green}"
xp8=f"{white}[{green}8{white}]{green}"
xp0=f"{white}[{red}0{white}]{red}"
xpx=f"{white}[{green}?{white}]{green}"
xpxx=f"{white}[{red}!{white}]{red}"
xpxxx=f"{white}➤{green}"
#-----------------------( INTERNET )-----------------------#
try:
    requests.get("https://www.google.com",timeout=5)
except requests.exceptions.ConnectionError:
    system("clear" if os.name == "posix" else "cls")
    print(f"{xpxx} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    exit()
#-----------------------( NO-MODULE )-----------------------#
try:
    import pycurl
except ImportError as e:
    system("clear" if os.name == "posix" else "cls")
    missing_module=str(e).split("'")[1]
    if missing_module == "pycurl":
        print(f"{xp} YOU DON'T HAVE PYCURL MODULE PLEASE INSTALL IT")
        print(f"{xp} RUN {xpxxx} pip install pycurl")
        print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        exit()
#-----------------------( KEY GENERATOR )-----------------------#
def getKey(): 
    a=str(os.geteuid())
    b=str(os.geteuid())
    try:
        build=subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
    except:
        build="UNKNOWN"
    x=(a+build+b).upper().replace(".","")
    z="X".join(x)
    keys=z[15:]
    return "ERROR-"+keys
final_key=getKey() 
#-----------------------( FILE KEY )-----------------------#
file_path='/data/data/com.termux/files/usr/bin/.kitty.txt'
try:
    with open(file_path,'r') as f:
        key1=f.read().strip()
except FileNotFoundError:
    try:
        with open(file_path,'w') as f:
            f.write(final_key)
    except Exception as e:
        pass
#-----------------------( SECURITY BOX )-----------------------#
packages=["com.httpcanary.pro","com.guoshi.httpcanary","com.wasim","com.purple.canary","com.guoshi.httpcanary.premium","app.greyshirts.sslcapture"]
base_path="/sdcard/Android/data"
try:
    for pkg in packages:
        if os.path.exists(os.path.join(base_path,pkg)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit()
except Exception as e:
    pass
def termux_uninstall():
    return (os.path.exists("/data/data/com.termux/files/usr/bin/pip") and os.path.exists("/data/data/com.termux/files/usr/bin/pip3"))
def anti_uninstall_warning():
    system("clear" if os.name == "posix" else "cls")
    print(f"{xpxx} YOU ARE USING ANTI-UNINSTALL SYSTEM")
    print(f"{xpxx} WARNING ONLY — SCRIPT WILL CONTINUE")
    print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def check_file(path,pattern):
    if not os.path.exists(path):
        return "pure_user"
    try:
        with open(path,"r",encoding="utf-8",errors="ignore") as f:
            return "bypass_user" if re.search(pattern,f.read()) else "pure_user"
    except:
        return "pure_user"
def url_sefty():
    return check_file("/data/data/com.termux/files/usr/lib/python3.13/site-packages/requests/api.py",r"\bprint\s*\(")
def url_sefty2():
    return check_file("/data/data/com.termux/files/usr/lib/python3.13/site-packages/httpx/_api.py",r"\bprint\s*\(")
def key_sefty():
    return check_file("/data/data/com.termux/files/usr/lib/python3.13/site-packages/httpx/_models.py",re.escape(final_key))
def key_sefty2():
    return check_file("/data/data/com.termux/files/usr/lib/python3.13/site-packages/requests/models.py",re.escape(final_key))
#-----------------------( HTTP CANARY )-----------------------#
package_name='com.httpcanary.pro'
path_canary='/sdcard/Android/data'
package_name2='com.guoshi.httpcanary'
path_canary2='/sdcard/Android/data'
package_name3='com.wasim'
path_canary3='/sdcard/Android/data'
package_name4='com.purple.canary'
path_canary4='/sdcard/Android/data'
package_name5='com.guoshi.httpcanary.premium'
path_canary5='/sdcard/Android/data'
package_name6='app.greyshirts.sslcapture'
path_canary6='/sdcard/Android/data'
#-----------------------( PROXY )-----------------------#
def load_proxies():
    proxy_url=["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt","https://www.proxy-list.download/api/v1/get?type=http","https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all","https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt","https://api.openproxylist.xyz/http.txt"]
    try:
        response=requests.get(proxy_url)
        if response.status_code==200:
            return [proxy.strip() for proxy in response.text.splitlines()]
    except requests.exceptions.RequestException:
        pass
    return []
proxies_list=load_proxies()
def ethanproxy():
    if proxies_list:
        proxy=random.choice(proxies_list)
        return {"http": f"http://{proxy}","https": f"http://{proxy}"}
    return None
#-----------------------( SYS )-----------------------#
sys.stdout.write('\x1b[1;37m\x1b]2; 💚<KALYAN KING>💚\x07')
#-----------------------( FILE-PATH )-----------------------#
sd_folder="/sdcard/KALYAN-AUTO"
kitty_folders=("AUTO","2FA","COKI")
os.makedirs(sd_folder,exist_ok=True)
for folder in kitty_folders:
    os.makedirs(os.path.join(sd_folder,folder),exist_ok=True)
#-----------------------( DATE )-----------------------#
__dic__={'1': 'JANUARY','2': 'FEBRUARY','3': 'MARCH','4': 'APRIL','5': 'MAY','6': 'JUNE','7': 'JULY','8': 'AUGUST','9': 'SEPTEMBER','10': 'OCTOBER','11': 'NOVEMBER','12': 'DECEMBER'}
__now__=datetime.now()
__days__=__now__.day
__months__=__dic__[str(__now__.month)]
__years__=__now__.year
__date__=f'{green}{__months__}{white}/{green}{__days__}{white}/{green}{__years__}{white}'
ltx=int(lt()[3])
a=ltx - 12 if ltx > 12 else ltx
tag="PM" if ltx > 12 else "AM"
#-----------------------( COUNTRY )-----------------------#
ip=requests.get("https://api.ipify.org").text
ip_info=requests.post(f"http://ip-api.com/json/{ip}")
af=json.loads(ip_info.text)
#-----------------------( SDCARD PERMISSION )-----------------------#
try:
    system("clear" if os.name == "posix" else "cls")
    system("rm -rf /sdcard/.txt > /dev/null 2>&1")
    with open("/sdcard/.txt","w") as f:
        f.write(" ")
except PermissionError:
    print(f"{xp} WITHOUT STORAGE PERMISSION YOU CANNOT")
    print(f"{xp} RUN THIS TOOL ALLOW STORAGE PERMISSION")
    print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    system("termux-setup-storage -y > /dev/null 2>&1")
    exit(f"{xp} RUN AGAIN THIS TOOL ")
#-----------------------( CLEAR )-----------------------#
def __CLEAR__():
    system("clear" if os.name == "posix" else "cls")
    print(logo)
def __ERRORLOGO__():
    system("clear" if os.name == "posix" else "cls");print(logo);__LINE__();print(info);__LINE__()
#-----------------------( SPECIAL-LINE )-----------------------#
def __LINE__():
    print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-----------------------( UA-NORMAL-MIX )-----------------------#
ua=UserAgent()

def ___EthanAutoUa1___():
    version=random.choice(['14','15','10','13','7.0.0','7.1.1','9','12','11','9.0','8.0.0','7.1.2','7.0','4','5','4.4.2','5.1.1','6.0.1','9.0.1'])
    model=random.choice(['1105','1107','15','3T','62A','6779','6833','7273','9A','A1','A1 5G','A1 Pro','A11','A11k','A11x','A12','A15','A15s','A16','A16e','A16k','A16s','A17','A17k','A18','A1i 5G','A1k','A1s','A1x','A2 5G','A25','A2x 5G','A3','A3 5G','A3 Pro 5G','A30','A31','A31c','A32','A33','A33m','A33t','A34','A35','A36','A37','A37t','A38','A39','A3s','A3x 5G','A4','A40','A400','A41','A42','A43','A44','A45','A46','A47','A48','A49','A5','A5 (2020)','A50','A51','A52','A53','A53 5G','A53m','A53s','A53s 5G','A54','A54 5G','A54s','A55','A55 5G','A55s 5G','A56','A56 5G','A57','A57 (2016)','A57 (2022)','A58','A58 5G','A59','A59 5G','A59m','A59s','A59t','A5S','A60','A7','A71','A71 (2018)','A71A','A72','A72n 5G','A73','A73 5G','A73t','A74','A74 5G','A76','A77','A77 5G','A77s','A77t','A78','A78 5G','A79','A79 5G','A79k','A79t','A7n','A7x','A8','A83','A83 (2018)','A83PRO','A83t','A85T','A9','A9 (2020)','A91','A92','A92s','A93','A93s','A94','A95','A96','A96 5G','A97','A98','A98 5G','A9x','AX5','AX5s','AX7','C1','CNM632','CNM652','CPH1114','CPH1235','CPH1427','CPH1451','CPH1615','CPH1664','CPH1869','CPH1927','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2535','CPH2551','CPH2553','CPH2557','CPH2569','CPH2573','CPH2579','CPH2581','CPH2583','CPH2585','CPH2589','CPH2591','CPH2599','CPH2603','CPH2605','CPH2607','CPH2609','CPH2611','CPH2613','CPH2617','CPH2619','CPH2621','CPH2625','CPH2629','CPH2631','CPH2637','CPH2639','CPH2641','CPH2643','CPH2661','CPH2663','CPH2665','CPH2667','CPH2669','CPH2681','CPH2683','CPH2687','CPH2843','CPH2931','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','CPH9977','f','F1','F1 Plus','F10','F11','F11 Pro','F11Pro','F15','F17','F17 Pro','F19','F19 Pro','F19 Pro Plus','F19s','F1s','F21 Pro','F21s Pro','F23 5G','F25 Pro 5G','F27 Pro+ 5G','F3','F3 Plus','F5','F5 Youth','F51','F61','F7','F9','F9 Pro','Find','Find 5','Find 5 Mini','Find 7','Find 7a','Find Clover','Find Melody','Find Muse','Find N','Find N 5G','Find N2','lFind N2 Flip','Find N3','Find N3 Flip','Find Way S','Find X','Find X Lamborghini','Find X2','Find X2 Lite','Find X2 Pro','Find X3','Find X3 Lite','Find X3 Neo','Find X3 Pro','Find X5','Find X5 Pro','Find X6','Find X6 Pro','Find X7','Find X7 Ultra','Find X7 Ultra SE','JLAJH6','Joy Plus','K1','K10','K10 5G','K10 Pro 5G','K10x','K11 5G','K11x 5G','K12 5G','K3','K5','K7','K7x','K9 5G','K9 Pro 5G','K9s','K9x','N1 Mini','N1T','N3','Neo','Neo 3','Neo 5','Neo 7','Neo 7s','Pad 2','Pad Air','Pad Air 2','Pad Neo','Pad WiFi','R10','R1001','R11','R11 Plus','R11plus','R11s','R11s Plus','R15','R15 Dream Mirror','R15 Neo','R15 Pro','R15x','R17','R17 Neo','R17 Pro','R1K','R1L','R1S','R1x','R2001','R2010','R2017','R3006','R5','R53','R6007','R7','R7 Lite','R7 Plus','R7 Plus F','R7005','R7007','R7s','R7s Plus','R7sm','R7st','R7t','R801','R805','R807','R811','R819','R819T','R8205','R8207','R823T','R829','R829T','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 11','Reno 11 Pro','Reno 12','Reno 12 5G','Reno 12 F 4G','Reno 12 F 5G','Reno 12 Pro 5G','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9','Reno 9 A','Reno 9 Pro','Reno 9 Pro+','Reno A','Reno Ace','Reno Ace 2','Reno K3','Reno Z','Reno10','Reno11','Reno2','RENO3','Reno4','Reno5','Reno8','Reno9','RX17 Neo','S1','S17','S3','S4','T29','Ulike 2','V5','V8821','Watch 2 46mm','Watch 41mm','Watch 46mm','X','x20','x22','X50Pro','X54','X9017','X907','Y15','Y21','Y3','Z1'])
    build=random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver=str(random.choice(range(77,577)))
    ver2=str(random.choice(range(57,77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''

def ___EthanAutoUa2___():
    ualist=[ua.random for _ in range(70)]
    return str(random.choice(ualist))
#-------------------------( FIRST FEMALE PH )-------------------------#
first_names1=["Maria", "Angelica", "Andrea", "Alyssa", "Bianca", "Camille", "Claudine", "Danica", "Diana", "Ella",
    "Erika", "Faith", "Gabriela", "Grace", "Hannah", "Isabel", "Jasmine", "Janine", "Jessica", "Julia",
    "Katherine", "Katrina", "Kayla", "Kyla", "Lara", "Lea", "Lianne", "Liza", "Lorraine", "Mae",
    "Mariel", "Mika", "Monica", "Nadine", "Nicole", "Patricia", "Paula", "Princess", "Rhea", "Rica",
    "Rose", "Samantha", "Sarah", "Shaina", "Sheena", "Stephanie", "Trisha", "Vanessa", "Yna", "Zara",
    "Zoe", "Althea", "Aira", "Ash", "Ashley", "Clarisse", "Dianne", "Jolina", "Keanna", "Kyra",
    "Mikaela", "Nica", "Shaira", "Zyra", "Lovely", "Precious", "Joy", "May", "Ellaine", "Angel",
    "Angela", "Anne", "Anna", "Aubrey", "Bea", "Carla", "Carmela", "Catherine", "Cheska",
    "Chloe", "Clara", "Dana", "Denise", "Elaine", "Ericka", "Frances", "Gina", "Hazel", "Heidi",
    "Irene", "Jamila", "Janelle", "Jessa", "Jillian", "Joyce", "Karla", "Kathleen", "Kaye", "Kimberly",
    "Kristine", "Laila", "Leanne", "Loren", "Lyka", "Maika", "Marissa", "Michelle", "Mitch", "Mona",
    "Naomi", "Nina", "Noemi", "Pamela", "Pearl", "Rachelle", "Regine", "Roxanne", "Sam", "Sandra",
    "Sharon", "Sheila", "Sheryl", "Tessa", "Tina", "Venus", "Veronica", "Wendy", "Yvette", "Zenaida",
    "Zena", "Alicia", "Amara", "Ariana", "Ayesha", "Beverly", "Cecilia", "Charmaine", "Cristina", "Desiree",
    "Dulce", "Evangeline", "Felicia", "Gloria", "Jocelyn", "Josephine", "Juliet", "Lourdes", "Lucia", "Marjorie",
    "Milagros", "Norma", "Olivia", "Rosalie", "Rowena", "Teresa", "Victoria", "Wilma", "Abigail", "Adriana",
    "Amelia", "Anika", "Bella", "Brianna", "Cindy", "Danielle", "Isla", "Sofia", "Sophia", "Luna",
    "Ava", "Eloisa", "Elise", "Mara", "Maya", "Nina Marie", "Sara Marie", "Anna Marie", "Clara Mae", "Joy Marie",
    "Ella Mae", "Kimberly Ann", "Mary Grace", "Mary Joy", "Mary Ann", "Ana Marie", "Jean", "Jhoanna", "Jovelyn", "Lovelyn",
    "Rizalyn", "Analyn", "Maricel", "Maribel", "Marites", "Mayette", "Cherry", "Cherry Mae", "Lovely Joy", "Precious Joy",
    "Angel Mae", "Angel Joy", "Aira Mae", "Alyssa Mae", "Bianca Mae", "Camille Mae", "Danica Mae", "Diana Mae", "Erika Mae", "Faith Mae",
    "Grace Mae", "Hannah Mae", "Jasmine Mae", "Janine Mae", "Jessica Mae", "Julia Mae", "Katrina Mae", "Kyra Mae", "Mika Mae", "Nica Mae",
    "Shaira Mae", "Zyra Mae", "Trisha Mae", "Vanessa Mae", "Zara Mae", "Zoe Mae", "Althea Mae", "Ashley Mae", "Clarisse Mae", "Dianne Mae",
    "Keanna Mae", "Lianne Mae", "Lorraine Mae", "Mariel Mae", "Monica Mae", "Nadine Mae", "Nicole Mae", "Patricia Mae", "Rhea Mae", "Rica Mae"]
#-------------------------( LAST FEMALE PH )-------------------------#
surnames1=[
    "Santos", "Reyes", "Cruz", "Garcia", "Dela Cruz", "Ramos", "Aquino", "Lopez", "Torres", "Navarro",
    "Castillo", "Mendoza", "Bautista", "Villanueva", "Flores", "Ortega", "Gonzales", "Delgado", "Ramirez", "Diaz",
    "Salazar", "Domingo", "Pascual", "Santiago", "Valdez", "Aguilar", "Alvarez", "Benedicto", "Cabrera", "Cortez",
    "De Leon", "Espinoza", "Fernandez", "Guerrero", "Hernandez", "Ibanez", "Jacinto", "Lazaro", "Manalo", "Navales",
    "Ocampo", "Panganiban", "Quintos", "Rebolledo", "Sison", "Tolentino", "Urbano", "Velasco", "Yap", "Zamora",
    "Abad", "Alcantara", "Balagtas", "Bautista", "Bernardo", "Carreon", "Dizon", "Estrella", "Fajardo", "Galang",
    "Hidalgo", "Ignacio", "Javier", "Luna", "Macapagal", "Magsino", "Navarro", "Olivares", "Padilla", "Quizon",
    "Razon", "Salvador", "Tadeo", "Umali", "Vergara", "Yambao", "Zafra", "Bagasao", "Calderon", "De Guzman",
    "Abella", "Bala", "Cabatbat", "Dela Peña", "Escalona", "Fabros", "Guinto", "Hontiveros", "Ilagan", "Jalandoni",
    "Lacson", "Macaraeg", "Neri", "Ona", "Pineda", "Quimson", "Rafanan", "Sagun", "Talavera", "Umali",
    "Abcede", "Balmes", "Capulong", "Dungo", "Enriquez", "Franco", "Gatchalian", "Hilario", "Isidro", "Joaquin",
    "Lantion", "Mariano", "Natividad", "Olivar", "Perez", "Quiazon", "Reodica", "Sarmiento", "Tiongson", "Uy",
    "Abadiano", "Balingit", "Crisostomo", "Dacanay", "Espiritu", "Ferrer", "Gomez", "Hernando", "Ibarrientos", "Jimenez",
    "Luna", "Magno", "Nolasco", "Ordonez", "Pascua", "Quinto", "Rosales", "Salonga", "Tayag", "Uy",
    "Alfonso", "Bautista", "Candelaria", "Dela Rosa", "Esguerra", "Feliciano", "Gamboa", "Hernandez", "Isidro", "Javier",
    "Lagman", "Marquez", "Natividad", "Ong", "Pangan", "Quimpo", "Ramos", "Santos", "Tupas", "Uy",
    "Abano", "Baldoza", "Carpio", "Dizon", "Estacio", "Fabian", "Galvez", "Hizon", "Ignacio", "Jacobe",
    "Limos", "Manlapaz", "Navalta", "Olea", "Perez", "Quinones", "Reyes", "Sanchez", "Tolosa", "Uy"
]
#-------------------------( FIRST MALE PH )-------------------------#
first_names2=["Juan", "Jose", "Antonio", "Manuel", "Francisco", "Ramon", "Eduardo", "Fernando", "Ricardo", "Roberto",
    "Luis", "Carlos", "Miguel", "Gabriel", "Daniel", "Adrian", "Christian", "Christopher", "Mark", "John",
    "Paul", "Peter", "James", "Jerome", "Joseph", "Joshua", "Matthew", "Nathaniel", "Noel", "Patrick",
    "Vincent", "Victor", "Xavier", "Albert", "Alfred", "Allan", "Andrew", "Anthony", "Arnold", "Arthur",
    "Benito", "Benjamin", "Bernardo", "Brandon", "Bryan", "Calvin", "Cedric", "Cesar", "Clarence", "Clifford",
    "Dennis", "Dominic", "Edgar", "Edwin", "Elias", "Emmanuel", "Enrico", "Eric", "Erwin", "Felix",
    "Francis", "Frederick", "Gary", "Gerald", "Gilbert", "Gregorio", "Harold", "Henry", "Ian", "Ismael",
    "Ivan", "Jaime", "Jasper", "Jefferson", "Jeremy", "Jericho", "Jerome", "Jesus", "Joel", "Jomar",
    "Jonathan", "Jordan", "Jorge", "Josef", "Joselito", "Jovito", "Julius", "Kenneth", "Kevin", "Kurt",
    "Lawrence", "Leo", "Leonardo", "Lester", "Lorenzo", "Louie", "Lucas", "Marvin", "Melvin", "Michael",
    "Nathan", "Neil", "Nestor", "Nicholas", "Noelito", "Norman", "Oliver", "Oscar", "Paolo", "Patrick",
    "Paulino", "Percival", "Philip", "Rafael", "Raymond", "Reynaldo", "Richard", "Rico", "Rodel", "Rogelio",
    "Rolando", "Romeo", "Ronald", "Roy", "Ruben", "Salvador", "Samuel", "Sergio", "Sherwin", "Sonny",
    "Stephen", "Steve", "Teodoro", "Tomas", "Victorino", "Wilfredo", "William", "Wilson", "Winston", "Zaldy",
    "John Mark", "John Paul", "John Michael", "John Lloyd", "John Patrick", "John Carlo", "John Rey", "John Vincent", "John Kenneth", "John Dave",
    "Mark Anthony", "Mark Joseph", "Mark Kevin", "Mark Angelo", "Mark Lester", "Mark John", "Mark Christian", "Mark Vincent", "Mark Anthony", "Mark Bryan",
    "James Michael", "James Patrick", "James Anthony", "James Carlo", "James Mark", "James Vincent", "James Kenneth", "James Dave", "James Paul", "James Ryan",
    "Christian Paul", "Christian Mark", "Christian James", "Christian John", "Christian Michael", "Christian Anthony", "Christian Dave", "Christian Ryan", "Christian Carlo", "Christian Lloyd",
    "Michael John", "Michael James", "Michael Anthony", "Michael Vincent", "Michael Paul", "Michael Ryan", "Michael Dave", "Michael Carlo", "Michael Bryan", "Michael Joseph",
    "Carlo", "Carlo Miguel", "Carlo James", "Carlo Anthony", "Carlo John", "Carlo Vincent", "Carlo Mark", "Carlo Ryan", "Carlo Joseph", "Carlo Dave",
    "Angelo", "Angelo Miguel", "Angelo James", "Angelo John", "Angelo Mark", "Angelo Paul", "Angelo Ryan", "Angelo Dave", "Angelo Joseph", "Angelo Vincent",
    "Bryan", "Bryan James", "Bryan John", "Bryan Mark", "Bryan Paul", "Bryan Michael", "Bryan Anthony", "Bryan Ryan", "Bryan Dave", "Bryan Vincent",
    "Ryan", "Ryan James", "Ryan John", "Ryan Mark", "Ryan Paul", "Ryan Michael", "Ryan Anthony", "Ryan Dave", "Ryan Vincent", "Ryan Joseph",
    "Lloyd", "Lloyd James", "Lloyd John", "Lloyd Mark", "Lloyd Paul", "Lloyd Michael", "Lloyd Anthony", "Lloyd Ryan", "Lloyd Dave", "Lloyd Vincent",
    "Jayson", "Jay", "Jaypee", "Jaymar", "Jaylord", "Jayvee", "Jhay", "Jhun", "Jomari", "Jomel",
    "Jun", "Junrey", "Junard", "Juniel", "Junmark", "Junver", "Junboy", "Junrico", "Junel", "Junbert",
    "Rodel", "Rodelio", "Rodelyn", "Rodelito", "Rodelmar", "Rodelson", "Rodelito", "Rodelvin", "Rodelman", "Rodelbert"]
#-------------------------( LAST MALE PH )-------------------------#
surnames2=["Santos","Reyes","Cruz","Garcia","Dela Cruz","Ramos","Aquino","Lopez","Torres","Navarro",
    "Castillo","Mendoza","Bautista","Villanueva","Flores","Ortega","Gonzales","Delgado","Ramirez","Diaz",
    "Salazar","Domingo","Pascual","Santiago","Valdez","Aguilar","Alvarez","Cabrera","Cortez","De Leon",
    "Espinoza","Fernandez","Guerrero","Hernandez","Ibanez","Jacinto","Lazaro","Manalo","Navales","Ocampo",
    "Panganiban","Quintos","Sison","Tolentino","Urbano","Velasco","Yap","Zamora","Abad","Alcantara",
    "Balagtas","Bernardo","Carreon","Dizon","Estrella","Fajardo","Galang","Hidalgo","Ignacio","Javier",
    "Luna","Macapagal","Magsino","Olivares","Padilla","Quizon","Razon","Salvador","Tadeo","Umali",
    "Vergara","Yambao","Zafra","Calderon","De Guzman","Abella","Cabatbat","Dela Pena","Escalona","Fabros",
    "Guinto","Hontiveros","Ilagan","Jalandoni","Lacson","Macaraeg","Neri","Ona","Pineda","Quimson",
    "Rafanan","Sagun","Talavera","Abcede","Balmes","Capulong","Dungo","Enriquez","Franco","Gatchalian",
    "Hilario","Isidro","Joaquin","Lantion","Mariano","Natividad","Olivar","Perez","Quiazon","Reodica",
    "Sarmiento","Tiongson","Uy","Abadiano","Balingit","Crisostomo","Dacanay","Espiritu","Ferrer","Gomez",
    "Hernando","Jimenez","Magno","Nolasco","Ordonez","Pascua","Quinto","Rosales","Salonga","Tayag",
    "Alfonso","Candelaria","Dela Rosa","Esguerra","Feliciano","Gamboa","Lagman","Marquez","Ong","Pangan",
    "Quimpo","Tupas","Abano","Baldoza","Carpio","Estacio","Fabian","Galvez","Hizon","Jacobe",
    "Limos","Manlapaz","Navalta","Olea","Quinones","Sanchez","Tolosa","Andaya","Arroyo","Atienza",
    "Bacani","Bagatsing","Balboa","Bangayan","Barrios","Basco","Batac","Belmonte","Benitez","Bernal",
    "Borja","Briones","Bugayong","Bulatao","Bungay","Caballero","Cabral","Calica","Camacho","Campos",
    "Cansino","Carandang","Cardenas","Cariaga","Casas","Castro","Catacutan","Catindig","Ceniza","Cerda",
    "Chavez","Chua","Cojuangco","Concepcion","Consunji","Cuenca","Cuevas","Custodio","David","De Vera",
    "De Villa","Del Mundo","Delos Reyes","Dimaculangan","Dimapilis","Dumlao","Eusebio","Evangelista","Felipe","Fortun",
    "Francisco","Fuentebella","Gaddi","Gatdula","Guintu","Gulle","Hipolito","Javellana","Katigbak","Lacdao",
    "Ladlad","Legaspi","Lontoc","Macalintal","Maceda","Macias","Magallanes","Magpantay","Malabanan","Mangubat",
    "Manzano","Matias","Mercado","Miranda","Molino","Montano","Montes","Nable","Narvaez","Nolasco",
    "Pabico","Pacquiao","Pajares","Palma","Paredes","Paterno","Penaflorida","Peralta","Ponce","Quirino",
    "Rabago","Regalado","Rigor","Robles","Roces","Roxas","San Diego","San Jose","San Juan","San Miguel",
    "San Pedro","Sandoval","Santillan","Sarmiento","Serna","Sevilla","Soriano","Suarez","Tabora","Tagle",
    "Tanchanco","Tantoco","Tiu","Tolentino","Trinidad","Valencia","Valenzuela","Vargas","Vasquez","Ventura",
    "Vergel","Verzosa","Villafuerte","Villareal","Yabut","Yulo","Zobel","Zubiri"]
#-------------------------( FIRST FEMALE NEPAL )-------------------------#
first_names3=["Aakriti","Aanchal","Aarati","Aarya","Aastha","Aayusha","Abha","Adhira","Alina","Amisha",
    "Anisha","Anjali","Anju","Ankita","Anu","Anusha","Anushka","Arati","Archana","Arpana",
    "Asmita","Asha","Ashmita","Ashmi","Astha","Babita","Barsha","Bhawana","Bimala","Bina",
    "Bindu","Bishakha","Chandani","Chhaya","Deepa","Deepika","Deepti","Devika","Dikshya","Dipa",
    "Dipika","Durga","Elina","Ganga","Garima","Gauri","Gita","Grishma","Hema","Indira",
    "Ishika","Ishita","Jamuna","Janaki","Jaya","Jenisha","Jharana","Juna","Junu","Kabita",
    "Kalpana","Kamala","Karuna","Kavita","Kiran","Kriti","Kritika","Kusum","Laxmi","Luna",
    "Madhu","Mamata","Manisha","Maya","Menuka","Mina","Mira","Monika","Nabina","Namrata",
    "Nandita","Nikita","Nirmala","Nisha","Nishma","Nita","Pabitra","Parbati","Pari","Paru",
    "Pooja","Prabha","Pragya","Prakriti","Pramila","Prarthana","Pratima","Preeti","Priya","Punam",
    "Rachana","Radha","Rajani","Ranjana","Rashmi","Rekha","Renuka","Reshma","Richa","Rina",
    "Rita","Ritu","Rojina","Roma","Roshana","Sabina","Sadhana","Sajina","Salina","Samikshya",
    "Sanchita","Sandhya","Sangita","Sanjita","Sarala","Sarita","Sarmila","Saru","Savitri","Seema",
    "Shanti","Sharada","Sharmila","Shikha","Shilpa","Shivani","Shraddha","Shristi","Shweta","Sita",
    "Smarika","Sneha","Soniya","Srijana","Subha","Suchita","Sudha","Sunaina","Sunita","Supriya",
    "Sushila","Swastika","Tanisha","Tara","Tejshree","Tilottama","Tripti","Tulasa","Urmila","Usha",
    "Bipana","Yamuna","Yashoda","Yojana","Aafreen","Aakansha","Aayumi","Arosha","Bibisha","Bimisha",
    "Binisha","Chahana","Cheska","Darsana","Dharana","Dhristi","Ekta","Eshika","Gitanjali","Harshika",
    "Ira","Jasmita","Jenifer","Jigyasa","Jyoti","Kaushiki","Khusbu","Kripa","Lekha","Madhavi",
    "Mahima","Malika","Mandira","Megha","Mithila","Mridula","Muskan","Nabisha","Neha","Nistha",
    "Niyati","Pallavi","Pavitra","Prerana","Prisha","Radhika","Raina","Rakshya","Ranjita","Rashika",
    "Rituja","Roshani","Rubina","Sabnam","Safina","Samjhana","Sampada","Sanju","Santosh","Sarisha",
    "Shagun","Shaila","Shivika","Shrutika","Simran","Smriti","Sonam","Srijita","Subina","Sugam",
    "Sumana","Sumitra","Sunisha","Surakshya","Susmita","Swikriti","Tanvi","Tarika","Trisana","Ujjwala",
    "Unnati","Urusha","Varsha","Vasudha","Vidya","Yamika","Yasmin","Yubina","Zara","Zenia",
    "Arohi","Bhumi","Chitralekha","Dipshikha","Ishwari","Jeevika","Komal","Lavanya","Namita","Prerna",
    "Rupa","Sajana","Toshika","Vandana","Yukti","Zinnia","Aahana","Bhawika","Charumati","Divyani"]
#-------------------------( LAST FEMALE NEPAL )-------------------------#
surnames3=["Adhikari","Acharya","Aryal","Awasthi","Bajgain","Baniya","Bastola","Bhattarai","Bhandari","Bhusal",
    "Chapagain","Dahal","Devkota","Dhakal","Dhungana","Gautam","Ghimire","Kafle","Kandel","Karki",
    "Khanal","Lamichhane","Mainali","Neupane","Niraula","Ojha","Panta","Paudel","Pokharel","Poudel",
    "Regmi","Rijal","Sapkota","Sharma","Sigdel","Subedi","Timilsina","Tiwari","Upadhyaya","Wagle",
    "Basnet","Bogati","Bohora","Budhathoki","Chand","Chhetri","Dangi","Deuba","Gharti","Hamal",
    "Karki","Khadka","Kunwar","Mahat","Malla","Oli","Rawat","Rana","Raut","Rokaya",
    "Rokaya","Rokaya","Shahi","Singh","Thakuri","Thapa","Bista","Bam","Bohara","Kathayat",
    "Ale","Baraily","Bote","Chepang","Danuwar","Ghale","Gurung","Hyolmo","Jirel","Lama",
    "Magar","Rai","Sherpa","Sunuwar","Tamang","Thami","Yakkha","Yonjan","Waiba","Moktan",
    "Dong","Syangtan","Thing","Lo","Ghising","Pakhrin","Blon","Rumba","Thokar","Titung",
    "Amatya","Awal","Bajracharya","Balami","Dangol","Dongol","Joshi","Kansakar","Karmacharya","Maharjan",
    "Nakarmi","Pradhan","Rajbhandari","Ranjitkar","Sakya","Shakya","Shrestha","Silpakar","Suwal","Tuladhar",
    "Vajracharya","Byanjankar","Chitrakar","Kasaju","Manandhar","Maskey","Malla","Mulmi","Napit","Prajapati",
    "Yadav","Jha","Jaiswal","Jaiswara","Chaudhary","Mandal","Mishra","Pathak","Pandey","Jaiswal",
    "Sah","Shah","Thakur","Singh","Gupta","Agrawal","Kushwaha","Mahato","Paswan","Rauniyar",
    "Teli","Yogi","Baniya","Kamat","Mehta","Karn","Raut","Sada","Sonar","Thakur",
    "Baral","Belbase","Bhandari","Bhatta","Bhat","Bista","Chaulagain","Dotel","Gaire","Gyawali",
    "Joshi","Khadgi","Kharel","Lamsal","Marasini","Nyaupane","Parajuli","Pathak","Rimal","Sedhai",
    "Tripathi","Upreti","Bhurtel","Koirala","Luitel","Mishra","Pangeni","Poudyal","Sapkota","Shiwakoti",
    "Adhikary","Basyal","Bastakoti","Bohuju","Budhair","Chaulagain","Darnal","Dotel","Duwadi","Gajurel",
    "Gartaula","Guragain","Kattel","Khadka","Koirala","Kuwar","Lohani","Mahatara","Neupani","Paneru",
    "Pudasaini","Risal","Sapkoti","Sigdel","Timsina","Achami","Balayar","Bhand","Bista","Chaulagain",
    "Darnal","Dhami","Gurau","Joshi","Kadayat","Kalikote","Karki","Khatri","Mahara","Mijar",
    "Nath","Rawal","Rokaya","Sarki","Sunar","Tamata","Thagunna","Airee","Badi","BK",
    "Bohora","Damai","Kami","Nepali","Pariyar","Sarki","Sunar","Bishwakarma","Gaine","Rana Magar",
    "Pun","Roka","Budha","Burathoki","Ghale","Tamang","Limbu","Subba","Maden","Phago",
    "Chemjong","Thebe","Mabohang","Nembang","Khambu","Kiranti","Lawati","Aathpariya","Chamling","Dewan",
    "Mahar","Mijar","Rokaya","Shah","Sen","Shrestha","Sharma","Subedi","Thapa","Adhikari",
    "Gurung","Rai","Sherpa","Tamang","Magar","Lama","Maharjan","Sakya","Pradhan","Tuladhar"]
#-------------------------( FIRST MALE NEPAL )-------------------------#
first_names4=["Aarav", "Aashish", "Abhas", "Abinash", "Adarsh", "Amit",
    "Amrit", "Anil", "Anish", "Ankit", "Anup", "Arjun",
    "Arun", "Ashok", "Ashwin", "Avinash", "Ayush", "Babin",
    "Bikash", "Bikram", "Binod", "Biraj", "Bishal", "Bishnu",
    "Bivek", "Chandan", "Chetan", "Deepak", "Dhiraj", "Dipak",
    "Gagan", "Ganesh", "Gaurav", "Hari", "Hemant", "Himal",
    "Ishan", "Jeevan", "Kamal", "Karan", "Kiran", "Kripal",
    "Krishna", "Kushal", "Lalit", "Madan", "Manish", "Milan",
    "Mohan", "Mukesh", "Nabin", "Naresh", "Niraj", "Nischal",
    "Nitesh", "Pawan", "Prabin", "Pradeep", "Prakash", "Pramod",
    "Pranav", "Prashant", "Prem", "Rabindra", "Rajan", "Rajesh",
    "Rakesh", "Ram", "Ramesh", "Roshan", "Sagar", "Santosh",
    "Saroj", "Shankar", "Shishir", "Sisir", "Sujan", "Suman",
    "Sunil", "Suraj", "Suresh", "Tek", "Tilak", "Ujjwal",
    "Umesh", "Upendra", "Yubraj", "Yogesh", "Aayush", "Bibek",
    "Bijay", "Dipesh", "Keshav", "Lokesh", "Mahesh", "Manoj",
    "Nawaraj", "Nirajan", "Pratap", "Rajanish", "Ranjan", "Rupesh",
    "Samir", "Sandeep", "Sanjay", "Subash", "Sudip", "Sushil",
    "Tej", "Tika", "Utsav", "Yam", "Yubaraj", "Aakash",
    "Balram", "Bhim", "Dev", "Dinesh", "Gopal", "Govinda",
    "Harihar", "Indra", "Janak", "Jiban", "Keshar", "Laxman",
    "Madhav", "Narayan", "Padam", "Paras", "Pukar", "Rabin",
    "Raghu", "Rishi", "Sabin", "Sanjog", "Sharad", "Shyam",
    "Srijan", "Subodh", "Sudarshan", "Taran", "Tulsi", "Utpal",
    "Vijay", "Yadav", "Yamraj", "Yatin",
    "Aadesh", "Aaditya", "Aagan", "Aakar", "Aasim", "Aatish",
    "Abhay", "Abiral", "Achyut", "Adesh", "Akhil", "Alok",
    "Amar", "Amol", "Ananta", "Anjan", "Anmol", "Arbind",
    "Arnav", "Aryan", "Ashim", "Ashir", "Ashutosh", "Atul",
    "Badal", "Balbahadur", "Basant", "Basu", "Bhaskar", "Bhoj",
    "Bijendra", "Bimal", "Bipin", "Birendra", "Biren", "Buddha",
    "Chandra", "Chirag", "Damodar", "Darpan", "Deependra",
    "Deven", "Dibya", "Dilip", "Drona", "Gautam", "Giri",
    "Gyan", "Hareram", "Hem", "Hom", "Ishwor", "Jagat",
    "Janardan", "Jitendra", "Kailash", "Kaji", "Kapil",
    "Kaushal", "Kiranraj", "Kuber", "Kundan", "Lokeshwar",
    "Madanraj", "Mahendra", "Milanraj", "Mithun", "Moti",
    "Nandan", "Narendra", "Navin", "Nawang", "Nikhil",
    "Nirmal", "Pabitra", "Padamraj", "Pankaj", "Prabesh",
    "Prabinraj", "Pradip", "Pramesh", "Pratik", "Pritam",
    "Puskar", "Rabinraj", "Raj", "Rajiv", "Ranjit",
    "Ratan", "Ritesh", "Rituraj", "Sabinraj", "Sachin",
    "Sagarraj", "Sameer", "Sampanna", "Sanjiv", "Santoshraj",
    "Sarbin", "Shailesh", "Shiv", "Shovit", "Siddhartha",
    "Subin", "Sudarshanraj", "Sudeep", "Sujit", "Sumanraj",
    "Sunir", "Surendra", "Tilakraj", "Ujjal", "Umeshraj",
    "Upen", "Utkarsh", "Vikash", "Vikram", "Yamdeep",
    "Yash", "Yograj", "Yubarajraj", "Zenish", "Zorawar"]
#-------------------------( LAST MALE NEPAL )-------------------------#
surnames4=["Adhikari", "Acharya", "Aryal", "Awasthi", "Bajgain", "Baniya",
    "Baral", "Basnet", "Bastola", "Belbase", "Bhattarai", "Bhandari",
    "Bhusal", "Bista", "Budhathoki", "Chalise", "Chand", "Chaulagain",
    "Chhetri", "Dahal", "Dhakal", "Dhungana", "Duwadi", "Gaire",
    "Gautam", "Ghimire", "Giri", "Gyawali", "Humagain", "Kafle",
    "Kandel", "Karki", "Khadka", "Khanal", "Kharel", "Lamichhane",
    "Lamsal", "Mainali", "Neupane", "Niraula", "Pachhai", "Pande",
    "Pandey", "Pangeni", "Paudel", "Pokharel", "Poudel", "Puri",
    "Regmi", "Rijal", "Sapkota", "Shahi", "Sharma", "Sigdel",
    "Subedi", "Tewari", "Thapa", "Timilsina", "Tiwari", "Upadhyaya",
    "Wagle", "Yogi", "Bohara", "Kunwar", "Rana", "Rawal",
    "Bohora", "Basyal", "Kathayat", "Malla", "Karki Chhetri",
    "Basnyat", "Bam", "Rokaya", "Bista Chhetri", "Rokaya Chhetri",
    "Khatri", "Khatiwada", "Maharjan", "Manandhar", "Shrestha",
    "Tuladhar", "Joshi", "Rajbhandari", "Dongol", "Dangol",
    "Pradhan", "Ranjitkar", "Mali", "Nakarmi", "Tamrakar",
    "Maharjan Newar", "Shakya", "Bajracharya", "Kansakar",
    "Silpakar", "Rajopadhyaya", "Nakarmi Newar", "Tuladhar Newar",
    "Rai", "Limbu", "Tamang", "Magar", "Gurung", "Sherpa",
    "Thakuri", "Gharti", "Ale", "Pun", "Roka", "Sijapati",
    "Yonjan", "Moktan", "Waiba", "Blon", "Lama", "Syangtan",
    "Thing", "Lo", "Ghising", "Pakhrin", "Dong", "Bal",
    "Thami", "Chepang", "Hayu", "Majhi", "Danuwar", "Sunuwar",
    "Jirel", "Baram", "Yakkha", "Chamling", "Bantawa", "Kulung",
    "Mewahang", "Lohorung", "Athpahariya", "Thulung", "Bhujel",
    "Darai", "Dura", "Kumal", "Bote", "Raute", "Raji",
    "Koche", "Meche", "Dhimal", "Tajpuriya", "Rajbanshi",
    "Satar", "Kisan", "Santhal", "Tharu", "Chaudhary",
    "Mahato", "Yadav", "Jha", "Mishra", "Jaiswal", "Gupta",
    "Sah", "Shah", "Agrawal", "Poddar", "Karn", "Jaiswal Tharu",
    "Mandal", "Paswan", "Ram", "Mehta", "Chaurasiya", "Teli",
    "Koirala", "Oli", "K.C.", "G.C.", "B.K.", "Airee",
    "Bohora Chhetri", "Chand Thakuri", "Deuba", "Devkota",
    "Dhungel", "Ghale", "Kafle Sharma", "Karki Thapa",
    "Khadgi", "Khatiwada", "Koirala Sharma", "Kshetri",
    "Lohani", "Mahat", "Mahatara", "Mijar", "Moktan Lama",
    "Nepali", "Nembang", "Nirauli", "Ojha", "Panta",
    "Parajuli", "Pathak", "Pokharia", "Prasai", "Puri Sharma",
    "Raut", "Rimal", "Sangraula", "Shiwakoti", "Simkhada",
    "Sitoula", "Subba", "Suwal", "Thagunna", "Thulung Rai",
    "Upreti", "Waiba Tamang", "Yonzon", "Zimba", "Ghale Gurung",
    "Ale Magar", "Pun Magar", "Rai Bantawa", "Sherchan",
    "Tulachan", "Gauchan", "Bhattachan", "Poon", "Jomsom",
    "Kusunda", "Lepcha", "Mukhia", "Namgyal", "Palungwa",
    "Phombo", "Rumba", "Samba", "Tumbahangphe", "Lingden",
    "Thebe", "Lawati", "Khamcha", "Khapangi", "Maden",
    "Nembang Rai", "Palikhe", "Rokka", "Sharma Acharya",
    "Thapa Magar", "Tiwari Nepal", "Uprety", "Waiba Lama",
    "Yakha", "Yonjan Tamang", "Zimba Sherpa", "Aale",
    "Basnet Chhetri", "Budha", "Budha Magar", "Chandara",
    "Gharti Magar", "Khadka Chhetri", "Lamgade", "Mahat Chhetri",
    "Poudyal", "Rana Magar", "Rokka Chhetri", "Singh Thakuri"]
#-------------------------( FIRST FEMALE PAKISTAN )-------------------------#
first_names5=["Ayesha", "Fatima", "Zainab", "Maryam", "Noor", "Hira", "Saba",
    "Amina", "Alina", "Mahnoor", "Laiba", "Dua", "Anaya", "Iqra",
    "Sana", "Mahira", "Rania", "Areeba", "Hania", "Zoya",
    "Amna", "Fiza", "Eman", "Nimra", "Sidra", "Rabia",
    "Hoorain", "Sumaira", "Kainat", "Ayat", "Iman", "Maham",
    "Aiza", "Zara", "Hiba", "Yusra", "Saniya", "Aqsa",
    "Sehrish", "Maira", "Bushra", "Nida", "Rida", "Uzma",
    "Saima", "Fariha", "Nawal", "Arisha", "Eshal", "Abeer",
    "Anum", "Farah", "Asma", "Sanam", "Warda", "Zohra",
    "Mehreen", "Hadiya", "Kashaf", "Laila", "Arooj", "Zimal",
    "Hooriya", "Jannat", "Aiman", "Aliza", "Minal", "Dania",
    "Abeer Fatima", "Aiman Fatima", "Alina Noor", "Anam", "Arfa",
    "Bisma", "Bushra Noor", "Cyra", "Emaan", "Erum", "Fizza",
    "Ghazal", "Hafsa", "Haniya", "Hina", "Ifrah", "Iffat",
    "Insha", "Iqra Noor", "Javeria", "Kanwal", "Khadija",
    "Laraib", "Liyana", "Maham Noor", "Mahvish", "Mahnoor Fatima",
    "Mariya", "Mehak", "Misbah", "Muneeba", "Muskan",
    "Naila", "Nawal Fatima", "Noor Fatima", "Parveen", "Quratulain",
    "Rameen", "Rania Noor", "Rimsha", "Saba Noor", "Sadia",
    "Sahar", "Saima Noor", "Samina", "Sara", "Sehar",
    "Shanzay", "Shiza", "Sidra Noor", "Sobia", "Sundas",
    "Tabinda", "Tania", "Tayyaba", "Urooj", "Wajiha",
    "Yumna", "Zainab Fatima", "Zarmeen", "Zoya Noor",
    "Aaliya", "Areej", "Arooba", "Asma Noor", "Ayesha Noor",
    "Beenish", "Dua Noor", "Eshal Fatima", "Fajr", "Fariha Noor",
    "Hania Noor", "Hoorain Fatima", "Humaira", "Itrat", "Jannat Noor",
    "Kainat Fatima", "Kashmala", "Laiba Noor", "Mahnoor Noor",
    "Mahira Noor", "Maryam Noor", "Mishal", "Naima", "Noreen",
    "Qandeel", "Rabia Noor", "Rida Fatima", "Saniya Noor", "Sehr Noor",
    "Sidra Fatima", "Sumbul", "Tahira", "Uzma Noor", "Warda Noor",
    "Yusra Noor", "Zara Noor", "Zohra Noor", "Aiza Noor",
    "Aliza Noor", "Anaya Noor", "Arisha Noor", "Eman Fatima",
    "Hiba Noor", "Iqra Fatima", "Kashaf Fatima", "Laila Noor",
    "Minal Noor", "Nida Fatima", "Rimsha Noor", "Sana Noor",
    "Zimal Noor", "Abeer Noor", "Anum Noor", "Cyra Noor",
    "Dania Noor", "Erum Fatima", "Fizza Noor", "Hadiya Noor",
    "Ifrah Noor", "Kanwal Noor", "Liyana Fatima", "Mehreen Noor",
    "Muskan Noor", "Naila Fatima", "Parisa", "Rameen Fatima",
    "Sobia Fatima", "Tayyaba Noor", "Wajiha Fatima", "Yumna Fatima"]
#-------------------------( LAST FEMALE PAKISTAN )-------------------------#
surnamese5=["Khan", "Ahmed", "Ahmad", "Ali", "Hussain", "Hasan", "Abbas",
    "Shah", "Sheikh", "Malik", "Mirza", "Qureshi", "Siddiqui",
    "Farooq", "Usman", "Umar", "Tariq", "Javed", "Iqbal",
    "Akhtar", "Anwar", "Aslam", "Arif", "Bashir", "Saeed",
    "Hamza", "Imran", "Kamran", "Adil", "Rizvi", "Naqvi",
    "Zaidi", "Kazmi", "Gilani", "Bokhari", "Chishti", "Sabri",
    "Abbasi", "Chaudhry", "Gondal", "Jutt", "Bhatti", "Awan",
    "Syed", "Paracha", "Lodhi", "Afridi", "Shinwari", "Mehsud",
    "Wazir", "Bangash", "Kakar", "Marri", "Bugti", "Jamali",
    "Leghari", "Khattak", "Yousafzai", "Khokhar", "Arain",
    "Sial", "Wattoo", "Sandhu", "Gill", "Bajwa", "Randhawa",
    "Virk", "Sidhu", "Brar", "Sethi", "Bhutto", "Zardari",
    "Sharif", "Haider", "Raza", "Nadeem", "Shahzad", "Waqas",
    "Rauf", "Latif", "Shabbir", "Ilyas", "Zafar", "Jamil",
    "Munir", "Akram", "Nasir", "Sadiq", "Rashid", "Wahid",
    "Fawad", "Bilal", "Danish", "Haroon", "Salman", "Saqib",
    "Naveed", "Tanveer", "Khurram", "Shehzad", "Adnan", "Waleed",
    "Rehman", "Rahman", "Parvez", "Zubair", "Shafiq", "Shahid",
    "Sohail", "Umair", "Yasir",
    "Patel", "Sharma", "Singh", "Verma", "Gupta", "Yadav",
    "Mishra", "Tiwari", "Pandey", "Shukla", "Tripathi", "Joshi",
    "Mehta", "Kapoor", "Malhotra", "Khanna", "Bhatia", "Nair",
    "Menon", "Iyer", "Reddy", "Naidu", "Rao", "Chowdhury",
    "Das", "Dutta", "Chatterjee", "Banerjee", "Mukherjee",
    "Ghosh", "Sen", "Roy", "Barman", "Sarkar", "Pradhan",
    "Thapa", "Gurung", "Rai", "Limbu", "Magar", "Tamang",
    "Sherpa", "Newar", "Karki", "Khadka", "Bista", "Adhikari",
    "Poudel", "Paudel", "Shrestha", "Basnet", "Gautam", "Oli",
    "Acharya", "Baral", "Budhathoki", "Chaulagain", "Dahal",
    "Dangol", "Ghimire", "Khatri", "Lamichhane", "Maharjan",
    "Nepal", "Panta", "Pokharel", "Regmi", "Sapkota", "Subedi",
    "Thakuri", "Bhandari", "Chhetri", "KC", "GC", "BK",
    "Shahi", "Rana", "Khanal", "Sigdel", "Baniya", "Aryal",
    "Bhatta", "Dhakal", "Kharel", "Neupane", "Pandit",
    "Pathak", "Rijal", "Timilsina", "Wagle", "Upadhyay",
    "Mir", "Dar", "Lone", "Wani", "Bhat", "Rather",
    "Koul", "Pandita", "Sapru", "Razdan", "Dhar", "Handoo",
    "Matoo", "Khar", "Zargar", "Wadhwa", "Chawla", "Oberoi",
    "Arora", "Suri", "Luthra", "Ahuja", "Chadha", "Gulati",
    "Anand", "Bedi", "Duggal", "Grover", "Juneja", "Kakkar",
    "Mahajan", "Monga", "Puri", "Sehgal", "Talwar", "Vohra",
    "Bansal", "Bindra", "Chhabra", "Chugh", "Dhingra",
    "Goel", "Jain", "Lodha", "Mittal", "Nagpal", "Narang",
    "Saini", "Sodhi", "Tandon", "Trehan", "Uppal", "Walia"]
#-------------------------( FIRST MALE PAKISTAN )-------------------------#
first_names6=["Muhammad", "Ali", "Ahmed", "Hassan", "Hussain", "Usman", "Umar",
    "Hamza", "Bilal", "Saad", "Salman", "Zain", "Zaid", "Ayan",
    "Rehan", "Daniyal", "Haris", "Talha", "Abdullah", "Ibrahim",
    "Ismail", "Yahya", "Musa", "Isa", "Imran", "Farhan", "Fahad",
    "Fawad", "Noman", "Naveed", "Waqar", "Yasir", "Arslan", "Adeel",
    "Adnan", "Kamran", "Shahzaib", "Sheheryar", "Hammad", "Huzaifa",
    "Raza", "Rizwan", "Shafiq", "Zubair", "Qasim", "Saif", "Abbas",
    "Taha", "Asim", "Atif", "Waqas", "Imtiaz", "Sohail", "Shahid",
    "Rashid", "Nadeem", "Akram", "Junaid", "Majid", "Kashif",
    "Kamal", "Liaqat", "Luqman", "Moin", "Mustafa", "Nabeel",
    "Omer", "Owais", "Parvez", "Qadeer", "Rafay", "Raheel",
    "Saqlain", "Sarim", "Sarmad", "Shahmeer", "Shayan", "Sufyan",
    "Tabish", "Taimoor", "Usama", "Umer", "Waleed", "Zain Ali",
    "Ali Raza", "Muhammad Ali", "Abdul Basit", "Abdul Hadi",
    "Abdul Qadir", "Abdul Wahab", "Abdul Samad", "Abdul Aziz",
    "Abdul Jabbar", "Abdul Hakeem", "Abdul Latif",
    "Ahsan", "Asad", "Azhar", "Babar", "Faisal", "Ghazanfar",
    "Hasnain", "Ikram", "Irfan", "Javed", "Khalid", "Latif",
    "Mazhar", "Mehmood", "Mujtaba", "Nisar", "Qamar", "Rameez",
    "Saifullah", "Tariq", "Younis", "Zeeshan", "Zulfiqar"]
#-------------------------( LAST MALE PAKISTAN )-------------------------#
surnames6=["Khan", "Ahmed", "Ahmad", "Ali", "Hussain", "Hasan", "Abbas", "Shah",
    "Sheikh", "Malik", "Mirza", "Qureshi", "Siddiqui", "Farooq", "Usman",
    "Umar", "Tariq", "Javed", "Iqbal", "Akhtar", "Anwar", "Aslam", "Arif",
    "Bashir", "Saeed", "Imran", "Kamran", "Adil", "Rizvi", "Naqvi",
    "Zaidi", "Kazmi", "Gilani", "Bokhari", "Chishti", "Sabri", "Abbasi",
    "Chaudhry", "Gondal", "Jutt", "Bhatti", "Awan", "Syed", "Paracha",
    "Lodhi", "Afridi", "Shinwari", "Mehsud", "Wazir", "Bangash", "Kakar",
    "Marri", "Bugti", "Jamali", "Leghari", "Khattak", "Yousafzai",
    "Khokhar", "Arain", "Sial", "Wattoo", "Sandhu", "Gill", "Bajwa",
    "Randhawa", "Virk", "Sidhu", "Brar", "Sethi", "Bhutto", "Zardari",
    "Sharif", "Haider", "Raza", "Nadeem", "Shahzad", "Waqas", "Rauf",
    "Latif", "Shabbir", "Ilyas", "Zafar", "Jamil", "Munir", "Akram",
    "Nasir", "Sadiq", "Rashid", "Wahid", "Fawad", "Bilal", "Danish",
    "Haroon", "Salman", "Saqib", "Naveed", "Tanveer", "Khurram",
    "Shehzad", "Adnan", "Waleed", "Rehman", "Rahman", "Parvez",
    "Zubair", "Shafiq", "Shahid", "Sohail", "Umair", "Yasir",
    "Zia", "Furqan", "Raheel", "Rameez", "Ahsan", "Asad", "Irfan",
    "Nisar", "Mehmood",
    "Patel", "Sharma", "Singh", "Verma", "Gupta", "Yadav", "Mishra",
    "Tiwari", "Pandey", "Shukla", "Tripathi", "Joshi", "Mehta",
    "Kapoor", "Malhotra", "Khanna", "Bhatia", "Nair", "Menon",
    "Iyer", "Reddy", "Naidu", "Rao", "Chowdhury", "Das", "Dutta",
    "Chatterjee", "Banerjee", "Mukherjee", "Ghosh", "Sen", "Roy",
    "Barman", "Sarkar", "Pradhan", "Thapa", "Gurung", "Rai",
    "Limbu", "Magar", "Tamang", "Sherpa", "Newar", "Karki",
    "Khadka", "Bista", "Adhikari", "Poudel", "Paudel", "Shrestha",
    "Basnet", "Gautam", "Oli", "Acharya", "Baral", "Budhathoki",
    "Chaulagain", "Dahal", "Dangol", "Ghimire", "Khatri",
    "Lamichhane", "Maharjan", "Nepal", "Panta", "Pokharel",
    "Regmi", "Sapkota", "Subedi", "Thakuri", "Bhandari", "Chhetri",
    "KC", "GC", "BK", "Shahi", "Rana", "Khanal", "Sigdel",
    "Baniya", "Aryal", "Bhatta", "Dhakal", "Kharel", "Neupane",
    "Pandit", "Pathak", "Rijal", "Timilsina", "Wagle", "Upadhyay",
    "Mir", "Dar", "Lone", "Wani", "Bhat", "Rather", "Koul",
    "Pandita", "Sapru", "Razdan", "Dhar", "Handoo", "Matoo",
    "Khar", "Zargar", "Wadhwa", "Chawla", "Oberoi", "Arora",
    "Suri", "Luthra", "Ahuja", "Chadha", "Gulati", "Anand",
    "Bedi", "Duggal", "Grover", "Juneja", "Kakkar", "Mahajan",
    "Monga", "Puri", "Sehgal", "Talwar", "Vohra", "Bansal",
    "Bindra", "Chhabra", "Chugh", "Dhingra", "Goel", "Jain",
    "Lodha", "Mittal", "Nagpal", "Narang", "Saini", "Tandon",
    "Trehan", "Uppal", "Walia"]
#-------------------------( GIRL NAME PH )-------------------------#
def get_girl_name_ph():
    return random.choice(first_names1),random.choice(surnames1)
#-------------------------( BOY NAME PH )-------------------------#
def get_boy_name_ph():
    return random.choice(first_names2),random.choice(surnames2)
#-------------------------( GIRL NAME NEPAL )-------------------------#
def get_girl_name_nepal():
    return random.choice(first_names3),random.choice(surnames3)
#-------------------------( BOY NAME NEPAL )-------------------------#
def get_boy_name_nepal():
    return random.choice(first_names4),random.choice(surnames4)
#-------------------------( GIRL NAME PAKISTAN )-------------------------#
def get_girl_name_pakistan():
    return random.choice(first_names5),random.choice(surnames5)
#-------------------------( BOY NAME PAKISTAN )-------------------------#
def get_boy_name_pakistan():
    return random.choice(first_names6),random.choice(surnames6)
#-------------------------( FAKE NUMBER )-------------------------#
def generate_phone_number():
    countries={'BD': {'code': '+88','prefixes': ['017','018','019','016','015','013','014'],'length':8},
        'KH': {'code': '+855','prefixes': ['010','011','012','013','014','015','016','017','092','093','097','098','099'],'length':6},
        'NP': {'code': '+977','prefixes': ['97','98'],'length':8},
        'IN': {'code': '+91','prefixes': ['98','99','97','96','95','94'],'length':8},
        'PK': {'code': '+92','prefixes':[ '300','301','302','303','304','305'],'length':7},
        'UK': {'code': '+44','prefixes': ['7400','7500','7600','7700','7800','7900'],'length':6},
        'PH': {'code': '+63','prefixes': ['917','918','919','920','921','922'],'length':7},
        'ID': {'code': '+62','prefixes': ['813','815','816','817','818','819'],'length':7},
        'OM': {'code': '+968','prefixes': ['71','72','73','79'],'length':6},
        'US': {'code': '+1','prefixes': ['201','202','303','312','415','646','718'],'length':7},
        'NG': {'code': '+234','prefixes': ['701','703','704','705','706','707','708','802','803'],'length':7},
        'ZA': {'code': '+27','prefixes': ['60','61','62','63','71','72','73'],'length':7},
        'VN': {'code': '+84','prefixes': ['32','33','34','35','36','37','38','39','56','58','70','76','77','78','79','81','82','83','84','85','88','91','94','96','97','98','99'],'length': 7}}
    country=random.choice(list(countries.keys()))
    info=countries[country]
    prefix=random.choice(info['prefixes'])
    number=''.join(random.choices(string.digits,k=info['length']))
    return f"{info['code']}{prefix}{number}"
#-----------------------( AUTO PASSWORD )-----------------------#
def get_pass():
    name_part=''.join(random.choices(string.ascii_letters,k=random.randint(5,7)))
    name_part=name_part.capitalize() if random.choice([True,False]) else name_part.lower()
    symbol_part=''.join(random.choices('!@#$%^&*()_+=',k=random.randint(2,3)))
    digit_part=''.join(random.choices(string.digits,k=random.randint(2,4)))
    end_part=''.join(random.choices(string.ascii_letters,k=random.randint(2,4)))
    optional_upper=''.join(random.choices(string.ascii_uppercase,k=random.randint(1,2)))
    parts=[name_part,symbol_part,digit_part,end_part,optional_upper]
    random.shuffle(parts)
    return ''.join(parts)
#-----------------------( ??? )-----------------------#
try:
    android_version=subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').strip()
    model=subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').strip()
    build=subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').strip()
    fbmf=subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').strip()
    fbbd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').strip()
    fbca=subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',', ':').strip()
    fbdm=f"{{density=2.25,height={subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True).decode('utf-8').strip()},width={subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').strip()}}}"
    try:
        fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].strip()
    except:
        fbcr='ZONG'
except:
    android_version,model,build,fbmf,fbbd,fbca,fbdm,fbcr='10','Unknown','Unknown','Unknown','Unknown','arm64-v8a','{density=2.25,height=720,width=1280}','ZONG'
device={'android_version': android_version,'model': model,'build': build,'fblc': 'en-US','fbmf': fbmf,'fbbd': fbbd,'fbdv': model,'fbsv': android_version,'fbca': fbca,'fbdm': fbdm}
#-----------------------( EXTRACTOR )-----------------------#
def extractor(data):
    soup=BeautifulSoup(data,"html.parser")
    data={}
    for inputs in soup.find_all("input"):
        name=inputs.get("name")
        value=inputs.get("value")
        if name:
            data[name]=value
    return data
#-----------------------( VERSION )-----------------------#
versn='0.1';version=str(versn)
#-----------------------( SHORT )-----------------------#
__COUNTRYS__=af['country'].upper()
os.system("xdg-open https://t.me/+ySgl6S0nEZwwYWFl")
#-----------------------( LOGO )-----------------------#
logo=("""\033[1;32m    ██   ██ ██ ████████ ████████ ██    ██ 
    ██  ██  ██    ██       ██     ██  ██  
    █████   ██    ██       ██      ████   
    ██  ██  ██    ██       ██       ██    
    ██   ██ ██    ██       ██       ██""")
#-----------------------( INFO )-----------------------#
info=(f"""{xp} AUTHOR    {xpxxx} {green}MR-ERROR
{xp} FACEBOOK  {xpxxx} {green}NIKA BREVOUR
{xp} TYPE      {xpxxx} {green}AUTO CREATE FACEBOOK
{xp} OWNER    {xpxxx} {green}NIKA BREVOUR/FLARE
{xp} STATUS    {xpxxx} {green}PAID
{xp} VERSION   {xpxxx} {green}{version}{reset}
{xp} KEY       {xpxxx} {green}{final_key}""")
#-----------------------( LOOP )-----------------------#
loop=0
tl=0
ok_count=0
cp_count=0
dones=[]
oks=[]
cps=[]
nov=[]
kitty=[]
nvs=[]
twf=[]
gen=[]
plist=[]
__COOKIE__=[]
__CP__=[]
__LOCK__=[]
#-----------------------( API BYPASS )-----------------------#
def http_canary():
    try:
        if os.path.exists(os.path.join(path_canary,package_name)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        if os.path.exists(os.path.join(path_canary2,package_name2)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary3,package_name3)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary4,package_name4)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary5,package_name5)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary6,package_name6)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        else:
            pass
    except:
        system("clear" if os.name == "posix" else "cls")
        print(f"{xp} TURN ON STORAGE PERMISSION")
        exit('\n')
#-----------------------( MAIN/MENU )-----------------------#
def __MENU__():
    __ERRORLOGO__()
    print(f"{xp1} AUTO CREATE FB ")
    print(f"{xp2} 2FA ")
    print(f"{xp3} COOKIE EXTRACT ")
    print(f"{xp0} EXIT TOOLS ")
    __LINE__()
    __MENUC__=input(f"{xpx} INPUT MENU {xpxxx} ")
    if __MENUC__=="1":
       __AUTOX__()
    elif __MENUC__=="2":__2FAX__()
    elif __MENUC__=="3":__COKIX__()
    elif __MENUC__=="0":__LINE__();print(f"{xp} EXIT SUCCESSFULLY ");time.sleep(1.1);__LINE__();os.system(f"exit")
    else:__LINE__();print(f"{xpxx} INVALID OPTION TRY AGAIN ");time.sleep(1);__MENU__()
#-----------------------( MAIN/MENU )-----------------------#
def __MENU__():      
    __ERRORLOGO__()
    print(f"{xp1} AUTO CREATE FB ")
    print(f"{xp2} 2FA ")
    print(f"{xp3} COOKIE EXTRACT ")
    print(f"{xp0} EXIT TOOLS ")
    __LINE__()
    __MENUC__=input(f"{xpx} INPUT MENU {xpxxx} ")
    if __MENUC__=="1":
       __AUTOX__()
    elif __MENUC__=="2":__2FAX__()
    elif __MENUC__=="3":__COKIX__()
    elif __MENUC__=="0":__LINE__();print(f"{xp} EXIT SUCCESSFULLY ");time.sleep(1.1);__LINE__();os.system(f"exit")
    else:__LINE__();print(f"{xpxx} INVALID OPTION TRY AGAIN ");time.sleep(1);__MENU__()
#-----------------------( AUTO-MENU )-----------------------#
def __AUTOX__():
    __ERRORLOGO__()
    __NUM__=input(f"{xp} HOW MANY FACEBOOK ACCOUNT LIMIT {xpxxx}︎ ")
    __ERRORLOGO__()
    print(f"{xp1} GIRL NAME PHILIPPINES ")
    print(f"{xp2} BOY NAME PHILIPPINES ")
    print(f"{xp3} GIRL NAME NEPAL ")
    print(f"{xp4} BOY NAME NEPAL ")
    print(f"{xp5} GIRL NAME PAKISTAN ")
    print(f"{xp6} BOY NAME PAKISTAN ")
    __LINE__()
    __NAME__=input(f"{xpx} INPUT NAME {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp1} FEMALE ")
    print(f"{xp2} MALE ")
    __LINE__()
    __GENDER__=input(f"{xpx} INPUT GENDER {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp1} AUTO PASSWORD ")
    print(f"{xp2} AUTO PASSWORD WITH NAMENUMBER ")
    print(f"{xp3} AUTO PASSWORD WITH SURNAME ")
    print(f"{xp4} MANUAL CUSTOM PASSWORD ")
    __LINE__()
    __PASS__=input(f"{xpx} INPUT PASSWORD {xpxxx} ")
    if __PASS__=="4":pww=input(f"{xpx} ETHER CUSTOMER PASSWORD {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp} SHOW ALL DETAILS...? ")
    __LINE__()
    show_details=input(f"{xpx} {white}[{green}Y{white}/{red}N{white}] {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp} TOTAL NEW ACCOUNT IDS {xpxxx} {__NUM__}")
    print(f"{xp} CREATING ACCOUNT STARTED")
    print(f"{xp} USER 1.1.1 VPN")
    __LINE__()
    for _ in range(int(__NUM__)):
        try:
            global oks,cps
            color=random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r {white}[{green}KITTY-CREATE{white}]-{white}[{green}OK:-%s{white}] '%(len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            ses=requests.Session()
            response=ses.get("https://x.facebook.com/reg")
            form=extractor(response.text)
            if __NAME__=="1":firstname,lastname=get_girl_name_ph()
            elif __NAME__=="2":firstname,lastname=get_boy_name_ph()
            elif __NAME__=="3":firstname,lastname=get_girl_name_nepal()
            elif __NAME__=="4":firstname,lastname=get_boy_name_nepal()
            elif __NAME__=="5":firstname,lastname=get_girl_name_pakistan()
            elif __NAME__=="6":firstname,lastname=get_boy_name_pakistan()
            if __GENDER__=="1":sex,gender="1","Female"
            elif __GENDER__=="2":sex,gender="2","Male"
            if __PASS__=="1":pww=get_pass()
            if __PASS__=="2":pww=f"{firstname.lower()}{random.choice([123,12345,123456,1234567,123456789,1234567890,143,143143,123123])}"
            if __PASS__=="3":pww=f"{firstname.lower()}{lastname.lower()}"
            phone=generate_phone_number()
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'lastname': lastname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': sex,
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": ___EthanAutoUa2___(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ___EthanAutoUa2___()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers,proxies=ethanproxy())
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
                coki="sb=Cracked.By-Error_Tool;"+";".join([f"{key}={value}" for key,value in login_coki.items()])
                uid=login_coki["c_user"]
                if show_details=='y':
                    print(f"\r{xp} NAME     {xpxxx} {firstname} {lastname}\033[1;37m")
                    print(f"\r{xp} NUMBER   {xpxxx} {phone}\033[1;37m")
                    print(f"\r{xp} GENDER   {xpxxx} {gender}\033[1;37m")
                    print(f"\r{xp} BIRTHDAY {xpxxx} {payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}\033[1;37m")
                    print(f"\r{xp} UID      {xpxxx} {uid}\033[1;37m")
                    print(f"\r{xp} PASS     {xpxxx} {pww}\033[1;37m")
                    print(f"\r{xp} COOKIE   {xpxxx} {coki}\033[1;37m")
                    __LINE__()
                else:
                    print(f'\r{green} [KALYAN-OK] '+uid+' | '+pww+'\033[1;97m')
                open('/sdcard/KALYAN-AUTO/AUTO/KALYAN-AUTO-OK.txt', 'a').write(uid+'|'+pww+'|'+coki+'\n')
                oks.append(uid)
            elif "checkpoint" in login_coki:
                uid=login_coki.get("c_user","unknown")
                cps.append(uid)
            time.sleep(1)
        except Exception as e:pass
    print("\033[1;37m")
    __LINE__()
    print(f"{xp} THE PROCESS HAS COMPLETED...!")
    __LINE__()
    print(f"{xp} {green}TOTAL OK {xpxxx} {len(oks)}")
    print(f"{xp} {red}TOTAL CP {xpxxx} {len(cps)}")
    print(f"{xp} {blue}TOTAL 2F {xpxxx} {len(twf)}")
    __LINE__()
    print(f"{xp} THANKS FOR USING.....! ")
    __LINE__()
    exit()
#-----------------------( 2FA-MENU )-----------------------#
def __2FAX__():
    print(f"{xp} COMING SOON")
    exit()
#-----------------------( COKI-MENU )-----------------------#
def __COKIX__():
    print(f"{xp} COMING SOON")
    exit()
#-----------------------( LAST-CALL )-----------------------#
__MENU__()
#-----------------------( END-CALL )-----------------------#
