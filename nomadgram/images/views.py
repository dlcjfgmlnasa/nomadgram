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

        # serializer = serializers.ImageSerializers(all_images)
        # 이미지 시리얼라이저는 단수야 왜나면 이건 1개의 이미지를 시리얼라이징하니까
        # 그래서 한개가 아니라 여러개를 시리얼라이징할거라고 알려줘야한다
        serializer = serializers.ImageSerializers(all_images, many=True)
        return Response(data=serializer.data)


class ListAllComments(APIView):
    def get(self, request, format=None):
        all_comments = models.Comment.objects.all()
        serializer = serializers.CommentSerializers(all_comments, many=True)
        return Response(data=serializer.data)


class ListAllLike(APIView):
    def get(self, request, format=None):
        all_likes = models.Like.objects.all()
        serializer = serializers.LikeSerializers(all_likes, many=True)
        return Response(data=serializer.data)