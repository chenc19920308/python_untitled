import logging
#这里可以自定义日志格式
logging.basicConfig(filename='example1.log',level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')