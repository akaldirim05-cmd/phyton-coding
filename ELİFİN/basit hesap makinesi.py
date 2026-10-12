print("Basit Hesap Makinesi")

sayi1 = float(input("Birinci sayıyı gir: "))
islem = input("İşlem seç (+, -, *, /): ")
sayi2 = float(input("İkinci sayıyı gir: "))

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 == 0:
        print("Bir sayı sıfıra bölünemez.")
    else:
        sonuc = sayi1 / sayi2
else:
    print("Geçersiz işlem girdin.")

if islem in ("+", "-", "*") or (islem == "/" and sayi2 != 0):
    print("Sonuç:", sonuc)