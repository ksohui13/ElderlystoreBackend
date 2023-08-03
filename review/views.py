from django.shortcuts import render
from rest_framework import viewsets
from review.models import ProdcutReview
from review.serializer import ReviewSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#리뷰 뷰셋
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ProdcutReview.objects.all()
    serializer_class = ReviewSerializer

#리뷰리스트 : 읽고 생성하기
class ReviewList(APIView):
    def get(self, request):
        qs = ProdcutReview.objects.all()
        serializer = ReviewSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, many=False) # 리스트로 여러개 작성할거면 many=True로 하면 됨. 리뷰에서는 2개 동시에 다는 일 없어서 False지만 상품 구매일때 여러개 살때는 True로 해도ㅗ 됨
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#리뷰 상세 가져오기, 수정, 삭제
class ReviewDetail(APIView):
    # 목록 불러오기
    def get(self, request, pk): # pk는 primary key
        qs = ProdcutReview.objects.get(id=pk)
        serializer = ReviewSerializer(qs, many=False)
        return Response(serializer.data)

    def patch(self,request,pk):
        qs = ProdcutReview.objects.get(id=pk)
        serializer = ReviewSerializer(qs, data=request.data, partial=True) # 모델속성 다 입력안해도 수정할 수 있게 주려면 partial
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = ProdcutReview.objects.get(id=pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)