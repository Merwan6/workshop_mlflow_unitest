import pytest
from age import categorize_by_age

def test_child():
    assert categorize_by_age(5) == "Child"

def test_adolescent():
    assert categorize_by_age(15) == "Adolescent"

def test_adult():
    assert categorize_by_age(30) == "Adult"

def test_golden_age():
    assert categorize_by_age(70) == "Golden age"

def test_negative_age():
    assert categorize_by_age(-1) == "Invalid age: -1"

def test_too_old():
    assert categorize_by_age(151) == "Invalid age: 151"

def test_boundary_child_adolescent():
    assert categorize_by_age(9) == "Child"
    assert categorize_by_age(10) == "Adolescent"

def test_boundary_adolescent_adult():
    assert categorize_by_age(18) == "Adolescent"
    assert categorize_by_age(19) == "Adult"

def test_boundary_adult_golden_age():
    assert categorize_by_age(65) == "Adult"
    assert categorize_by_age(66) == "Golden age"
