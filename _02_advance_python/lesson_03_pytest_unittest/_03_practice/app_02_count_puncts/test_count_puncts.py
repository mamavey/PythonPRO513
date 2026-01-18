# from _02_advance_python.lesson_03_pytest_unittest._03_practice.app_02_count_puncts.count_puncts import count_punct_marks
from count_puncts import count_punct_marks

def test_empty_string():
    assert count_punct_marks('') == 0

def test_no_punctuation():
    assert count_punct_marks('Hello world') == 0

def test_single_punctuation():
    assert count_punct_marks('Hello world!') == 1

def test_multiple_punctation():
    assert count_punct_marks('Hello, world! How are you?') == 3

def test_edge_case():
    assert count_punct_marks('!!!') == 3

def test_all_punctuation():
    assert count_punct_marks('.,:;!?') == 6