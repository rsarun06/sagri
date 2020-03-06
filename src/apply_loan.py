"""
author: rs
created_on: 5th March 2020
"""
import os
import sys
import traceback
# Appending PYTHONPATH
PYTHON_PATH = os.getcwd()  + "/.."
sys.path.append(PYTHON_PATH)
from src.process_loan import ProcessLoan
from pprint import pprint as pp

class LoanApplication(object):
    """
    This class has all the attributes to collect application details
    """
    def __init__(self):
        """
        Details to be collected are as follows:
            aadhar - Applcation UID
            loan_amount - Loan Amount
            loan_tenure - Loan repayment tenure
            land_coordinates - Loan coordinates of the farm as a list of tuple in decimal degrees metric
        """
        self.aadhar = None
        self.loan_amount = None
        self.loan_tenure = None
        self.land_coordinates = []
        # self.aadhar = 123
        # self.loan_amount = 10000
        # self.loan_tenure = 6
        # self.land_coordinates = [(12.685249, 77.874669),
        #                          (12.685102, 77.875160),
        #                          (12.685515, 77.875310),
        #                          (12.685672, 77.874819)
        #                          ]


    def print_application(self):
        """
        This method used to print the application details
        :return: None
        """
        loan_details = "Aadhar :: {} Loan Amount :: {} Loan Tenure :: {} Land_coordinates :: {}"
        print(loan_details.format(self.aadhar, self.loan_amount, self.loan_tenure, self.land_coordinates))

    def get_application(self):
        """
        This is the entry point from where the application details are collected
        :return: None
        """
        self.aadhar = input("Please enter your AADHAR number :: ")
        self.loan_amount = input("Please enter the loan amount :: ")
        loan_tenure = input("Please enter the loan tenure :: ")
        self.loan_tenure = int(loan_tenure)
        self.get_land_coordinates()

    def get_land_coordinates(self):
        """
        This is used to get the farm land coordinates
        Coordinates should be of the format "12.3445434, 77.1232131"
            It should not contain only decimal values
        Minimum of 3 coordinates should be entered
        :return:
        """
        loop_flag = True
        while loop_flag:
            land_coordinates = input("Please enter your land coordinates in decimal lat long"\
                                     "format [eg: 12.6952305,77.88333] :: ")
            formatted_coord = self.format_land_coordinates(land_coordinates)
            if formatted_coord:
                self.land_coordinates.append(formatted_coord)
            # Prompting loan applicant to decide if he wants to enter more coordinates
            get_land_coordinates = input("Press any key other than N to continue entering your land coordinates :: ")
            if get_land_coordinates.lower() == "n":
                loop_flag = False
                no_of_coordinates = len(self.land_coordinates)
                # To check if minimum of 3 coordinates are entered
                if no_of_coordinates < 3:
                    print("Minimum of 3 sets of coordinates are required.\nYou have entered only {} coordinates"
                          .format(no_of_coordinates))
                    # Prompting loan applicant to decide if he wants to enter more coordinates
                    quit_application = input("Press any key other than N to continue entering your land coordinates, "\
                                             "otherwise your loan application will be discarded :: ")
                    if quit_application.lower() != "n":
                        loop_flag = True

    def format_land_coordinates(self, coord):
        """
        Converting string format coordinates to decimal degrees
        This validates if the entered coordinates are inthe expected format
        :param coord:
        :return:
        """
        formatted_coord = ()
        for data in coord.split(","):
            if data:
                val = eval(data)
            else:
                val = None
                print("You have entered Invalid value for coordinates.\nEntered data is discarded.")
            if isinstance(val, float):
                formatted_coord += (val,)
            else:
                print("You have entered Invalid value for coordinates.\nEntered data is discarded.")
            # If If more than one comma is there, print Invalid value
            if len(formatted_coord) > 2:
                # Raise Exception
                print("You have entered Invalid value for coordinates.\nEntered data is discarded.")
        if len(formatted_coord) != 2:
            print("You have entered Invalid value for coordinates.\nEntered data is discarded.")
        elif formatted_coord:
            return formatted_coord


if __name__ == "__main__":
    try:
        loan_app_obj = LoanApplication()
        loan_app_obj.get_application()
        # loan_app_obj.print_application()
        application_details = ProcessLoan(loan_app_obj).process_loan()
        print("-------------------------------------Applicaion Response-------------------------------------")
        pp(application_details)
        print("---------------------------------------------------------------------------------------------")
    except Exception:
        traceback.print_exc()
        print("Exception occured")