"""
Тип ошибки 1: Неуказание уровня логирования
Возникает, когда при настройке Logger не был указан уровень логирования,
это приводит к игнорированию сообщений с более низким уровнем.
"""
import logging

# logger = logging.getLogger('example_logger')
#
#
# logger.debug('Это сообщение DEBUG')
# logger.info('Это сообщение INFO')
# logger.warning('Это сообщение WARNING')
# logger.error('Это сообщение ERROR')
# print()

"""
Решение:
убедимся, что уровень логирования установлен, причём корректно, 
чтобы отфильтровать сообщения по нужному уровню.
"""

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

logger.debug('Это сообщение DEBUG')
logger.error('Это сообщение ERROR')