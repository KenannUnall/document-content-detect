import os
import shutil
import random

def split_dataset(
    images_dir,
    labels_dir,
    output_dir,
    train_split=0.75,
    val_split=0.2,
    test_split=0.05,
    exts=(".jpg", ".png")
):
    # Çıktı klasörleri
    train_dir = os.path.join(output_dir, "train")
    val_dir = os.path.join(output_dir, "val")
    test_dir = os.path.join(output_dir, "test")

    for folder in [train_dir, val_dir, test_dir]:
        os.makedirs(os.path.join(folder, "images"), exist_ok=True)
        os.makedirs(os.path.join(folder, "labels"), exist_ok=True)

    # Dosyaları listele
    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(exts)]

    if not image_files:
        print("Hiç görsel bulunamadı.")
        return

    # Karıştır ve böl
    random.shuffle(image_files)
    total = len(image_files)
    train_count = int(total * train_split)
    val_count = int(total * val_split)

    train_files = image_files[:train_count]
    val_files = image_files[train_count:train_count + val_count]
    test_files = image_files[train_count + val_count:]

    def copy_files(file_list, dest_dir):
        for file in file_list:
            image_path = os.path.join(images_dir, file)
            label_path = os.path.join(labels_dir, os.path.splitext(file)[0] + ".txt")

            shutil.copy(image_path, os.path.join(dest_dir, "images", file))
            if os.path.exists(label_path):
                shutil.copy(label_path, os.path.join(dest_dir, "labels", os.path.basename(label_path)))
            else:
                print(f"Uyarı: Etiket dosyası bulunamadı: {label_path}")

    copy_files(train_files, train_dir)
    copy_files(val_files, val_dir)
    copy_files(test_files, test_dir)

    print(f"Toplam {total} görsel: {len(train_files)} train, {len(val_files)} val, {len(test_files)} test olarak ayrıldı.")

if __name__ == "__main__":
    split_dataset(
        images_dir="C:/Users/KENAN/Desktop/last_dataset/dataset/images",
        labels_dir="C:/Users/KENAN/Desktop/last_dataset/dataset/labels",
        output_dir="C:/Users/KENAN/Desktop/last_dataset/dataset-split",
        train_split=0.75,
        val_split=0.2,
        test_split=0.05
    )
