import requests
import unittest
from unittest.mock import patch, Mock

#Diese code ist aus folgenden Tutorial: Professional Python Testing with Mock          von: NeuralNine upload: 2023

def get_user_data(user_id):
    response = requests.get(f"http://example15ikja8Hkee.com/users/{user_id}")
    return response.json()

class TestUserData(unittest.TestCase):
    @patch("requests.get")
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        response_dict = {"name": "John", "email": "john@gmail.com"}
        mock_response.json.return_value = response_dict
        mock_get.return_value = mock_response
        user_data = get_user_data(1)
        mock_get.assert_called_with("http://example15ikja8Hkee.com/users/1")
        self.assertEqual(user_data, response_dict)





#Nachfolgender Code von: mCoding   video Modern Python Logging          aus 2023
import logging.config
logger = logging.getLogger("my-app")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
 #   "filters": {...},
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "root": {"level": "DEBUG", "handlers": ["stdout"]}
    },
}
def log():
    logging.config.dictConfig(config=logging_config)
    logger.addHandler(logging.StreamHandler(...))
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("exception message")



#papalel Programming   video from mCoding    name: Unlocking your CPU cores in Python (multiprocessing)

#! python asyncion     wen man disk schreibt oder io bound
#! threades     kann sachen schneller machen wen python z.b etwas in c macht z.b dot product weil python locked ist mit threades kann einer starten dot
#!  dotproduct berechen während dessen kann der nächst den pytho code ausführen und dann auch beginngen das dot produckt simultan zu errechenn
#! sie können aber nicht gleichzeitig den python code ausführen dafür multi processing  (nutzung gut für io oder auch in der gui mit rechnungen um 
#!   responsive zu bleiben)  cpu wird mehr aber nicht voll genutzt
#! multiprocessing ist gut wen mann von einander getrent ist  man will ein python pool object man kann auch unorderd oder orderd machen

#pytest von mCoding name Automated Testing in Python with pytest, tox, and Guthub Actions

if __name__ == "__main__":
    log()
    unittest.main()
    