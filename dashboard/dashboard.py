import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/main_data.csv', parse_dates=['datetime'])
    return df

df = load_data()

# Sidebar: Filter data
st.sidebar.title("Filter Data")
start_date = st.sidebar.date_input("Mulai", df["datetime"].min().date())
end_date = st.sidebar.date_input("Sampai", df["datetime"].max().date())
selected_station = st.sidebar.selectbox("Pilih Stasiun", df["station"].unique())
selected_pollutant = st.sidebar.selectbox("Pilih Polutan", ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])

# Filter data berdasarkan pilihan
df_filtered = df[(df["datetime"].dt.date >= start_date) & 
                 (df["datetime"].dt.date <= end_date) & 
                 (df["station"] == selected_station)]

# Header
st.title("Dashboard Analisis Kualitas Udara")

### **1️⃣ Bagaimana Tren Polusi Udara Selama Setahun Terakhir?**
st.subheader(f"Tren {selected_pollutant} di {selected_station}")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_filtered, x="datetime", y=selected_pollutant, ax=ax)
plt.xticks(rotation=45)
plt.title(f"Tren {selected_pollutant} dari {start_date} sampai {end_date}")
st.pyplot(fig)

### **2️⃣ Apakah Ada Hubungan Antara Polusi Udara dan Faktor Cuaca?**
st.subheader("Korelasi antara Polutan dan Faktor Cuaca")

# Heatmap Korelasi
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_filtered.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

# Scatterplot Interaktif
st.subheader("Hubungan antara Polusi dan Faktor Cuaca")
x_var = st.selectbox("Pilih Faktor Cuaca (X-Axis)", ['TEMP', 'PRES', 'DEWP', 'WSPM', 'RAIN'])
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df_filtered, x=x_var, y=selected_pollutant, alpha=0.6)
plt.title(f"Korelasi antara {x_var} dan {selected_pollutant}")
st.pyplot(fig)

### **3️⃣ Bagaimana Perbedaan Tingkat Polusi antara Dua Stasiun Pemantauan?**
st.subheader(f"Perbandingan {selected_pollutant} di Dua Stasiun")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='station', y=selected_pollutant, data=df)
st.pyplot(fig)

# Footer
st.write("Dashboard ini dibuat menggunakan Streamlit.")