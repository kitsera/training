import logging
import logging.handlers

LOG_FILENAME = 'my_log_file.log'

logging.basicConfig(filename=LOG_FILENAME, format='%(asctime)s %(message)s', level=logging.DEBUG, filemode='w')

logging.debug('msg')
