from rest_framework import serializers
from . import models
"""
시리언라이즈(serializers) 
api는 json과 일을 한다 api에서 json을 얻는다 프론트엔드에서 json을 요구한다 
serializer는 파이썬 오브젝트를 제이슨 오브젝트로 변환하는 작업을 한다 또한 제이슨 오브젝트를 파이썬 오브젝트로 변환하는 작업도 같이한다 
즉 파이썬은 json으로 변환시키는 작업을 한다고 생각하면 편할듯하다 
    
# 시리얼라이즈 => 장고/파이썬 월드와 자바스크립트 월드를 연결하는 다리
              => 파이썬 => 시리얼라이즈 => 자바스크립트 오브젝트
"""

class CommentSerializers(serializers.ModelSerializer):
    # image = ImageSerializers()  # nested serializer 
    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializers(serializers.ModelSerializer):
    # image = ImageSerializers()  # 이미지에 대한 정보 더 얻어와서 이미지를 시리얼라이즈하고 있다 !! 주의 변수이름은 모델의 변수이름이랑 같아야한다
    class Meta:
        model = models.Like
        fields = '__all__'  
            # 우리는 모든 필드를 가져올껀데
            # 필드는 생성자, 그리고 이미지가 있지 둘다 들고올꺼야
            # 이때 어떤 특정 필드(이미지)는 foreign key가 아니라 이미지 시리얼라이저라고 작성하는 것

    """
    [{
        "id": 1,
        "image": {
            "id": 1,
            "create_at": "2018-06-15T14:21:26.293879+09:00",
            "update_at": "2018-06-15T14:21:26.293879+09:00",
            "file": "/media/jekyll-logo.png",
            "location": "부산",
            "caption": "블라블라블라",
            "creator": 2
        },
        "create_at": "2018-06-18T11:28:30.357558+09:00",
        "update_at": "2018-06-18T11:28:30.357558+09:00",
        "creator": 2
    }]
    """

class ImageSerializers(serializers.ModelSerializer):
    # 이미지 시리얼라이저에서 image set를 사용할 수는 없음
    comments = CommentSerializers(many=True) # 이런식으로 하면 id가 아니라 상세한 내용을 불러올수 있다
    likes = LikeSerializers(many=True)

    # 이렇게 서로 연결된 오브젝트들을 불러올수있다

    class Meta:
        # Meta 클래스는 extra 클래스다
        # 설정하는 클래스
        model = models.Image
        # fields = '__all__'  # 여기서 모든 필드를 불러오고는 있지만 사실은 set field(hidden filed)는 불러오지 않는다 
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',   # 이렇게 직접적으로 지정해주면 보인다!!
            'likes',      # 여기서 id말고 데이터를 보고싶으면 nested serializer를 사용하면 된다
        )

    # 그래서 정리하자면
    # 모델 A가 모델 B를 가리지고 있을때 모델 B는 set을 갖게되는데, 이는 모델 B를 가리키고있는 모든 모델에 대한 세트가 되는것이다
    """
        {
        "id": 1,
        "file": "/media/jekyll-logo.png",
        "location": "부산",
        "caption": "블라블라블라",
        "comment_set": [
            {
                "id": 1,
                "create_at": "2018-06-15T14:21:30.036894+09:00",
                "update_at": "2018-06-15T14:21:30.036894+09:00",
                "message": "123123123123123",
                "creator": 2,
                "image": 1
            },
            {
                "id": 2,
                "create_at": "2018-06-18T16:05:36.396588+09:00",
                "update_at": "2018-06-18T16:05:36.396588+09:00",
                "message": "123123",
                "creator": 2,
                "image": 1
            }
        ],
        "like_set": [
            {
                "id": 1,
                "create_at": "2018-06-18T11:28:30.357558+09:00",
                "update_at": "2018-06-18T11:28:30.357558+09:00",
                "creator": 2,
                "image": 1
            }
        ]},
    """