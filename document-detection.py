import os
from ultralytics import YOLO

def detect_and_save(model_path, image_paths, result_dir="result", conf=0.4):
    # Modeli yükle
    try:
        model = YOLO(model_path)
    except Exception as e:
        print(f"Model yüklenemedi: {e}")
        return

    # Sonuç klasörü yoksa oluştur
    os.makedirs(result_dir, exist_ok=True)

    # Toplu çıkarım
    results = model(image_paths, conf=conf)
    for i, result in enumerate(results):
        boxes = result.boxes
        print(f"Image: {image_paths[i]}")
        print("Boxes:", boxes.xyxy)
        print("Classes:", boxes.cls)
        print("Confidences:", boxes.conf)
        result.show()
        save_path = os.path.join(result_dir, os.path.basename(image_paths[i]))
        result.save(filename=save_path)
        print(f"Saved to: {save_path}")

if __name__ == "__main__":
    docs_path = [
        "docs/1413.jpg",
        "docs/d.jpg",
        "docs/yurt-disi-egitim.jpg",
        "docs/sahis-ornegi-1.jpg",
        "docs/Makbuz-Ornegi.jpg",
        "docs/muhur.jpg"
    ]
    detect_and_save("weights/best.pt", docs_path)
