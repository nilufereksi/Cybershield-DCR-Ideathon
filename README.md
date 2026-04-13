# 🔐 CYBERSHIELD DCR Ideathon Project

![cybershield dcr ideathon github ](https://github.com/user-attachments/assets/a26059c4-64cb-40a9-bba0-359e004250b0)


> **IKU Aws&Cloud Ideathon 2026**  
> AI destekli, sıfır-bilgi ispatı (Zero-Knowledge Proof) mimarisiyle çalışan siber tehdit tespit platformu.

---

## 📌 Proje Özeti

**CYBERSHIELD DCR**, kurumsal ağ trafiğini **şifrelenmiş halde** analiz ederek siber tehditleri gerçek zamanlı tespit eden bir yapay zeka platformudur. Ham veri asla açık şekilde işlenmez; bunun yerine **SHA-256 hashing** ve **AES-256 şifreleme** ile bir "Data Clean Room" mimarisi oluşturulur.

- 🛡️ **Anomali Tespiti** → NSL-KDD veri setiyle eğitilmiş Isolation Forest modeli
- 🔑 **Veri Gizliliği** → SHA-256 maskeleme + AES-256 (Fernet) şifreleme
- ☁️ **Cloud-Ready** → AWS S3 + KMS entegrasyon mimarisi
- 📊 **Interaktif Arayüz** → Streamlit tabanlı web uygulaması

---

## 🧠 Mimari

```
Kullanıcı Verisi
      │
      ▼
SHA-256 Maskeleme
      │
      ▼
AES-256 Şifreleme (Fernet)
      │
      ▼
Data Clean Room (AWS KMS)
      │
      ▼
Isolation Forest Modeli
      │
      ▼
Tehdit Skoru / Anomali Kararı
```

---

## 🗂️ Proje Yapısı

```
Ideathon/
├── app.py                    # Ana Streamlit uygulaması
├── requirements.txt          # Python bağımlılıkları
├── dockerfile                # Docker container yapılandırması
├── nsl_kdd_final_v2.pkl      # Eğitilmiş Isolation Forest modeli
├── src/
│   ├── trainer.py            # ThreatDetectionEngine sınıfı (model eğitimi)
│   ├── data_processor.py     # Veri ön işleme modülü
│   └── generate_mock_data.py # Test verisi üretici
├── notebooks/
│   └── Untitled0.ipynb       # Keşifsel veri analizi (EDA)
└── data/                     # NSL-KDD veri seti (gitignore'da)
    ├── KDDTrain+.csv
    └── KDDTest+.csv
```

---

## ⚙️ Kurulum

### Gereksinimler

- Python 3.9+
- pip

### Adımlar

```bash
# 1. Repoyu klonla
git clone https://github.com/<KULLANICI_ADIN>/Ideathon.git
cd Ideathon

# 2. Sanal ortam oluştur (isteğe bağlı ama önerilen)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. Uygulamayı başlat
streamlit run app.py
```

---

## 🚀 Kullanım

1. Tarayıcıda `http://localhost:8501` adresine git.
2. **🛡️ Anomali Analizi** sekmesinde ağ trafiği parametrelerini gir:
   - IP Adresi, Bağlantı Süresi, Kaynak/Hedef Bayt, Bağlantı Sayısı
3. **ŞİFRELİ ANALİZİ BAŞLAT** butonuna bas.
4. Sistem veriyi SHA-256 ile maskeler, AES-256 ile şifreler ve AI modeline iletir.
5. Sonuç: `✅ GÜVENLİ` veya `🚨 ANOMALİ TESPİT EDİLDİ`
6. **📊 Güvenli Veri Paylaşımı** sekmesinde ZKP mimarisinin detaylarını incele.

---

## 🔒 Güvenlik Katmanları

| Katman | Yöntem | Durum |
|:---|:---|:---|
| Veri Anonimleştirme | SHA-256 Hashing | ✅ Aktif |
| Depolama Güvenliği | AES-256 (AWS S3) | ✅ Şifreli |
| Anahtar Yönetimi | AWS KMS | ✅ Senkronize |
| Model Mimarisi | Isolation Forest | ✅ Cloud-Ready |

---

## 🤖 Model Detayları

| Özellik | Değer |
|:---|:---|
| Algoritma | Isolation Forest |
| Veri Seti | NSL-KDD (Network Security Lab) |
| Eğitim Boyutu | ~125,000 kayıt |
| Anomali Oranı (contamination) | %5 |
| Özellikler | duration, src_bytes, dst_bytes, count, srv_count |

---

## 📦 Bağımlılıklar

```
pandas
numpy
scikit-learn
streamlit
plotly
joblib
cryptography
```

---

## 🐳 Docker ile Çalıştırma

```bash
docker build -t zkp-cyber-intel .
docker run -p 8501:8501 zkp-cyber-intel
```

---

## 📄 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır.


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
</p>
