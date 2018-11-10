import signature
import time
api_key = "5e9089d4fc44c3c357b4d46b91a52b440ac6acf7b5680caebb695994ad27750c"
boilerplate_header = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json",
    "API-Key": api_key,
    "Signature": None,
    "Timestamp": None,
    "Secret": "3e76857dd94e6d07eddd946a11f2211874bf7e89c85b49e8b4a3c3afdee5fbbe"
}

def generate_branded_header(request_type, brand, face_value):
    header = boilerplate_header
    header["Signature"] = signature.generate_signature(request_type, brand, face_value)
    header["Timestamp"] = signature.timestamp
    print(header)
    return header

