#global variable use for the test cases

import requests as req
import logging 
import re

SESSION = req.Session()

APP_URL = "http://localhost:8080"
ADMIN_USER="admin"
ADMIN_PW="admin"

LOG= logging.getLogger() #define a globale logger

class HideSensitiveData(logging.Filter):  #added a hidding filter
    
    def filter(self, record):
        record.msg= str(record.msg).replace(ADMIN_PW, "******")
        #record.msg= re.sub(r'Authorization.*?,',
         #                  'Authorization\': \'******\', ', str(record.msg))
        return True

LOG.addFilter(HideSensitiveData())
