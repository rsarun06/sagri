# Sagri Task

One Paragraph of project description goes here


### Prerequisites


```
python3
```

### Setting up Environment
Do the following in a virtual environment.
```
pip3 install -r devops/requirements.txt
```

To execute the script, go to `sagri/src` and enter the below command.

```
python3 src/apply_loan.py

```
You will  be prompted to enter the below details.
```
Please enter your AADHAR number :: 1231231231
Please enter the loan amount :: 10000
Please enter the loan tenure :: 5
Please enter your land coordinates in decimal lat longformat [eg: 12.6952305,77.88333] :: 12.1231212, 77.874669
Press any key other than N to continue entering your land coordinates :: y
Please enter your land coordinates in decimal lat longformat [eg: 12.6952305,77.88333] :: 12.685102, 77.875160
Press any key other than N to continue entering your land coordinates :: 
Please enter your land coordinates in decimal lat longformat [eg: 12.6952305,77.88333] :: 12.685515, 77.875310
Press any key other than N to continue entering your land coordinates :: 
Please enter your land coordinates in decimal lat longformat [eg: 12.6952305,77.88333] :: 12.685672, 77.874819  
Press any key other than N to continue entering your land coordinates :: n

```
On entering `N`. You application response details will be shown as below.
```
-------------------------------------Applicaion Response-------------------------------------
{'application_details': {'loan_amount': 25000,
                         'loan_tenure': 5,
                         'rejection_reason': None,
                         'status': 'approved'},
 'risk_details': {'cra_score': 137.1,
                  'credit_score': 549.7567847143606,
                  'lcr_score': 157.20000000000002,
                  'ndvi_score': 255.45678471436057,
                  'risk_reason': None,
                  'risk_status': False}}
---------------------------------------------------------------------------------------------

```

                