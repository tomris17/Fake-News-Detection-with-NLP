# Fake News Detection with NLP

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit-learn-ML-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains a natural language processing (NLP) pipeline that classifies news articles as real or fake based on headlines and body texts using TF-IDF and Machine Learning[cite: 18].

---

## Project Workflow
1. **Data Preprocessing**: Loading dataset from `data.csv`[cite: 18] and handling missing values in headline and body text[cite: 18].
2. **Feature Engineering**: Combining `Headline` and `Body` columns into a unified `content` feature[cite: 18].
3. **Text Vectorization**: Converting textual data into numerical vectors using `TfidfVectorizer` with English stop words filtering[cite: 18].
4. **Model Training & Evaluation**: Training a `MultinomialNB` classifier and evaluating performance using accuracy score[cite: 18].
5. **Model Serialization**: Saving the trained model using `joblib` (`fake_news_model.pkl`)[cite: 18].
6. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/fake-news-detection-nlp.git](https://github.com/YOUR_USERNAME/fake-news-detection-nlp.git)
   cd fake-news-detection-nlp
