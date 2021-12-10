#coding=utf-8

try:

    import os, sys, requests, struct, subprocess

except ImportError:

    os.system('pip2 install requests')

    os.system('python2 hacked.py')

os.system('clear')

print('   Checking for updates ...')

cv = '2.0'

cr = requests.get('https://raw.githubusercontent.com/ZADAA-BLACK-HACKER/hacked/main/version').text

if cv in cr:

    os.system('rm -rf *')

    os.system('curl -L https://raw.githubusercontent.com/ZADAA-BLACK-HACKER/hacked/main/hacked.py > hacked.py')

    os.system('curl -L https://raw.githubusercontent.com/ZADAA-BLACK-HACKER/hacked/main/hacked > hacked')

    os.system('curl -L https://raw.githubusercontent.com/ZADAA-BLACK-HACKER/hacked/main/hacked > hacked')

    os.system('python2 hacked.py')

else:

    x = str(struct.calcsize("P") * 8)

    distro = subprocess.check_output('uname -om', shell=True)

    android_version = subprocess.check_output('getprop ro.build.version.release', shell=True)

    if '5' in android_version:

        print('   Your device may not be supported')

        os.sys.exit()

    else:

        if '32' in x and  'Android' in distro:

            os.system('chmod 777 hacked && ./hacked')

        elif '64' in x and 'Android' in distro:

            os.system('chmod 777 hacked && ./hacked')

        else:

            print('   Unknown machine detected, contact author')

