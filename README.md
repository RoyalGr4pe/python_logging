# Python Logger 

How to use


    from python_logging.logger import logger

    """
    ptt is print to terminal
    clear_log will clear the log file on run
    """
    logger.config(file="offspring_release.log", ptt=True, clear_log=True)
    
    try:
        name = 5 + "5"
        error = None
    except Exception as error:
        logger.info(msg="Info", error=error)
        logger.debug(msg="Info", error=error)
        logger.warning(msg="Info", error=error)
        logger.error(msg="Info", error=error)
        logger.critical(msg="Info", error=error)
        logger.success(msg="Info", error=error)
        logger.log(msg="Info", log_type="Custom Log", error=error)


Run the below command to install

    pip install git+https://github.com/RoyalGr4pe/python_logging.git
