const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minuti
  max: 100, // limite di richieste per IP
  message: 'Troppe richieste, riprova più tardi'
});

const botLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minuto
  max: 30, // limite messaggi per utente
  message: 'Per favore, attendi prima di inviare altri messaggi'
});

module.exports = { limiter, botLimiter };
