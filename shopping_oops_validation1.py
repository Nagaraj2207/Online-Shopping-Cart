# Here we import re module.

import re

# Here we create multiple functions for validation.

def cus_name_validation(string_name):
    if not string_name.isalpha():
        raise Exception ("\nCustomer Name must be a Alphabets.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nCustomer Name should not be empty.")
    elif len(string_name)<=2:
        raise Exception ("\nPlease Enter the proper Customer Name.")

def cus_phone_number_validation(string_name):
    ph_num_pattern = re.match("^[6-9]{1}[0-9]{9}$",string_name)
    if string_name.isalpha():
        raise ValueError ("\nCustomer Phone Number must be in digits (or) numbers.")
    elif len(string_name) != 10:
        raise Exception ("\nCustomer Phone Number must be 10 digits")
    elif not ph_num_pattern:
        raise Exception ("\nCustomer Phone Number must be starts with 6-9 and 10 digits(Eg:6379276534)")
    count = 0
    for x in string_name:
        if int(x)==0:
            count +=1
    if count >= 8:
        raise Exception ("\nPhone Number must not be contain more than or equal to 8 0's")

def location_validation(string_name):
    if string_name.isdigit():
        raise Exception ("\nLocation must be a Alphabets.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nLocation should not be empty.")
    elif len(string_name)<=2:
        raise Exception ("\nPlease Enter the proper Location.")

def user_quant_validation(string_name):
    if string_name.isalpha():
        raise Exception ("\nQuantity must be numbers.")
    elif len(string_name)==0 or string_name.isspace():
        raise Exception ("\nQuantity must not be empty.")
    elif int(string_name)<=0:
        raise Exception ("\nQuantity must be positive integer")

