from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True) # 데이터가 처음으로 생성될때 마다 자동으로 날짜 추가
    update_at = models.DateTimeField(auto_now=True) # 모델이 저장될때 마다 자동으로 새로고침을 실시

    class Meta:
        # 이건 모델이 아니고 abstract 모델이라는 것을 설명
        # 모델 메타 데이터는 필드가 아닌것이다 # 필드가 아닌 모든것 이다??
        abstract = True # abstract True 라고 입력하면 이모델은 abstract base model 이 되는 것이다
                        # abstract base model 은 데이터베이스를 생성하기 위해 사용되지 않는다 
                        # 대신 다른모델들을 위한 base로 사용됨 -> 필드들이 추가

class Image(TimeStampedModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()


class Comment(TimeStampedModel):
    message = models.TextField()    # 유저의 경우와 달리, 이전에 생성된 데이터가 없기 때문에 디폴트 값 (null 같은) 지정이 필요없다
    

