def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        user.first_name = response['name']['givenName']
        user.last_name = response['name']['familyName']
        user.save()
    
