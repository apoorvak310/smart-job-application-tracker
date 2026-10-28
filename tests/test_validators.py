from util.validators import validate_email, validate_phone
import pytest

@pytest.mark.parametrize("email,expected",[
    ("apoorva@gmail.com","apoorva@gmail.com"),
    ("appu@vinnu.com","appu@vinnu.com"),
    ("a@ppu@.com",None),
    ("",None)
])
def test_email(email, expected):
    assert validate_email(email) == expected

@pytest.mark.parametrize("phone,expected",[
    ("9876543210","9876543210"),
    ("7865432198","7865432198"),
    ("987654321",False),
    ("",None)
])
def test_phone(phone,expected):
    assert validate_phone(phone) == expected