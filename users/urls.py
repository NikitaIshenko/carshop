from django.urls import path
import users.views as users

app_name="users"

urlpatterns = [
    path("", users.index, name="index"),
    path("update-client/<int:pk>/", users.ClientUpdate.as_view(), name="update_client"),
    path("delete-client/<int:pk>/", users.ClientDelete.as_view(), name="delete_client"),
    path("create-client/", users.ClientCreate.as_view(), name="create_client"),
    path("update-saller/<int:pk>/", users.SallerUpdate.as_view(), name="update_saller"),
    path("delete-saller/<int:pk>/", users.SallerDelete.as_view(), name="delete_saller"),
    path("create-saller/", users.SallerCreate.as_view(), name="create_saller"),
] 