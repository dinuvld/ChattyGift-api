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
    data = {
        "client_request_id": str(signature.client_request_id),
        "brand": "tesco",
        "face_value": {
            "amount": 10,
            "currency": "GBP"
        },
        "delivery_method": "code",
        "fulfilment_by": "rewardcloud",
        "fulfilment_parameters": {
            "to_name": "Receiver",
            "to_email": "vlad@reward.cloud",
            "from_name": "Reward Cloud",
            "from_email": "noreply@reward.cloud",
            "subject": "[TestCode] Here is your gift card!"
        },
        "personalisation": {
            "to_name": "Recipient",
            "from_name": "Sender",
            "message": "Here is your gift",
            "template": "standard"
        },
        "sector": "voluntary-benefits"
    }
    header = boilerplate_header
    header["Signature"] = signature.generate_signature(request_type, brand, face_value)
    header["Timestamp"] = signature.timestamp
    print(header)
    return header

