from django.shortcuts import render
from products.models import Products, ProductImage
from django.db.models import Sum, Q
from django.views import View
from django.http import JsonResponse

class ProductView(View):
    def get(self, request):
        try:
            main_category = request.GET.get('main_category', None)
            best_seller = request.GET.get('best_seller', None)
            #sub_category = request.GET.get('sub_category', None)
            keyword = request.GET.get('keyword', None)
            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 100))
            product_images = request.GET.get('product_images', None)

            if main_category and main_category != None:
                products = Products.objects.filter(Q(sub_category__main_category__id = main_category))

            if best_seller and best_seller != None:
                quantity = int(best_seller)
                products = Products.objects.annotate(quantity_sum = Sum('orderitem__quantity')).order_by('-quantity_sum')[:quantity]

            if keyword and keyword != None:
                products = Products.objects.filter(Q(name__icontains = keyword) | Q(collection__name__icontains = keyword))

            if limit > 100:
                return JsonResponse({'message' : 'TOO_MUCH_LIMIT'}, status = 400) 
            
            limit = offset + limit

            if (main_category or best_seller or sub_category or keyword) == None:
                products = Products.objects.all()[offset:limit]

            result = [{
                'product_id'           : products.product_id,
                'main_category'        : products.main_category,
                'product_name'         : products.product_name,
                'price_origin'         : products.price_origin,
                'price_sale'           : products.price_sale,
                'discount'             : products.discount,
                'product_sotck'        : products.product_sotck,
                'product_des'          : products.product_des,
                'product_image'        : product_images.image_url,
                'ingredient'           : products.ingredient,
                'quantity'             : products.quantity,

            } for products in products and product_images in products]
            return JsonResponse({'result':result}, status = 200)
        
        except Products.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status = 404)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)

class ProductDetail(View):
    def get(self, request, product_id):
        try:
            products = Products.objects.get(id=product_id)
            product_images = ProductImage.objects.get()
            result = {
                'product_id'           : products.product_id,
                'main_category'        : products.main_category,
                'product_name'         : products.product_name,
                'price_origin'         : products.price_origin,
                'price_sale'           : products.price_sale,
                'discount'             : products.discount,
                'product_sotck'        : products.product_sotck,
                'product_des'          : products.product_des,
                'product_image'        : product_images.image_url,
                'detail_description'   : products.detail_description,
                'ingredient'           : products.ingredient,
                'quantity'             : products.quantity,
            }
            
            return JsonResponse({'result' : result}, status = 200)
        
        except Products.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status = 404)
         
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)
