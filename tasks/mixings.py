from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin





# Власна міксина для перевірки чи користувач є власником об'єкта
class UserOwnerMixin(object):
    # Метод dispatch обробляє запити GET, POST та інші, перед передачою їх у view
    def dispatch(self, request, *args, **kwargs):
        # Отримуємо об'єкт (наприклад задачу чи резюме), який потрібно перевірити
        isinstance = self.get_object()
        # Якщо користувач, який не є автором (creator) об'єкта, то йому доступ заборонено
        if isinstance.creator != self.request.user:
            # Викликаємо помилку PermissionDenied (покаже сторінку 403)
            raise PermissionDenied
        # Якщо умова виконана - виконуємо стандартний метод dispatch (дозволяємо доступ)
        return super().dispatch(request, *args, **kwargs)




# Власна міксина яка перевіряє чи користувач є власником резюме
class ResumeOwnerMixin(UserPassesTestMixin):
    # Метод test_func використовується для перевірки доступу
    def test_func(self):
        # Отримуємо об'єкт (резюме), з яким працює користувач
        obj = self.get_object()
        # Повертаємо True, якщо користувач, який зробив запит, є власником резюме
        return obj.user == self.request.user
    



# Створюємо міксину для перевірки чи користувач має роль "admin"
class WorkerOwnerMixin(UserPassesTestMixin):
    # Метод test_func перевіряє доступ
    def test_func(self):
        # Якщо у користувача роль 'admin', то доступ дозволено
        return self.request.user.role == 'admin'