import os
from pathlib import Path
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from email.message import EmailMessage
import aiosmtplib

from dotenv import load_dotenv
# Ensure .env is loaded from the backend root directory
BACKEND_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(BACKEND_ROOT / ".env", override=True)

router = APIRouter()

RECIPIENT = "alwwwu274@gmail.com"
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


class MailRequest(BaseModel):
    email: EmailStr
    subject: str
    message: str


@router.post("/email")
async def send_mail(body: MailRequest):
    if not SMTP_USER or not SMTP_PASSWORD:
        raise HTTPException(status_code=500, detail="SMTP credentials not configured")

    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = RECIPIENT
    msg["Subject"] = body.subject
    msg["Reply-To"] = body.email
    msg.set_content(body.message)

    try:
        await aiosmtplib.send(
            msg,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SMTP_USER,
            password=SMTP_PASSWORD,
            start_tls=True,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

    return {"message": f"Mail sent successfully to {RECIPIENT}"}