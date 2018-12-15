import requests

cnamUrl = 'https://api.opencnam.com/v3/phone/'
myDid = input('Enter DID to check')
myAcct = input('Enter CNAM Account')
myToken = input('Enter Auth')

myResp = requests.get(cnamUrl + myDid + '?account_sid=' + myAcct + '&auth_token=' + myToken)
if myResp.status_code != 200:
    # Error
    raise ApiError('GET /phone/ {}'.format(myResp.status_code))
print(myResp.status_code)
print(myResp.content)