
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gpt/', methods=['GET', 'POST'])
def gpt():
    user_input = request.json.get('message')   # 👈 JSON now

    try:
        response = client.chat.completions.create(
            model="google/gemini-3-flash-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Keep answers short."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=100
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})   # 👈 return JSON

    except Exception as e:
        return jsonify({"error": str(e)})
   




if __name__ == "__main__":
    app.run(debug=True)





