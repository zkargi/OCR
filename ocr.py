import cv2
from paddleocr import PaddleOCR

# OCR motorunu başlat
ocr_motoru = PaddleOCR(lang='tr')  # Tek dil için 'tr' veya 'en' gibi bir dil kodu kullanın

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)  # 0, birincil kamerayı kullanacak şekilde ayarlanabilir

while True:
    # Kameradan bir frame al
    ret, frame = kamera.read()

    # Frame alınamazsa döngüyü sonlandır
    if not ret:
        print("Kamera bağlantısı başarısız.")
        break

    # OCR ile resimdeki metni oku
    sonuc = ocr_motoru.ocr(frame)

    # Eğer sonuç yoksa (None), bir mesaj yazdır ve döngüye devam et
    if sonuc is None:
        print("Metin tanınamadı.")
        continue

    # Tanınan plaka metnini saklamak için boş bir liste oluştur
    taninan_plakalar = []

    # Tanınan metni terminale yazdır ve plaka olarak kabul edilen metinleri kaydet
    for result in sonuc:
        if result is None:
            continue
        for line in result:
            print(line[1])
            taninan_plakalar.append(line[1])

    # Plaka metnini ekrana yazdır
    if taninan_plakalar:
        # Tanınan plaka metnini al, varsayılan olarak ilk sırada bulunanı al
        plaka_metni = str(taninan_plakalar[0])  # Metni dizeye dönüştür

        # Metni frame üzerine yazdır
        cv2.putText(frame, plaka_metni, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Frame'i göster
    cv2.imshow('Plaka Tanıma', frame)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını ve pencereyi kapat
kamera.release()
cv2.destroyAllWindows()
