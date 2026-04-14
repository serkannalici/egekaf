import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Secrets'tan verileri çek
# Not: Streamlit Cloud Dashboard > Settings > Secrets kısmında 
# ogrenci_listesi ve gsheets_url tanımlı olmalıdır.
ogrenci_verisi = st.secrets["ogrenci_listesi"]
url = st.secrets["gsheets_url"]

# Google Sheets Bağlantısı
conn = st.connection("gsheets", type=GSheetsConnection)

st.set_page_config(page_title="EGEKAF 2026 Kontrol", page_icon="🚌")

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
                    existing_data = conn.read(spreadsheet=url)
                    
                    # Yeni biniş kaydı
                    new_entry = pd.DataFrame([{"Telefon": tel_input, "Ad Soyad": isim}])
                    
                    # Veriyi birleştir ve tabloyu güncelle
                    updated_df = pd.concat([existing_data, new_entry], ignore_index=True)
                    conn.update(spreadsheet=url, data=updated_df)
                    
                    st.balloons()
                    st.success(f"İşlem Başarılı! İyi yolculuklar {isim}.")
                except Exception as e:
                    st.error(f"Bir hata oluştu: {e}")
            else:
                st.warning("Lütfen yukarıdaki onay kutusunu işaretleyin.")
    else:
        st.error("Girdiğiniz numara listede bulunamadı. Lütfen kontrol ediniz.")

st.markdown("---")
st.caption("Ege Kariyer Fuarı 2026")