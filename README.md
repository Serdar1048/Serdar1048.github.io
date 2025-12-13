# Veri Bilimi Portfolyo Web Sitesi

Modern, minimalist ve yönetimi kolay kişisel portfolyo web sitesi.

## Özellikler
- **Kolay Yönetim:** Tüm projeler tek bir `projects.json` dosyasından yönetilir.
- **Modern Tasarım:** Tailwind CSS ile şık ve temiz görünüm.
- **İnteraktif:** Streamlit uygulamalarını site içinde (iframe) çalıştırır.
- **Duyarlı (Responsive):** Mobil ve masaüstü uyumlu.

## Kurulum ve Yerel Çalıştırma

Bu projeyi bilgisayarınızda görüntülemek için yerel bir sunucuya ihtiyacınız vardır (Doğrudan `index.html` dosyasına tıklayarak açarsanız, tarayıcı güvenlik kuralları gereği JSON dosyası yüklenmeyebilir).

1. **Terminali açın** ve proje klasörüne gidin:
   ```bash
   cd C:\Users\SERDAR\Desktop\website
   ```

2. **Yerel Sunucuyu Başlatın** (Python yüklü ise):
   ```bash
   python -m http.server
   ```
   *Eğer port 8000 doluysa `python -m http.server 8080` deneyebilirsiniz.*

3. **Tarayıcıda Açın:**
   Adres çubuğuna `http://localhost:8000` yazın.

## İçerik Yönetimi

Yeni bir proje eklemek veya mevcut olanı düzenlemek için `projects.json` dosyasını açın.

### JSON Formatı:
```json
{
  "id": 3,
  "title": "Proje Başlığı",
  "description": "Kısa açıklama (Kart üzerinde görünür)",
  "image": "Resim URL (https://... veya ./img/resim.jpg)",
  "github": "https://github.com/kullanici/proje",
  "demo_url": "https://share.streamlit.io/...", 
  "details": "Markdown benzeri detaylı açıklama. ### Başlık ve - Liste destekler."
}
```
*Not: Streamlit linklerinizin sonuna `?embed=true` eklerseniz daha temiz görünür.*

## GitHub Pages ile Yayına Alma (Canlıya Çekme)

Web sitenizi tüm dünyaya açmak için şu adımları izleyin:

1. **GitHub'da Yeni Bir Depo (Repository) Oluşturun:**
   - [GitHub.com](https://github.com) adresine gidin.
   - Sağ üstteki `+` butonundan "New repository" seçin.
   - Depo adı olarak `username.github.io` (kullanıcı adınız ile değiştirin) veya herhangi bir isim verin.
   - "Public" seçeneğini işaretleyin ve "Create repository" deyin.

2. **Kodları GitHub'a Gönderin:**
   Terminalinizde şu komutları sırasıyla çalıştırın:
   ```bash
   git init
   git add .
   git commit -m "İlk yayın: Portfolyo sitesi oluşturuldu"
   git branch -M main
   git remote add origin https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git
   git push -u origin main
   ```
   *(KULLANICI_ADINIZ ve REPO_ADINIZ kısımlarını kendi bilgilerinizle değiştirin)*

3. **GitHub Pages Ayarlarını Yapın:**
   - GitHub'da deponuzun sayfasına gidin.
   - Üst menüden **Settings** > **Pages** sekmesine tıklayın.
   - **Source** kısmında `Deploy from a branch` seçili olsun.
   - **Branch** kısmında `main` ve `/ (root)` seçip **Save** butonuna basın.

Birkaç dakika içinde siteniz `https://KULLANICI_ADINIZ.github.io/REPO_ADINIZ` adresinde yayında olacaktır!
