print("-"*60)
print ("\t\t\tSelamat Datang Di Toko Kue Sule")
print("-"*60)

keju = 6000
coklat = 3500

k = float(input("Masukkan jumlah kue keju : "))
c = float(input("Masukkan jumlah kue coklat : "))

#harga diskon = 1 - persentase diskon
# diskon 10% ----> harga diskon = 1 - 0,1 = 0,9

#kue keju
if k >= 1 and k <= 3 :
     k = k * keju
     print("Harga Kue Keju = Rp.",k)    
elif k >= 4 and k <= 15 :
    #diskon 10%
     k = k * keju * 0.9
     print("Harga Kue Keju = Rp.",k)
elif k >= 16 and k <= 25 :
    #diskon 15%
     k = k * keju * 0.85
     print("Harga Kue Keju = Rp.",k)
else :
    print("Maaf jumlah pesanan Kue Keju tidak sesuai ")

#kue coklat
if c >= 1 and c <= 4 :
     c = c * coklat
     print("Harga Kue Coklat = Rp.",c)
elif c >= 5 and c <= 20 :
    #diskon 7%
     c = c * coklat * 0.93
     print("Harga Kue Coklat = Rp.",c)
elif c >= 21 and c <= 35 :
    #diskon 12%
     c = c * coklat * 0.88
     print("Harga Kue Coklat = Rp.",c)
else :
    print("Maaf jumlah pesanan Kue Colkat tidak sesuai")