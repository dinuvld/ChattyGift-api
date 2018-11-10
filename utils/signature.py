import time
import hmac
import hashlib

client_request_id = int(time.time()*1000) - 1
api_key = "5e9089d4fc44c3c357b4d46b91a52b440ac6acf7b5680caebb695994ad27750c"
secret_key = bytearray("3e76857dd94e6d07eddd946a11f2211874bf7e89c85b49e8b4a3c3afdee5fbbe", 'utf-8')
endpoint = "digital-issue"
timestamp = str(int(round(time.time() * 1000)))


def generate_signature_seed(request_type, brand, face_value):
    face_value = str(face_value)
    return api_key + '-' + request_type + '-' + endpoint + '-' + str(client_request_id) + '-' + brand + '-' + "GBP" + '-' + face_value + '-' + timestamp

def generate_signature(request_type, brand, face_value):
    seed = generate_signature_seed(request_type, brand, face_value)
    signature_hmac = hmac.new(secret_key, bytearray(seed, 'utf-8'), hashlib.sha256)
    signature = str(signature_hmac.hexdigest())
    print(seed)
    print(signature)
    return signature
