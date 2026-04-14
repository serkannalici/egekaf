import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Sayfa yapılandırması
st.set_page_config(page_title="EGEKAF 2026 Kontrol", page_icon="🚌")

# Secrets'tan öğrenci listesini çek
# Not: ogrenci_listesi hala Secrets içinde TOML formatında durmalı
ogrenci_verisi = st.secrets["ogrenci_listesi"]

# Google Sheets Bağlantısı (Service Account bilgilerini Secrets'tan otomatik alır)
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🚌 EGEKAF 2026 Otobüs Kontrolü")
st.write("Lütfen telefon numaranızı girerek binişinizi onaylayın.")

tel_input = st.text_input("Telefon Numaranız (Örn: 5xxxxxxxxx)", max_chars=10)

if tel_input:
    if tel_input in ogrenci_verisi:
        isim = ogrenci_verisi[tel_input]
        st.success(f"Hoş Geldiniz, **{isim}**")
        
        onay = st.checkbox(f"Otobüse binişimi ({isim}) onaylıyorum.")
        
        if st.button("Onayla ve Kaydet"):
            if onay:
                try:
                    # Mevcut verileri oku
                    existing_data = conn.read()
                    
                    # Eğer tablo boşsa veya başlıklar yoksa DataFrame oluştur
                    if existing_data is None or existing_data.empty:
                        existing_data = pd.DataFrame(columns=["Telefon", "Ad Soyad"])
                    
                    # mükerrer kaydı önlemek için kontrol
                    if tel_input in existing_data["Telefon"].astype(str).values:
                        st.warning("Bu numara ile daha önce biniş onayı verilmiş.")
                    else:
                        # Yeni biniş kaydı
                        new_entry = pd.DataFrame([{"Telefon": tel_input, "Ad Soyad": isim}])
                        
                        # Veriyi birleştir ve tabloyu güncelle
                        updated_df = pd.concat([existing_data, new_entry], ignore_index=True)
                        conn.update(data=updated_df)
                        
                        st.balloons()
                        st.success(f"İşlem Başarılı! İyi yolculuklar {isim}.")
                except Exception as e:
                    st.error(f"Bağlantı Hatası: {e}")
            else:
                st.warning("Lütfen yukarıdaki onay kutusunu işaretleyin.")
    else:
        st.error("Girdiğiniz numara listede bulunamadı.")

st.markdown("---")
st.caption("Ege Kariyer Fuarı 2026 - Aydın Tekstil Park")