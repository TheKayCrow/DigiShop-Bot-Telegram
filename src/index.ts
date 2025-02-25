import * as dotenv from 'dotenv';
import { createBot } from './bot';

dotenv.config();

const token = process.env.BOT_TOKEN;
if (!token) {
    throw new Error('BOT_TOKEN must be provided in environment variables!');
}

const bot = createBot(token);

export default bot;
