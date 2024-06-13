from rest_framework import routers

from apps.carts.viewsets import CartViewSet
from apps.cart_items.viewsets import CartItemViewSet
from apps.receipts.viewsets import ReceiptViewSet
from apps.products.viewsets import ProductViewSet

router = routers.SimpleRouter()

router.register(r'carts', CartViewSet, basename='carts')
router.register(r'cart_items', CartItemViewSet, basename='cart_items')
router.register(r'receipts', ReceiptViewSet, basename='receipts')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls
