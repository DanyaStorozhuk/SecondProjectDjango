from django.urls import path
from  tasks import views

app_name = "tasks"

urlpatterns = [
    # перенаправляє користувача на список (головна сторінка де багато формочок)
    path("task/", views.TaskListView.as_view(), name="task-list"),

    # перенаправляє на перегляд задачі
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),

    # перенаправляє на редагування завдання 
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),

    # перенаправляє на видалення завдання
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),

    # перенаправляє на створення нової задачі
    path("task-create", views.TaskCreateView.as_view(), name="task-create"),

    # початкова сторінка яка автоматично з'являється (щоб зайти або залогінитися)
    path("", views.HomeView.as_view(), name="task-home"),

    # перенаправляє на регестрацію
    path("register/", views.register, name='register'),

    # перенаправляє на логін (щоб вже увійти в створений профіль)
    path("login/", views.login , name='login'),

    # перенаправляє на створення коментаря
    path("task-comment/", views.CommentCreateView.as_view(), name="task-comment"),

    # перенаправляє на список підтверджених резюме 
    path("worker-task-detail", views.WorkerTaskDetailView.as_view(), name="worker-task-detail"),

    # перенаправляє на список коментарів
    path("task_view_list", views.CommentsListViews.as_view(), name="task_view_list"),

    # перенаправляє на список завдань
    path("task-task", views.TaskListTask.as_view(), name="task-task"),

    #  перенаправляє на оголошення класу, статусу задачі на "done"
    path("<int:pk>/complete/", views.TaskCompleteView.as_view(), name="task-complete"),

    # перенаправляє на список створених моделей авто
    path("task-auto", views.CarTaskDetailView.as_view(), name="task-auto"),

    # перенаправляє на створення нового резюме
    path("task-resume", views.ResumeView.as_view(), name="task-resume"),

    # Це перенаправлення на прийнятя та відхилення резюме
    path("resume/<int:pk>/approve/", views.ResumeApproveView.as_view(), name="resume-approve"),
    path("resume/<int:pk>/reject/", views.ResumeRejectView.as_view(), name="resume-reject"),


    # перенаправляє на список резюме
    path("new-resume", views.ResumeListView.as_view(), name="new-resume"),

    # перенаправляє на додавання авто
    path("add-auto", views.CarView.as_view(), name="add-auto"),

    # перенаправляє на редагувати резюме
    path("<int:pk>/update/resume", views.TaskUpdateResume.as_view(), name="task-update-resume"),
    path("<int:pk>/delete/resume", views.TaskDeleteResume.as_view(), name="task-delete-resume"),
    path("<int:pk>/resume", views.TaskDetailViewResume.as_view(), name="task-detail-resume"),

]


