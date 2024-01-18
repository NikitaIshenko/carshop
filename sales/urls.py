from django.urls import path
import sales.views as sales

app_name="sales"

urlpatterns = [
    path("", sales.index, name="index"),
    path("update/<int:pk>/", sales.SaleUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", sales.SaleDelete.as_view(), name="delete"),
    path("create/", sales.SaleCreate.as_view(), name="create")
] 