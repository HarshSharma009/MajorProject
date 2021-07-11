from django.urls import path

from . import views

urlpatterns = [
    path("stockpage", views.index, name="index"),
    path("cstock", views.cstock, name="cstock"),
    path("predict", views.predict, name="predict"),
    path("predict_stock/<str:symbol>/<str:period>/<int:sim>/<int:future>", views.stock_predict, name="predict_stock"),
    path("trade", views.trade, name="trade"),
    path("trade_stock/<str:symbol>/<str:period>/<int:init>/<int:skip>", views.stock_trade, name="trade_stock")
]
