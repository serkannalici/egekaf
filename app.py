import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Sayfa yapılandırması
st.set_page_config(page_title="EGEKAF 2026 Kontrol", page_icon="🚌")

# Secrets'tan öğrenci listesini çek
ogrenci_verisi = st.secrets["ogrenci_listesi"]

# Google Sheets Bağlantısı
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
                    
                    # Tablo boşsa başlıklarla oluştur
                    if existing_data is None or existing_data.empty:
                        existing_data = pd.DataFrame(columns=["Telefon", "Ad Soyad", "Onay Durumu", "Tarih"])
                    
                    # Mükerrer kaydı önlemek için kontrol
                    if tel_input in existing_data["Telefon"].astype(str).values:
                        st.warning(f"Sayın {isim}, bu numara ile daha önce biniş onayı verilmiş.")
                    else:
                        # Yeni biniş kaydı (3. sütun: Onay Durumu)
                        yeni_kayit = {
                            "Telefon": tel_input, 
                            "Ad Soyad": isim, 
                            "Onay Durumu": "Otobüse biniş onaylandı",
                            "Tarih": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        }
                        new_entry = pd.DataFrame([yeni_kayit])
                        
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