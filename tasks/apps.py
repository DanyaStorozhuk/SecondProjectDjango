from django.apps import AppConfig

# Створюємо клас конфігурації для нашого додатку "tasks"
class TasksConfig(AppConfig):
    # Вказуємо тип поля яке автоматично буде створюватися для певних ключів моделей у цьому додатку
    # BigAutoField - це велике число, яке автоматично інкременшується
    default_auto_field = 'django.db.models.BigAutoField'

    # Назва додатку. Django використовує її для реєстрації додатку у проєкті
    name = 'tasks'
