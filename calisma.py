import os
import shutil

def update_label_files(directory, new_class_id='4', backup=True):
    """
    Belirtilen dizindeki tüm .txt dosyalarının her satırındaki ilk karakteri verilen sınıf ID'si ile değiştirir.
    Args:
        directory (str): Etiket dosyalarının bulunduğu dizin.
        new_class_id (str): Yeni sınıf ID'si (varsayılan: '4').
        backup (bool): Dosya güncellenmeden önce yedeği alınsın mı? (varsayılan: True)
    """
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    updated, skipped, failed = 0, 0, 0

    for file_name in txt_files:
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"[HATA] {file_name} okunamadı: {e}")
            failed += 1
            continue

        new_lines = []
        changed = False
        for line in lines:
            if line.strip():
                if line[0] != new_class_id:
                    new_lines.append(new_class_id + line[1:])
                    changed = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

        if changed:
            if backup:
                try:
                    shutil.copy(file_path, file_path + ".bak")
                except Exception as e:
                    print(f"[UYARI] {file_name} için yedek alınamadı: {e}")
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                updated += 1
            except Exception as e:
                print(f"[HATA] {file_name} yazılamadı: {e}")
                failed += 1
        else:
            skipped += 1

    print(f"\nİşlem tamamlandı: {updated} dosya güncellendi, {skipped} dosya zaten güncel, {failed} dosyada hata oluştu.")

if __name__ == "__main__":
    LABELS_DIR = "C:\\Users\\KENAN\\Desktop\\datasets-v2\\stamp\\valid\\labels"
    update_label_files(LABELS_DIR, new_class_id='4', backup=True)
