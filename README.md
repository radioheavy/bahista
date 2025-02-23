# Bahista - Futbol Veri Analiz Sistemi

Bu proje, DataFC API'sini kullanarak futbol verilerini çeken ve analiz eden bir sistemdir.

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/radioheavy/bahista.git
cd bahista
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
# veya
.\venv\Scripts\activate  # Windows için
```

3. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyası oluşturun ve DataFC API anahtarınızı ekleyin:
```
DATAFC_API_KEY=your_api_key_here
```

## Kullanım

Örnek kullanım için `src/data_fetcher.py` dosyasını çalıştırın:

```bash
python src/data_fetcher.py
```

## Özellikler

- Asenkron veri çekme
- Lig maçlarını sorgulama
- Takım istatistiklerini görüntüleme
- Hata yönetimi ve loglama

## Lisans

MIT