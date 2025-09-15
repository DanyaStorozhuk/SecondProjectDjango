from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
        ("new", "Нове"),
        ("in_progress", "В роботі"),
        ("done", "Завершено"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Легке"),
        ("medium", "Нормальне"),
        ("high", "Складне"),
    ]

    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title
    

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Адміністратор"),
        ("user", "Користувач"),
    ]
    
    username = models.CharField(max_length=50, unique=True)
    # blank=True - дозволяє залишити поле порожнім при заповнені форми
    passport = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    # blank=True - дозволяє залишити поле порожнім при заповнені форми
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")

    def __str__(self):
        return self.username
    

class Comment(models.Model):
    # task = models.ForeignKey(Task, on_delete=models.CASCADE )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.text} - {self.created_at}"


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    # ForeignKey означає «багато записів цієї моделі можуть належати одному запису іншої моделі» (many-to-one).
    # on_delete=models.CASCADE - Тобто, якщо видалити CustomUser, то всі Car з owner на цього користувача також будуть видалені.
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cars_images/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.owner} - {self.brand} - {self.model}"
    

class Resume(models.Model):
    STATUS_CHOICES = [
        ("new", "Нове"),
        ("accepted", "Прийнято"),
        ("rejected", "Відхилено"),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="resumes")
    title = models.CharField(max_length=200)
    experience = models.TextField()
    education = models.CharField(max_length=150, blank=True)
    skils = models.TextField()
    data_create =  models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

