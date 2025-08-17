# backend/main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
import requests, smtplib
from email.mime.text import MIMEText
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
import dotenv
from groq import Groq
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = FastAPI()

# Load environment variables from .env file
dotenv.load_dotenv()

# Enable CORS for all origins (customize as needed)
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

client = Groq(api_key=os.environ.get("groq"))  # Load from .env file


class SummarizeRequest(BaseModel):
    transcript: str
    prompt: str

class EmailRequest(BaseModel):
    summary: str
    recipient: str

@app.post("/summarize")
def summarize(req: SummarizeRequest):
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        messages=[
            {"role": "system", "content": "You are a summarizer assistant."},
            {"role": "user", "content": f"{req.prompt}\n\nTranscript:\n{req.transcript}"}
        ],
    )

    summary = chat_completion.choices[0].message.content
    return {"summary": summary}

@app.post("/send-email")
def send_email(req: EmailRequest):
    message = Mail(
        from_email= os.environ.get("email"),  # Load from .env file
        to_emails=req.recipient,
        subject="Meeting Summary",
        plain_text_content=req.summary
    )

    try:
        sg = SendGridAPIClient(os.environ.get("sendgrid"))  # Load from .env file
        response = sg.send(message)

        # ✅ Always return message + status
        return {"message": "Email sent successfully!", "status": response.status_code}

    except Exception as e:
        return {"message": "Failed to send email", "error": str(e)}

@app.get("/", response_class=HTMLResponse)
async def serve_index():
	return FileResponse("index.html")

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
