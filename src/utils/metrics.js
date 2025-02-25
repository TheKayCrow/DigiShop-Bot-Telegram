const winston = require('winston');
const { limiter } = require('./middleware/rateLimiter');
const Metrics = require('./utils/metrics');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

app.use(limiter);

Metrics.logUserAction(userId, 'search_product');

class Metrics {
  static logUserAction(userId, action) {
    logger.info('user_action', {
      userId,
      action,
      timestamp: new Date().toISOString()
    });
  }

  static logError(error) {
    logger.error('error', {
      message: error.message,
      stack: error.stack,
      timestamp: new Date().toISOString()
    });
  }

  static logPerformance(operation, duration) {
    logger.info('performance', {
      operation,
      duration,
      timestamp: new Date().toISOString()
    });
  }
}

module.exports = Metrics;
