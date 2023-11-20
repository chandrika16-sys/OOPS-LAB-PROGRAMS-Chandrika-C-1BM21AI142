import re  
  
def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False  
  
email = "chandrika7c@gmail.com"  
if validate_email(email):  
    print("True")  
else:  
    print("False")  
