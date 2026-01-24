import logging

# Создание логгера
logger = logging.getLogger('example_logger')
logger.setLevel(level=logging.DEBUG)

# Создание обработчика для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Форматирование сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(console_handler)

if __name__ == '__main__':
    logger.debug("Это сообщение DEBUG.")
    logger.info("Это сообщение INFO.")
    logger.warning("Это сообщение WARNING.")
    logger.error("Это сообщение ERROR.")
    logger.critical("Это сообщение CRITICAL!")
