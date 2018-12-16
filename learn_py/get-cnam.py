import requests

cnamUrl = 'https://api.opencnam.com/v3/phone/'
myDid = input('Enter DID to check: ')
if len(myDid) != 11 and isinstance(myDid, str):
    print('Please enter valid 11 digit Phone Number')
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