from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('addtocart/', views.AddToCart.as_view(),
         name="add_to_cart"),
    path('removerdocarrinho/', views.RemoveFromCart.as_view(),
         name="removerdocarrinho"),
    path('cart/', views.Cart.as_view(),
         name="cart"),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name="resumodacompra"),

]
