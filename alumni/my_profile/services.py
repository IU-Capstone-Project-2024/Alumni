from login.models import CustomUser

def get_user_profile(email):
    """
    Get the user profile for a given email
    """
    try:
        return CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None
    
def get_user_interests(email):
    """
    Get user interests for a given email
    """
    profile = get_user_profile(email)
    array_interests = []
    if profile:
        for int in profile.interests.all():
            array_interests.append(int.name)
    return array_interests

def get_user_location(email):
    """
    Get user location for a given email
    """
    profile = get_user_profile(email)
    if profile:
        return profile.location
    return None

def get_user_alias(email):
    """
    Get user location for a given email
    """
    profile = get_user_profile(email)
    if profile:
        return profile.alias
    return None