CONFIG = {
    'log': {
        'level': 'DEBUG',   # 与log库的level一致，包括DEBUG, INFO, ERROR
                            #   DEBUG   - Enable stdout, file, mail （如果在dest中启用）
                            #   INFO    - Enable file, mail         （如果在dest中启用）
                            #   ERROR   - Enable mail               （如果在dest中启用）
        'dest': {
            'stdout': True, # None: disabled,
            'file': None,   # None: disabled, 
                                        # PATH: log file path, 
                                        # '': Default path under ./logs/
            'syslog': ('10.8.0.2', 514),    # None: disabled, or (ip, port)
            'mail': 'Henry TIAN <6314849@qq.com>'   # None: disabled,
                                                    # MAIL: send to
                                                    # '': use setting ['mail']['to']
        },
        'sql': 1
    },
    'mail': {
        'from': 'Henry TIAN <15050506668@163.com>',
        'to': 'Henry TIAN <6314849@qq.com>'
    },
    'smtp': {
        'host': 'smtp.163.com',
        'port': 25,
        'user': '15050506668@163.com',
        'pwd': '123456'
    },
    'port': 8000,
    'timeout': 3600,
    'interval': 10,
    'tmp_dir': '/tmp'
}