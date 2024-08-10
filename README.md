# X API Python Package

A simple Python library for posting tweets on X.com using X API v2.

## Installation

You can install the package using pip:

```bash
pip install x-pyapi
```

## Usage

```
from x_pyAPI import X_API

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'

def main():
    # Initialize API
    twitter_api = X_API(CONSUMER_KEY, CONSUMER_SECRET)

    # Authorize (only needed once)
    twitter_api.authorize()

    # Get user information
    user = twitter_api.get_user_info()

    # Post a tweet
    tweet_text = "Hello world!"
    twitter_api.post_tweet(tweet_text)

if __name__ == "__main__":
    main()

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
