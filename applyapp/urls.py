from django.urls import path
from . import views #★views.py랑 연결

urlpatterns = [
    path('', views.index, name = 'index'), #★기본으로 index페이지를 띄워라.
    path('login/', views.login, name = 'login'), #★
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout, name = 'logout'),
    path('create/',views.create, name = 'create'),
    path('create_article/', views.create_article, name = 'create_article'),
    path('delete_article/', views.delete_article, name = 'delete_article'),
    path('update/', views.update, name = 'update'),
    path('update_article/', views.update_article, name ='update_article'),
]

#★url을 통해 입력된 사용자의 요청을 view의 어떤 함수에 넘길지 설정해준다.
#★먼저 앱명.views파일을 import 해주고 path를 추가해준다.
#★path('url주소', '앱이름.views.함수명', 이름)의 형식으로 작성하며 들어가는 이름은 templates 변수로 사용할 수 있다.

'''
♧♧♧♧♧♧장고 페이지 만들기 순서♧♧♧♧♧♧
프로젝트 생성 -> app생성 -> settings.py에 app등록 -> templates 디렉토리와 html파일 생성 -> views.py에 함수 생성 -> urls.py에 template 등록

♣app을 추가했을 때
app생성 -> settings.py에 app등록 -> templates 디렉토리와 html파일 생성 -> views.py에 함수 생성 -> urls.py에 template 등록

 

♣view 또는 html파일을 새로 생성했을 때
templates 디렉토리와 html파일 생성 -> views.py에 함수 생성 -> urls.py에 template 등록
'''
