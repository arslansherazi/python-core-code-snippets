import logging
from logging import handlers

from elasticapm import Client
from elasticapm.handlers.logging import LoggingHandler
apm_client = Client(service_name='division_logs')

DIVISION_TRANSACTION_TYPE = 'division'
DIVISION_TRANSACTION_NAME ='division_transaction'
TRANSACTION_STATUS = 'completed'


def get_logger(log_file_path):
    # logger
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)%')

    # handler for logging into file
    file_handler =  handlers.TimedRotatingFileHandler(log_file_path, when='midnight', backupCount=10)
    file_handler.suffix = '%Y-%m-%d'
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # handler for logging into apm
    apm_handler = LoggingHandler(client=apm_client)
    apm_handler.setLevel(logging.ERROR)
    logger.addHandler(apm_handler)

    return logger


if __name__ == '__main__':
    logger = None
    try:
        apm_client.begin_transaction(DIVISION_TRANSACTION_TYPE)
        logger = get_logger('./logs')
        division = 100/0
    except Exception:
        if logger:
            logger.exception('Something went wrong during division')
    finally:
        apm_client.end_transaction(DIVISION_TRANSACTION_NAME, TRANSACTION_STATUS)
