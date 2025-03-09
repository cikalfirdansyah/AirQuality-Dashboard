# 🌍 Dashboard Analisis Kualitas Udara  

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis tren polusi udara berdasarkan data dari beberapa stasiun pemantauan di Beijing.  

---

## 📌 1. Deskripsi Proyek  

Proyek ini bertujuan untuk menganalisis kualitas udara dan faktor-faktor yang memengaruhinya dengan menggunakan data dari beberapa stasiun pemantauan. Dashboard interaktif memungkinkan pengguna untuk:  

✅ **Melihat tren polusi udara** selama periode waktu tertentu.  
✅ **Menganalisis hubungan antara polusi udara dan faktor cuaca** seperti suhu, tekanan udara, dan curah hujan.  
✅ **Membandingkan tingkat polusi udara antarstasiun pemantauan.**  

---

## 📂 2. Dataset yang Digunakan  

Dataset utama (`main_data.csv`) berisi data kualitas udara dari beberapa stasiun pemantauan di Beijing.  

### **📊 Struktur Dataset**  

| **Kolom**    | **Deskripsi**  |
|-------------|--------------|
| `datetime`  | Waktu pencatatan data (YYYY-MM-DD HH:MM:SS) |
| `station`   | Nama stasiun pemantauan (contoh: Guanyuan, Wanshouxigong) |
| **📊 Polutan** | |
| `PM2.5`     | Konsentrasi PM2.5 dalam µg/m³ |
| `PM10`      | Konsentrasi PM10 dalam µg/m³ |
| `NO2`       | Konsentrasi NO2 dalam µg/m³ |
| `SO2`       | Konsentrasi SO2 dalam µg/m³ |
| `CO`        | Konsentrasi CO dalam mg/m³ |
| `O3`        | Konsentrasi O3 dalam µg/m³ |
| **🌦️ Faktor Cuaca** | |
| `TEMP`      | Suhu udara dalam derajat Celsius |
| `PRES`      | Tekanan udara dalam hPa |
| `DEWP`      | Titik embun dalam derajat Celsius |
| `RAIN`      | Curah hujan dalam mm |
| `WSPM`      | Kecepatan angin dalam m/s |

### **📌 Lokasi Dataset**  
Dataset utama tersimpan dalam folder berikut:  
dashboard/main_data.csv


## ⚙️ 3. Setup Virtual Environment  

Sebelum menjalankan dashboard, buat **virtual environment** agar dependencies tetap terisolasi.  

### **1️⃣ Buat Virtual Environment**  
#### **bash**
```
python -m venv venv
```
### **2️⃣ Aktifkan Virtual Environment**
#### **Windows**
```
venv\Scripts\activate
```
#### **Mac/Linux**
```
source venv/bin/activate
```
## 📦 4. Instalasi Library
Sebaiknya instal library menggunakan file requirements.txt untuk menghindari masalah dependency.

### **1️⃣ Pastikan Virtual Environment Aktif**
Jalankan perintah berikut di terminal:
```
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
``` 
atau
```
 venv\Scripts\activate (Windows)
```
### 2️⃣ Install Dependencies dengan requirements.txt
#### bash
```
pip install -r requirements.txt
```
Jika kamu belum memiliki requirements.txt, buat file tersebut dan isi dengan:

#### nginx
```
 streamlit
 pandas
 matplotlib
 seaborn
```
## 🚀 5. Menjalankan Dashboard
Setelah menginstal semua dependencies, jalankan dashboard dengan perintah berikut:

bash
```
streamlit run dashboard/dashboard.py
```
Jika ada error, pastikan kamu berada dalam folder proyek yang benar dan sudah mengaktifkan virtual environment.

## 📜 6. Struktur Folder Proyek
Pastikan struktur folder seperti ini agar tidak terjadi error:

### **cpp**

### 📂 submission
#### ├── 📂 dashboard   
#### │   ├── main_data.csv
#### │   ├── dashboard.py
#### ├── 📂 data
#### │   ├── PRSA_Data_Guanyuan_20130301-20170228.csv
#### │   ├── PRSA_Data_Wanshouxigong_20130301-20170228.csv
#### ├── AirQuality.ipynb
#### ├── requirements.txt
#### ├── README.md
#### ├── url.txt

## 🛠️ 7. Troubleshooting
Jika terjadi error, coba lakukan langkah berikut:

#### 1️⃣ Pastikan virtual environment sudah aktif.
#### 2️⃣ Cek apakah semua library sudah terinstal dengan menjalankan:

#### bash
```
pip list
```
#### 3️⃣ Jika ada library yang hilang, instal ulang dengan:

#### bash
```
pip install -r requirements.txt
```
#### 4️⃣ Pastikan kamu berada di direktori proyek yang benar sebelum menjalankan perintah Streamlit. 

## 📊 8. Pertanyaan Bisnis
Dashboard ini dibuat untuk menjawab beberapa pertanyaan bisnis terkait kualitas udara:

1️⃣ Bagaimana Tren Polusi Udara Selama Setahun Terakhir?

- Analisis tren konsentrasi polutan dalam rentang waktu tertentu untuk melihat pola musiman atau fluktuasi harian.

2️⃣ Apakah Ada Hubungan Antara Polusi Udara dan Faktor Cuaca?
- Visualisasi hubungan antara tingkat polutan dan variabel cuaca seperti suhu, tekanan udara, dan curah hujan.

3️⃣ Bagaimana Perbandingan Tingkat Polusi antara Dua Stasiun Pemantauan?
- Membandingkan konsentrasi polutan di dua stasiun pemantauan yang berbeda untuk mengetahui apakah ada perbedaan signifikan.
