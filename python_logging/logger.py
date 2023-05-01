from datetime import datetime
from inspect import getframeinfo, stack
from datetime import datetime
from colours import colour
import inspect


def __print_layout(caller: inspect.Traceback, error_colour: str, log_type: str, message: str, time: str) -> str:
    return f"""
{colour.BOLD}-------------------------------------------------
| [{error_colour}{log_type}{colour.WHITE}]
|
| Log Info: {error_colour}{message}{colour.WHITE}
|
| [{colour.BLUE}{caller.filename}{colour.WHITE}:{colour.PURPLE}{caller.lineno}{colour.WHITE}]
| [{colour.GREEN}{time}{colour.WHITE}] 
-------------------------------------------------"""


def __log_file_layout(caller: inspect.Traceback, log_type: str, message: str, time: str) -> str:
    return f"""[{time}] | {caller.filename}:{caller.lineno} | [{log_type}] | {message}
"""


class LogClass(object):
    def __init__(self):
        """
        Initilize so object can use self
        """
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
        """
        Configure logger with some settings
        """
        self.file = file
        self.ptt = ptt
        self.date_fmt = date_fmt
        
        if clear_log:
            self.__clear_log()


    def __clear_log(self):
        """
        Clear the log file
        """
        with open(self.file, 'w') as file:
            file.truncate()

    
    def __main_log(self, caller: inspect.Traceback, msg: str, log_type: str, log_colour: str) -> None:
        now = datetime.today()
        time = now.strftime(self.date_fmt)

        if self.ptt:
            print_log_message = __print_layout(caller=caller, error_colour=log_colour, log_type=log_type, message=msg, time=time)
            print(print_log_message)

        log_file_message = __log_file_layout(caller=caller, log_type=log_type, message=msg, time=time)
        with open(self.file, 'a') as file:
            file.write(log_file_message) 


    def log(self, msg: str, log_type: str, log_colour: str = colour.PURPLE) -> None:
        """
        Custom log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type=log_type, log_colour=log_colour)     


    def info(self, msg: str) -> None:
        """
        Info Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="INFO", log_colour=colour.CYAN)


    def debug(self, msg: str) -> None:
        """
        Debug Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="DEBUG", log_colour=colour.DARKCYAN)


    def warning(self, msg: str) -> None:
        """
        Warning Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="WARNING", log_colour=colour.YELLOW)


    def error(self, msg: str) -> None:
        """
        Error Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="ERROR", log_colour=colour.RED)


    def critical(self, msg: str) -> None:
        """
        Critical Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="CRITICAL", log_colour=colour.MAGENTA)


    def success(self, msg: str) -> None:
        """
        Success Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="SUCCESS", log_colour=colour.GREEN)


logger = LogClass()