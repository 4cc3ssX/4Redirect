# 4Redirect

This is the open redirect scanner using Python. If any bug or error please contact me. Thank u!❤️

# Usage
default files

**payloads.txt** : for payloads list

**sites.txt** : for targets website list

```
root@kali:~# python3 4redirect.py


  ____ ___         ___             __ 
 / / // _ \___ ___/ (_)______ ____/ /_
/_  _/ , _/ -_) _  / / __/ -_) __/ __/
 /_//_/|_|\__/\_,_/_/_/  \__/\__/\__/

  MSF: http://www.mmsecurity.net/forum/member.php?action=register&referrer=9450
		                 		v1.0 
    
[ TARGET ] Websites list file path. default[sites.txt]: 
[ SYMBOLS ] Special character. default[!!]: 
[ PAYLOAD ] Payload list path. default[payloads.txt]: 
------------------------------------------------------------
[ SCAN ] Scanning the target(s)...

[ VULNERABLE ] http://localhost/redirect.php?url=http://www.google.com <302>
[ VULNERABLE ] http://localhost/redirect2.php?url=http://www.google.com <302>
[ VULNERABLE ] http://localhost/redirect3.php?url=http://www.google.com <302>

[ SUCCESS ] Success rate: 100.00%

```

# Disclaimer

Author will not responsible for any misuses and unauthorized action. Use at your own risk.
