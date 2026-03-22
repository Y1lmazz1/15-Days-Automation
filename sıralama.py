import os

def dosyalari_numaralandir(klasor_yolu):
    # Klasördeki dosyaları listele
    dosyalar = os.listdir(klasor_yolu)
    
    # Dosyaları alfabetik sıraya diz (işlem sırasının karışmaması için)
    dosyalar.sort()

    sayac = 1
    for dosya_adi in dosyalar:
        # Dosyanın tam yolunu oluştur
        eski_yol = os.path.join(klasor_yolu, dosya_adi)
        
        # Klasörleri atla, sadece dosyaları işle
        if os.path.isfile(eski_yol):
            # Dosya uzantısını al (.jpg, .txt vb.)
            uzanti = os.path.splitext(dosya_adi)[1]
            
            # Yeni dosya adını oluştur (Örn: 1.jpg)
            yeni_ad = f"{sayac}{uzanti}"
            yeni_yol = os.path.join(klasor_yolu, yeni_ad)
            
            # Yeniden adlandır
            os.rename(eski_yol, yeni_yol)
            print(f"Değiştirildi: {dosya_adi} -> {yeni_ad}")
            
            sayac += 1

# Kendi klasör yolunu buraya yaz (Windows için ters eğik çizgilere dikkat: r"C:\Dosyalar" gibi)
hedef_klasor = r"C:\Users\YILMAZ\Desktop\dogungunu"
dosyalari_numaralandir(hedef_klasor)