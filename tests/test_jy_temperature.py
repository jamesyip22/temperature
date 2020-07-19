import pytest

from jy_temperature.jy_temperature import convert

def test_0C_is_32F():
    assert convert(0,'c','f') == 32
    
def test_212F_is_100C():
    assert convert(212,'f','c') == 100
    
def test_K_to_F():
    assert convert(283.15,'k','f') == 50
    
def test_F_to_K():
    assert convert(-459.67,'f','k') == 0
    
def test_K_to_C():
    assert convert(0,'k','c') == -273.15
    
def test_C_to_K():
    assert convert(0,'c','k') == 273.15

def test_neg_k_still_works():
    assert convert(-273.15,'k','c') == 0
    assert convert(-0,'k','c') == -273.15
    
def test_upper_to_lower_works():
    assert convert(212,'F','c') == 100
    assert convert(212,'F','C') == 100