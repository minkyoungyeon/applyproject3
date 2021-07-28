from django.db import models
from  django.contrib.auth.models import User #★장고에서 기본 제공하는 User모델 사용하겠다.
# Create your models here.

#★모델 생성
class Article(models.Model): #★모델 선언
    author = models.ForeignKey(User,on_delete = models.CASCADE) #★지원자=유저 모델 참조. CASCADE 방식을 따름.
    title = models.CharField(max_length=100) #★지원 글 제목=문자열 필드 사용. 제한 길이 100자
    content = models.TextField() #★지원 내용=문자열 필드 사용. 길이 제한 없음.
    create_at = models.DateTimeField(auto_now_add=True) #★지원날짜=날짜필드 사용. 현재 시간 반영.
    

    #★__str 함수는 관리자 페이지에서 데이터베이스를 확인할 때 함수에서 반환하는 속성을 기준으로 레코드를 확인할 수 있또록 한다.
    def __str__(self): 
        return self.title
    class Meta(): #메타데이터 생성, 게시글 이라는 이름으로 저장
        db_table = '게시글'
        verbose_name ='게시글'
        verbose_name_plural = '게시글'
