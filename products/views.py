from django.shortcuts import render
from products.models import Products
from django.db.models import Sum, Q
from django.views import View
from django.http import JsonResponse

class ProductView(View):
    def get(self, request):
        try:
            main_category = request.GET.get('main_category', None)
            best_seller = request.GET.get('best_seller', None)
            sub_category = request.GET.get('sub_category', None)
            keyword = request.GET.get('keyword', None)
            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 100))

            if main_category and main_category != None:
                products = Products.objects.filter(Q(sub_category__main_category__id = main_category))

            if best_seller and best_seller != None:
                quantity = int(best_seller)
                products = Products.objects.annotate(quantity_sum = Sum('orderitem__quantity')).order_by('-quantity_sum')[:quantity]

            if sub_category and sub_category != None:
               products = Products.objects.filter(Q(sub_category__id = sub_category))

            if keyword and keyword != None:
                products = Products.objects.filter(Q(name__icontains = keyword) | Q(collection__name__icontains = keyword))

            if limit > 100:
                return JsonResponse({'message' : 'TOO_MUCH_LIMIT'}, status = 400) 
            
            limit = offset + limit

            if (main_category or best_seller or sub_category or keyword) == None:
                products = Products.objects.all()[offset:limit]

            result = [{
                'product_id'           : products.product_id,
                'main_category_id'     : products.main_category_id,
                'product_name'         : products.product_name,
                'price_origin'         : products.price_origin,
                'price_sale'           : products.price_sale,
                'discount'             : products.discount,
                'product_sotck'        : products.product_sotck,
                'product_des'          : products.product_des,
                'product_date'         : products.product_date,
                'product_ordering_num' : products.product_ordering_num, 

            } for products in products]
            return JsonResponse({'result':result}, status = 200)
        
        except Products.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status = 404)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)

class ProductDetail(View):
    def get(self, request, product_id):
        try:
            products = Products.objects.get(id=product_id)
            result = {
                'product_id'           : products.product_id,
                'main_category_id'     : products.main_category_id,
                'product_name'         : products.product_name,
                'price_origin'         : products.price_origin,
                'price_sale'           : products.price_sale,
                'discount'             : products.discount,
                'product_sotck'        : products.product_sotck,
                'product_des'          : products.product_des,
                'product_date'         : products.product_date,
                'product_ordering_num' : products.product_ordering_num, 
            }
            
            return JsonResponse({'result' : result}, status = 200)
        
        except Products.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status = 404)
         
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)