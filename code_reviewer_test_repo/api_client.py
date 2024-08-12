import requests
from local_settings import ANALYTICS_API_TOKEN

class AnalyticsApiClient():
    """
    A simple client to interact with Analytics API
    """

    def analytics_get(self, url, params={}):
        response = requests.get(
            url,
            headers={'Authorization': ANALYTICS_API_TOKEN},
            # timeout=1.5,
            params=params
        )
        return response.json()

    def get_analytics_recommendation(self, url):
        """
        https://learn.lytics.com/documentation/developer/api-docs/content#content-recommendation
        https://learn.lytics.com/documentation/developer/api-docs/content#generic-content-recommendation
        """

        analytics_api_url = 'https://api.lytics.io/api/content/recommend'
        params = {
            'url': url,
            'limit': 10,
        }
        response = self.analytics_get(analytics_api_url, params)

        return response