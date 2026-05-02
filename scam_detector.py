import re

scam_keywords = [
    "win money", "free gift", "click here", "urgent",
    "bank account", "password", "lottery", "claim now",
    "verify account", "limited offer"
]

def detect_scam(text):
    text = text.lower()

    score = 0

    for keyword in scam_keywords:
        if keyword in text:
            score += 1

    url_pattern = r'https?://\S+|www\.\S+'
    if re.search(url_pattern, text):
        score += 2

    email_pattern = r'\S+@\S+'
    if re.search(email_pattern, text):
        score += 1

    if score >= 3:
        return "⚠️ Scam Detected"
    else:
        return "✅ Safe Message"