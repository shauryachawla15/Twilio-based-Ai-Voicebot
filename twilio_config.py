from fastapi import APIRouter
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Connect
from twilio.rest import Client
import os

# ================================
# 🔐 TWILIO CREDENTIALS
# ================================

ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = "your_twilio_number"

# Create Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ================================
# 🚀FASTAPI ROUTER
# ================================

router = APIRouter()

# ================================
#  VOICE WEBHOOK (VERY IMPORTANT)
# ================================

@router.post("/voice")
async def voice():
    response = VoiceResponse()

    # Optional: initial greeting (helps prevent instant call drop)
    response.say("Hello, your AI voice bot is now connected.", voice="alice")

    # Connect call audio to WebSocket
    connect = Connect()
    connect.stream(
        url="wss://sodless-contessa-unaspiringly.ngrok-free.dev/ws"
    )

    response.append(connect)

    # Return XML (VERY IMPORTANT)
    return Response(content=str(response), media_type="text/xml")