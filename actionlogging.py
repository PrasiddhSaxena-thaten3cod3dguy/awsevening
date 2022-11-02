import logging

logging.basicConfig(filename="awsevening.log",filemode="w",format='[%(asctime)s]:%(levelname)s:%(message)s')

logger= logging.getLogger()

logger.setLevel(logging.DEBUG)

def agevalidation():
    try:
        age=int(input("Please enter your age!!: "))
    except Exception as e:
        logger.critical(e)
    print("Done")

agevalidation()

# Handle the exception of when a number is divided by zero and take the log of  it .Severity will be info