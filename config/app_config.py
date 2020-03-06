"""
author: rs
created_on: 5th March 2020
"""
# Weight of Rule Engine segments
# Cummulative weigthage should not cross 1
RULE_ENGINE_WEIGHTAGE = {
                            "NDVI_WGT": 0.3,  # Based on NDVI of land
                            "CRA_WGT": 0.3,  # Credit Rating Agencies (CIBIL, Experain, etc)
                            "LCR_WGT": 0.4  # Local credit rating based on past loan performance
                        }
# Land value per cent (100 cents = 1 acre) in rupees
LAND_VAL_PER_CENT = 100
# Maximum loan amount in rupees
MAX_LOAN_AMOUNT = 25000
# Maximum Loan tenure in months
MAX_LOAN_TENURE = 6
# Maximum Land value percentage eligible for loan
MAX_LAND_VALUE_WEIGHTAGE = 0.4
# LOAN RISK SCORE
LOAN_RISK_SCORE = 500
# MIN NVDI, CRA and LC_SCORE
MIN_NVDI_SCORE = 100
MIN_CRA_SCORE = 100
MIN_LCR_SCORE = 100
