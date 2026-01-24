import logging

# настройка базового конфигуратора
logging.basicConfig(level=logging.DEBUG)

logging.debug("Это сообщение отладочного уровня.")
logging.info("Это информационное сообщение.")
logging.warning("Это предупреждение")
logging.error("Это сообщение об ошибке")
logging.critical("Это критическая ошибка!")
