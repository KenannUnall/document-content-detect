import os

# Düzenlemek istediğin dizini belirt
dizin_yolu = "C:\\Users\\KENAN\\Desktop\\datasets-v2\\stamp\\valid\\labels"

# Dizindeki tüm txt dosyalarını al
txt_dosyalari = [f for f in os.listdir(dizin_yolu) if f.endswith('.txt')]

for dosya_adi in txt_dosyalari:
    dosya_yolu = os.path.join(dizin_yolu, dosya_adi)
    
    # Dosyayı oku
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        satirlar = dosya.readlines()
    
    # Her satırın ilk karakterini 'X' ile değiştir
    yeni_satirlar = []
    for satir in satirlar:
        if satir.strip():  # Boş satırları atla
            yeni_satirlar.append('4' + satir[1:])
        else:
            yeni_satirlar.append(satir)
    
    # Değişiklikleri dosyaya yaz
    with open(dosya_yolu, 'w', encoding='utf-8') as dosya:
        dosya.writelines(yeni_satirlar)

print("Tüm txt dosyaları başarıyla güncellendi.")
