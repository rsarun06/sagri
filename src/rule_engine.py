"""
author: rs
created_on: 5th March 2020
"""
from utils.mock_credit_score import mock_cra_score, mock_lcr_score
from utils.compute_ndvi import compute_ndvi_score
from config.app_config import RULE_ENGINE_WEIGHTAGE, LOAN_RISK_SCORE, MIN_NVDI_SCORE, MIN_CRA_SCORE, MIN_LCR_SCORE


class RuleEngine(object):
    """
    RuleEnigne decides the risk factor of the loan application
    """
    def __init__(self, loan_obj):
        """
        :param loan_obj: Loan Object which contains the loan application details
        """
        self.loan_obj = loan_obj
        self.aadhar = loan_obj.aadhar
        self.land_coordinates = loan_obj.land_coordinates

    def get_cra_score(self, aadhar):
        """
        Get CRA Score for the given Aadhar
        :param aadhar: Aadhar ID
        :return: CRA Score
        """
        return mock_cra_score(aadhar)

    def get_lcr_score(self, aadhar):
        """
        Get LCR score for the given Aadhar
        :param aadhar: Aadhar ID
        :return: LCR Score
        """
        return mock_lcr_score(aadhar)

    def get_ndvi_score(self, land_coordinates):
        """
        GET NDVI score for the given land coordinates
        :param land_coordinates: Land coordinates
        :return: NDVI Score
        """
        return compute_ndvi_score(land_coordinates)

    def get_risk_status(self):
        """
        Compute the risk details for the given loan application
        :return: risk details
                {'cra_score': 226.79999999999998,
                  'credit_score': 615.2951998436262,
                  'lcr_score': 149.20000000000002,
                  'ndvi_score': 239.2951998436262,
                  'risk_reason': None,
                  'risk_status': False
                }
        """
        risk_obj = {
            "risk_status": False,
            "risk_reason": None,
            "credit_score": 0
        }
        # GET NDVI, CRA and LCR score
        ndvi_score = RULE_ENGINE_WEIGHTAGE.get("NDVI_WGT") * self.get_ndvi_score(self.land_coordinates)
        cra_score = RULE_ENGINE_WEIGHTAGE.get("CRA_WGT") * self.get_cra_score(self.aadhar)
        lcr_score = RULE_ENGINE_WEIGHTAGE.get("LCR_WGT") * self.get_lcr_score(self.aadhar)
        # Compute the final credit score by adding nvdi, cra and lsr scores along with the configured weightage
        risk_obj["credit_score"] = ndvi_score + cra_score + lcr_score
        risk_obj["ndvi_score"] = ndvi_score
        risk_obj["cra_score"] = cra_score
        risk_obj["lcr_score"] = lcr_score
        # If NDVI score is less than the minimum required value application's risk_status is set to True
        if ndvi_score < MIN_NVDI_SCORE:
            risk_obj["risk_status"] = True
            risk_obj["risk_reason"] = "Bad NDVI score"
        # If CRA score is less than the minimum required value application's risk_status is set to True
        if cra_score < MIN_CRA_SCORE:
            risk_obj["risk_status"] = True
            risk_obj["risk_reason"] = "Bad CRA Score"
        # If LCR score is less than the minimum required value application's risk_status is set to True
        if lcr_score < MIN_LCR_SCORE:
            risk_obj["risk_status"] = True
            risk_obj["risk_reason"] = "Bad CRA Score"
        # If computed credit score is less than the minimum required value application's risk_status is set to True
        if risk_obj["credit_score"] < LOAN_RISK_SCORE:
            risk_obj["risk_status"] = True
            risk_obj["risk_reason"] = "Bad Credit score"
        return risk_obj
