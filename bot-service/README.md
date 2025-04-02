# Telegram Expense Tracker - Bot Service

Python service that processes expense messages and stores them in a Supabase database.

## Features
- Message analysis with LangChain + GPT-4o
- Expense categorization
- Supabase database integration
- User whitelisting

## Requirements
- Python 3.11+
- OpenAI API key
- Supabase account

## Setup Instructions
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your credentials
6. Run the service: `python app.py`

## API Endpoints
- POST `/process-message`: Process a Telegram message

## Testing
Run tests with pytest: `pytest tests/` 