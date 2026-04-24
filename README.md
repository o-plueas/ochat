

   Flask GPT Chat App (OpenRouter + Gemini)

A simple Flask web application that connects to the OpenRouter API and uses the Gemini Flash model to generate short AI responses. The app accepts user input via JSON and returns AI-generated replies.


  Features

  Flask-based backend
  JSON API endpoint for chat interaction
  Uses OpenRouter API
  Powered by `google/gemini-3-flash-preview`
  Fast and concise AI responses
  Environment variable support with `.env`



  Project Structure


  Installation

    1. Clone the repository

   
git clone git remote add origin https://github.com/o-plueas/ochat.git


    2. Create a virtual environment

   bash
python -m venv venv
source venv/bin/activate      On Windows: venv\Scripts\activate
   

    3. Install dependencies

   bash
pip install flask openai python-dotenv
   

    

  Environment Variables

Create a `.env` file in the root directory:

   
OPENROUTER_API_KEY=your_api_key_here
   

    

  Running the App

   bash
python app.py
   

The app will start at:

   
http://127.0.0.1:5000/
   

    

  API Usage

    Endpoint

   
POST /gpt/
   

    Request Body (JSON)

   json
{
  "message": "Hello, how are you?"
}
   

    Response

   json
{
  "reply": "I'm doing well! How can I help?"
}
   

    Error Response

   json
{
  "error": "Error message here"
}
   

    

  Code Overview

  Flask handles routing and server logic
  OpenAI client is configured to use OpenRouter
  `/` route serves the frontend (`home.html`)
  `/gpt/` route processes AI requests

    

  Configuration

You can modify:

  Model  

   python
model="google/gemini-3-flash-preview"
   

  Max tokens  

   python
max_tokens=100
   

  System prompt  

   python
"You are a helpful assistant. Keep answers short."
   

    

  Example cURL Request

   bash
curl -X POST http://127.0.0.1:5000/gpt/ \
-H "Content-Type: application/json" \
-d '{"message": "Tell me a joke"}'
   

    

  Notes

  Ensure your API key is valid and has access to OpenRouter models
  The app runs in debug mode by default (not recommended for production)

    

  Production Tips

  Set `debug=False`
  Use a production server like `gunicorn`
  Add request validation and rate limiting

    

 License

This project is open-source and available under the MIT License.

    

If you want, I can also create a minimal frontend (`home.html`) or help you deploy it.
