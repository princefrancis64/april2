import logging
logging.basicConfig(filename="test3.log", level= logging.INFO, format = '%(levelname)s %(name)s %(asctime)s %(message)s')



def divide(a,b):
    logging.info("the number entered by the user is %s and %s",a,b)
    try:
        logging.info("we are into a function")
        div=a/b
        logging.info("we have completed a division operation")
        logging.info("the result of code is %s", div)
        return div
    except Exception as e:
        logging.exception(e)


(divide(4,0))