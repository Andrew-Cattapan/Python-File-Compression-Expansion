"""This program tests the password program."""


import pytest
import Assignment_7


def test_check_password_length_valid():
    assert Assignment_7.check_password_length("A" * 16) == "Pass"


def test_check_password_length_invalid():
    assert Assignment_7.check_password_length("g#3") == "Fail"
    with pytest.raises(AssertionError):
        Assignment_7.check_password_length(23)


def test_check_string_has_one_of_valid():
    assert Assignment_7.check_string_has_one_of("b23a", "a") == "Pass"
    assert Assignment_7.check_string_has_one_of("g", "g") == "Pass"
    assert Assignment_7.check_string_has_one_of("banana", "wow") == "Fail"


def test_check_string_has_one_of_invalid():
    with pytest.raises(AssertionError):
        Assignment_7.check_string_has_one_of(23, "abc")
    with pytest.raises(AssertionError):
        Assignment_7.check_string_has_one_of("abc", 23)
    with pytest.raises(AssertionError):
        Assignment_7.check_string_has_one_of("", "adequatepassword")


def test_check_character_is_part_of_valid():
    assert Assignment_7.check_character_is_part_of("toast", "a") == True
    assert Assignment_7.check_character_is_part_of("t", "t") == True
    assert Assignment_7.check_character_is_part_of("hungry", "b") == False


def test_check_character_is_part_of_invalid():
    with pytest.raises(AssertionError):
        Assignment_7.check_character_is_part_of("banana", "morethanasinglecharacter")
    with pytest.raises(AssertionError):
        Assignment_7.check_character_is_part_of("banana", 2)
    with pytest.raises(AssertionError):
        Assignment_7.check_character_is_part_of(23, "a")
    with pytest.raises(AssertionError):
        Assignment_7.check_character_is_part_of("", "morethanasinglecharacter")


def test_password_strength_valid():
    assert Assignment_7.password_strength("a") == 1
    assert Assignment_7.password_strength("T") == 1
    assert Assignment_7.password_strength("#") == 1
    assert Assignment_7.password_strength("3") == 1
    assert Assignment_7.password_strength("T3") == 2
    assert Assignment_7.password_strength("Tt3") == 3
    assert Assignment_7.password_strength("Tt#3") == 4
    assert Assignment_7.password_strength("Thispassw0rdsh0uldwork!") == 5
    

def test_password_strength_invalid():
    with pytest.raises(AssertionError):
        Assignment_7.password_strength(42)


def test_check_if_in_file_valid():
    assert Assignment_7.check_if_in_file("words.txt", "banana") == "Match"
    assert Assignment_7.check_if_in_file("10 million password list.txt", "andrew") == "Match"


def test_check_if_in_file_invalid():
    with pytest.raises(AssertionError):
        Assignment_7.check_if_in_file(23, "pleasefail")
    with pytest.raises(AssertionError):
        Assignment_7.check_if_in_file("not words.txt", "anyoldpassword")
    with pytest.raises(AssertionError):
        Assignment_7.check_if_in_file("pleasealsofail", 67)


def test_create_file_invalid():
    with pytest.raises(AssertionError):
        Assignment_7.create_file(4, "heylookanumberyoushouldfreakout")
    with pytest.raises(AssertionError):
        Assignment_7.create_file("heylookanothernumber.txt", 6)


def test_append_file_valid():
    assert Assignment_7.append_file("words.txt", "wowshouldIloopsomeofthis") == "Success"
    assert Assignment_7.append_file("10 million password list.txt", "yupthistestagain") == "Success"


def test_append_file_invalid():
    with pytest.raises(AssertionError):
        Assignment_7.append_file(4, "likeIcouldmakeloopcode")
    with pytest.raises(AssertionError):
        Assignment_7.append_file("filethatdoesnotexist.txt", "butthatmightbe")
    with pytest.raises(AssertionError):
        Assignment_7.append_file("morecomplicatedthan", 6)
