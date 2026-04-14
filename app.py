import streamlit as st

# Güvenli alandan verileri çek (Secrets)
# Veriler Streamlit Dashboard üzerinden tanımlanacak
ogrenci_verisi = st.secrets["ogrenci_listesi"]

st.set_page_config(page_title="EGEKAF 2026 Kontrol", page_icon="🚌")

st.title("🚌 EGEKAF 2026 Otobüs Kontrolü")

# Basit bir session state ile onay durumunu tutalım
if 'onaylandi' not in st.session_state:
    st.session_state.onaylandi = False

tel_input = st.text_input("Telefon Numaranız (Örn: 5xxxxxxxxx)", max_chars=10)

if tel_input:
    if tel_input in ogrenci_verisi:
        isim = ogrenci_verisi[tel_input]
        st.success(f"Hoş Geldiniz, **{isim}**")
        
        onay = st.checkbox(f"Otobüse binişimi ({isim}) onaylıyorum.")
        
        if st.button("Onayla ve Kaydet"):
            if onay:
                st.session_state.onaylandi = True
                st.balloons()
                st.success(f"Kayıt Başarılı! İyi yolculuklar {isim}.")
            else:
                st.warning("Lütfen önce onay kutusunu işaretleyin.")
    else:
        st.error("Numara bulunamadı. Lütfen kontrol ediniz.")