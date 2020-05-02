import requests,sys,os,json
from threading import Thread

r = '\033[031m'
g = '\033[032m'
y = '\033[033m'
b = '\033[036m'
n = '\033[00m'
cookies = {} 
headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
vuln_vitims = {}
def main():
    path = input(f"[ {y}TARGET{n} ] Websites list file path. default[sites.txt]: ")
    path = path if path else "sites.txt"
    special_char = input(f"[ {y}SYMBOLS{n} ] Special character. default[!!]: ")
    special_ = special_char if special_char else "!!"
    paylist = input(f"[ {y}PAYLOAD{n} ] Payload list path. default[payloads.txt]: ")
    paylist = paylist if paylist else "payloads.txt"
    print('-'*60)
    if os.path.isfile(path) and os.path.isfile(paylist):
        p = open(path, 'r').readlines()
        pay = open(paylist, 'r').readlines()
        if len(p) >= 1 and len(pay) >= 1:
            print(f"[ {y}SCAN{n} ] Scanning the target(s)...\n")
            for target in p:
                for payload in pay:
                    t = Thread(target=scan, args=(target.rstrip(),payload.rstrip(),special_))
                    t.start()
                    t.join()
        else:
            print(f"[ {r}ERROR{n} ] Your url or payload file seem empty!")
            sys.exit(0)
        if bool(vuln_vitims):
            for url,code in vuln_vitims.items():
                if code == 301 or code == 302:
                    print(f"[ {g}VULNERABLE{n} ] %s <%d>" % (url,code))
                else:
                    print(f"[ {r}NOT VULNERABLE{n} ] %s <%d>" % (url,code))
        print(f"\n[ {g}SUCCESS{n} ] Success rate: {len(vuln_vitims.keys())/len(p)*100:.2f}%")
    else:
        print(f"[ {r}NOT FOUND{n} ] Payload or Url file not found!")
def scan(target,payload,special):
    r = requests.get(target.replace(special, payload), cookies=cookies, headers=headers, verify=False, allow_redirects=False)
    vuln_vitims[target.replace(special, payload)] = r.status_code
    return 0
if __name__ == '__main__':
    banner = r"""
  {r}____ ___         {b}___    {g}         __ 
 {r}/ / // _ \___ {b}___/ (_)___{g}___ ____/ /_
{r}/_  _/ , _/ -_){b} _  / / __/{g} -_) __/ __/
 {r}/_//_/|_|\__/{b}\_,_/_/_/  {g}\__/\__/\__/

  {r}MSF{b}: http://www.{n}mmsecurity.n{g}et/forum/member.php?action=register&referrer=9450{n}
		                 		{r}v1.0{n} 
    """.format(r=r,g=g,b=b,n=n)
    print(banner)
    main()
