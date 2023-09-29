import urllib.parse
import hashlib
import hmac
import base64

def get_kraken_signature(urlpath, data, secret) -> str:

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

if __name__ == '__main__':
    api_sec = "kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg=="

    data = {
        "nonce": "1616492376594", 
        "ordertype": "limit", 
        "pair": "XBTUSD",
        "price": 37500, 
        "type": "buy",
        "volume": 1.25
    }

    signature = get_kraken_signature("/0/private/AddOrder", data, api_sec)
    print("API-Sign: {}".format(signature))