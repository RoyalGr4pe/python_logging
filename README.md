# Python Logger 

How to use


    from python_logging.logger import logger

    """
    ptt is print to terminal
    clear_log will clear the log file on run
    """
    logger.config(file="offspring_release.log", ptt=True, clear_log=True)

    logger.info(msg="Info")
    logger.debug(msg="Info")
    logger.warning(msg="Info")
    logger.error(msg="Info")
    logger.critical(msg="Info")
    logger.success(msg="Info")
    logger.log(msg="Info", log_type="Custom Log")


Run the below command to install

    pip install git+https://github.com/RoyalGr4pe/python_logging.git