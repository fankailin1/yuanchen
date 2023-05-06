import logging.config

simple_format = '%(levelname)s - %(asctime)s - %(message)s'
logfile_path2 = 'boss.log'

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': simple_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 打印到文件的日志，收集 DEBUG以上的日志
        'std': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': "ERROR.log",
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,  # 日志文件最大个数
            'encoding': 'utf-8'
        },
        'boss': {
            'level': "INFO",
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': "INFO.log",
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,  # 日志文件最大个数
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        'aa': {
            'handlers': ['std', 'console', 'boss'],
            'level': "DEBUG",
            'propagate': 'True'
        },
    },
}

logging.config.dictConfig(LOGGING_DIC)
logger = logging.getLogger("aa")

