"""
URL configuration for task_treking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# реєструємо кастомний handler для 403
handler403 = 'tasks.views.custom_403_view'

urlpatterns = [
    # Стандартний шлях до адмінки Django
    path('admin/', admin.site.urls),

    # Підключаємо маршути з додатку tasks
    # '' - означає головну сторінку
    # include(('tasks.urls', 'tasks')) - підключаємо файл urls.py з tasks
    # namespace = 'tasks' - задаємо простір імен для зручності у шаблонах та reverse()
    path('', include(('tasks.urls', 'tasks'), namespace='tasks')), 
]

# Якщо ми у режимі розробки (DEBUG=True), підключаємо статичні медіафайли
# MEDIA_URL – URL, за яким доступні медіафайли
# MEDIA_ROOT – папка на диску, де вони фізично зберігаються
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
