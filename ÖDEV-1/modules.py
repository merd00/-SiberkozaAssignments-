# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
import datetime
from datetime import date
import time
from time import time
from camelcase import CamelCase

today_mo = datetime.date.today()
print(today_mo)


time_mo = time()
print(time_mo)

c_mo = CamelCase()
print(c_mo.hump("Ben seni affetsem geceler affetmez"))



import validator
email_es = "test text"

if validator.validate_email(email_es):
    print("Email is valid")
else:
    print("email is invalid")