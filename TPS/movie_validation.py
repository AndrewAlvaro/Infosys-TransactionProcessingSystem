# validation.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import re # regular expression

# ################
# Validation Class for movieGUI
# ################

class Validation():

    def is_numeric(self, val):
        val = str(val) # only str have the isnumeric() method
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False  

    def is_alphabetic(self, val):
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False  

    def is_alphanumeric(self, val):
        val = str(val)
        if val.isalnum():
            print("Alphanumeric")
            return True
        else:
            print("Not alphanumeric")
            return False  
    
    def is_not_symbol(self, val):
        val = str(val)
        # Check that it is only Alphabetic and Numeric allowed
        if re.match(r'^[a-zA-Z0-9_ :.]*$', val):
            print("Valid movie name")
            return True
        else:
            print("Invalid movie name")
            return False  

    def is_symbol(self, val):
        val = str(val)
        # Check that it is only Alphabetic and Numeric allowed
        if re.match(r'^[ A-Z0-9+]*$', val):
            print("Valid movie name")
            return True
        else:
            print("Invalid movie name")
            return False  
    pass

# ###########
# Main method
# ###########

# The main method is only executed when the file is 'run' (not imported in another file)

if __name__ == '__main__':
    # Instead of writing separate test scripts, could write them here
    # The test scripts would not be executed when the file is imported into another one
    pass        