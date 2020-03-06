"""
author: rs
created_on: 5th March 2020
"""
import random


def mock_cra_score(aadhar):
    """
    :param aadhar: Aadhar number of the loan application for whom Credit score is to be retrieved
    :return: Credit score for the given Aadhar
    """
    return random.randint(100,900)


def mock_lcr_score(aadhar):
    """
    :param aadhar: Aadhar number of the loan application for whom Credit score is to be retrieved
    :return: Local Credit score for the given Aadhar
    """
    return random.randint(100, 900)