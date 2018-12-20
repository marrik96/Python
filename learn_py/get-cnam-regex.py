import requests, re

cnamUrl = 'https://api.opencnam.com/v3/phone/'
myDid = input('Enter DID to check: ')
myDidCheck = re.compile(r'\d{11}')
CheckResult = myDidCheck.search(myDid)
if CheckResult == None:
    print('Please enter valid 11 digit Phone Number with no dashes or ()!')
    exit()
myAcct = input('Enter CNAM Account: ')
myToken = input('Enter Auth: ')
myResp = requests.get(cnamUrl + myDid + '?account_sid=' + myAcct + '&auth_token=' + myToken)
if myResp.status_code != 200:
    # Error
    print('HTTP Error: ' + str(myResp.status_code))
    exit()
code = myResp.status_code
name = myResp.content
response = str(code) + '\n' + str(name)
print(response.replace('b', ''))