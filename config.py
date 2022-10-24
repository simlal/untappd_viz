# Ask for Client ID and Client Secret keys
id = input('Enter Client ID : ')
secret= input('Enter Secret key : ')

# Verify credentials
credentials = {'client id' : id, 'client secret' : secret}
print(credentials)
print(credentials['client id'])
print(credentials['client secret'])