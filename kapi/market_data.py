#************************************************************************************
#   This file contains the class that allows you to get market information related
#   to crypto from Kraken's API.
#************************************************************************************
from ksession import KSession

class MarketData():

    """
    This class serves to provide the user with market data type information.
    """

    def __init__(self, ksession: KSession) -> None:
        self.__ksession = ksession

    def GetServerTime(self, timeout: float = None) -> tuple[int, str]:
        """
        Gets time from Kraken's servers.
        """

        # Build up our URL for the request
        url = "https://api.kraken.com/0/public/Time"

        # Send out the request
        response = self.__ksession.SendRequest(
            method="GET",
            url=url,
            params=None,
            data=None,
            json=None,
            timeout=timeout
        )

        # Extract the data from the result key
        data: dict = response.get("result")

        # Get the unix timestamp from the data and the RFC standard
        # equivalent in the form of a string
        timestamp = data.get("unixtime")
        rfc_time  = data.get("rfc1123")

        return timestamp, rfc_time