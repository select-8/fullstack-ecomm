from django.contrib.auth.models import User

class EmailAuth:
    '''Authenticate a user by exact match on the email and password'''

    def authenticate(self, request, username=None, password=None):
        '''
        get an instance of `User` based off the email and 
        verifiy the password
        '''
        try:
            user = User.objects.get(email=username) 

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        '''
        Used by the Django Authentication system to retrieve a user instance
        '''
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
