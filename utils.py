from cryptography.fernet import Fernet
import requests
import ujson

# to generate your key: Fernet().generate_key()
KEY = b''

f = Fernet(KEY)


def save_user_data(data: dict):
    encrypted_data = f.encrypt(ujson.dumps(data).encode())
    try:
        with open('user_data', 'wb') as data:
            data.write(encrypted_data)
    except:
        pass


def get_user_data() -> dict:
    try:
        with open('user_data', 'rb') as data:
            decrypt_data = ujson.loads(f.decrypt(data.read()).decode())
            return decrypt_data
    except:
        return {}


def send_balance(from_key, to_key, amount, pay_pass):
    url = f"https://market.csgo.com/api/v2/money-send/{amount}/{to_key}"
    params = {
        "pay_pass": pay_pass,
        "key": from_key
    }
    r = requests.get(url, params=params, timeout=20)
    return r


def send_wax_balance(from_key: str, steam_id: str, amount: int):
    url = "https://api.waxpeer.com/v1/transfer-money/"
    params = {
        "api": from_key,
        "steam_id": steam_id,
        "amount": amount
    }
    r = requests.post(url, params=params)
    return r


def get_tm_balance(api_key: str):
    url = "https://market.csgo.com/api/v2/get-money"
    params = {
        "key": api_key
    }
    r = requests.get(url, params=params, timeout=20)
    return r


def get_wax_balance(api_key: str):
    url = "https://api.waxpeer.com/v1/user"
    params = {
        "api": api_key
    }
    r = requests.get(url, params=params, timeout=20)
    return r
