from django.urls import path
import automobile.views as automobile

app_name="automobile"

urlpatterns = [
    path("", automobile.index, name="index"),
    path("update/<int:pk>/", automobile.AutomobileUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", automobile.AutomobileDelete.as_view(), name="delete"),
    path("create/", automobile.AutomobileCreate.as_view(), name="create"),
    path("equipment/", automobile.index_eq, name="index_eq"),
    path("update-equipment/<int:pk>/", automobile.EquipmentUpdate.as_view(), name="update_eq"),
    path("delete-equipment/<int:pk>/", automobile.EquipmentDelete.as_view(), name="delete_eq"),
    path("create-equipment/", automobile.EquipmentCreate.as_view(), name="create_eq")
] 