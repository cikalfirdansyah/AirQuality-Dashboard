import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Kualitas Udara", layout="wide")

# Fungsi untuk load data
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/main_data.csv', parse_dates=['datetime'])
    return df

df = load_data()

# Sidebar untuk filter interaktif
st.sidebar.title("🔍 Filter Data")
try:
    start_date = st.sidebar.date_input("Mulai", df["datetime"].min().date())
    end_date = st.sidebar.date_input("Sampai", df["datetime"].max().date())
    
    if start_date > end_date:
        st.sidebar.error("⚠️ Tanggal mulai harus lebih kecil dari tanggal akhir!")
        st.stop()
        
    selected_station = st.sidebar.selectbox("📍 Pilih Stasiun", df["station"].unique())
    selected_pollutant = st.sidebar.selectbox("☁️ Pilih Polutan", ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])

    # Filter data berdasarkan pilihan
    df_filtered = df[(df["datetime"].dt.date >= start_date) & 
                     (df["datetime"].dt.date <= end_date) & 
                     (df["station"] == selected_station)]
    
except Exception as e:
    st.sidebar.error(f"Terjadi kesalahan: {e}")
    st.stop()

# Header
st.title("📊 Dashboard Analisis Kualitas Udara")
st.markdown("""
Dashboard ini menyajikan analisis data kualitas udara berdasarkan polutan utama yang diamati di berbagai stasiun pemantauan.
Silakan gunakan filter di sidebar untuk menyesuaikan data yang ingin Anda eksplorasi.
""")

# **1️⃣ Bagaimana Tren Polusi Udara Selama Setahun Terakhir?**
st.subheader(f"📈 Bagaimana Tren {selected_pollutant} di {selected_station}?")
st.markdown("""
**📌 Penjelasan:**  
Tren polusi udara dapat memberikan wawasan tentang pola perubahan kualitas udara dalam jangka waktu tertentu.  
Apakah ada lonjakan kadar polutan pada bulan-bulan tertentu? Apakah ada penurunan akibat kebijakan lingkungan?  
Grafik ini membantu melihat pola perubahan polutan selama periode yang dipilih.
""")

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=df_filtered, x="datetime", y=selected_pollutant, ax=ax, marker="o", linewidth=1.5)
plt.xticks(rotation=45)
plt.xlabel("Tanggal")
plt.ylabel(f"Konsentrasi {selected_pollutant} (µg/m³)")
plt.title(f"Tren {selected_pollutant} dari {start_date} hingga {end_date}")
st.pyplot(fig)

# **2️⃣ Apakah Ada Hubungan Antara Polusi Udara dan Faktor Cuaca?**
st.subheader("🌦️ Apakah Faktor Cuaca Mempengaruhi Tingkat Polusi?")
st.markdown("""
**📌 Penjelasan:**  
Beberapa faktor cuaca dapat mempengaruhi tingkat polusi udara. Misalnya:  
- **Hujan (RAIN)** dapat membantu membersihkan udara dari partikel polutan.  
- **Kecepatan angin (WSPM)** dapat menyebarkan polutan ke area lain.  
- **Tekanan udara (PRES) & Suhu (TEMP)** dapat mempengaruhi reaksi kimia di atmosfer yang membentuk polutan.  

Dua visualisasi berikut akan membantu menganalisis hubungan antara polutan dan faktor cuaca.
""")

# Heatmap Korelasi
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_filtered.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
plt.title("Heatmap Korelasi Polutan dan Faktor Cuaca")
st.pyplot(fig)

# Scatterplot Interaktif
st.subheader("📊 Hubungan antara Polusi dan Faktor Cuaca")
x_var = st.selectbox("Pilih Faktor Cuaca (X-Axis)", ['TEMP', 'PRES', 'DEWP', 'WSPM', 'RAIN'])
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df_filtered, x=x_var, y=selected_pollutant, alpha=0.6)
plt.xlabel(x_var)
plt.ylabel(f"Konsentrasi {selected_pollutant}")
plt.title(f"Korelasi antara {x_var} dan {selected_pollutant}")
st.pyplot(fig)

# **3️⃣ Bagaimana Perbedaan Tingkat Polusi antara Dua Stasiun Pemantauan?**
st.subheader("🏙️ Bagaimana Perbedaan Kadar Polutan di Dua Stasiun?")
st.markdown("""
**📌 Penjelasan:**  
Setiap daerah mungkin memiliki tingkat polusi yang berbeda karena faktor-faktor seperti:  
- **Kepadatan lalu lintas**  
- **Aktivitas industri**  
- **Kondisi geografis dan arah angin**  

Perbandingan ini membantu memahami bagaimana lokasi mempengaruhi kualitas udara.
""")

stasiun_1 = st.selectbox("Pilih Stasiun 1", df["station"].unique())
stasiun_2 = st.selectbox("Pilih Stasiun 2", df["station"].unique())

df_compare = df[(df["station"] == stasiun_1) | (df["station"] == stasiun_2)]

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='station', y=selected_pollutant, data=df_compare)
plt.title(f"Perbandingan {selected_pollutant} antara {stasiun_1} dan {stasiun_2}")
plt.xlabel("Stasiun")
plt.ylabel(f"Konsentrasi {selected_pollutant} (µg/m³)")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("📌 **Catatan:** Dashboard ini dikembangkan menggunakan **Streamlit** untuk memvisualisasikan data kualitas udara. Semua data bersumber dari dataset pemantauan udara.")