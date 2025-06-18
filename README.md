# 🚲 Dashboard Analisis Data Bike Sharing

Proyek akhir kelas **Analisis Data dengan Python** dari Dicoding.

## 📁 Struktur File

```
submission/
├── dashboard/
│   └── dashboard.py          # Streamlit dashboard
├── data/
│   └── day.csv               # Dataset asli dari Kaggle
├── day.csv                   # Dataset salinan untuk kebutuhan dashboard (root)
├── notebook.ipynb            # Notebook proses analisis
├── requirements.txt          # Library yang dibutuhkan
└── README.md                 # Petunjuk penggunaan
```

> ⚠️ **Catatan Penting:**  
> Untuk menghindari error path saat menjalankan dashboard, pastikan file `day.csv` berada di **root folder**, bukan di dalam folder `dashboard/`.

---

## ▶️ Cara Menjalankan Dashboard

### 1. **Instal library dependencies**

Pastikan Anda berada di folder proyek, lalu jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

---

## 🧪 (Opsional Tapi Disarankan) Menjalankan di Virtual Environment

Agar lebih aman dan tidak bentrok dengan project lain, Anda bisa menggunakan **virtual environment**:

### 🔧 Buat Virtual Environment

```bash
# Buat environment baru bernama 'env'
python -m venv env
```

### ▶️ Aktifkan Virtual Environment

- **Windows:**

```bash
env\Scripts\activate
```

- **Mac/Linux:**

```bash
source env/bin/activate
```

### 📦 Instalasi Library

```bash
pip install -r requirements.txt
```

---

## 🚀 Jalankan Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Streamlit akan menampilkan link lokal di terminal seperti:

```
Local URL: http://localhost:8501
```

Klik link tersebut untuk membuka dashboard di browser Anda.

---

## 📄 Dataset

Dataset yang digunakan:  
**Bike Sharing Dataset** dari Kaggle  
📦 Sumber: [https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

---

## 📝 Informasi Tambahan

- Jika terjadi error file tidak ditemukan (`FileNotFoundError`), pastikan file `day.csv` berada di **folder yang sama dengan `dashboard.py`** dijalankan (biasanya folder root).
- Semua analisis dan insight dapat dilihat pada file `notebook.ipynb`.

---

## 📬 Kontak

Proyek ini dibuat sebagai bagian dari submission Dicoding oleh:

**Nama:** rikyraharjo  
**Kelas:** Analisis Data dengan Python  
**Platform:** [https://www.dicoding.com](https://www.dicoding.com)
