"""A function to calculate tax on certain amount per year"""


def cal_tax(earning):
    """The if conditions to calculate the paid tax :param: earning (int) which is then rounded"""
    if earning < 12000:
        return earning
    if earning <= 36000:
        return round((earning * 0.2), 2)
    # else:
    return round((earning * 0.4), 2)
