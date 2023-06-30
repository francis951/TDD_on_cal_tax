"""
import a function cal_tax from cal_tax.py
"""
from cal_tax import cal_tax

def test_cal_tax():
    """Testing for tax of those earning less than or equal 12000.00"""
    assert cal_tax(12000) == 00.0

def test_cal_tax_1():
    """Testing for tax of those earning more than or equal 36000.00"""
    assert cal_tax(24000) == 2400.0
