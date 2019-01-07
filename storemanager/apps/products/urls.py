from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from django.urls import path

urlpatterns = {
    path('products/', CreateView.as_view(), name="create"),
    path('products/<int:pk>/', DetailsView.as_view(), name="details"),

}

urlpatterns = format_suffix_patterns(urlpatterns)