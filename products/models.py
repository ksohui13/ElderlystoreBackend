from django.db import models
from mainshop.models import TimeStampModel

#상품
class Product(TimeStampModel):
    product_id = models.AutoField(primary_key=True)                                        #상품 번호
    main_category= models.ForeignKey('MainCategory', on_delete=models.SET_NULL, null=True) #어떤 카테고리인지
    product_name = models.TextField()                               #상품명
    product_des = models.TextField()                                #상품 설명
    detail_description = models.TextField()                         #상품상세설명
    ingredient = models.TextField()                                 #원재료
    price_origin = models.IntegerField(default=0)                    #정가
    price_sale = models.IntegerField(default=0)                      #노인 복지 스토어 가격
    discount = models.IntegerField(default=0)                      #정가 - 복지스토어 가격 (할인가격)
    product_sotck = models.IntegerField(default=0)                   #재고
    #product_date = models.DateTimeField(auto_now=True)      #등록 날짜 : 상속받음
    #product_ordering_num = models.IntegerField()            #상품주문수량 > quantity로 변경해야하는지?
    quantity = models.IntegerField(default=0)               #주문되면 주문된 수량만큼 상승

    class Meta:
        db_table = 'products'
        
#카테고리 : 푸드, 리빙, 교육/문화
class MainCategory(TimeStampModel):
    main_category = models.CharField(max_length=50)

    class Meta:
        db_table = 'main_categories'

#서브 카테고리 : 유제품, 가공식품,...,/의류, 가전제품,.../연극, 콘서트,...등
#현재는 계획x
class SubCategory(TimeStampModel):
    main_category = models.ForeignKey('MainCategory', on_delete=models.SET_NULL, null=True)
    sub_category = models.CharField(max_length=50)

    class Meta:
        db_table = 'sub_categories'

#상품 이미지
class ProductImg(TimeStampModel):
    image_url    = models.URLField()                                        #파일 url
    is_thumbnail = models.BooleanField(default=False)                       #썸네일 여부
    product      = models.ForeignKey('Product', on_delete=models.CASCADE)   #등록할 제품

    class Meta:
        db_table = 'product_images'

    class Meta:
        db_table = 'product_img'
