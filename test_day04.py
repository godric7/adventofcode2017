from day_04 import is_passphrase_valid, is_passphrase_valid2


def test_part_one_should_validate_exemple():
    assert is_passphrase_valid('aa bb cc dd ee') is True
    assert is_passphrase_valid('aa bb cc dd aa') is False
    assert is_passphrase_valid('aa bb cc dd aaa') is True


def test_part_two_should_validate_exemple():
    assert is_passphrase_valid2('abcde fghij') is True
    assert is_passphrase_valid2('abcde xyz ecdab') is False
    assert is_passphrase_valid2('a ab abc abd abf abj') is True
    assert is_passphrase_valid2('iiii oiii ooii oooi oooo') is True
    assert is_passphrase_valid2('oiii ioii iioi iiio') is False
