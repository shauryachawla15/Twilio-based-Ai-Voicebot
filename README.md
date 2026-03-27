# 🎙️ Twilio-based AI Voicebot

A real-time AI voicebot that can talk to users over a phone call using:

- 📞 Twilio Media Streams  
- 🧠 OpenAI (Speech-to-Text + LLM + Text-to-Speech)  
- ⚡ FastAPI + WebSockets  

---

## 🚀 Features

- ✅ Real-time phone call interaction  
- 🎧 Speech-to-Text (STT)  
- 🤖 Intelligent AI responses  
- 🔊 Text-to-Speech (TTS) voice replies  
- ⚡ Live audio streaming  
- 🌍 Handles noisy/multi-language input (responds in English)  

---

## 🧠 Architecture

```
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
```

---

## 📂 Project Structure

```
voicebot/
│── app.py              # FastAPI entry point
│── ws_handler.py       # WebSocket audio handler
│── stt.py              # Speech-to-text logic
│── tts.py              # Text-to-speech logic
│── llm.py              # AI response logic
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/shauryachawla15/Twilio-based-Ai-Voicebot.git
cd Twilio-based-Ai-Voicebot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg (IMPORTANT)

Download FFmpeg and add it to system PATH.

Verify installation:

```bash
ffmpeg -version
```

### 5. Set Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
```

---

## ▶️ Run the Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 📞 Twilio Setup

1. Go to Twilio Console  
2. Configure Voice Webhook  
3. Enable Media Streams  

### Example TwiML

```xml
<Response>
    <Connect>
        <Stream url="wss://your-domain/ws" />
    </Connect>
</Response>
```

---

## 🧪 How It Works

1. User calls Twilio number  
2. Audio is streamed in real-time  
3. Audio → Text (STT)  
4. AI generates response  
5. Response → Audio (TTS)  
6. Audio sent back to user  

---

## ⚠️ Important Notes

- FFmpeg must be installed and added to PATH  
- Audio is buffered before processing  
- Small chunks may reduce transcription accuracy  
- AI responses are forced in English  
