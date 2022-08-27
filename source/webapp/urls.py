from django.urls import path

from webapp.views import IndexView, ProductView, ProductCreate, ProductUpdate, ProductDelete, CreateReview, UpdateReview, DeleteReview

app_name = "webapp"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('products/add/', ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/review/add/', CreateReview.as_view(), name="create_review"),
    path('reviews/<int:pk>/update/', UpdateReview.as_view(), name="update_review"),
    path('reviews/<int:pk>/delete/', DeleteReview.as_view(), name="delete_review"),
]
