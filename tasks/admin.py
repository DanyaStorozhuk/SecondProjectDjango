from django.contrib import admin
from tasks.models import Task, CustomUser, Car, Comment, Resume

# Register your models here.


# Реєструємо модель Task у адмінці, щоб можна було керувати нею через веб-інтерфейс
admin.site.register(Task)

# Реєструємо модель CustomUser у адмінці
admin.site.register(CustomUser)

# Реєструємо модель Car у адмінці
admin.site.register(Car)

# Реєструємо модель Comments у адмінці
admin.site.register(Comment)

# Реєструємо модель Resume у адмінці
admin.site.register(Resume)