import bot from './index';

function validateBotToken(token: string) {
    // Basic token format validation
    const tokenFormat = /^\d+:[A-Za-z0-9_-]{35}$/;
    if (!tokenFormat.test(token)) {
        throw new Error('Invalid bot token format. Please check your .env file.');
    }
}

async function startBot() {
    try {
        console.log('Initializing bot...');
        const token = process.env.BOT_TOKEN || '';
        validateBotToken(token);
        
        console.log('Starting bot...');
        await bot.launch();
        console.log('Bot is running!');
    } catch (error) {
        if (error instanceof Error) {
            console.error('Failed to start bot:', error.message);
            if (error.message.includes('404: Not Found')) {
                console.error('Invalid bot token. Please check your .env file and make sure the token is correct.');
            }
        }
        process.exit(1);
    }
}

// Start the bot
startBot();

// Enable graceful stop
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
