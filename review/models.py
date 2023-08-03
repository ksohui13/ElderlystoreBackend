from django.db import models
from mainshop.models import TimeStampModel
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User

#리뷰
class ProdcutReview(TimeStampModel):
    review_id = models.AutoField(primary_key=True)                  #리뷰 번호
    #product = models.ForeignKey('Product', on_delete=models.CASCADE) #리뷰가 적힐 제품 : 상속
    review_content = models.TextField()                              #리뷰 내용
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)  #닉네임
    review_star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) #리뷰 별점 0~5점
    #review_date = models.DateTimeField(auto_now=True)                #리뷰 작성 날짜

    class Meta:
        db_table = 'product_review'