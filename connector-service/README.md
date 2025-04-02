# Telegram Expense Tracker - Connector Service

This is the Node.js service that connects to the Telegram Bot API and forwards messages to the Bot Service for processing.

## ✨ Features

- Telegram Bot API integration  
- Message forwarding to the Bot Service via HTTP  
- Sends response messages back to users  
- Includes a `/health` endpoint for server checks  

## 📦 Requirements

- Node.js LTS (v18 or newer)  
- Telegram Bot Token from BotFather  
- Railway (or similar platform) to run the bot continuously  

## ⚙️ Setup Instructions

1. Clone this repository  
2. Navigate to the `connector-service` directory:  
   ```bash
   cd connector-service
   ```
3. Install dependencies:  
   ```bash
   npm install
   ```
4. Copy the environment template:  
   ```bash
   cp .env.example .env
   ```
5. Fill in the following environment variables in `.env`:  
   - `TELEGRAM_BOT_TOKEN`  
   - `BOT_SERVICE_URL`  
   - (Optional) `PORT` (default is `3000`)  
6. Build the TypeScript code:  
   ```bash
   npm run build
   ```
7. Start the service:  
   ```bash
   npm start
   ```

## 🚀 Development Mode

To run the bot live without building:  
```bash
npm run dev
```

This uses ts-node with ES module support.  

## ☁️ Deployment (Recommended: Railway)

Deploy this service to [Railway](https://railway.app) or any Node-compatible host:

1. Set the root directory to `connector-service`  
2. Railway will auto-detect:  
   - Build command: `npm run build`  
   - Start command: `npm start`  
3. Add environment variables:  
   - `TELEGRAM_BOT_TOKEN`  
   - `BOT_SERVICE_URL` → use the URL of your deployed Bot Service on Vercel  

Once deployed, the bot will be live and listen to messages in real time.  

## 🔐 Environment Variables

| Variable             | Description                                                    |
|----------------------|----------------------------------------------------------------|
| `TELEGRAM_BOT_TOKEN` | Telegram Bot token (from BotFather)                            |
| `BOT_SERVICE_URL`    | URL of the deployed Bot Service (e.g., https://...vercel.app)  |
| `PORT`               | Optional. Port for the /health check (default: 3000)           |
