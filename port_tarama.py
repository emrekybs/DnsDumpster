#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print(""" 
Port tarama 

1)Hızlı Tarama
2)Servis ve Versiyon Bilgisi
3)Isletim Sistemi Bilgisi



""")

islemno = input("Islem Numarasini Girin: ")

if(islemno=="1"):
          hedefip = input("Hedef Ip Girin: ")
          os.system("nmap " + hedefip)
elif(islemno=="2"):
          hedefip = input("Hedef Ip Girin: ")
          os.system("nmap -sS sV " + hedefip)
elif(islemno=="3"):
          hedefip = input("Hedef Ip Girin: ")
          os.system("nmap -0 " + hedefip)
else: 
       print(" none :(")

