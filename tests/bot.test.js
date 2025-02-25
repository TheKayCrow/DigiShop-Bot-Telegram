const { expect } = require('chai');
const sinon = require('sinon');
const Bot = require('../src/bot');

describe('Telegram Bot Tests', () => {
  let bot;
  
  beforeEach(() => {
    bot = new Bot();
  });

  describe('Message Handling', () => {
    it('should handle start command', async () => {
      const msg = { text: '/start', chat: { id: 123 } };
      const result = await bot.handleMessage(msg);
      expect(result).to.be.true;
    });

    it('should handle product search', async () => {
      const msg = { text: 'search product', chat: { id: 123 } };
      const result = await bot.handleMessage(msg);
      expect(result).to.be.true;
    });
  });
});
