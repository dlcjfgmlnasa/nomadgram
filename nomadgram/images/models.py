from django.db import models
from nomadgram.users import models as user_models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True) # 데이터가 처음으로 생성될때 마다 자동으로 날짜 추가
    update_at = models.DateTimeField(auto_now=True) # 모델이 저장될때 마다 자동으로 새로고침을 실시

    class Meta:
        # 모델을 구성하는데 사용하는 클래스
        # 이건 모델이 아니고 abstract 모델이라는 것을 설명
        # 모델 메타 데이터는 필드가 아닌것이다 # 필드가 아닌 모든것 이다??
        abstract = True # abstract True 라고 입력하면 이모델은 abstract base model 이 되는 것이다
                        # abstract base model 은 데이터베이스를 생성하기 위해 사용되지 않는다 
                        # 대신 다른모델들을 위한 base로 사용됨 -> 필드들이 추가


@python_2_unicode_compatible
class Image(TimeStampedModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True) # ForeignKey()

    # 이미지 오브젝트(id:1)를 좋아요한 리스트를 어떻게 알 수 있을까??
    # => 모든 댓글들을 살펴보고 이미지 ID 1이 있다면 해당 댓글은 이미지 1을 위해서 생성되었다고 할수 있다
    # => 이것을 비효율적 , 모든 댓글을 다 찾아야되기 때문에
    # 장고는 이 작업을 수행해 준다 => set!!
    # image_set = {LOOK IN ALL THE COMMENTS FOR THE ONES THAT HAVE 'IMAGE' = THIS IMAGE ID} 이런 쿼리문을 사용한다고 생각하면 됨
    # foreignkey를 이용하면 이렇게 숨겨진 필드를 이용할 수 있다

    # string representation
    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)


@python_2_unicode_compatible
class Comment(TimeStampedModel):
    message = models.TextField()    # 유저의 경우와 달리, 이전에 생성된 데이터가 없기 때문에 디폴트 값 (null 같은) 지정이 필요없다
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='comments') # 추가적으로 이름을 바꾸는 방법


@python_2_unicode_compatible
class Like(TimeStampedModel):
    """ Like model """
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='likes')


    def __str__(self):
        return 'User : {} - Image Caption : {}'.format(self.creator.username, self.image.caption)

# model relationships
"""
You are trying to add a non-nullable field 'creator' to comment without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py

 이런 버그가 발생 => 이말의 뜻은 null=true 값이 필요하다는 의미
"""

"""
HTTP - hypertext transfer protocol
인터넷이 서로 서로 커뮤니케이션 하는 방법
디바이스-서버, 클라이언트-서버 거의 모든 것들이 http를 통과한다
아래의 내용이 표준이고 이것을 무조건 따라야하는것을 아니나 따르는것이 좋다

Client
Server

Requests
Responses

Requests - 
Consume a resource
Create a resource
Update a resource
Delete a resource

Headers: Method (액션 - 어떤행동을 하는지)
GET - Consume a resource
POST - Create a resource
PUT - Update a resource
DELETE - Delete a resource

Header : 
    (GET host: google.com)
body:

Header :

Body :
    HTML

Header : 
    (POST host: google.com)
body:
    (username:'nico', password: 'kbob')

login(request.body['username'], requset.body['password'])

Header : 
    (POST host: google.com)
body:
    (username:'nico', password: 'kbob')
update(request.body['username'], requset.body['password'])

Header : 
    (DELETE host: google.com)
body:
    (username:'nico', password: 'kbob')
update(request.body['username'], requset.body['password'])


------------------------------------------------------------------
장고앱은 models, views, urls로 작동한다
models : 이전에 작업한 데이터
views : function - 유저삭제, 로그인 유저, 이미지 업로드와 같은

Client: google.com

Server: GET google.com/user => (look) => URL => View() => 
"""
"""
REST API
/getAllDogs
/scheduleWalkOneThePark
/getDowOwner
/getAllDogsByOwner
api를 디자인할 때는 명사를 집중해야된다
NOUNS ARE GOOD -> 명사는 좋아요
VERBS ARE BAD -> 동사는 나빠요
REST API를 만들때 동사는 제외하는것이 좋다

동사는 CRUD 액션에서 발생한다
CRUD - (Create, Read, Update, Delete)
Create - POST
Read - GET
Update - PUT
DELETE - DELETE

우리가 모든 강아지를 불러모으고 싶다
=> getAllDogs() Fuck!! 절대 이렇게 하지 마라
아래와 같이 해라
GET -> /dogs
POST -> /dogs
UPDATE -> /dogs
DELETE -> /dogs

이렇게 dogs를 collection 취급받고 있다
/dogs
GET => /dogs/kung
POST => /dogs/kung (error)
PUT => /dogs/kung (if Kung exists update, not error)
DELTE => /dogs/kung

GET => /dogs/search?color=brown 강아지중 갈색강아지를 불러온다


GET /owners/nicolas/dogs -> List of all the dogs that Nicolas has.
POST /onwers/nicolas/dogs -> Create a dogs for Nicolas
PUT /onwers/nicolas/dogs -> Update all of Nicolas' dogs
DELETE /onwers/nicolas/dogs -> Bye bye

GET /owners/nicolas/dogs/search?color=brown

다른 디바이스에 연결하고 싶을때
아래와 같이하면 명확하고 좋다 
/v1/dogs/search?color=brown
/v2/dogs/search?color=brown

API는 이해하기 쉽고, 보자마자 이해할 수 있어야 된다
"""