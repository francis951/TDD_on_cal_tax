"""A function to calculate tax on certain amount per year"""


def cal_tax(earning):
    """The if conditions to calculate the paid tax :param: earning (int) which is then rounded"""
    if earning < 12000:
        tax = 0
    if earning <= 36000:
        tax = (earning - 12000) * 0.2
    # if earning >= 36000:
    else:
        tax  = (earning - 36000) * 0.4
    
    return tax