# Telegram Expense Tracker - Connector Service

Node.js service that connects Telegram API with the Bot Service.

## Features
- Telegram Bot API integration
- Message forwarding to Bot Service
- Response handling

## Requirements
- Node.js LTS (18.x or newer)
- Telegram Bot token

## Setup Instructions
1. Clone this repository
2. Install dependencies: `npm install`
3. Copy `.env.example` to `.env` and fill in your credentials
4. Build the TypeScript code: `npm run build`
5. Start the service: `npm start`
   
## Development
- Run in development mode: `npm run dev`

## Environment Variables
- `TELEGRAM_BOT_TOKEN`: Your Telegram Bot token
- `BOT_SERVICE_URL`: URL of the Bot Service
- `PORT`: Port for the health check server (default: 3000) 