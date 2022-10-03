from cgitb import lookup
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)

products_routers = routers.NestedDefaultRouter(
    router, 'products', lookup='product')

products_routers.register('reviews', views.ReviewViewSet, 'product-reviews')


items_routers = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
items_routers.register('items', views.CartItemViewSet, 'cart-items')


# URLConf
urlpatterns = router.urls + products_routers.urls + items_routers.urls
