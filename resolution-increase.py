from PIL import Image

# Görseli yükle
image = Image.open("docs/yurt-disi-egitim-13246672013.jpg")

# 2 kat çözünürlük artır
new_size = (image.width * 2, image.height * 2)
high_res_image = image.resize(new_size, Image.LANCZOS)

# Yeni görüntüyü 300 DPI ile kaydet
high_res_image.save("docs/high_res_image.jpg", dpi=(400, 400))