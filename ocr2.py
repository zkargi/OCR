import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from paddleocr import PaddleOCR

# OCR motorunu başlat
ocr_motoru = PaddleOCR(lang='tr')  # Tek dil için 'tr' veya 'en' gibi bir dil kodu kullanın

# Resim dosyasının yolunu belirt
file_path = 'C:\\Users\\stajyer\\Desktop\\serino\\metin.png'
# Resmin mevcut olup olmadığını kontrol et
if not os.path.exists(file_path):
    print(f"Dosya bulunamadı: {file_path}")
else:
    # Resmi oku
    with open(file_path, 'rb') as f:
        resim = f.read()

    # Resmi numpy dizisine çevir
    resim_ham = np.frombuffer(resim, np.uint8)
    resim_cv2 = cv2.imdecode(resim_ham, cv2.IMREAD_COLOR)

    # OCR ile resimdeki metni oku
    sonuc = ocr_motoru.ocr(resim_cv2)

    # Sadece metinleri terminale yazdır
    for result in sonuc:
        for line in result:
            print(line[1])

    # Resmi matplotlib ile göster
    resim_rgb = cv2.cvtColor(resim_cv2, cv2.COLOR_BGR2RGB)
    plt.imshow(resim_rgb)
    plt.axis('off')  # Eksenleri gizle
    plt.show()
