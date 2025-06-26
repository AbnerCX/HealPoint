from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    
    def create_user(self, phone_number, password=None):
        """
        Default custom user creation method for HealPoint.
        It requires a phone number and a password.
        """
        if not phone_number:
            raise ValueError("Users must have a phone number")
        
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, password=None):
        """
        Custom superuser creation method for HealPoint.
        """
        user = self.create_user(phone_number, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class UserHealPoint(AbstractBaseUser, PermissionsMixin):
    
    phone_number = models.CharField(max_length=10, unique=True, verbose_name="phone number")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []  
    
    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"