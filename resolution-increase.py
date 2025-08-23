from PIL import Image
import os

def increase_resolution(input_path, output_path, scale=2, dpi=(300, 300)):
    if not os.path.exists(input_path):
        print(f"Girdi dosyası bulunamadı: {input_path}")
        return

    image = Image.open(input_path)
    new_size = (image.width * scale, image.height * scale)
    high_res_image = image.resize(new_size, Image.LANCZOS)
    high_res_image.save(output_path, dpi=dpi)
    print(f"Yüksek çözünürlüklü görsel kaydedildi: {output_path} (DPI: {dpi})")

if __name__ == "__main__":
    input_file = "docs/yurt-disi-egitim-13246672013.jpg"
    output_file = "docs/high_res_image.jpg"
    increase_resolution(input_file, output_file, scale=2, dpi=(400, 400))