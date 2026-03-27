from openai import OpenAI
from pydub import AudioSegment
import tempfile
import io

client = OpenAI()

def speech_to_text(audio_bytes):
    try:
        # ✅ Proper mulaw decoding
        audio = AudioSegment.from_raw(
            io.BytesIO(audio_bytes),
            sample_width=1,
            frame_rate=8000,
            channels=1
        )

        # Convert to WAV
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            audio.export(f.name, format="wav")
            temp_filename = f.name

        with open(temp_filename, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe",
                file=audio_file
            )

        return transcript.text

    except Exception as e:
        print("STT Error:", e)
        return ""