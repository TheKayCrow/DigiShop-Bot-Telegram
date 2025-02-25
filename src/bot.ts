import { Telegraf } from 'telegraf';
import { commands } from './commands';
import { translations } from './i18n/translations';

export function createBot(token: string) {
    const bot = new Telegraf(token);

    // Set bot commands description for BotFather (Italian)
    const commandDescriptions = [
        { command: 'start', description: translations.it.commands.start },
        { command: 'search', description: translations.it.commands.search },
        { command: 'categories', description: translations.it.commands.categories },
        { command: 'cart', description: translations.it.commands.cart },
        { command: 'help', description: translations.it.commands.help }
    ];

    // Register commands in bot
    Object.entries(commands).forEach(([command, handler]) => {
        bot.command(command, handler);
    });

    // Set commands in BotFather
    bot.telegram.setMyCommands(commandDescriptions).catch(console.error);

    // Handle unknown commands
    bot.on('text', async (ctx) => {
        if (ctx.message.text.startsWith('/')) {
            const lang = ctx.from?.language_code === 'en' ? 'en' : 'it';
            await ctx.reply(translations[lang].unknown_command);
        }
    });

    return bot;
}
