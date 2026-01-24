import logging

# Создание логгера
logger = logging.getLogger('example_logger')
logger.setLevel(level=logging.DEBUG)

# Создание обработчика для вывода в файл
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Форматирование сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)
# logger.removeHandler(file_handler)

if __name__ == '__main__':
    logger.debug("Это сообщение DEBUG.")
    logger.info("Это сообщение INFO.")
    logger.warning("Это сообщение WARNING.")
    logger.error("Это сообщение ERROR.")
    logger.critical("Это сообщение CRITICAL!")
