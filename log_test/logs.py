import logging

# Налаштування базового формату логів
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a", encoding="utf-8",
)


logging.debug("Це повідомлення рівня DEBUG — для розробників")
logging.info("Програма запущена")
logging.warning("Закінчується пам’ять")
logging.error("Не вдалося зберегти файл")
logging.critical("Фатальна помилка! Програма завершиться")
