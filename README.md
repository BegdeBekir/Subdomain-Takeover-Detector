# Subdomain Takeover Detector Helper

`Subdomain Takeover Detector Helper`, verilen subdomain listesini tarayarak potansiyel **dangling / unclaimed subdomain** risklerini tespit eder.  
CNAME kayıtlarını ve HTTP yanıtlarını kontrol ederek, takeover olasılığı olan subdomainleri işaretler.

---

## 🚀 Özellikler
- Subdomain listesini tek seferde kontrol eder.
- CNAME kayıtlarını kontrol eder.
- HTTP yanıtını kontrol ederek takeover riskini tespit eder.
- Potansiyel takeover olan subdomainleri raporlar.
- Çıktıyı dosya olarak kaydeder (`--output`).

---

## 📦 Kurulum

1. Python 3 kurulu olduğundan emin olun.
2. Gerekli kütüphaneleri yükleyin:
```bash
pip install requests dnspython
```
3. `subdomain_takeover_helper.py` dosyasını projeye ekleyin.
4. Subdomain listesi için bir `.txt` dosyası oluşturun (her satıra bir subdomain).

---

## 💻 Kullanım

### 1️⃣ Input dosyasını hazırla
`subdomains.txt` örneği:

```
test.example.com
blog.example.org
dev.testsite.com
```

### 2️⃣ Script’i çalıştır
```bash
python subdomain_takeover_helper.py --input subdomains.txt --output takeover_results.txt
```

### 3️⃣ Çıktıyı incele
`takeover_results.txt` örneği:

```
test.example.com | CNAME: None | Status: 200 | Notes: 
blog.example.org | CNAME: username.github.io | Status: 404 | Notes: Potential takeover detected!
dev.testsite.com | CNAME: None | Status: None | Notes: NXDOMAIN - Subdomain does not exist
```

### 4️⃣ Sonuçları pentest sırasında kullan
- Potansiyel takeover olan subdomainleri hızlıca raporlayabilirsin.
- Pentest sırasında riskli alanları önceliklendirebilirsin.

---

## 🛠 Katkıda Bulunma
- Hata bulursanız veya yeni özellik eklemek isterseniz issue açabilir veya PR gönderebilirsiniz. 🚀

---

## 📄 Lisans
Bu proje MIT lisansı ile dağıtılmaktadır.
