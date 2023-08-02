from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#헬퍼클래스
class UserManager(BaseUserManager):

    def create_user(self, email, username, password,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)

        #user = self.model(email=self.normalize_email(email), **extra_fields)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(email=email, password=password,)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

#실제 모델이 상속받아 생성하는 클래스가 Abstract
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True) 
    username = models.CharField(max_length=30, null = True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    password1 = models.CharField(max_length=30,  null=False, blank=False,default='password1')
    password2 = models.CharField(max_length=30,  null=False, blank=False,default='password2')
    name = models.CharField(max_length=30,  null=False, blank=False,default='name')   #실명
    nickname = models.CharField(max_length=30, null = True, default='nickname')
    phone = models.CharField(max_length=100, null=False, blank=False,default='phone')
    birthday = models.CharField(max_length=30,  null=False, blank=False,default='birthday')
    address1 = models.CharField(max_length=255, null=False, blank=False, default='address1') #우편번호
    address2 = models.CharField(max_length=255, null=False, blank=False, default='address2') #주소지
    address3 = models.CharField(max_length=255, null=False, blank=False, default='address3') #상세주소
    usertype = models.CharField(max_length=255, null=False, blank=False, default='usertype') #구매자/판매자
    profile = models.ImageField(upload_to="", null = True, blank=True, default='profile')                      #프로필

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return"<%d %s>" % (self.pk, self.email)
