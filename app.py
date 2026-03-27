from fastapi import FastAPI, WebSocket
from ws_handler import handle_audio_stream
from twilio_config import client, TWILIO_PHONE_NUMBER
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Connect
from twilio_config import router

app = FastAPI(title="AI VoiceBot API")
app.include_router(router)

@app.get("/")
def home():
    return {"message": "VoiceBot API running 🚀"}

@app.get("/test")
def test():
    return {"status": "working"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await handle_audio_stream(websocket)

@app.get("/call")
def make_call():
    call = client.calls.create(
        to="+918920922796",
        from_="+14783752185",
        url="https://sodless-contessa-unaspiringly.ngrok-free.dev/voice"
    )
    return {"status": "calling", "sid": call.sid}

