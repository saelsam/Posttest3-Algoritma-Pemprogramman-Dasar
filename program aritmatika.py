import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen() 
print("-"*60)
print ("\tAplikasi Penghitung Volume Bangun Ruang")
print("-"*60)

bangun = ['Kubus' , 'Balok' , 'Limas' , 'Kerucut' , 'Tabung' , 'Prisma' , 'Bola' ]
tool = ['panjang_alas', 'lebar_alas', 'tinggi_alas', 'sisi', 'jari_jari', 'alas_segitiga', 'luas alas', 'volume', 'tinggi_segitiga']
print("[1] Volume", bangun[0])
print("[2] Volume", bangun[1])
print("[3] Volume", bangun[2])
print("[4] Volume", bangun[3])
print("[5] Volume", bangun[4])
print("[6] Volume", bangun[5])
print("[7] Volume", bangun[6])
nama = int (input("Masukkan Bangun Ruang Yang Dipilih (1-7): "))

clear_screen()
if nama == 1:
    print("-"*60)
    print ("\t\t       VOLUME KUBUS ")
    print("-"*60)
    tool[4] = float(input("Masukkan panjang sisi : "))
    volume = tool[4] * tool[4] * tool[4]
    print ("Volume", bangun[0], "=", volume)

elif nama == 2 :
    print("-"*60)
    print ("\t\t       VOLUME BALOK ")
    print("-"*60)
    tool[1] = float(input("Masukkan panjang : "))
    tool[2] = float (input("Masukkan lebar : "))
    tool[3] = float (input("Masukkan tinggi : "))
    tool[7] = tool[1] * tool[2] * tool[3]
    print ("Volume", bangun[1], "=", tool[7])

elif nama == 3 :
    print("-"*60)
    print ("\t\t       VOLUME LIMAS ")
    print("-"*60)
    print ("\t       Mencari Luas Alas Limas")
    tool[0] = float(input("Masukkan Panjang Alas : "))
    tool[1] = float(input("Masukkan Lebar Alas : "))
    print ("Luas Alas = ", tool[0] * tool[1])
    tool[2] = float(input("Masukkan Tinggi Limas : "))
    tool[7] = tool[0] * tool[1] * tool[2]
    print ("Volume", bangun[2], "=", tool[7])

elif nama == 4 :
    print("-"*60)
    print ("\t\t       VOLUME KERUCUT ")
    print("-"*60)
    print ("Mencari Luas Alas Kerucut : ")
    tool[4] = float (input("Masukkan Jari-Jari Alas : "))
    print ("Luas Alas = ", 22 / 7 * tool[4] * tool[4])
    tool[2] = float(input("Masukkan Tinggi Kerucut : "))
    tool[7] = 1 / 3 * 22 / 7 * tool[4] * tool[4] * tool[2]
    print ("Volume", bangun[3], "=", tool[7])

elif nama == 5 :
    print("-"*60)
    print ("\t\t       VOLUME TABUNG ")
    print("-"*60)
    print ("Mencari Luas Alas Tabung")    
    tool[4] = float(input("Masukkan Jari-Jari Alas : "))
    print ("Luas Alas = ", 22 / 7 * tool[4] * tool[4])
    tool[2] = float(input("Masukkan Tinggi Tabung : "))
    tool[7] = 22 / 7 * tool[4] * tool[4] * tool[2]
    print ("Volume", bangun[4], "=", tool[7])

elif nama == 6 :
    print("-"*60)
    print ("\t\t       VOLUME PRISMA ")
    print("-"*60)
    print ("Mencari Luas Alas Dalam Bentuk Segitiga")
    tool[5] = float(input ("Masukkan Alas Segitiga : "))
    tool[8] = float(input ("Masukkan Tinggi Segitiga : "))
    print ("Luas Alas = ", 1 / 2 * tool[5] * tool[8] )
    tool[2] = float(input("Masukkan Tinggi Prisma : "))
    tool[7] = 1 / 2 * tool[5] * tool[8] * tool[2]
    print ("Volume", bangun[5], "=", tool[7])

elif nama == 7 :
    print("-"*60)
    print ("\t\t       VOLUME BOLA ")
    print("-"*60)
    tool[4] = float(input("Masukkan Jari-Jari Bola : "))
    tool[7] = 4 / 3 * 22 / 7 * tool[4] * tool[4] * tool[4]
    print ("Volume", bangun[6], "=", tool[7])