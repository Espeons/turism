from django.urls import path


from alex import views

urlpatterns = [
    path('contact/', views.ContactCreateView.as_view(), name='create_contact'),
    path('galery/', views. GaleryTemplateView.as_view(), name='galery'),
    path('list_products/', views.ProductListView.as_view(), name='list-products'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_card/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('create_rev/', views.RevCreateView.as_view(), name='create-rev'),
    path('list_rev/', views.RevListView.as_view(), name='list-rev'),
    path('delete_rev/<int:pk>/', views.RevDeleteView.as_view(), name='delete-rev'),
    path('details_rev/<int:pk>/', views.RevDetailView.as_view(), name='details-rev'),

]
