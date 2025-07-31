import os
import shutil
import random

# Klasör yolları
images_dir = "C:/Users/KENAN/Desktop/last_dataset/dataset/images"
labels_dir = "C:/Users/KENAN/Desktop/last_dataset/dataset/labels"
output_dir = "C:/Users/KENAN/Desktop/last_dataset/dataset-split"

# Çıktı klasörleri
train_dir = os.path.join(output_dir, "train")
val_dir = os.path.join(output_dir, "val")
test_dir = os.path.join(output_dir, "test")

# Her sınıf için klasörleri oluştur
for folder in [train_dir, val_dir, test_dir]:
    os.makedirs(os.path.join(folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(folder, "labels"), exist_ok=True)

# Dosyaları listele
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Karıştır ve böl
random.shuffle(image_files)
train_split = 0.75
val_split = 0.2
test_split = 0.05

train_count = int(len(image_files) * train_split)
val_count = int(len(image_files) * val_split)

train_files = image_files[:train_count]
val_files = image_files[train_count:train_count + val_count]
test_files = image_files[train_count + val_count:]

# Dosyaları kopyala
def copy_files(file_list, dest_dir):
    for file in file_list:
        image_path = os.path.join(images_dir, file)
        label_path = os.path.join(labels_dir, file.replace('.jpg', '.txt').replace('.png', '.txt'))
        
        shutil.copy(image_path, os.path.join(dest_dir, "images", file))
        
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(dest_dir, "labels", os.path.basename(label_path)))

# Kopyalama işlemleri
copy_files(train_files, train_dir)
copy_files(val_files, val_dir)
copy_files(test_files, test_dir)

print("Veriseti başarıyla train, validation ve test olarak ayrıldı.")
