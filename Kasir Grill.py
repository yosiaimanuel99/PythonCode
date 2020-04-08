ulang="y"
while ulang=="Y" or ulang=="y":
    print("==========================================================")
    print("=======================Nongki Grill=======================")
    print("==========================================================")
    nama=input("Nama Pemesan\t:")
    jam=int(input("Jam Pemesanan\t:"))
    jmlh1=int(input("Jumlah orang\t:"))
    paket=input("Paket(A/B/C/D)\t:")
    bayar=input("Pembayaran(Debit/Credit/Cash)\t:")
    ##Pemesanan
    if jam==9 or jam<=11 :
        waktu="Pagi"
        durasi="60 Menit"
    elif jam==12 or jam<=15:
        waktu="Siang" 
        durasi="80 Menit"
    elif jam==16 or jam<=19:
        waktu="Sore"
        durasi="80 Menit"
    elif jam==20 or jam<=22:
        waktu="Malam"
        durasi="90 Menit"
        if paket=="A" or paket=="a":
            namaPaket="Beef Lover"
            if waktu=="Pagi":
                price=60000
            elif waktu=="Siang":
                price=65000
            elif waktu=="Sore":
                price=70000
            elif waktu=="Malam":
                price=75000
        elif paket=="B" or paket=="b":
            namaPaket="Meat Supreme"
            if waktu=="Pagi":
                price=65000
            elif waktu=="Siang":
                price=70000
            elif waktu=="Sore":
                price=75000
            elif waktu=="Malam":
                price=80000
        elif paket=="C" or paket=="c":
            namaPaket="Meat Premium"
            if waktu=="Pagi":
                price=70000
            elif waktu=="Siang":
                price=75000
            elif waktu=="Sore":
                price=80000
            elif waktu=="Malam":
                price=85000
        elif paket=="D" or paket=="d":
            namaPaket="Beef + Meet Premium"
            if waktu=="Pagi":
                price=85000
            elif waktu=="Siang":
                price=90000
            elif waktu=="Sore":
                price=95000
            elif waktu=="Malam":
                price=100000
    else:
        waktu=""
        durasi=""
        namaPaket=""
        price=0
    ##Pembayaran
    if jmlh1>=4:
        jmlh2=jmlh1-1
        if bayar=="Debit" or bayar=="debit":
            potongan=0.2
        elif bayar=="Credit" or bayar=="credit":
            potongan=0.1
    else:
        jmlh2=jmlh1-0
        potongan=0
    PPN=0.1
    subtotal=price*jmlh2
    ppn=subtotal*PPN
    diskon=subtotal*potongan
    total=subtotal+ppn-diskon
    print(nama)
    print(jam)
    print(durasi)
    print(jmlh1)
    print(jmlh2)
    print(namaPaket)
    print(price)
    print(bayar)    
    print(subtotal)
    print(ppn)
    print(diskon)
    print(total)
    

