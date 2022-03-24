from turtle import color
import pytest
from utils import termutils

text = 'asd123'

def test_color_state__ok():
    assert termutils.color_state(text, ok=True) == '\033[92m' + text + '\033[0m'
    
def test_color_state__err():
    assert termutils.color_state(text, ok=False) == '\033[91m' + text + '\033[0m'