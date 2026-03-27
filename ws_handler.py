import json
import base64
from stt import speech_to_text
from llm import get_bot_reply
from tts import text_to_speech

async def handle_audio_stream(websocket):
    audio_buffer = b""
    CHUNK_THRESHOLD = 32000   # ~2–3 sec audio

    while True:
        data = await websocket.receive_text()
        msg = json.loads(data)

        if msg["event"] == "start":
            start_info = msg.get("start", {})
            stream_sid = start_info.get("streamSid")
            call_sid = start_info.get("callSid")
            print(
                f"Stream started: {stream_sid} | Call SID: {call_sid}"
            )

        if msg["event"] == "media":
            payload = msg["media"]["payload"]

            # base64 → bytes
            chunk = base64.b64decode(payload)
            audio_buffer += chunk

            print("🎧 Receiving... buffer size:", len(audio_buffer))

            # ✅ Process only after enough audio
            if len(audio_buffer) > CHUNK_THRESHOLD:
                text = speech_to_text(audio_buffer)
                print("🧑 User:", text)

                audio_buffer = b""  # reset buffer

                # ✅ Skip empty/noisy text
                if not text or len(text.strip()) < 2:
                    continue

                # 🤖 LLM
                reply = get_bot_reply(text)
                print("🤖 Bot:", reply)

                # 🔊 TTS
                audio_base64 = text_to_speech(reply)

                if audio_base64:
                    await websocket.send_json({
                        "event": "media",
                        "streamSid": stream_sid,
                        "media": {
                            "payload": audio_base64
                        }
                    })

        elif msg["event"] == "stop":
            print("⏹️ Stream stopped")
            break