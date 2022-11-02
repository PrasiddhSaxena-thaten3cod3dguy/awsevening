import logging

logging.basicConfig(filename="awsevening.log",filemode="w",format='[%(asctime)s]:%(levelname)s:%(message)s')

logger= logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("This is Just a Debug Message!! Please fix it later on")
logger.info("This is just for your information about the line no 10")
logger.warning("This is a Warning messages coming from Heaven of line no 11")
logger.error("This is an error occured at line no 12")
logger.critical("This is a critical Error!! from line no 13")
print("Go check your log files")

