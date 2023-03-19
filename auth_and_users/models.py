from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
#from django.contrib.auth.validators import UnicodeUsernameValidator


ROLE_CHOICES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')
    confirmation_code = models.CharField(max_length=200, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']



'''
class CustomAccountManager(BaseUserManager):
    def create_user(self, email):
        user = self.model(email=email)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, role):
        user = self.create_user(email=email)
        user.set_password(password)
        user.role = 'admin'
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)

        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    validators=[UnicodeUsernameValidator()]
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomAccountManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email     
'''   

