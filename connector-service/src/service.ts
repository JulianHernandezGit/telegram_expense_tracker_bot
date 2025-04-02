import axios from 'axios';
import { config } from './config.js';

interface ProcessMessageResponse {
  status: 'success' | 'error' | 'ignored';
  message?: string;
  reason?: string;
  expense?: {
    description: string;
    amount: number;
    category: string;
  };
}

export async function processMessage(telegramId: string, messageText: string): Promise<ProcessMessageResponse> {
  try {
    const response = await axios.post(`${config.botServiceUrl}/process-message`, {
      telegram_id: telegramId,
      message_text: messageText
    });

    return response.data;
  } catch (error) {
    console.error('Error calling bot service:', error);
    return {
      status: 'error',
      reason: 'Failed to communicate with bot service'
    };
  }
} 