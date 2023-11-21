#************************************************************************************
#   This file holds the class that allows you to create a client instance and it
#   is through this client connection that we access the Kraken API.
#************************************************************************************
from kcredentials import KCredentials
from ksession import KSession
from kapi.market_data import MarketData
import requests

class KClient():

    """
    This class allows the user to send different types of requests to Kraken's servers.
    The requests can include ticker information, order placement and account info.
    """

    def __init__(self, credentials: KCredentials, session: requests.Session = None) -> None:
        self.__ksession    = KSession(credentials, session)
        self.__market_data = MarketData(self.__ksession)

    @property
    def ksession(self) -> KSession:
        return self.__ksession
    
    @property
    def market_data(self) -> MarketData:
        return self.__market_data

"""
def main():

    kcredentials = KCredentials()

    kclient = KClient(kcredentials)

    timestamp, rfc = kclient.market_data.GetServerTime()

    return 0

if __name__ == "__main__": main()
"""