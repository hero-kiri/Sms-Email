# RegisterDjango

Этот проект демонстрирует, как отправлять электронные письма с использованием Django.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone <repository_url>
    cd RegisterDjango
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Создайте файл `.env` в корне проекта и добавьте следующие переменные:
    ```
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_password
    ```

## Использование

1. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

2. Перейдите по адресу `http://127.0.0.1:8000/` в вашем браузере.

3. Заполните форму и нажмите "Отправить", чтобы отправить письмо.

## Код

### Загрузка переменных окружения 
`core/settings.py`
```settings.py
import os
import dotenv
from pathlib import Path

# Load environment variables
dotenv.load_dotenv()

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

### Отправка письма
`mainapp/utils.py`
```python
from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(subject, email, message):
    recipient_list = [email]
    from_email = 'hero.beka.kg@gmail.com'

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Письмо отправлено')
    except Exception as e:
        return HttpResponse(str(e))
```

### Представление
`mainapp/views.py`
```python
from django.shortcuts import render
from .utils import send_email

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_email(subject, email, message)
    return render(request, 'index.html')
```

### URL конфигурация
`mainapp/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### Шаблон
`templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Добро пожаловать на сайт</h1>
    <h2>Заполните данные</h2>
    <form method="post">
        {% csrf_token %}
        <input type="text" name="subject" placeholder="Заголовок">
        <input type="email" name="email" placeholder="Почта">
        <input type="text" name="message" placeholder="Сообщение">
        <input type="submit" value="Отправить">
    </form>
</body>
</html>
```

Теперь вы можете отправлять письма с помощью вашего Django приложения.