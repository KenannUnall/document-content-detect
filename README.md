# Document Content Detect

Bu proje, görsellerdeki belge içeriklerini tespit etmek için YOLO tabanlı bir nesne algılama modeli kullanır. Proje, birden fazla belge görseli üzerinde toplu olarak çalışabilir ve tespit edilen sonuçları hem ekrana yazdırır hem de çıktı görsellerini kaydeder.

## Özellikler

- YOLO modeli ile belge içeriği tespiti
- Birden fazla görselde toplu (batch) işleme
- Sonuçların görselleştirilmesi ve kaydedilmesi

## Gereksinimler

- Python 3.8+
- [Ultralytics YOLO](https://docs.ultralytics.com/)
- Gerekli ek kütüphaneler: `pip install ultralytics`

## Kullanım

1. **Model Ağırlıklarını Ekleyin:**  
   `weights/best.pt` dosyasını projenizin `weights` klasörüne yerleştirin. Model ağırlık dosyasına [buradan](https://huggingface.co/Kenan-Unal/document-content-detect) erişebilirsiniz.

2. **Görselleri Ekleyin:**  
   Tespit yapmak istediğiniz görselleri `docs` klasörüne ekleyin ve `docs_path` listesine dosya adlarını ekleyin.

3. **Çalıştırın:**  
   Terminalde aşağıdaki komutu kullanarak scripti çalıştırın:
   ```bash
   python document-detection.py
   ```

4. **Sonuçlar:**  
   - Tespit edilen kutular ve sınıflar terminalde görüntülenir.
   - Sonuç görselleri `result` klasörüne kaydedilir.

## Dosya Açıklamaları

- `document-detection.py`: Ana tespit scripti.
- `weights/best.pt`: Eğitilmiş YOLO model ağırlıkları.
- `docs/`: Test edilecek görsellerin bulunduğu klasör.
- `result/`: Sonuç görsellerinin kaydedileceği klasör.

## Katkı

Katkıda bulunmak isterseniz, lütfen bir fork oluşturup pull request gönderin.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. 