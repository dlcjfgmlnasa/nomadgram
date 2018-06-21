from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.
class ListAllImage(APIView):
    # APIView는 아래와 같이 작동
    # 우리가 사용한 http request에 따라 각가 다른 function을 사용할 예정

    def get(self, request, format=None):
        # requset : 클라이언트에게서 오브젝트를 요청하는 것
        all_images = models.Image.objects.all() # 모델 안에 있는 모든 오브젝트 종류의 이미즈를 가져와라고 말한것
        # 이제 이거를 json으로 변환해줘야 된다
        # request를 접근하는 방식은 view functions의 두번째 attribute를 확인하면 됨

        # serializer = serializers.ImageSerializers(all_images)
        # 이미지 시리얼라이저는 단수야 왜나면 이건 1개의 이미지를 시리얼라이징하니까
        # 그래서 한개가 아니라 여러개를 시리얼라이징할거라고 알려줘야한다
        serializer = serializers.ImageSerializers(all_images, many=True)
        return Response(data=serializer.data)


class ListAllComments(APIView):
    def get(self, request, format=None):
        # 우리가 function 단위에서 진행하는 http request는 브라우저가 우리에게 보내는 http request랑은 다르다
        # view를 만들때 마다 장고는 request object를 첫번째 argument안에 넣을것이다
        # "페이지가 요청될때마다 장고는 해당 요청에 대한 메타데이터를 포함한 http request를 생성한다 "
        # 그리고 우리는 메타데이터가 필요하다 해당 데이터는 여러가지 정보를 우리에게 줄것임
        # 예) HttpRequest.schema : http인지 https인지 확인할수 있다 print(request.schema)
        # 이렇게 장고에서는 많은 속성들을 미리 만들어놓았다
        # 수행하는 방법은 request를 통해 여러개의 미들웨어를 실행해서 가능하다 
        # HttpRequest.POST : 사진을 업로드하기위해 
        # HttpRequest.user : 승인-미들웨어에서 오는건데, 우리가 사용할 수 있는 유저 오브젝트를 제공
        # 아래와 같은 방법으로 요청받은 유저가 승인이 되었는지 아닌지를 체크할 수 있다
        # if request.user.is_authenticated:
        # ... # Do something for logged-in users.
        #    else:
        # ... # Do something for anonymous users.
        # https://docs.djangoproject.com/en/2.0/ref/request-response/
        # 위의 주소에 나와있는 request들은 이해할 필요성이 있고 많은 것들이 request를 통해서 관리가 된다 
        # request.user.following
        user_id = request.user.id
        print(request.session)
        all_comments = models.Comment.objects.filter(creator=user_id)
        serializer = serializers.CommentSerializers(all_comments, many=True)
        return Response(data=serializer.data)


class ListAllLike(APIView):
    def get(self, request, format=None):
        all_likes = models.Like.objects.all()
        serializer = serializers.LikeSerializers(all_likes, many=True)
        return Response(data=serializer.data)

"""
장고는 어떻게 Query를 만드는가??
query 뜻은 장고의 DB를 어떻게 검색하느냐에 대한 것이다
all_comment = models.Liked.objects.all() 과 같은 모델을 생성할 때 그 때 마다 DB와 소통하는 방법을 디폴트로 얻는다.
데이터 베이스랑 직접적으로 소통할 필요없이. 파이썬이 번역을 해줄 꺼임
따라서 우리가 해야될 일은 DB에 있는 object들을 부르면 된다 -> 이를 query 생성이라고 한다
all() -> 모든 데이터를 불러온다
filter() -> 일부데이터를 불러온다 
ex) model.Comment.object.filter(id=1)
    model.Comment.object.filter(creator=2)
이런식으로 sql 코드 없이도 db를 검색할 수 있음
너가 모델을 생성할때마다, 장고는 디폴트로 이를 찾는 방법들을 제시해줄 것임

"""