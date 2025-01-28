# accounts/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class UsernameOrEmailBackend(ModelBackend):
    """
    Autentica um usuário utilizando nome de usuário ou e-mail.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        
        try:
            # Busca o usuário pelo nome de usuário ou e-mail (case-insensitive)
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)  # Previne timing attacks
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
