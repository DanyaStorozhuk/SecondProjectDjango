from django import forms
from tasks.models import CustomUser, Task, Comment, Resume, Car
from django.contrib.auth.forms import UserCreationForm









# Форма для створення/редарування завдання 
class TaskForm(forms.ModelForm):
    # Внутрішній клас Meta, який описує параметри форми
    class Meta:
        # Вказуємо модель з якою працює форма
        model = Task
        # Поля, які будуть доступні у формі
        fields = ["title", "description", "status", "priority", "due_date"]
        # Налаштовуємо вигляд (CSS класи) для окремих полів
        widgets = {
            'status': forms.Select(attrs={'class': 'supernova-input-777'}),
            'priority': forms.Select(attrs={'class': 'supernova-input-777'}),
        }

    # Ініціалізуємо форму
    def __init__(self, *args, **kwargs):
        # Викликаємо ініціалізацію базового класу
        super(TaskForm, self).__init__(*args, **kwargs)
        # Для кожного поля додаємо Bootstrap-клас form-control
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        # Для поля due_date додаємо ще один кастомний клас
        self.fields["due_date"].widget.attrs["class"] += "my-custom=datepiker"






# Форма для створення/редагування резюме
class TaskFormResume(forms.ModelForm):
    class Meta:
        model = Resume
        # Поля які будуть у формі
        fields = ["user", "title", "experience", "education", "skils"]
        # Кастомізуємо CSS вигляд для полів
        widgets = {
            # Поле для вибору користувача з випадаючого списку
            "user": forms.Select(attrs={"class": "form-control"}), 
            # Поле ввиводу тексту
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Назва резюме"}),
            # Багато рядкове поле
            "experience": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Досвід роботи"}),
            # Текстове поле для освіти
            "education": forms.TextInput(attrs={"class": "form-control", "placeholder": "Освіта"}),
            # Багато рядкове поле для навичок
            "skils": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Навички"}),
        }


    # Ініціалізуємо форму
    def __init__(self, *args, **kwargs):
        # Викликаємо ініціалізацію батьківського класу 
        super().__init__(*args, **kwargs)
        # Додаємо Bootstrap-класи для всіх полів
        # Перебираємо всі поля
        for field in self.fields:
            # Додаємо клас form-control для стилізації
            self.fields[field].widget.attrs.update({"class": "form-control"})



# Форма для реєстрації нового користувача
# Наслідуємо від стандартної UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Використовуємо внутрішній клас Meta базової форми
    class Meta(UserCreationForm.Meta):
        # Працюємо з кастомною моделю користувача
        model = CustomUser
        # Поля нашої форми
        fields = ['username', 'email', 'passport', 'phone', 'password1', 'password2']


# Форма для створення коментарів
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['text']


# Форма для фільтрації завдань за статусом
class TaskFilterForm(forms.Form):
    # можливі варіанти статусів
    STATUS_CHOICES = [
        ("", "Всі"),
        ("new", "Нове"),
        ("in_progress", "В роботі"),
        ("done", "Завершено"),
    ]


    # Поле вибору статусу (необов'язкове)
    # choices=STATUS_CHOICES - Передаємо список можливих варіантів для вибору (масив кортежів зі значенням і підписом)
    # required=False -  Поле необов’язкове — користувач може залишити його порожнім
    # label="Статус" - Підпис, який буде відображатися біля поля у формі (у шаблоні)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")


    # Ініціалізація форми
    def __init__(self,*args, **kwargs):
        # Викликаємо базовий конструктор
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        # Додаємо Bootstrap-стилі дял поля статусу
        self.fields["status"].widget.attrs.update({"class": "form-control"})



# Форма для фільтрації коментарів за датою
class CommentFilterForm(forms.Form):

    # Поле для вибору дати (календарик)
    # required=False не обов'язкове
    # Підпис біля поля 
    #  HTML5 datepicker (календарик)
    date = forms.DateField(required=False, label="date", widget=forms.DateInput(attrs={'type': 'date'}))


# Форма для створення/редагування резюме
class ResumeForm(forms.ModelForm):
    # Вкладений клас Meta для налаштування форми
    class Meta():
        # Вказуємо з якою моделю ми працюємо
        model = Resume
        # Поля моделі які будуть відображенні у формі
        fields = ['user', 'title', 'experience','education','skils']


# Форма для створення/редагування автомобіля
class CarForm(forms.ModelForm):
    # Вкладений клас Meta для налаштування форми
    class Meta():
        # Вказуємо модель з якою ми працюємо
        model = Car
        # Поля моделі які будуть відображені у формі
        fields = ['brand', 'model', 'year','owner', 'photo']