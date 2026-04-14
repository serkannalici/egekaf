import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Secrets'tan verileri çek
ogrenci_verisi = st.secrets["ogrenci_listesi"]
url = st.secrets["gsheets_url"]

# Google Sheets Bağlantısı
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🚌 EGEKAF 2026 Otobüs Kontrolü")

tel_input = st.text_input("Telefon Numaranız", max_chars=10)

if tel_input:
    if tel_input in ogrenci_verisi:
        isim = ogrenci_verisi[tel_input]
        st.success(f"Hoş Geldiniz, **{isim}**")
        
        onay = st.checkbox(f"Otobüse binişimi onaylıyorum.")
        
        if st.button("Onayla ve Kaydet"):
            if onay:
                # Veriyi Tabloya Yazma İşlemi
                new_data = pd.DataFrame([{"Telefon": tel_input, "Ad Soyad": isim}])
                
                # Mevcut verileri oku ve yeni veriyi ekle
                existing_data = conn.read(spreadsheet=url)
                updated_df = pd.concat([existing_data, new_data], ignore_index=True)
                
                # Tabloyu güncelle
                conn.update(spreadsheet=url, data=updated_df)
                
                st.balloons()
                st.success(f"Kayıt Başarılı! İyi yolculuklar {isim}.")
            else:
                st.warning("Lütfen önce onay kutusunu işaretleyin.")
    else:
        st.error("Numara bulunamadı.")

# Sizin takip edebilmeniz için gizli bir admin paneli (Opsiyonel)
with st.sidebar:
    if st.text_input("Yönetici Şifresi", type="password") == "Fethiye2026":
        st.write("📊 **Anlık Biniş Listesi**")
        data = conn.read(spreadsheet=url)
        st.dataframe(data)