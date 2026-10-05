import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Fake News Detection App", layout="centered")

st.title("Fake News Detection with NLP")
st.write(
    "Bu uygulama, haber makalelerinin başlık ve metin içeriklerini analiz ederek haberin gerçek mi yoksa sahte mi olduğunu tahmin eder."
)

@st.cache_resource
def load_model():
    return joblib.load("fake_news_model.pkl")

try:
    model = load_model()
    
    headline_input = st.text_input("Haber Başlığı (Headline):")
    body_input = st.text_area("Haber Metni (Body):")
    
    if st.button("Haber Kontrolü Yap"):
        if headline_input.strip() != "" or body_input.strip() != "":
            content = headline_input + " " + body_input
            st.success(f"Analiz Edilen İçerik: {content}")
            st.info("Model başarıyla yüklendi. Tahmin işlemi gerçekleştirilmeye hazırdır.")
        else:
            st.warning("Lütfen başlık veya gövde metninden en az birini girin.")

except Exception as e:
    st.error(f"Model yüklenirken bir hata oluştu: {e}")