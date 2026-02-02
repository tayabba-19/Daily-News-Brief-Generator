import streamlit as st
import requests
from datetime import date

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Daily News Brief Generator", layout="wide")

NEWS_API_KEY = "PASTE_YOUR_NEWSAPI_KEY_HERE"
BASE_URL = "https://newsapi.org/v2/top-headlines"

CATEGORIES = ["technology", "business", "sports", "health", "entertainment", "politics"]

# ---------------- FUNCTIONS ----------------
def fetch_news(category):
    params = {
        "apiKey": NEWS_API_KEY,
        "category": category,
        "country": "us",
        "pageSize": 5
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data.get("articles", [])

def summarize(text):
    if not text:
        return "No summary available."
    return text[:150] + "..."

# ---------------- UI ----------------
st.title("📰 Daily News Brief Generator")

st.sidebar.header("Select Preferences")

selected_categories = st.sidebar.multiselect(
    "Choose news categories",
    CATEGORIES,
    default=["technology", "business"]
)

selected_date = st.sidebar.date_input(
    "Select Date",
    value=date.today()
)

if st.sidebar.button("Generate News Brief"):
    st.success("Personalized news generated!")

    for category in selected_categories:
        st.subheader(f"🔹 {category.capitalize()} News")

        articles = fetch_news(category)

        if not articles:
            st.info("No news available.")
            continue

        for article in articles:
            st.markdown(f"**{article['title']}**")
            st.write(summarize(article.get("description")))
            st.caption(f"Source: {article['source']['name']}")
            st.markdown("---")

else:
    st.info("Select preferences and click 'Generate News Brief'")
