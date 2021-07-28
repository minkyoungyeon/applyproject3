from django.shortcuts import render, redirect #★render, redirect 사용
from django.contrib.auth.models import User #★유저모델 사용
from django.contrib import auth #★관리자기능 사용하겠다
from .models import Article #★models.py에서 생성한 Article 모델을 불러와주세요~

# Create your views here.

def index(request): #★index 함수, 기본 메인 페이지
    contents = reversed(Article.objects.all()) #★content 변수에 Article 모델의 모든 것을 불러와라. index는 reverse함수를 통해 모델의 개별 데이터 url을 문자열로 반환한다.
    return render(request, 'index.html',{'contents': contents}) #★index.html을 불러오고 contents안에 있는 정보를 index.html로 전달
'''
models.py에서 Article 클래스를 import 해준다음
Article 클래스의 인스턴스들을 쿼리셋으로 받아 contents변수에 저장, 딕셔너리 형태로 return 해준다.

♡♡♡쿼리셋(QuerySet)이란?
데이버테이스에서 전달받은 테이블의 레코드 목록


♡♡♡쿼리셋 메소드
- all() : 모든 데이터를 queryset으로 반환
- filter(조건) : 조건식으로 데이터를 찾음
- exclude(조건) : 조건에 일치 하지 않는 데이터
- order_by(정렬필드) : 지정한 필드를 기준으로 오른차순정렬. 내림차순은 '-'를 붙여줌


쿼리셋 메소드는 아래와 같은 방식으로 사용가능
def index(request):
	posts = Post.objects.all()
	posts = Post.objects.filter(조건)	
	posts = Post.objects.exclude(조건)
	posts = Post.objects.order_by(정렬필드)
	return render(request, 'model.html', {'posts':posts})
    
    
필기-★View와 html의 관계! 참조
'''



def signup(request): #★회원가입 함수
    if request.method == 'POST': #★서버 요청방식이 POST 방식인 경우 새로운 유저를 만드는 절차를 밟는다.
        if request.POST['password'] == request.POST['re_password']: #★입력한 비밀번호와 '비밀번호 확인'에 입력한 비밀번호가 일치한 경우 
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password']) #★User모델의 객체에 user를 생성한다. 즉 회원을 추가한다. user의 이름은 POST 방식으로 받아온 username으로 하고, 비밀번호는 POST 방식으로 받아온 비밀번호로 정한다.
            auth.login(request, user) #★회원가입된 user정보를 요청
            return redirect('index') #★회원가입 성공시 index 페이지로 넘어감
    return render(request,'signup.html') #★signup으로 GET 요청이 왔을 때 회원가입 화면을 띄워준다.

def login(request): #★로그인 함수
    if request.method == 'POST':  #★서버 요청방식이 POST 방식인 경우
        username = request.POST['username']  #★id요청
        password = request.POST['password'] #★비밀번호 요청
        user = auth.authenticate(request, username=username, password=password) #★입력한 id와 비밀번호가 회원정보에 저장된 id와 비밀번호가 일치한다면
        if user is not None: #★해당 user 객체가 존재한다면
            auth.login(request, user) #★로그인한다.
            return redirect('index') #★index페이지 띄워준다.
        else : #★불일치한다면
            return render(request, 'login.html', {'error' : '아이디나 비밀번호가 틀렸습니다.'}) #★아이디와 비밀번호가 틀렸다는 error메시지 띄우기
    else : #★로그인으로 GET 요청이 들어왔을 때 로그인 화면을 띄워준다.
        return render(request, 'login.html')

def logout(request): #★로그아웃 함수
    auth.logout(request) #★로그아웃 요청이 들어오면 로그인 페이지를 띄워주세요.
    return redirect('login')


def create(request): #★create.html을 띄우기 위한 함수
    return render(request, 'create.html')


def create_article(request): #★지원서 작성하는 함수
    article = Article()  #★빈 article 객체를 하나 생성한다.
    article.title = request.GET['title'] #★name속성의 값이 title인 input 태그에 입력된 값을 article 객체의 title에 저장한다.
    article.content = request.GET['content'] #★name속성 값이 content인 input 태그에 입력된 값을 article 객체의 content에 저장한다.
    article.author = request.user #★article 객체의 author(지원자)는 user정보를 가져온다.
    article.save() #★article객체 최종저장
    return redirect('index') #★글 다 쓰면 index페이지 띄워줘라.

def delete_article(request): #★지원서 삭제 함수
    article_id = request.GET['post_id']  #★GET 요청으로 들어온 id 파라미터를 article_id에 받음
    article = Article.objects.get(id = article_id) #★삭제할 레코드의 id 값을 전달
    article.delete() #★article객체를 지운다.
    return redirect('index') #★다 지우면 index 페이지를 띄워줘라.

def update(request): #★지원서 수정 (수정페이지)함수
    article_id = request.GET['post_id'] #★GET 요청으로 들어온 id 파라미터를 article_id에 받음
    article = Article.objects.get(id = article_id) #★수정할 레코드의 id 값을 전달
    return render(request, 'update.html', {'article':article}) #★기존에 작성한 내용과 함께 update.html을 띄워준다.


def update_article(request):#★지원서 수정 (수정한 거 반영하는) 함수
    article_id = request.GET['post_id']#★GET 요청으로 들어온 id 파라미터를 article_id에 받음
    title = request.GET['title'] #★title에 GET 방식으로 요청된 name 속성 값이 'title'인 input 태그 내의 값을 저장한다.
    content = request.GET['content'] #★content에 GET 방식으로 요청된 name 속성 값이 'content'인 input 태그 내의 값을 저장한다.
    article = Article.objects.get(id = article_id)#★수정할 레코드의 id 값을 전달
    article.title = title #★article 객체의 title에 위에서 정의한 title 넣기
    article.content = content #★article 객체의 content에 위에서 정의한 content 넣기
    article.save() #★최종 저장
    return redirect('index') #★index페이지를 띄워준다.
