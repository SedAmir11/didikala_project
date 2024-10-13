from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app_didikala.models import Product , banner , ProductDetail
from .serializers import ProductSerializer , BannerSerializer , ProductDetailSerializer

@api_view(['GET'])
def apiproduct_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def banner_list_api(request):
    banner_list = banner.objects.all()
    return Response(BannerSerializer(banner_list , many = True).data, 200)

@api_view(['POST'])
def apiproduct_create(request):
    name = request.data.get('name')
    categories = request.data.getlist('categories')
    price = request.data.get('price')
    brand_id = request.data.get('brand') 
    image = request.FILES.get('image')
    count = request.data.get('count')
    discount = request.data.get('discount')
    star = request.data.get('star')

    product = Product(
        name=name,
        price=price,
        brand_id=brand_id,
        image=image,
        count=count,
        discount=discount,
        star=star
    )

    try:
        product.save() 
        product.categories.set(categories)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message' : 'The product created'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def apiproduct_delete(request):
    proudct_id = request.data.get('product_id')
    
    try:
        product = Product.objects.get(id = proudct_id)
        product.delete()
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message' : 'The product deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def apiproduct_update(request):
    product_id = request.data.get('product_id')
    name = request.data.get('name')
    categories = request.data.getlist('categories')
    price = request.data.get('price')
    brand_id = request.data.get('brand') 
    image = request.FILES.get('image')
    count = request.data.get('count')
    discount = request.data.get('discount')
    star = request.data.get('star')
    
    try:
        product = Product.objects.get(id = product_id)
      
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    if name is not None:  
        product.name = name
    if categories:  
        product.categories.set(categories)
    if price is not None:  
        product.price = price
    if brand_id is not None:  
        product.brand_id = brand_id  
    if image:
        product.image = image
    if count is not None:  
        product.count = count
    if discount is not None:  
        product.discount = discount
    if star is not None:  
        product.star = star
    
    product.save()
    
    return Response({'message' : f'The product {product_id} updatead'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def apiproductdetail_list(request):
    product_id = request.query_params.get('product_id')
    if not product_id:
        return Response({'message': 'product_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product_detail = ProductDetail.objects.get(product_id=product_id)
        serializer = ProductDetailSerializer(product_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ProductDetail.DoesNotExist:
        return Response({'message': 'Product detail not found'}, status=status.HTTP_404_NOT_FOUND)