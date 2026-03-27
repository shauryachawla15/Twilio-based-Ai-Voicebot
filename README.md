\# 🎙️ Twilio-based AI Voicebot

A real-time AI voicebot that can talk to users over a phone call using:

\- 📞 Twilio Media Streams

\- 🧠 OpenAI (Speech-to-Text + LLM + Text-to-Speech)

\- ⚡ FastAPI + WebSockets

\---

\## 🚀 Features

\- ✅ Real-time phone call interaction

\- 🎧 Speech-to-Text (STT)

\- 🤖 Intelligent AI responses

\- 🔊 Text-to-Speech (TTS) voice replies

\- ⚡ Live audio streaming

\- 🌍 Handles noisy/multi-language input (responds in English)

\---

\## 🧠 Architecture

User Call (Twilio)

↓

📡 Media Stream (WebSocket)

↓

🎧 Audio Buffer (mulaw → wav using ffmpeg)

↓

🧠 Speech-to-Text (OpenAI)

↓

🤖 LLM Response

↓

🔊 Text-to-Speech

↓

📡 Send Audio Back

↓

📞 User hears AI

\---

\## 📂 Project Structure

voicebot/

│── app.py # FastAPI entry point

│── ws\_handler.py # WebSocket audio handler

│── stt.py # Speech-to-text logic

│── tts.py # Text-to-speech logic

│── llm.py # AI response logic

│── requirements.txt

│── .gitignore

│── README.md

\---

\## ⚙️ Setup

\### 1. Clone repo

\`\`\`bash

git clone https://github.com/shauryachawla15/Twilio-based-Ai-Voicebot.git

cd Twilio-based-Ai-Voicebot

2\. Create virtual environment

python -m venv venv

venv\\Scripts\\activate

3\. Install dependencies

pip install -r requirements.txt

4\. Install FFmpeg (IMPORTANT)

Download FFmpeg and add it to system PATH.

Verify installation:

ffmpeg -version

5\. Set environment variables

Create a .env file:

OPENAI\_API\_KEY=your\_openai\_api\_key

TWILIO\_ACCOUNT\_SID=your\_sid

TWILIO\_AUTH\_TOKEN=your\_token

▶️ Run the Server

uvicorn app:app --reload

Server runs at:

http://127.0.0.1:8000

📞 Twilio Setup

Go to Twilio Console

Configure Voice Webhook

Use Media Streams

Example TwiML:

🧪 How It Works

User calls Twilio number

Audio is streamed in real-time

Audio → Text (STT)

AI generates response

Response → Audio (TTS)

Audio sent back to user

⚠️ Important Notes

FFmpeg must be installed and added to PATH

Audio is buffered before processing

Small chunks may reduce transcription accuracy

AI responses are forced in English
