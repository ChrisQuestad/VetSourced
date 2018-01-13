from django.contrib.auth.decorators import user_passes_test, login_required

rec_login_required = user_passes_test(lambda u: u.is_employer, login_url='login/')

def employer_login_required(view_func):
    decorated_view_func = login_required(rec_login_required(view_func), login_url='login/')
    return decorated_view_func
