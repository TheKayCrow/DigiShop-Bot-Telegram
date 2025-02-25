export const translations = {
    it: {
        welcome: `
Benvenuto su DigiShop Bot! 🛍️

Comandi disponibili:
/search - Cerca prodotti
/categories - Sfoglia categorie
/cart - Visualizza carrello
/help - Mostra comandi disponibili

Seleziona un comando per iniziare!`,
        search: 'Inserisci il nome del prodotto da cercare: 🔍',
        categories: 'Scegli una categoria:\n\n' +
            '📱 Elettronica\n' +
            '👕 Moda\n' +
            '🏠 Casa e Giardino\n' +
            '🎮 Gaming\n' +
            '📚 Libri',
        cart_empty: 'Il tuo carrello è vuoto. 🛒\nUsa /search per cercare prodotti!',
        help: 'DigiShop Bot - Aiuto:\n\n' +
            '/start - Inizia lo shopping\n' +
            '/search - Cerca prodotti\n' +
            '/categories - Sfoglia categorie\n' +
            '/cart - Visualizza carrello\n' +
            '/help - Mostra questo aiuto',
        unknown_command: 'Comando sconosciuto. Usa /help per vedere i comandi disponibili.',
        commands: {
            start: 'Inizia lo shopping',
            search: 'Cerca prodotti',
            categories: 'Sfoglia categorie',
            cart: 'Visualizza carrello',
            help: 'Mostra comandi disponibili'
        }
    },
    en: {
        welcome: `
Welcome to DigiShop Bot! 🛍️

Available commands:
/search - Search for products
/categories - Browse categories
/cart - View shopping cart
/help - Show available commands

Select a command to get started!`,
        search: 'Enter product name to search: 🔍',
        categories: 'Choose a category:\n\n' +
            '📱 Electronics\n' +
            '👕 Fashion\n' +
            '🏠 Home & Garden\n' +
            '🎮 Gaming\n' +
            '📚 Books',
        cart_empty: 'Your cart is empty. 🛒\nUse /search to find products!',
        help: 'DigiShop Bot - Help:\n\n' +
            '/start - Start shopping\n' +
            '/search - Search products\n' +
            '/categories - Browse categories\n' +
            '/cart - View cart\n' +
            '/help - Show this help',
        unknown_command: 'Unknown command. Use /help to see available commands.',
        commands: {
            start: 'Start shopping',
            search: 'Search products',
            categories: 'Browse categories',
            cart: 'View shopping cart',
            help: 'Show available commands'
        }
    }
};

export type Language = keyof typeof translations;
