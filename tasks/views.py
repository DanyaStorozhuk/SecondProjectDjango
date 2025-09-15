from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from tasks import models 
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View, UpdateView, DeleteView
from tasks.forms import TaskForm, CustomUserCreationForm, CommentForm, TaskFilterForm, ResumeForm, CarForm,  CommentFilterForm, TaskFormResume
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Task, CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from tasks.mixings import UserOwnerMixin, ResumeOwnerMixin, WorkerOwnerMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
# Create your views here.


# Функція реєстрації користувача



def custom_403_view(request, exception=None):
    return render(request, "tasks/errors403.html", status=403)



def register(request):
    # Перевіряємо чи надійшов POST запит
    if request.method == "POST":
        # Створюємо форму з даних POST
        form = CustomUserCreationForm(request.POST)
        # Перевіряємо валідність форми 
        if form.is_valid():
            # Зберігаємо користувача в базу
            form.save()
            # Переходимо на сторінку логіну
            return redirect('tasks:login')
    else:
        # при GET - запиті ми створюємо порожню форму
        form = CustomUserCreationForm()
    # Рендеримо шаблон з формою
    return render(request, 'tasks/register.html', {'form': form})


# Функція логіну користувача

def login(request):
    # якщо POST - запит 
    if request.method == "POST":
        # Створюємо форму авторизації з даних
        form = AuthenticationForm(data=request.POST)
        # Перевірка валідності
        if form.is_valid():
            # Отримуємо користувача з форми 
            user = form.get_user()
            # Логін користувача в сесію
            auth_login(request, user)
            # Перенаправляємо на список завдань
            return redirect('tasks:task-list')
        else:
            # Для дебагу в консолі
            print("Помилки форми:", form.errors)
            # Повертаємо форму з помилками
            return render(request, 'tasks/login.html', {'form': form})
    else:
        # Порожня форма при GET 
        form = AuthenticationForm()
    # Рендер шаблону
    return render(request, 'tasks/login.html', {'form': form})


# Список всіх завдань 

# Обмежуємо доступ лише для авторизованих користувачів
@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    # Модель завдань
    model = models.Task
    # Змінна для шаблону
    context_object_name = 'tasks'
    # Шаблон для відображення
    template_name = 'tasks/task_list.html'


    # Фільтруємо завдання за статусом, якщо передано в GET-параметрах
    def get_queryset(self):
        queryset = super().get_queryset()
        # Отримуємо status з GET
        status = self.request.GET.get("status", "")
        if status:
            # Фільтруємо 
            queryset = queryset.filter(status=status)
        return queryset
    
    # Отримуємо додаткові дані у контекст шаблону TaskListView
    def get_context_data(self, **kwargs):
        # Викликаємо стандартний метод батьківького класу, щоб зберегти наявні дані контексту
        context = super().get_context_data(**kwargs)
        # Додаємо у контекст форму фільтрації задач, ініціалізовану GET - параметри
        context["form"] = TaskFilterForm(self.request.GET)
        # Додаємо у котектс списків всіх користувачів (workers)
        context['workers'] = CustomUser.objects.all()
        # Повертаємо оновлений контекст 
        return context
    
    
     
# Клас для відображення списку коментарів
class CommentsListViews(ListView):
    # Вказуємо модельку, якою працює цей ListView
    model = models.Comment
    # Ім'я зміної, яка буде передана у шаблон
    context_object_name = 'comments'
    # Шаблон який буде рендеритися
    template_name = 'tasks/task_view_list.html'


    # Метод для отримання даних з БД
    def get_queryset(self):
        # Отримуємо стандартний queryset (усі коментарі)
        queryset = super().get_queryset()
        # Ініціалізуємо форму фільтрації коментарів GET-параметрами
        self.form = CommentFilterForm(self.request.GET or None)

        # Перевіряємо чи форма валідна 
        if self.form.is_valid():
            # Отримуємо значення дати з форми
            date = self.form.cleaned_data.get('date')
            # Якщо дата є - фільтруємо коментарі за датою створення
            if date:
                queryset = queryset.filter(created_at=date)

        # Повертаємо (відфільтрований) queryset
        return queryset
    

    # Додаємо форму у контекст шаблону 
    def get_context_data(self, **kwargs):
        # Отримуємо базовий контекст
        context = super().get_context_data(**kwargs)
        # Додаємо форму фільтра у контекст
        context['form'] = self.form
        # повертаємо context
        return context



# Клас для відображення списку завдань
class TaskListTask(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_task.html'

    # Отримує параметр status із GET-запиту. Якщо status присутній, фільтрує завдання за цим статусом
    def get_queryset(self):
        # Отримуємо всі завдання
        queryset = super().get_queryset()
        # Отримуємо параметр status з URL
        status = self.request.GET.get("status", "")
        if status:
            # Фільтруємо задачі
            queryset = queryset.filter(status=status)
        return queryset

    # Додає TaskFilterForm до контексту, ініціалізовану з GET-параметрів (або порожню, якщо параметрів немає)
    def get_context_data(self, **kwargs):
        # Викликає метод батьківського класу (DetailView/ListView) і отримує початковий контекст
        context = super().get_context_data(**kwargs)
        # Додає форму фільтрації задач, ініціалізовану GET-параметрами користувача
        context["form"] = TaskFilterForm(self.request.GET or None)
        # Повертає готовий контекст у шаблон
        return context


# Клас для перегляду деталей задачі
class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = 'tasks/task_detail.html'




# Клас для перегляду деталей резюме
class TaskDetailViewResume(DetailView):
    model = models.Resume
    context_object_name = "resume"
    template_name = 'tasks/task_detail_resume.html'



# Клас для створення нової задачі
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = "tasks/task_form.html"
    # Використовуємо форму TaskForm (форми з forms.py)
    form_class = TaskForm
    # Дозволяє перенаправити користувача кудись після того як ми створили нашу задачу
    success_url = reverse_lazy('tasks:task-list')


    # Метод для збереження автора задачі
    def form_valid(self, form):
        # Встановлюємо автора задачі як поточного користувача
        form.instance.creator = self.request.user
        # Викликаємо стандартний метод CreateView
        return super().form_valid(form)
    


# Клас для домашньої сторінки
class HomeView(TemplateView):
    # Просто відображає шаблон
    template_name = 'tasks/task_home.html'




# Клас для створення коментарів
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    # Використовуємо створену форму
    form_class = CommentForm
    template_name = 'tasks/task_comment.html'
    # Після створення коментаря користувач перенаправляється на список задач
    success_url = reverse_lazy('tasks:task-list')


    # Метод дял збереження автора коментаря
    def form_valid(self, form):
        # Автором коментаря буде поточний користувач
        form.instance.author = self.request.user
        # Делегуємо батьківському класу стандартне збереження і редирект
        return super().form_valid(form)
    


# Клас який робить список підтверджених резюме
class WorkerTaskDetailView(ListView):
    model = models.Resume
    context_object_name = 'workers'
    template_name = 'tasks/worker_task_detail.html'

    # Перевизначаємо отримання quereset, щоб повертати тільки потрібні об'єкти
    def get_queryset(self):
        # Фільтруємо резюме за полем status - тільки зі значенням "accepted"
        return models.Resume.objects.filter(status = "accepted")



# Клас списку нових резюме 
class ResumeListView(WorkerOwnerMixin, ListView):
    model = models.Resume
    context_object_name = 'resumes'
    template_name = 'tasks/new_resume.html'


    # Перевизначаємо джерло даних
    def get_queryset(self):
        # Повертаємо тільки резюме зі статусом "new"
        return models.Resume.objects.filter(status = "new")


# Клас для списку моделей авто
class CarTaskDetailView(ListView):
    model = models.Car
    context_object_name = 'cars'
    template_name = 'tasks/task_auto.html'
    
    


# Оголошення класу дії View для зміни статусу задачі на "done"
# UserOwnerMixin — перевіряє, що користувач є власником задачі
# LoginRequiredMixin вимагає вхід
class TaskCompleteView(LoginRequiredMixin, UserOwnerMixin, View):
    # Обробник POST-запиту (кнопка/форма завершити)
    def post(self, request, *args, **kwargs):
        # Отримуємо об'єкт задачі (get_object - знаходится нижче)
        task = self.get_object()
        # Проставляємо новий статус - "done"
        task.status = "done"
        # Зберігаємо зміни у БД
        task.save()
        # Робимо редирект назад на список задач (через reverse_lazy)
        return HttpResponseRedirect(reverse_lazy("tasks:task-list"))
    
    # Сервісний метод: дістаємо задачу за первиним ключем з URL
    def get_object(self):
        # З дікт-словника kwargs беремо параметр 'pk', переданий у маршуті
        task_id = self.kwargs.get('pk')
        # Шукаємо задачу; якщо не знайдена - підніме 404
        return get_object_or_404(models.Task, pk=task_id)
    



# Клас для редагувати завдання
class TaskUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    model = models.Task
    form_class = TaskForm
    template_name = "tasks/task_update_form.html"
    success_url = reverse_lazy("tasks:task-list")

# Клас для видалення завдання
class TaskDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = models.Task
    form_class = TaskForm
    template_name = "tasks/task_delete_confirmation.html"
    success_url = reverse_lazy("tasks:task-list")


# Клас для редагувати резюме
class TaskUpdateResume(LoginRequiredMixin, ResumeOwnerMixin, UpdateView):
    model = models.Resume
    form_class = TaskFormResume
    template_name = "tasks/task_update_resume.html"
    success_url = reverse_lazy("tasks:task-list")

# Клас для видалення Резюме
class TaskDeleteResume(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = models.Resume
    form_class = TaskFormResume
    template_name = "tasks/task_delete_resume.html"
    success_url = reverse_lazy("tasks:task-list")



# Оголошення класу CreateView для створення нового резюме
class ResumeView(CreateView):
    model = models.Resume
    form_class = ResumeForm
    template_name = "tasks/task_resume.html"
    success_url = reverse_lazy("tasks:task-list")

    # Якщо форма валідна то викликається цей метод
    def form_valid(self, form):
        # Перед збереженням прив'язуємо резюме до поточного користувача
        form.instance.user = self.request.user  
        # Викликаємо реалізацію батьківського класу (створення + редирект)
        return super().form_valid(form)




# Оголошення простого View, який обробляє POST для зміни статусу резюме
class ResumeApproveView(View):
    # Обробник POST-запиту з первинним ключем резюме
    def post(self, request, pk):
        # Отримуємо об'єкт резюме за pk; якщо не знайдено - підніме DoesNotExist
        resume = models.Resume.objects.get(pk=pk)
        # Міняємо статус на "accepted"
        resume.status = "accepted"
        # Зберігаємо зімни в БД
        resume.save()
        # Редиректимо на сторінку зі списком прийнятих резюме
        return redirect('tasks:worker-task-detail')
    



# Клас для відхилення або прийняття резюме 
class ResumeRejectView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Resume
    template_name = "tasks/resume_delete.html"
    # Редирект після успішного видалення
    success_url = reverse_lazy("tasks:new-resume")

    # Метод перевірка прав доступу для UserPassesTestMixin
    def test_func(self):
        # Дозволити доступ тільки користувачу з роллю "admin"
        return(self.request.user.role == "admin")

 

# Клас для додавання автомобілля 
class CarView(WorkerOwnerMixin, CreateView):
    model = models.Car
    form_class = CarForm
    template_name = "tasks/add_auto.html"
    success_url = reverse_lazy("tasks:task-list")

    # Викликається якщо форма валідна 
    def form_valid(self, form):
        # Прив'язуємо створюваний автомобіль до поточного користувача як власника
        form.instance.owner = self.request.user 
        # Викликаємо бітьківську реалізацію: зберегти + редирект
        return super().form_valid(form)
    


