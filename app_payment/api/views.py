from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app_payment.models import Basket , BasketItem , Product
from .serializers import BasketSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def apibasket_list(request):
    basket = Basket.objects.all()
    data = BasketSerializer(basket, many=True).data
    return Response(data, status.HTTP_200_OK)

@api_view(['DELETE'])
def apibasket_delete(request):
    pk = request.POST.get('pk')
    try:
        basket = Basket.objects.get(id=pk)
        basket.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Basket.DoesNotExist:
        return Response({'message': 'Basket not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': f'Deleted unsuccessfully! Error: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def apibasket_create(request):
    user_id = request.POST.get('user_id', None)
    product_id = request.POST.get('product_id', None)
    count = int(request.POST.get('count', 0))
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    if count > product.count:
        return Response({'message': 'The count is more than stock'}, status=status.HTTP_400_BAD_REQUEST)

    basket, created = Basket.objects.get_or_create(user=user)
    basket_item, item_created = BasketItem.objects.get_or_create(basket=basket, product=product)

    if not item_created:
        new_count = basket_item.count + count
        if new_count > product.count:
            return Response({'message': 'The count is more than stock'}, status=status.HTTP_400_BAD_REQUEST)
        basket_item.count = new_count
        basket_item.save()
    else:
        basket_item.count = count
        basket_item.save()

    return Response({'message': 'Item added to basket'}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def apibasket_update(request):
    basket_item_id = request.POST.get('basket_item_id', None)
    new_count = int(request.POST.get('count', 0))
    
    try:
        basket_item = BasketItem.objects.get(id=basket_item_id)
    except BasketItem.DoesNotExist:
        return Response({'message': 'Basket item not found'}, status=status.HTTP_404_NOT_FOUND)

    if new_count > basket_item.product.count:
        return Response({'message': 'The count is more than stock'}, status=status.HTTP_400_BAD_REQUEST)
    
    basket_item.count = new_count
    basket_item.save()

    return Response({'message': 'Basket item updated successfully'}, status=status.HTTP_200_OK)
