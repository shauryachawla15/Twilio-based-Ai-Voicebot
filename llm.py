from openai import OpenAI

client = OpenAI()

def get_bot_reply(user_text):
    if not user_text.strip():
        return ""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant. Keep replies short and conversational."},
            {"role": "user", "content": user_text}
        ]
    )

    return response.choices[0].message.content