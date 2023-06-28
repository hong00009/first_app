# Django

1. 프로젝트 생성
``` bash
django-admin startproject <project name>
```

2. 프로젝트 폴더 이동
``` bash
cd <project name>
```

3. vscode 실행

4. 가상환경 설정
``` bash
python -m venv venv
```

5. 가상환경 활성화 - (venv) 표기됨
``` bash
source venv/Scripts/activate
```


6. 가상환경 비활성화
``` bash
deactivate
```

7. 가상환경 내부에 django 설치
```bash
pip install django
```

8. 서버 실행 확인 (종료: Ctrl+C)
``` bash
python manage.py runserver
```

9. 앱 생성
``` bash
django-admin startapp <app name>
```


10. 앱 등록
- `settings.py`의
`INSTALLED_APPS`에 등록

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    '<app name>',   # <<==여기
]
```

11. urls.py 
```python
from first_app import views  # <<== 여기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),  # <<== 여기
]

```
12. views.py
```python
# request 인자는 필수
def index(request):
    return render(request, 'index.html')
```

13. `<app name>` 폴더 안에 `templates` 폴더 생성

14. templates 폴더 안에 각종 html 파일 생성 및 작성
! (느낌표) + Tab (탭) 으로 기본양식 자동작성가능


## 추가 설명

1. migrate 하라고 경고뜰때가 있음 > 나중에 model 파트에서 다룰예정

2. `block content` 설정값을 최상단 폴더(templates)에 별도로 둘때는 path 추가설정
 `settings.py` 에서
```python
TEMPLATES = [
    {
       
        'DIRS': [],   # <== 여기
	....
    }]
```
이부분을
`'DIRS': [BASE_DIR / 'templates'] `

3. 자동완성 
`div.container` + `Tab`
```html
<div class-"container"></div>
```

`div#1`+`Tab`
```html
<div id="1"></div>
```


4. 블록
``` html
<!-- base.html -->
{% block content %}
{% endblock %}
```

```html
<!-- 1 -->
{% extends 'base.html' %}

<!-- 2 -->
{% block content %}
	...
	...
{% endblock %}
```
5. `<app name>/views.py`  에서 주요 기능 만들어 적용하는데
`urls.py` 에서 path 설정, `views.py`에서 기능설정, `~~.html` 만들기 순서로 작성함