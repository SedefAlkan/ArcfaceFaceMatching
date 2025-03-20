# ArcFace ile Yüz Karşılaştırma

## Genel Bakış
Bu Python betiği, **DeepFace'in ArcFace Modelini** kullanarak yüz doğrulama işlemi gerçekleştirir. Bir CSV dosyasında listelenen resim çiftlerini karşılaştırır ve sonuçları Matplotlib kullanarak görselleştirir. Karşılaştırma sonuçları arasında benzerlik skoru ve tahmin edilen karar bulunur.

## Özellikler
- CSV dosyasından resim dosya yollarını okur.
- **DeepFace** (ArcFace modeli) kullanarak yüz doğrulama yapar.
- Resim çiftlerini dosya adları olmadan gösterir.
- Gerçek ve tahmin edilen benzerlik sonuçlarını görüntüler.
- Her karşılaştırma için işleme durumunu konsola yazdırır.

## Gereksinimler
Aşağıdaki bağımlılıkların yüklü olduğundan emin olun:

```bash
pip install pandas matplotlib opencv-python deepface
```

## Veri Seti Formatı
Veri seti aşağıdaki şekilde düzenlenmelidir:
- **Veri Seti Klasörü**: Resim dosyalarını içerir.
- **CSV Dosyası (master1.csv)**: Karşılaştırılacak resim çiftlerinin dosya adlarını ve beklenen sonuçları içerir.

### CSV Dosyası Formatı
| file_x      | file_y      | Decision |
|------------|------------|----------|
| img1.jpg   | img2.jpg   | Yes      |
| img3.jpg   | img4.jpg   | No       |

- `file_x` ve `file_y`: Veri seti klasöründeki resimlerin yolları.
- `Decision`: Gerçek beklenen sonuç (**Yes** veya **No**).

## Kullanım
Betiği veri seti ve CSV dosyası ile aynı dizinde çalıştırın:

```bash
python arcface.py
```

Betiğin gerçekleştireceği işlemler:
1. CSV dosyasını okur.
2. Her resim çiftini yükleyip karşılaştırır.
3. Sonuçları bir ızgara formatında, resim dosya adları olmadan görüntüler.
4. Benzerlik skorlarını ve tahminleri konsola yazdırır.

## Örnek Çıktı
```
Processed: img1.jpg vs img2.jpg - Predicted: Yes - Score: 0.4123
Processed: img3.jpg vs img4.jpg - Predicted: No - Score: 0.6789
```

## Notlar
- Veri setindeki resimlerin net ve düzgün hizalanmış olduğundan emin olun.
- İşlem süresi, resim çifti sayısına ve sistem performansına bağlıdır.
- Görseller işlenirken bir hata oluşursa, betik hatayı yazdırır ancak çalışmayı durdurmaz.

## Lisans
Bu proje açık kaynaklıdır. Dilediğiniz gibi değiştirip dağıtabilirsiniz.

