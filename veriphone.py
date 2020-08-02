import requests
__docu__ = "https://veriphone.io/docs/v2"

class Wrapper:
    def __init__(self, API_Key):
        self.api_key = API_Key
        self.base_url = "https://api.veriphone.io/v2/"

    def Verify_key(self, phone_number):
        """
        Comment: Verifying the API Key for the APi
        Input: Name of Instance
        Output: True if worked, False if not
        Special: nothing special
        """
        url = self.base_url + "verify"
        params = {"key" : self.api_key, "phone": phone_number}
        r = requests.get(url, params=params)
        print r.content


if __name__ == '__main__':
    import json
    with open("creds.json", "r") as f:
        creds = json.load(f)
    test = Wrapper(creds["API-Key"])
    inp = raw_input("Please enter a Phone number you want verified: ")
    test.Verify_key(inp)
