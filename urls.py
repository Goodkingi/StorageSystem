from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("About",views.About,name ="about"),
    path("Feature",views.Feature,name="all-links"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("ledger",views.ledger,name="ledger"),
    path("product-list",views.product,name="product-list"),
    path("detail/<int:id>",views.detail,name="detail"),
    path("order",views.order,name="order"),
    path("reports",views.report,name="reports"),
]