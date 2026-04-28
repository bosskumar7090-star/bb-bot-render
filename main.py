import requests

class BBB_Smart_Session:
    def __init__(self):
        # Free Proxy List (Aap yahan paid proxy bhi daal sakte ho)
        self.proxies = {
            "http": "http://username:password@proxy_address:port", # Agar paid hai
            "https": "http://username:password@proxy_address:port"
        }
        # Agar free proxy use kar rahe ho toh simple list banao

    def request_otp(self, phone):
        url = "https://www.bigbasket.com/svc/registration/otp-gen/" # Example URL
        
        # Ye line IP block bypass karegi
        try:
            # 'proxies' parameter add karne se IP badal jata hai
            response = requests.post(url, data={"phone": phone}, proxies=self.proxies, timeout=5)
            return "OTP Sent Successfully!"
        except Exception as e:
            return f"Error: {str(e)}"
