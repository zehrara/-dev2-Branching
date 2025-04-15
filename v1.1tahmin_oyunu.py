import random

def zorluk_sec():
    print("Zorluk seviyeni seç:")
    print("1 - Kolay (10 tahmin)")
    print("2 - Orta (7 tahmin)")
    print("3 - Zor (5 tahmin)")
    
    while True:
        secim = input("Seçimin (1/2/3): ")
        if secim == "1":
            return 10
        elif secim == "2":
            return 7
        elif secim == "3":
            return 5
        else:
            print("Lütfen 1, 2 veya 3 gir.")

def oyun():
    print("🎮 Sayı Tahmin Oyununa Hoş Geldin!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
    
    tahmin_hakki = zorluk_sec()
    gizli_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    while tahmin_hakki > 0:
        try:
            tahmin = int(input("Tahminin nedir? "))
            tahmin_sayisi += 1
            tahmin_hakki -= 1

            if tahmin < gizli_sayi:
                print(f"Daha büyük bir sayı dene. Kalan hakkın: {tahmin_hakki}")
            elif tahmin > gizli_sayi:
                print(f"Daha küçük bir sayı dene. Kalan hakkın: {tahmin_hakki}")
            else:
                print(f"🎉 Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettin!")
                break
        except ValueError:
            print("Lütfen sadece sayı gir.")
    
    else:
        print(f"😢 Tahmin hakkın bitti! Doğru sayı: {gizli_sayi}")

if __name__ == "__main__":
    oyun()
