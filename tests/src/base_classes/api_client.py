import requests
from requests import Response, Session


class APIClient:
    def __init__(self, base_address: str, session: Session = None):
        self.base_address = base_address
        if session:
            self.session = session
        else:
            self.session = None

    def post(self, path=None, params=None, data=None, json=None,
             headers=None, cookies=None) -> Response:
        url = f"{self.base_address}{path}"

        if self.session:
            return self.session.post(url=url, params=params, data=data,
                                     json=json, headers=headers, cookies=cookies)
        else:
            return requests.post(url=url, params=params, data=data,
                                 json=json, headers=headers, cookies=cookies)

    def get(self, path=None, params=None, headers=None, cookies=None) -> Response:
        url = f"{self.base_address}{path}"

        if self.session:
            return self.session.get(url=url, params=params, headers=headers, cookies=cookies)
        else:
            return requests.get(url=url, params=params, headers=headers, cookies=cookies)