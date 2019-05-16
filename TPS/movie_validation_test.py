# validation_test.py
# France Cheong
# 20/12/2018

# Import file/class to test
from movie_validation import Validation


def test_is_numeric(validation):
    print("\n1.Testing is_numeric()") 
    
    # True
    assert (validation.is_numeric(10))

    # False
    assert (not validation.is_numeric(10.002))
    assert (not validation.is_numeric("abc"))
    assert (not validation.is_numeric("10abc"))

def test_is_alphabetic(validation):
    print("\n2. Testing is_alphabetic()")

    # True
    assert (validation.is_alphabetic("abc"))

    # False
    assert (not validation.is_alphabetic(10))    
    assert (not validation.is_alphabetic(10.002)) 
    assert (not validation.is_alphabetic("10abc"))

def test_is_alphanumeric(validation):
    print("\n3. Testing is_alphanumeric()")

    # True
    assert (validation.is_alphanumeric(10))  
    assert (validation.is_alphanumeric("abc")) 
    assert (validation.is_alphanumeric("10abc")) 

    # False 
    assert (not validation.is_alphanumeric(10.02))
    assert (not validation.is_alphanumeric("_")) 
    assert (not validation.is_alphanumeric(" "))
    assert (not validation.is_alphanumeric(".")) 

def test_is_not_symbol(validation):
    print("\n4. Testing is_not_symbol()")

    #True
    assert (validation.is_not_symbol("Captain Marvel"))
    assert (validation.is_not_symbol("Captain Marvel 1"))

    #False
    assert (not validation.is_not_symbol("Captain Marvel 1!"))

def test_is_symbol(validation):
    print("\n5. Testing is_symbol()")

    #True 
    assert (validation.is_symbol("G"))
    assert (validation.is_symbol("M"))
    assert (validation.is_symbol("MA15+"))
    assert (validation.is_symbol("R18+"))

    #False
    assert (not validation.is_symbol("g"))
    assert (not validation.is_symbol("m"))
    assert (not validation.is_symbol("ma15+"))
    assert (not validation.is_symbol("r18+"))
        
if __name__ == '__main__':
    
    print("\nTesting ...")

    # Instantiate a validation object
    validation = Validation()

    test_is_numeric(validation)

    test_is_alphabetic(validation)

    test_is_alphanumeric(validation)

    test_is_not_symbol(validation)

    test_is_symbol(validation)