from datetime import datetime
from inspect import getframeinfo, stack
from datetime import datetime
from python_logging.colours import colour
import inspect


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

    
    def __main_log(self, caller: inspect.Traceback, msg: str, log_type: str, log_colour: str, error: Exception) -> None:
        now = datetime.today()
        time = now.strftime(self.date_fmt)

        if self.ptt:
            print_log_message = self.__print_layout(caller=caller, error_colour=log_colour, log_type=log_type, message=msg, time=time, error=error)
            print(print_log_message)

        log_file_message = self.__log_file_layout(caller=caller, log_type=log_type, message=msg, time=time)
        with open(self.file, 'a') as file:
            file.write(log_file_message) 


    def __print_layout(self, caller: inspect.Traceback, error_colour: str, log_type: str, message: str, time: str, error: Exception) -> str:
        line_break = "|\n"
        top = f"\n{colour.BOLD}-------------------------------------------------\n"
        error_names = f"| [{error_colour}{log_type}{colour.WHITE}]"
        log_info = f"| Log Info: {error_colour}{message}{colour.WHITE}\n"
        file_loc = f"| [{colour.BLUE}{caller.filename}{colour.WHITE}:{colour.PURPLE}{caller.lineno}{colour.WHITE}]\n"
        time = f"| [{colour.GREEN}{time}{colour.WHITE}]\n"
        bottom = f"-------------------------------------------------"
        if error:
            error_names += f"[{error_colour}{type(error).__name__}{colour.WHITE}]\n"
            error_info = f"| Error: {error_colour}{error}{colour.WHITE}\n"
            return top + error_names + line_break + log_info + error_info + line_break + file_loc + time + bottom
        else:
            error_names += "\n"
            return top + error_names + line_break + log_info + line_break + file_loc + time + bottom


    def __log_file_layout(self, caller: inspect.Traceback, log_type: str, message: str, time: str) -> str:
        return f"[{time}] | {caller.filename}:{caller.lineno} | [{log_type}] | {message}\n"


    def log(self, msg: str, log_type: str, log_colour: str = colour.PURPLE, error: Exception = None) -> None:
        """
        Custom log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type=log_type, log_colour=log_colour, error=error)     


    def info(self, msg: str, error: Exception = None) -> None:
        """
        Info Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="INFO", log_colour=colour.CYAN, error=error)


    def debug(self, msg: str, error: Exception = None) -> None:
        """
        Debug Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="DEBUG", log_colour=colour.DARKCYAN, error=error)


    def warning(self, msg: str, error: Exception = None) -> None:
        """
        Warning Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="WARNING", log_colour=colour.YELLOW, error=error)


    def error(self, msg: str, error: Exception = None) -> None:
        """
        Error Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="ERROR", log_colour=colour.RED, error=error)


    def critical(self, msg: str, error: Exception = None) -> None:
        """
        Critical Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="CRITICAL", log_colour=colour.MAGENTA, error=error)


    def success(self, msg: str, error: Exception = None) -> None:
        """
        Success Log
        """
        caller = getframeinfo(stack()[1][0])
        self.__main_log(caller=caller, msg=msg, log_type="SUCCESS", log_colour=colour.GREEN, error=error)


logger = LogClass()