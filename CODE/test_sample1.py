import pytest
from soft_asserts import SoftAssert


def test_equal():
    soft_assert = SoftAssert()
    soft_assert.soft_assert(1 == 2, "1 is not equal to 2")
    soft_assert.assert_all()  # Проверка только равенства


def test_true():
    soft_assert = SoftAssert()
    soft_assert.soft_assert(False, "False is not True")
    soft_assert.assert_all()  # Проверка только истинности


if __name__ == "__main__":
    pytest.main()
