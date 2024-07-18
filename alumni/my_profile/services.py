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
    Get user interests for a given email as array
    """
    profile = get_user_profile(email)
    array_interests = []
    if profile:
        for int in profile.interests.all():
            array_interests.append(int.name)
    return array_interests


def get_all_users():
    """
    Retrieve all users from the database as a list of dictionaries
    with keys 'alias' and 'location'.
    """
    users_for_map = []
    for user in CustomUser.objects.all():
        user_data = {
            'alias': user.alias,
            'location': user.location
        }
        users_for_map.append(user_data)
    return users_for_map
