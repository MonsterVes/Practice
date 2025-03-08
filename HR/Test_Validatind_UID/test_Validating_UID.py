
from Validating_UID import is_valid

def test_is_alnum():
     assert is_valid("B1CD102354") == True
     assert is_valid("B1CD1(2354") == False

def test_correct_len():
     assert is_valid("B1CD102354") == True
     assert is_valid("B1CD1") == False
     assert is_valid("B1CD1eeunnk899") == False

def test_is_not_repeat():
     assert is_valid("B1CD102354") == True
     assert is_valid("B1CD102355") == False

def test_is_alnum():
     assert is_valid("B1CD102354") == True
     assert is_valid("B1CD1(2354") == False

