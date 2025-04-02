# Telegram Expense Tracker Bot

A Telegram bot that helps track expenses by analyzing user messages, categorizing expenses, and storing them in a Supabase database.

## 📦 Project Overview

This project consists of two services:

### 1. Bot Service (Python – FastAPI)

- Analyzes incoming messages using LangChain + OpenAI GPT-4o  
- Extracts expense details and categorizes them into predefined types  
- Stores expense data in a Supabase database  

### 2. Connector Service (Node.js – Telegram Bot)

- Interfaces with the Telegram Bot API  
- Receives and forwards messages to the Bot Service  
- Returns AI-generated responses to users  

## ⚙️ Technologies Used

- FastAPI (Python)  
- Node.js + `node-telegram-bot-api`  
- Supabase (PostgreSQL + REST API)  
- LangChain + OpenAI GPT-4o  
- Railway (Connector Service)  
- Vercel (Bot Service)  

## 🚀 Getting Started

### Prerequisites

- Python 3.11+  
- Node.js LTS  
- Supabase account  
- OpenAI API key  
- Telegram Bot token from BotFather  

### Setup Instructions

1. Clone this repository  
2. Follow the setup guides in each service:

- `bot-service/README.md` → for the Python AI Bot  
- `connector-service/README.md` → for the Telegram Connector  

## 💬 Usage

Once both services are deployed and running:

1. Send a message to your bot on Telegram:
   Example:  
   Pizza 20 bucks  
2. The Connector Service forwards the message to the Bot Service  
3. The Bot Service processes it, extracts the data, and saves it  
4. If successful, the bot replies with something like:  
   Food expense added ✅  
5. The expense is saved in your Supabase database

## ☁️ Deployment Overview

### Bot Service

- Deployed to **Vercel**
- Uses `vercel.json` and exposes `/process-message`
- Environment variables:
  - `SUPABASE_URL`
  - `SUPABASE_API_KEY`
  - `OPENAI_API_KEY`

### Connector Service

- Deployed to **Railway**
- Runs in background using Telegram polling
- Environment variables:
  - `TELEGRAM_BOT_TOKEN`
  - `BOT_SERVICE_URL` → URL from Vercel deployment

## 🔐 Security Note

Row Level Security (RLS) is disabled by default for testing.  
For production, enable RLS and define appropriate policies in Supabase.

## 📄 License

This project is licensed under the ISC License.
