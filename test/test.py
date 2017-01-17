# support only AU, CA, GB, FR, IT, SG, JP, DE, US, IN, C2, HK
import paypalrestsdk

# to get cid and secret : https://developer.paypal.com/developer/applications/createbtcred
cid='xxxx'
secret='xxxx'

api=paypalrestsdk.set_config(mode='sandbox', client_id=cid, client_secret=secret)

tk=api.get_access_token()

print("*"*50)
print(tk)
print("*"*50)

#ref: https://groups.google.com/forum/#!topic/google-appengine/4XiBBTn2XrE
