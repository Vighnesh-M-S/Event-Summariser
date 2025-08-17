# AI Meeting Summarizer & Sharer

## 📌 Overview

This is a **full-stack application** that allows users to: - Upload or
paste a meeting transcript - Enter a custom summarization prompt (e.g.,
"Summarize only action items") - Generate an AI-powered structured
summary using **Groq API** - Edit the summary before sending - Share the
final summary via **email** using SendGrid

The frontend is built with **HTML, CSS, and JavaScript**, while the
backend uses **FastAPI (Python)**.

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   **Frontend**: HTML, CSS, JavaScript
-   **Backend**: Python (FastAPI)
-   **AI Model**: Groq (`llama-3.3-70b-versatile`)
-   **Email Service**: SendGrid API
-   **Deployment**: (Frontend - Netlify/Vercel, Backend -
    Render/Railway)

------------------------------------------------------------------------

## 🚀 How It Works

1.  User pastes or uploads a transcript in the frontend.
2.  User enters a custom prompt.
3.  Frontend sends transcript + prompt → **Backend**.
4.  Backend calls **Groq API** → generates structured summary.
5.  Summary is returned to frontend, displayed in editable text box.
6.  User edits if needed and enters recipient email.
7.  Frontend sends request → backend calls **SendGrid API** → email is
    delivered.

------------------------------------------------------------------------

## 🛠️ API Endpoints

### 1. `/summarize`

**POST Request**

``` json
{
  "transcript": "Full transcript text...",
  "prompt": "Summarize in bullet points for executives"
}
```

**Response**

``` json
{
  "summary": "- Action: Prepare revised marketing plan..."
}
```

------------------------------------------------------------------------

### 2. `/send-email`

**POST Request**

``` json
{
  "summary": "- Action: Prepare revised marketing plan...",
  "recipient": "user@example.com"
}
```

**Response**

``` json
{
  "message": "Email sent successfully!",
  "status": 202
}
```

------------------------------------------------------------------------

## 🔑 Environment Variables

Create a `.env` or export variables in your shell:

``` bash
export GROQ_API_KEY="your_groq_api_key"
export SENDGRID_API_KEY="your_sendgrid_api_key"
```

------------------------------------------------------------------------

## 🖥️ Running Locally

### Install dependencies

``` bash
pip install fastapi uvicorn groq sendgrid
```

### Run backend

``` bash
python main.py
```

or

``` bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Open frontend

Simply open `index.html` in your browser.

------------------------------------------------------------------------

## 🌍 Deployment

-   **Backend**: Deploy `main.py` (FastAPI) to Render or Railway.

🔗 **Deployed Link**: https://event-summariser.onrender.com/

------------------------------------------------------------------------
