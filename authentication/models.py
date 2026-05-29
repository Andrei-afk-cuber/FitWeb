from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# user manager
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, commit=True):
        if not email:
            raise ValueError('Пользователь должен иметь почту')
        if not first_name:
            raise ValueError('Пользователь должен иметь имя')
        if not last_name:
            raise ValueError('Пользователь должен иметь фамилию')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)

        if commit:
            user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            commit=False
        )

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user

# user model
class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    GENDER_CHOICES = (
        ('M', 'Мужчина'),
        ('F', 'Женщина'),
    )
    ACTIVITY_CHOICES = (
        (1, 'Нет активности'),
        (2, 'Легкая активность'),
        (3, 'Умеренная активность'),
        (4, 'Высокая активность'),
        (5, 'Очень высокая активность')
    )
    TARGET_CHOICES = (
        ('loss', 'Снижение веса'),
        ('maintain', 'Поддержание веса'),
        ('gain', 'Набор веса')
    )

    email = models.EmailField(
        'почта', max_length=100, unique=True
    )
    first_name = models.CharField(
        'Имя', max_length=50
    )
    last_name = models.CharField(
        'Фамилия', max_length=50
    )
    gender = models.CharField(
        'Пол', max_length=1, choices=GENDER_CHOICES, default='M'
    )
    weight = models.FloatField(verbose_name='Вес', default=0)
    height = models.FloatField(verbose_name='Рост', default=0)
    age = models.IntegerField(
        'Возраст', validators=[MinValueValidator(12), MaxValueValidator(100)], default=12
    )
    activity_status = models.IntegerField(
        'Статус физической активности', choices=ACTIVITY_CHOICES, default=1
    )
    target = models.CharField(
        'Цель', max_length=10, choices=TARGET_CHOICES, default='maintain'
    )
    is_active = models.BooleanField('Активированный', default=False)
    is_staff = models.BooleanField('Работник', default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def body_mass_index(self):
        return round(self.weight / (self.height / 100) ** 2, 1)