import { Context } from 'telegraf';
import { translations } from '../i18n/translations';
import { Language } from '../i18n/translations';

function getUserLanguage(ctx: Context): Language {
    // Get user language from context or default to Italian
    return (ctx.from?.language_code === 'en' ? 'en' : 'it') as Language;
}

export const commands = {
    start: async (ctx: Context) => {
        const lang = getUserLanguage(ctx);
        await ctx.reply(translations[lang].welcome);
    },

    search: async (ctx: Context) => {
        const lang = getUserLanguage(ctx);
        await ctx.reply(translations[lang].search);
    },

    categories: async (ctx: Context) => {
        const lang = getUserLanguage(ctx);
        await ctx.reply(translations[lang].categories);
    },

    cart: async (ctx: Context) => {
        const lang = getUserLanguage(ctx);
        await ctx.reply(translations[lang].cart_empty);
    },

    help: async (ctx: Context) => {
        const lang = getUserLanguage(ctx);
        await ctx.reply(translations[lang].help);
    }
};
