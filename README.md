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

5. 가상환경 활성화
``` bash
source venv/Scripts/activate
```


6. 가상환경 비활성화
``` bash
deactivate
```

7. 가상환경 내부에 django 설치
```bash
pip insttall django
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

11. urls.py 
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]

```
12. views.py
```python
def index(request):
    return render(request, 'index.html')
```

13. templates 폴더 생성