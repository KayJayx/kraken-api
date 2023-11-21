#************************************************************************************
#   This file holds the class that allows you to send out requests to Kraken's 
#   servers.
#************************************************************************************
from kcredentials import KCredentials
from typing import Union
import requests

class KSession():

    """
    This class allows the user to send different types of requests to Kraken's servers.
    """

    def __init__(self, credentials: KCredentials, session: requests.Session = None) -> None:
        self.credentials = credentials
        self.session     = session

    def SendRequest(self, method: str, url: str, params: dict, data: dict, json: dict, 
                    timeout: float) -> Union[dict, list]:
        """
        This is the central function that handles all of the different types of requests.
        """

        headers = {
            "User-Agent"    : "".join(["Mozilla/5.0 ", 
                                       "(Windows NT 10.0; ",
                                       "Win64; x64) ",
                                       "AppleWebKit/537.36 (KHTML, like Gecko) ",
                                       "Chrome/97.0.4692.71 ",
                                       "Safari/537.36"]),
            #"Authorization" : f"Bearer {self.credentials.access_token.token}",
            "Content-Type"  : "application/json"
        }

        # Send the request
        if self.session is not None:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=timeout,
                allow_redirects=False
            )
        else:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=timeout,
                allow_redirects=False
            )

        # Check response
        if not response.ok:

            if len(response.content) > 0:
                response = response.json()
                raise requests.HTTPError(response["error"])

            raise requests.HTTPError()

        # Certain requests will not return any content
        if len(response.content) == 0:
            response = {"response" : "request was successful"}
        elif len(response.content) > 0:
            response = response.json()

        return response