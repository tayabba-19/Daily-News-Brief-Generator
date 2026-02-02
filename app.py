import streamlit as st
import requests
from datetime import date

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Daily News Brief Generator",
    layout="wide"
)

# ---------------- API CONFIG ----------------
NEWSDATA_API_KEY = "pub_aab44dd9e821419cb2ca4c650672ecb2"
BASE_URL = "https://newsdata.io/api/1/news"

# Categories supported by Newsdata.io
CATEGORIES = [
    "technology",
    "business",
    "sports",
    "health",
    "entertainment",
    "politics"
]

# ---------------- FUNCTIONS ----------------
def fetch_news(category):
    params = {
        "apikey": NEWSDATA_API_KEY,
        "language": "en",
        "category": category,
        "size": 5
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return []

    data = response.json()
    return data.get("results", [])


def summarize(text):
    if not text:
        return "Summary not available."
    return text[:180] + "..."


# ---------------- UI ----------------
st.title("📰 Daily News Brief Generator")
st.write("Personalized daily news brief using AI summarization")

# Sidebar
st.sidebar.header("🔧 Preferences")

selected_categories = st.sidebar.multiselect(
    "Select news categories",
    CATEGORIES,
    default=["technology", "business"]
)

selected_date = st.sidebar.date_input(
    "Select date",
    value=date.today()
)

generate = st.sidebar.button("Generate News Brief")

# ---------------- OUTPUT ----------------
if generate:
    if not selected_categories:
        st.warning("Please select at least one category.")
    else:
        st.success("Your personalized news brief is ready!")

        for category in selected_categories:
            st.subheader(f"🔹 {category.capitalize()} News")

            articles = fetch_news(category)

            if not articles:
                st.info("No news available for this category.")
                continue

            for article in articles:
                st.markdown(f"### {article.get('title', 'No title')}")
                st.write(summarize(article.get("description")))
                st.caption(
                    f"Source: {article.get('source_id', 'Unknown')} | "
                    f"Date: {article.get('pubDate', '')[:10]}"
                )
                st.markdown("---")
else:
    st.info("👈 Select preferences and click **Generate News Brief**")
