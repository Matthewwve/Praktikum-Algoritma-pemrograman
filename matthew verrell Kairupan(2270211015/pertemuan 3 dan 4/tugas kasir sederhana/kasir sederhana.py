print("--------------------------------------------------")
print("----------------- Dimsum Matthew -----------------")
print("--------------------------------------------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsibelanja():
   global totalbeli
   global porsi
   global beli
   print("\n------------------ MENU DIMSUM ------------------")
   print("1. chiken dimsum - Rp 24000")
   print("2. vegie dimsum - Rp 22000")
   print("3. fish dimsum - Rp 24000")
   print("4. mushroom dimsum - Rp 23000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalbeli=porsi*24000
       print (porsi," porsi chiken dimsum = Rp", totalbeli)
       beli=("chiken dimsum")
   elif nomor==2:
       totalbeli=porsi*22000
       print (porsi," porsi vegie dimsum = Rp", totalbeli)
       beli=("vegie dimsum")
   elif nomor==3:
       totalbeli=porsi*24000
       print (porsi, " porsi fish dimsum = Rp", totalbeli)
       beli=("fish dimsum")
   elif nomor==4:
       totalbeli=porsi*23000
       print (porsi, " porsi mushroom dimsum = Rp", totalbeli)
       beli=("mushroom dimsum")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsibelanja()
totalsemua=totalbeli

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n================== STRUK BELANJA ====================")
print("\n================== DIMSUM MATTHEW ===================")
print("alamat : Bekasi, Jatisampurna")
print("no telf : 08121271230")

import datetime
x=datetime.datetime.now()
print(x)

print("=====================================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,beli,"( Rp", totalbeli,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("=====================================================")
print("========== TERIMA KASIH TELAH MEMBELI ===============")
print("=====================================================")