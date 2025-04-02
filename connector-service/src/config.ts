import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

// Get __dirname equivalent in ESM
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment variables
const envPath = path.resolve(__dirname, '../.env');
if (fs.existsSync(envPath)) {
  dotenv.config({ path: envPath });
} else {
  dotenv.config();
}

export const config = {
  telegramBotToken: process.env.TELEGRAM_BOT_TOKEN || '',
  botServiceUrl: process.env.BOT_SERVICE_URL || 'http://localhost:8000',
  port: parseInt(process.env.PORT || '3000', 10)
};

// Validate required config
if (!config.telegramBotToken) {
  throw new Error('TELEGRAM_BOT_TOKEN environment variable is required');
}
if (!config.botServiceUrl) {
  throw new Error('BOT_SERVICE_URL environment variable is required');
} 