import { Telegraf, Context } from 'telegraf';
import { User } from 'telegraf/types';
import { createBot } from '../bot';
import { commands } from '../commands';
import { translations } from '../i18n/translations';

// Mock Telegraf
const mockCommand = jest.fn();
const mockOn = jest.fn();
const mockSetMyCommands = jest.fn().mockResolvedValue(true);

jest.mock('telegraf', () => {
    return {
        Telegraf: jest.fn().mockImplementation(() => ({
            command: mockCommand,
            on: mockOn,
            launch: jest.fn(),
            telegram: {
                setMyCommands: mockSetMyCommands
            }
        }))
    };
});

describe('Telegram Bot', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    it('should register all commands', async () => {
        createBot('fake-token');
        
        const expectedCommands = ['start', 'search', 'categories', 'cart', 'help'];
        expectedCommands.forEach(cmd => {
            expect(mockCommand).toHaveBeenCalledWith(cmd, expect.any(Function));
        });

        expect(mockSetMyCommands).toHaveBeenCalledWith([
            { command: 'start', description: translations.it.commands.start },
            { command: 'search', description: translations.it.commands.search },
            { command: 'categories', description: translations.it.commands.categories },
            { command: 'cart', description: translations.it.commands.cart },
            { command: 'help', description: translations.it.commands.help }
        ]);
    });

    describe('Command Handlers', () => {
        let mockContext: Partial<Context>;
        
        beforeEach(() => {
            const mockUser: User = {
                id: 12345,
                is_bot: false,
                first_name: 'Test User',
                language_code: 'en'
            };

            mockContext = {
                reply: jest.fn(),
                from: mockUser
            };
        });

        it('should handle start command correctly', async () => {
            await commands.start(mockContext as Context);
            expect(mockContext.reply).toHaveBeenCalledWith(translations.en.welcome);
        });

        it('should handle search command correctly', async () => {
            await commands.search(mockContext as Context);
            expect(mockContext.reply).toHaveBeenCalledWith(translations.en.search);
        });

        it('should handle categories command correctly', async () => {
            await commands.categories(mockContext as Context);
            expect(mockContext.reply).toHaveBeenCalledWith(translations.en.categories);
        });

        it('should handle cart command correctly', async () => {
            await commands.cart(mockContext as Context);
            expect(mockContext.reply).toHaveBeenCalledWith(translations.en.cart_empty);
        });
    });
});
