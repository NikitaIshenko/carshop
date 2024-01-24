from django.urls import path
import main.views as main

app_name = 'main'

urlpatterns = [
    path("", main.main, name="index"),
    path("marks/", main.mark, name="marks"),
    path("top_saller/", main.top_saller, name="top_saller"),
    path("client-card/", main.client_card, name="client_card"),
    path("most-mark-eq/", main.most_mark_eq, name="most_mark_eq")
] 