from django.db import models
from core.models import TimeStampModel

class Product(TimeStampModel):
    #products
    #상품 번호
    product_id = models.IntegerField()
    #카테고리 식별 id
    main_category_id = models.CharField()
    # 상품명
    product_name = models.TextField()
    #상품 설명
    product_des = models.TextField()
    #정가
    price_origin = models.IntegerField()
    #노인 복지 스토어 가격
    price_sale = models.IntegerField()
    #정가 - 복지스토어 가격
    price_sale = models.IntegerField()
    #재고
    product_sotck = models.IntegerField()
    #등록 날짜
    product_date = models.DateTimeField(auto_now=True)
    #상품주문수량
    product_ordering_num = models.IntegerField()

    class Meta:
        db_table = 'products'

class ProductImg(TimeStampModel):
    #product_img
    #파일 이름
    origin_file_name = models.CharField()
    #상품 번호
    product_number = models.IntegerField()
    #상품이미지 파일번호
    file_number = models.IntegerField()
    #썸네일 이미지
    thumbnail = models.ImageField(upload_to='products/images', blank=False)
    #파일 크기
    file_size = models.IntegerField()
    #생성일
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'product_img'

class ProdcutReview(TimeStampModel):
    #product_review / 상품 번호 중복이라서 안 적음
    #리뷰번호
    review_number = models.IntegerField()
    #리뷰내용
    review_content = models.TextField()
    #닉네임
    nickname = models.CharField()
    #리뷰 별점
    review_star = models.IntegerField()
    #리뷰 작성 날짜
    review_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_review'

class ProductQna(TimeStampModel):
    #product_qna
    #문의 번호
    qna_number = models.IntegerField()
    #문의 댓글
    qna_question = models.TextField()
    #답변
    qna_answer = models.TextField()
    #문의 작성 날짜
    qna_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_qna'