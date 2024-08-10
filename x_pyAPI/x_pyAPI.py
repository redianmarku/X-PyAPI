from requests_oauthlib import OAuth1Session
import json

class X_API:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.oauth = self._create_oauth_session()

    def _create_oauth_session(self, access_token=None, access_token_secret=None):
        return OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

    def authorize(self):
        # Get request token
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        fetch_response = self.oauth.fetch_request_token(request_token_url)
        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")

        # Get authorization URL
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = self.oauth.authorization_url(base_authorization_url)
        print(f"Please go here and authorize: {authorization_url}")
        verifier = input("Paste the PIN here: ")

        # Get access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        self.oauth = self._create_oauth_session(resource_owner_key, resource_owner_secret)
        oauth_tokens = self.oauth.fetch_access_token(access_token_url, verifier=verifier)
        self.access_token = oauth_tokens["oauth_token"]
        self.access_token_secret = oauth_tokens["oauth_token_secret"]
        self.oauth = self._create_oauth_session(self.access_token, self.access_token_secret)

    def post_tweet(self, tweet_text):
        payload = {"text": tweet_text}
        response = self.oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )
        if response.status_code == 201:
            print("Tweet posted successfully.")
            return response.json()
        else:
            print(f"Failed to post tweet: {response.status_code} {response.text}")
            return None


    def get_user_info(self, user_fields="created_at,description"):
        params = {"user.fields": user_fields}
        response = self.oauth.get("https://api.twitter.com/2/users/me", params=params)
        
        if response.status_code != 200:
            raise Exception(
                f"Request returned an error: {response.status_code} {response.text}"
            )
        
        print("Response code:", response.status_code)
        json_response = response.json()
        
        # Extract user info from the response
        user_data = json_response.get("data", {})
        name = user_data.get("name", "N/A")
        username = user_data.get("username", "N/A")
        description = user_data.get("description", "N/A")
        created_at = user_data.get("created_at", "N/A")

        # Print extracted information
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Description: {description}")
        print(f"Created At: {created_at}")
        
        return {
            "name": name,
            "username": username,
            "description": description,
            "created_at": created_at
        }
