import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/day.csv")  # kamu bisa copy day.csv sebagai main_data.csv
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['season_label'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['weather_label'] = df['weathersit'].map({
        1: 'Cerah',
        2: 'Mendung',
        3: 'Hujan Ringan',
        4: 'Cuaca Ekstrem'
    })
    return df

df = load_data()

# Judul
st.title("🚲 Dashboard Analisis Bike Sharing")

# Sidebar Filter
st.sidebar.header("Filter")
selected_year = st.sidebar.multiselect("Pilih Tahun", options=df['yr'].unique(), default=df['yr'].unique())

# Filter data
df_filtered = df[df['yr'].isin(selected_year)]

# Visualisasi 1 - Total peminjaman per musim
st.subheader("Total Peminjaman per Musim")
season_data = df_filtered.groupby("season_label")['cnt'].sum().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(data=season_data, x='season_label', y='cnt', palette='Set2', ax=ax1)
ax1.set_title("Total Peminjaman Sepeda per Musim")
ax1.set_xlabel("Musim")
ax1.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig1)

# Visualisasi 2 - Suhu vs Jumlah Sewa
st.subheader("Korelasi Suhu terhadap Jumlah Sewa")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df_filtered, x='temp', y='cnt', hue='season_label', alpha=0.7, ax=ax2)
ax2.set_title("Suhu vs Jumlah Sewa")
ax2.set_xlabel("Suhu (Normalisasi)")
ax2.set_ylabel("Jumlah Sewa")
st.pyplot(fig2)

# Visualisasi 3 - Boxplot Cuaca
st.subheader("Distribusi Jumlah Sewa Berdasarkan Cuaca")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df_filtered, x='weather_label', y='cnt', palette='Set3', ax=ax3)
ax3.set_title("Jumlah Sewa berdasarkan Cuaca")
ax3.set_xlabel("Cuaca")
ax3.set_ylabel("Jumlah Sewa")
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("© 2025 - Analisis Data Bike Sharing | Dicoding Final Project")
