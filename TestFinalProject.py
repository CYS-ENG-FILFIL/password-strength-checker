from finalProject import checkLength, checkNum, checkUppercase, checkSpecialChar


def test_checkLength():
    assert checkLength("12345678") == True
    assert checkLength("123") == False


def test_checkNum():
    assert checkNum("abc123") == True
    assert checkNum("abcdef") == False


def test_checkUppercase():
    assert checkUppercase("Abcdef") == True
    assert checkUppercase("abcdef") == False


def test_checkSpecialChar():
    assert checkSpecialChar("abc!") == True
    assert checkSpecialChar("abcdef") == False