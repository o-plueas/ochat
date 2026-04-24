

   Flask GPT Chat App (OpenRouter + Gemini)

A simple Flask web application that connects to the OpenRouter API and uses the Gemini Flash model to generate short AI responses. The app accepts user input via JSON and returns AI-generated replies.

  Features

  Flask-based backend
  JSON API endpoint for chat interaction
  Uses OpenRouter API
  Powered by `google/gemini-3-flash-preview`
  Fast and concise AI responses
  Environment variable support with `.env`

Live Site = (https://ochat-one.vercel.app/)
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
   


 License

This project is open-source and available under the MIT License.

    