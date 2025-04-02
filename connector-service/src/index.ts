import { startBot } from './bot.js';
import { config } from './config.js';
import http from 'http';

// Create a simple health check server
const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok' }));
  } else {
    res.writeHead(404);
    res.end();
  }
});

// Start the server
server.listen(config.port, () => {
  console.log(`Server is running on port ${config.port}`);
});

// Start the Telegram bot
startBot();

// Handle process termination
process.on('SIGINT', () => {
  console.log('Shutting down...');
  server.close();
  process.exit(0);
}); 