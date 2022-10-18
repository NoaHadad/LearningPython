import pytest
import os
from generator import fibonacci, reader


def test_fibonacci():
    fibonnaci_series = fibonacci()
    expected = [0 ,1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ,34]
    for i in range(10):
        assert next(fibonnaci_series) == expected[i]


FILE_LINES = ['When u get tired, learn to rest, no quit', 
              'Victory has thousand fathers but defeat is an orphan',
              'They cant kill u if u already dead',
              'For every minute u are angry u lose 60 seconds of hapiness',
              'If your ahip doesnt come in, swim out to it',
              'If u thell the truth, u dont have to remember anything',
              'Keep your friends close and your enemies closer',
              'Theres no place like home',
              'Earn your leadership every day',
              'Everything you’ve ever wanted is on the other side of fear']

              
@pytest.fixture
def empty_file():
    file_name = "emptyTestfile.txt"
    f = open(file_name, "a")
    f.close()
    yield file_name
    os.remove(file_name)


@pytest.fixture
def ten_lines_file():
    file_name = "tenLinesTestfile.txt"
    with open(file_name, "w") as f:
        lines = [line + '\n' for line in FILE_LINES]
        f.writelines(lines)
    yield file_name
    os.remove(file_name)


def test_empty_file_reader(empty_file):
    empty_file_reader = reader(empty_file, 1)
    with pytest.raises(StopIteration) as e:
        next(empty_file_reader)  


def test_ten_lines_reader(ten_lines_file):
    ten_lines_file_reader = reader(ten_lines_file, 3)
    assert next(ten_lines_file_reader) == FILE_LINES[:3]
    assert next(ten_lines_file_reader) == FILE_LINES[3:6]
    assert next(ten_lines_file_reader) == FILE_LINES[6:9]
    assert next(ten_lines_file_reader) == FILE_LINES[9:]  
    with pytest.raises(StopIteration) as e:
        next(ten_lines_file_reader)