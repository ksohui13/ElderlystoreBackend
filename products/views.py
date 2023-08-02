from django.shortcuts import render
from products.models import Product
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
                products = Product.objects.filter(Q(sub_category__main_category__id = main_category))

            if best_seller and best_seller != None:
                quantity = int(best_seller)
                products = Product.objects.annotate(quantity_sum = Sum('orderitem__quantity')).order_by('-quantity_sum')[:quantity]

            if sub_category and sub_category != None:
               products = Product.objects.filter(Q(sub_category__id = sub_category))

            if keyword and keyword != None:
                products = Product.objects.filter(Q(name__icontains = keyword) | Q(collection__name__icontains = keyword))

            if limit > 100:
                return JsonResponse({'message' : 'TOO_MUCH_LIMIT'}, status = 400) 
            
            limit = offset + limit

            if (main_category or best_seller or sub_category or scent or keyword) == None:
                products = Product.objects.all()[offset:limit]

            result = [{
                'id'            : product.id,
                'name'          : product.name,
                'collection'    : product.collection.name,
                'sub_category'  : product.sub_category.name,
                'size_g'        : product.size_g,
                'size_oz'       : product.size_oz,
                'price'         : product.price,
                'description'   : product.description,
                'image'         : product.productimage_set.get(is_thumbnail=True).image_url
            } for product in products]
            return JsonResponse({'result':result}, status = 200)
        
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status = 404)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)

class ProductDetail(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            images = [product_image.image_url for product_image in product.productimg_set.order_by('_is_thumbnail').all()]
            scent = [scent.description for scent in product.scent_set.all()]
            result = {
                    'id'            : product.id,
                    'name'          : product.name,
                    'collection'    : product.collection.name,
                    'sub_category'  : product.sub_category.name,
                    'size_g'        : product.size_g,
                    'size_oz'       : product.size_oz,
                    'price'         : product.price,
                    'description'   : product.description,
                    'image'         : product.productimage_set.get(is_thumbnail=True).image_url
            }
            
            return JsonResponse({'result' : result}, status = 200)
        
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NOT_FOUND'}, status = 404)
         
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)