import tweepy

def get_x_user_info(username, api_key, api_secret, access_token, access_token_secret):
    """
    Fetches user information from X (formerly Twitter) using the official API.
    """
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        user = api.get_user(screen_name=username)
        return {
            "id": user.id_str,
            "name": user.name,
            "username": user.screen_name,
            "description": user.description,
            "followers_count": user.followers_count,
            "location": user.location,
            "profile_image_url": user.profile_image_url_https
        }
    except Exception as e:
        print(f"Error fetching user info: {e}")
        return None