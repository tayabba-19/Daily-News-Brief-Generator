# Daily-News-Brief-Generator
# 📰 Daily News Brief Generator

An AI-powered web application that generates **personalized daily news briefs**
based on user-selected preferences such as Technology, Business, Sports, Health,
Entertainment, and Politics.

The goal of this project is to help users stay informed without information
overload by providing **short, clear, and relevant news summaries** from multiple
sources.

---

## 📌 Problem Statement

In today’s fast-paced digital world, users are exposed to a huge volume of news
from different platforms. Most news applications show generic headlines, forcing
users to manually browse multiple categories and sources.

This project solves that problem by:
- Filtering news based on user interests
- Summarizing long articles into short, readable briefs
- Displaying personalized news on a single dashboard

---

## 🎯 Objective

The objectives of this project are:
- To build a personalized news briefing application
- To aggregate news from multiple sources using an API
- To generate concise summaries instead of long articles
- To design a clean and easy-to-use user interface
- To deploy a fully functional end-to-end solution on the cloud

---

## 🚀 Features

- ✅ User preference–based news selection  
- ✅ Multiple news categories supported  
- ✅ Short and readable news summaries  
- ✅ Category-wise daily news brief  
- ✅ Clean and simple UI using Streamlit  
- ✅ Cloud deployment with public access  

---

## 🛠️ Tech Stack

**Backend & Logic**
- Python

**Frontend**
- Streamlit

**News Source**
- Newsdata.io API (free tier)

**Deployment**
- Streamlit Cloud

**Version Control**
- GitHub

---

## 🧠 How Personalization Works

1. User selects preferred news categories from the sidebar  
2. The application fetches news only for the selected categories  
3. Each category is displayed as a separate section  
4. News articles are summarized and shown as a daily brief  

This ensures that users only see news relevant to their interests.

---

## 🔄 Application Flow

1. User opens the application  
2. User selects preferred news categories  
3. User clicks **Generate News Brief**  
4. Backend fetches news from Newsdata.io API  
5. Articles are summarized  
6. Personalized news brief is displayed on the home page  

---

## 📥 Input

- User-selected news categories  
- Optional date selection (UI level)

## 📤 Output

A personalized daily news brief, for example:

**Your Daily Technology Brief**
- AI regulation discussions intensify globally  
- Major tech companies announce new AI tools  

**Business Highlights**
- Markets show mixed trends amid inflation concerns  

Sources are displayed with each article.

---

## 🌐 Deployment

The application is deployed on **Streamlit Cloud** and is publicly accessible.

**Live App Link:**  
👉 https://daily-news-brief-generator-lkkn8nnzx5zvxa63ypwmjp.streamlit.app/

---

## 📁 Project Structure
daily-news-brief-generator/ │ ├── app.py ├── requirements.txt ├── README.md └── preferences.json
