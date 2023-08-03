from rest_framework import viewsets
from products.models import Product
from products.serializer import ProductSerializer
from django.views import View
from django.http import JsonResponse
from django.db.models import Sum, Q
from products.models import Product

#상품추가
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #get
    def get_queryset(self):
        qs = super().get_queryset() 

        search_name = self.request.query_params.get('name',) 
        if search_name:
            qs = qs.filter(name__icontains=search_name) #대소문자 구분없이 검색
        return qs

class ProductView(View):
    def get(self, request):
        try:
            main_category = request.GET.get('main-category', None)
            best_seller   = request.GET.get('best-seller', None)
            sub_category  = request.GET.get('sub-category', None)
            keyword       = request.GET.get('keyword', None)
            offset        = int(request.GET.get('offset', 0))
            limit         = int(request.GET.get('limit', 100))
            
            if main_category and main_category != None:
                products = Product.objects.filter(Q(sub_category__main_category__id=main_category))
            
            if best_seller and best_seller != None:
                quantity = int(best_seller)
                products = Product.objects.annotate(quantity_sum=Sum('orderitem__quantity')).order_by('-quantity_sum')[:quantity]
            
            if sub_category and sub_category != None:
                products = Product.objects.filter(Q(sub_category__id=sub_category))

            if keyword and keyword != None:
                products = Product.objects.filter(Q(name__icontains=keyword)|Q(collection__name__icontains=keyword))

            if limit > 100:
                return JsonResponse({'message' : 'TOO_MUCH_LIMIT'}, status=400)

            limit  = offset + limit

            if (main_category or best_seller or sub_category or keyword) == None:
                products = Product.objects.all()[offset:limit]

            result = [{
                    'id'          : product.id,
                    'product_name': product.product_name,
                    'main_category': product.main_category.main_category,
                    'price_origin': product.price_origin,
                    'price_sale'  : product.price_sale,
                    'discount'    : product.discount,
                    'product_des' : product.product_des,
                    'image'       : product.productimage_set.get(is_thumbnail=True).image_url
                } for product in products]
            return JsonResponse({'result': result}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status=404)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            images  = [product_image.image_url for product_image in product.productimage_set.order_by('-is_thumbnail').all()]
            scent   = [scent.description for scent in product.scent_set.all()]
            result = {
                    'id'                 : product.id,
                    'product_id'         : product.product_id,
                    'main_category'      : product.main_category,
                    'price_origin'       : product.price_origin,
                    'price_sale'         : product.price_sale,
                    'discount'           : product.discount,
                    'quantity'           : product.quantity,
                    'detail_description' : product.detail_description,
                    'ingredient'         : product.ingredient,
                    'image'              : images
                }
            return JsonResponse({'result': result}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status=404)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)