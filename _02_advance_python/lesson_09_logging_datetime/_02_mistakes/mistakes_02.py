"""
Тип ошибки 2: Использование неправильных форматов логирования
Возникает, когда при настройке Logger не был указан формат сообщений.
Некорректное форматирование может привести к тому,
что в логах будет недостаточно информации, например, нет времени события или уровня логирования.
"""
import logging
#
# logger = logging.getLogger('example_logger')
# logger.setLevel(logging.DEBUG)
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
#
# # Форматирование сообщений
# # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# # console_handler.setFormatter(formatter)
#
# logger.addHandler(console_handler)
#
# logger.info('Это сообщение INFO')
# logger.warning('Это сообщение WARNING')

"""
настроим форматирование с использованием всех нужных полей: %(asctime)s, %(levelname)s, %(message)s.
"""

logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.info('Это сообщение INFO')
logger.warning('Это сообщение WARNING')

# вывод:
# 2026-01-14 20:23:25,223 - INFO - Это сообщение INFO
# 2026-01-14 20:23:25,223 - WARNING - Это сообщение WARNING