# Telegram Expense Tracker Bot

A Telegram bot that helps track expenses by analyzing user messages, categorizing expenses, and storing them in a database.

## Project Overview

This project consists of two services:

### 1. Bot Service (Python)
- Analyzes incoming messages to extract expense details
- Uses LangChain with OpenAI GPT-4o for message interpretation
- Categorizes expenses into predefined categories
- Persists expense data to Supabase database

### 2. Connector Service (Node.js)
- Interfaces with Telegram API
- Receives and forwards messages to Bot Service
- Returns responses to users via Telegram API

## Getting Started

### Prerequisites
- Python 3.11+ for Bot Service
- Node.js LTS for Connector Service
- Supabase account for database hosting
- OpenAI API key for GPT-4o access
- Telegram Bot API token

### Setup
1. Clone this repository
2. Set up each service following the instructions in their respective README files:
   - [Bot Service README](./bot-service/README.md)
   - [Connector Service README](./connector-service/README.md)

## Usage
Once both services are running, you can interact with the bot on Telegram:
1. Send a message containing expense information (e.g., "Pizza 20 bucks")
2. The bot will analyze the message, extract the expense details, and categorize it
3. If successful, the bot will respond with a confirmation (e.g., "Food expense added ✅")
4. The expense will be stored in your Supabase database

## Deployment
Both services can be deployed to Vercel:
1. Set up environment variables in Vercel dashboard
2. Deploy each service following the instructions in their respective README files
3. Update the Bot Service URL in Connector Service to point to the deployed URL

## License
This project is licensed under the ISC License. 