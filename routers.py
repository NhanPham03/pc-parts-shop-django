from rest_framework import routers

from apps.users.viewsets import UserViewSets
from apps.carts.viewsets import CartViewSets
from apps.items.viewsets import ItemViewSets
from apps.cart_item.viewsets import CartItemViewSets
from apps.receipts.viewsets import ReceiptViewSets
from apps.products.viewsets import ProductViewSets

router = routers.SimpleRouter()

router.register(r'users', UserViewSets, basename='users')
router.register(r'carts', CartViewSets, basename='carts')
router.register(r'items', ItemViewSets, basename='items')
router.register(r'cart_item', CartItemViewSets, basename='cart_item')
router.register(r'receipts', ReceiptViewSets, basename='receipts')
router.register(r'products', ProductViewSets, basename='products')

urlpatterns = router.urls
