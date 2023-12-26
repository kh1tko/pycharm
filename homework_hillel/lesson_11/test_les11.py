import time
import pytest


def test_delayed_execution_1():
    time.sleep(2)
    print("Test 1 executed")


def test_delayed_execution_2():
    time.sleep(2)
    print("Test 2 executed")


def test_delayed_execution_3():
    time.sleep(2)
    print("Test 3 executed")


def test_delayed_execution_4():
    time.sleep(2)
    print("Test 4 executed")


@pytest.mark.unique
def test_unique_delayed_execution():
    time.sleep(2)
    print("Unique Test executed")
