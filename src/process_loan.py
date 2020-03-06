"""
author: rs
created_on: 5th March 2020
"""
from utils.compute_land_area import compute_land_area
from config.app_config import LAND_VAL_PER_CENT, MAX_LOAN_AMOUNT, MAX_LAND_VALUE_WEIGHTAGE, MAX_LOAN_TENURE
from src.rule_engine import RuleEngine

class ProcessLoan(object):
    """
    This class process the loan application and return the response
    """

    def __init__(self, loan_obj):
        """
        :param loan_obj: Loan Object which contains the loan application details
        """
        self.loan_obj = loan_obj
        self.loan_amount = loan_obj.loan_amount
        self.loan_tenure = loan_obj.loan_tenure
        self.land_coordinates = loan_obj.land_coordinates

    def get_eligible_loan_amount(self):
        """
        Computing Eligible Loan amount for the given land coordinates
        :return: Eligible loan amount
        """
        # MAX_LAND_VALUE_WEIGHTAGE is the percent of land value being considered as loan collateral
        # LAND_VAL_PER_CENT is the current land value per cent
        # compute_land_area is the mock method that is used to compute the area of the applicants land coordinates
        land_value = compute_land_area(self.land_coordinates) * LAND_VAL_PER_CENT * MAX_LAND_VALUE_WEIGHTAGE
        if land_value > MAX_LOAN_AMOUNT :
            return MAX_LOAN_AMOUNT
        return land_value

    def get_loan_tenure(self):
        """
        Compute the loan tenure for the given loan application
        :return: Loan tenure
        """
        if self.loan_tenure > MAX_LOAN_TENURE:
            return MAX_LOAN_TENURE
        return self.loan_tenure

    def get_risk_details(self):
        """
        Compte risk details for the given loan application
        :return: Risk Details
        """
        return RuleEngine(self.loan_obj).get_risk_status()

    def process_loan(self):
        """
        Process the loan application and respond backwith risk details and application status
        :return: Application response
                {'application_details':
                                        {   'application_rejection_reason': 'Bad Credit score',
                                            'application_status': 'rejected',
                                             'loan_amount': 0,
                                             'loan_tenure': 0,
                                             'rejection_reason': None,
                                             'status': None
                                            },
                'risk_details': { 'cra_score': 81.0,
                                  'credit_score': 473.2844555079146,
                                  'lcr_score': 274.0,
                                  'ndvi_score': 118.28445550791454,
                                  'risk_reason': 'Bad Credit score',
                                  'risk_status': True
                                  }
                }
        """
        approved_loan_amount = int(self.get_eligible_loan_amount())
        approved_loan_tenure = self.get_loan_tenure()
        risk_details = self.get_risk_details()
        application_response = {}
        application_response["application_details"] = {
                                                        "status": None,
                                                        "loan_amount": 0,
                                                        "loan_tenure": 0,
                                                        "rejection_reason": None
                                                        }

        application_response["risk_details"] = risk_details
        if not risk_details.get("risk_status"):
            application_response["application_details"]["status"] = "approved"
            application_response["application_details"]["loan_amount"] = approved_loan_amount
            application_response["application_details"]["loan_tenure"] = approved_loan_tenure
        else:
            application_response["application_details"]["application_status"] = "rejected"
            application_response["application_details"]["application_rejection_reason"] = risk_details.get("risk_reason")
        return application_response

