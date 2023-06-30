"""
import a function cal_tax from cal_tax.py
"""
from cal_tax import cal_tax

def test_cal_tax():
    """Testing for tax of those earning less than or equal 12000.00"""
    assert cal_tax(12000) == 23300.0

