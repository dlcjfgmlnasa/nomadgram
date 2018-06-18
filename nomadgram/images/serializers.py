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

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        # Meta 클래스는 extra 클래스다
        # 설정하는 클래스
        model = models.Image
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'