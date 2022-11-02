# Handle the exception of when a number is divided by zero and take the log of  it .Severity will be info
import logging

logging.basicConfig(filename="awsevening.log",filemode="w",format='[%(asctime)s]:%(levelname)s:%(message)s')

logger= logging.getLogger()

logger.setLevel(logging.DEBUG)

try:
    x= 5 / 0 
    print(x)
except ZeroDivisionError as e:
    logger.critical(f"{e} in line number 14")