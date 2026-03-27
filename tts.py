from openai import OpenAI
from pydub import AudioSegment
import tempfile
import base64

client = OpenAI()

def text_to_speech(text):
    try:
        # Step 1: Generate MP3
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            mp3_file = f.name

        audio = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        )

        audio.stream_to_file(mp3_file)

        # Step 2: Convert MP3 → mulaw 8kHz
        sound = AudioSegment.from_file(mp3_file, format="mp3")

        sound = sound.set_frame_rate(8000).set_channels(1)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            wav_file = f.name
            sound.export(wav_file, format="wav", codec="pcm_mulaw")

        # Step 3: Read + base64 encode
        with open(wav_file, "rb") as f:
            mulaw_bytes = f.read()

        return base64.b64encode(mulaw_bytes).decode("utf-8")

    except Exception as e:
        print("TTS Error:", e)
        return None