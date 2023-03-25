from datetime import datetime
from loguru import logger

class logging(object):
    def __init__(self):
        pass

    @staticmethod
    def staticmethod():
        print("""
        config
        ------
        file: file you want your logs in
        date_fmt: set the format of the date and time you want to be displayed in the log
        ptt: print to terminal. Set to true if you want logs in terminal
        clear_log: set to true if you want the log file to be erased before running
        _________________________________________________________________________________
        
        log
        ---
        msg: The message you want to display
        log_type: The custom name of your log
        _____________________________________        
        """)

    def config(
            self, 
            file: str = "logging.log", 
            date_fmt: str = "%H:%M:%S %d-%m-%Y", 
            ptt: bool = False, 
            clear_log: bool = False
            ):
        self.file = file
        self.ptt = ptt
        self.date_fmt = date_fmt
        
        if clear_log:
            self.__clear_log()

    def __clear_log(self):
        with open(self.file, 'w') as file:
            file.truncate()
    
    def log(self, msg: str, log_type: str):
        if self.ptt: logger.log(10, msg)
        now = datetime.now()
        time = now.strftime(self.date_fmt)
        with open(self.file, 'a') as file:
            log = f"[{time}] | [{log_type}]: {msg}\n"
            file.write(log)        

    def info(self, msg: str):
        if self.ptt: logger.info(msg)
        now = datetime.now()
        time = now.strftime(self.date_fmt)
        with open(self.file, 'a') as file:
            log = f"[{time}] | [INFO]: {msg}\n"
            file.write(log)

    def debug(self, msg: str):
        if self.ptt: logger.debug(msg)
        now = datetime.now()
        time = now.strftime(self.date_fmt)
        log = f"[{time}] | [DEBUG]: {msg}\n"
        with open(self.file, 'a') as file:
            file.write(log)

    def warning(self, msg: str):
        if self.ptt: logger.warning(msg)
        now = datetime.now()
        time = now.strftime(self.date_fmt)
        log = f"[{time}] | [WARNING]: {msg}\n"
        with open(self.file, 'a') as file:
            file.write(log)

    def error(self, msg: str):
        if self.ptt: logger.error(msg)
        now = datetime.now()
        time = now.strftime(self.date_fmt)
        log = f"[{time}] | [ERROR]: {msg}\n"
        with open(self.file, 'a') as file:
            file.write(log)

    def critical(self, msg: str):
        if self.ptt: logger.critical(msg)
        now = datetime.now()
        time = now.strftime(self.date_fmt)
        log = f"[{time}] | [CRITICAL]: {msg}\n"
        with open(self.file, 'a') as file:
            file.write(log)

    def success(self, msg: str):
        if self.ptt: logger.success(msg)
        now = datetime.now()
        time = now.strftime(self.date_fmt)
        log = f"[{time}] | [SUCCESS]: {msg}\n"
        with open(self.file, 'a') as file:
            file.write(log)