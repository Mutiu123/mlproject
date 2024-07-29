import sys
from src.logger import logging

# Your error message format
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message


# It will give you your error message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    # This will print the error message
    def __str__(self):
        return self.error_message 
    


if __name__=="__main__":

    try:
        result = 5/0
    except Exception as e:
        
        logging.info("Division by Zero")
        raise CustomException(e, sys)
    