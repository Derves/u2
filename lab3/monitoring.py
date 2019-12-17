import requests
import json
import logging
import threading

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
    except Exception as ex:
        logging.error("Unable to connect to the server!\nERROR:\n%s", ex)
        print("\nUnable to connect to the server!\nERROR: \n", ex, flush=True)
    else:
        print("\nAll is good!\n", flush=True)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])
    
    threading.Timer(60, main, [url]).start()


if __name__ == '__main__':
    main("http://localhost:8000/health")

