# Telegram Expense Tracker - Bot Service

This is the Python-based service that processes Telegram messages to extract expense details using AI and stores them in a Supabase database.

## ✨ Features

- Message interpretation using LangChain + GPT-4o  
- Expense extraction and categorization  
- Supabase integration for data storage  
- User whitelisting via `users` table  

## 📦 Requirements

- Python 3.11+  
- OpenAI API key  
- Supabase project with API key and public schema  

## ⚙️ Setup Instructions

1. Clone this repository  
2. Navigate to the `bot-service` directory  
3. Create a virtual environment:  
   ```bash
   python -m venv venv
   ```
4. Activate it:  
   - **Windows**:  
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:  
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
6. Copy `.env.example` to `.env` and fill in:  
   - `SUPABASE_URL`  
   - `SUPABASE_API_KEY`  
   - `OPENAI_API_KEY`  
7. Run the service locally:  
   ```bash
   python app.py
   ```

## 📡 API Endpoints

- **POST** `/process-message`  
  Accepts a JSON payload `{ telegram_id, message_text }`, processes the message using GPT, and stores the result in Supabase.

## 🧪 Testing

To run unit tests:  
```bash
pytest tests/
```

## ☁️ Deployment (Recommended: Vercel)

This service can be deployed to [Vercel](https://vercel.com):

1. Set the root directory to `bot-service`  
2. Vercel will auto-detect and deploy the FastAPI service  
3. Set the following environment variables:  
   - `SUPABASE_URL`  
   - `SUPABASE_API_KEY`  
   - `OPENAI_API_KEY`  

Once deployed, the `/process-message` endpoint will be available via HTTPS.

## 🔐 Environment Variables

| Variable             | Description                                  |
|----------------------|----------------------------------------------|
| `SUPABASE_URL`       | Your Supabase project URL                    |
| `SUPABASE_API_KEY`   | Service Role or anon key                     |
| `OPENAI_API_KEY`     | API key for GPT-4o access                    |
