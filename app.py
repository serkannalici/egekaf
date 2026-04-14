import streamlit as st

# EGEKAF 2026 Güncel Katılımcı Listesi
ogrenci_verisi = {
    "5445700995": "Efe Mustafa Göçmen", "5319108943": "Samed Dinler",
    "5521801297": "Hamidov Soumah", "5387390599": "Melike Çetinkaya",
    "5050190615": "Berna Yankın", "5422845301": "Emine Gülbel",
    "5433553002": "Ervanur Hanay", "5534926335": "Öykü Soyakça",
    "5300732501": "Muhamet Mustafa Polat", "5445749061": "Şaban Alphan Erdoğan",
    "5536753245": "Asude Özbey", "5520093421": "Yusuf Ali Çağnat",
    "5434459949": "Güneş Söylemez", "5389873458": "Kevser Yılmaz",
    "5316685044": "Seçil Arıcan", "5535856497": "Sıla Demirel",
    "5383430407": "Yağmur Kılıç", "5393615355": "Batuhan Vapur",
    "5319409090": "Elif Bolat", "5077486762": "Aydeniz Aydoğmuş",
    "5012403848": "Zeynep Akbulut", "5334460214": "Efe Akın Görgel",
    "5411297239": "Alptuğ Şanlı", "5467941269": "Utku Yetim",
    "5061749898": "Emir Bekman", "5365002678": "Ramazan Çoşkun",
    "5399497414": "Tuğba Atik", "5550064316": "Musa Çelik",
    "5444899588": "Rumeysa Ölçer", "5386497879": "Betül Dönmez",
    "5070110051": "Mustafa Yiğit Nal", "5339400225": "Esen Geç",
    "5366437250": "Onur Arslan", "5058994859": "Polat Can Akpolat",
    "5464860960": "Gamze Türker", "5466999507": "Meryem Nur Yıkılmaz",
    "5510265842": "Yusuf Akbaş", "5533861749": "Barış Altu",
    "5527821549": "Elanur Kılıç", "5550447546": "Duygu Varol",
    "5426735587": "Yusuf Dönmez", "5313656107": "Rumesya baydar",
    "5432248860": "Nurhayat Demircan", "5316486309": "Canan yıldız",
    "5519487047": "Yiğit Murat Karslı", "5523036902": "Sinem Yörük",
    "5411453712": "Emirhan Aktaş"
}

st.set_page_config(page_title="EGEKAF 2026 Otobüs Kontrol", page_icon="🚌")

st.title("🚌 EGEKAF 2026 Otobüs Giriş Kontrolü")
st.write("Lütfen listedeki isminizi doğrulamak için telefon numaranızı giriniz.")

# Kullanıcı girişi
tel_input = st.text_input("Telefon Numaranız (Örn: 5xxxxxxxxx)", max_chars=10)

if tel_input:
    # Telefon numarası eşleştirme
    if tel_input in ogrenci_verisi:
        isim = ogrenci_verisi[tel_input]
        st.success(f"Hoş Geldiniz, **{isim}**")
        
        onay = st.checkbox(f"Otobüse binişimi ({isim}) onaylıyorum.")
        
        if st.button("Onayla ve Kaydet"):
            if onay:
                # Veriyi kaydetme simülasyonu (Gerçek senaryoda DB veya Google Sheets'e yazılır)
                st.balloons()
                st.info(f"Kayıt Başarılı! {isim} olarak otobüs binişiniz sisteme işlendi.")
                # Loglama için (Terminalde görünür)
                print(f"ONAY ALINDI: {isim} ({tel_input})") 
            else:
                st.warning("Lütfen yukarıdaki onay kutusunu işaretleyiniz.")
    else:
        st.error("Girdiğiniz numara listede bulunamadı. Lütfen numaranızı kontrol ediniz.")

st.markdown("---")
st.caption("Aydın Tekstil Park Fuar Alanı - Ege Kariyer Fuarı 2026")