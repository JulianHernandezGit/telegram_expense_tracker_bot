import TelegramBot from 'node-telegram-bot-api';
import { config } from './config.js';
import { processMessage } from './service.js';

// Create a bot instance
const bot = new TelegramBot(config.telegramBotToken, { polling: true });

export function startBot(): void {
  console.log('Starting Telegram bot...');

  // Handle messages
  bot.on('message', async (msg) => {
    const chatId = msg.chat.id;
    const telegramId = msg.from?.id.toString();
    const messageText = msg.text;

    if (!telegramId || !messageText) {
      return;
    }

    try {
      const response = await processMessage(telegramId, messageText);
      
      // Only reply if we have a success status
      if (response.status === 'success') {
        bot.sendMessage(chatId, response.message || '');
      }
    } catch (error) {
      console.error('Error processing message:', error);
      // Do not send error messages to users as per requirements
    }
  });

  console.log('Telegram bot started successfully');
} 