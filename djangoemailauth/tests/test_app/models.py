from djangoemailauth.models import AbstractEmailUser


class EmailUser(AbstractEmailUser):
    """ Main User model """
    class Meta:
        app_label = "djangoemailauth"
