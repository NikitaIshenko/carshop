from django.urls import path
import automobile.views as automobile

app_name="automobile"

urlpatterns = [
    path("", automobile.index, name="index"),
    path("update/<int:pk>/", automobile.AutomobileUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", automobile.AutomobileDelete.as_view(), name="delete"),
    path("create/", automobile.AutomobileCreate.as_view(), name="create")
] 