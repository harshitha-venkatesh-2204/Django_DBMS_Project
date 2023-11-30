from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
    path('', views.main, name="index"),
	path('product/', views.product, name="Shop"),
	path('cart/', views.cart, name="cart"),
	path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('search/', views.search_products, name='search_products'),
    path('sp/', views.sp, name="product1"),
    path('sp1/', views.sp1, name="product2"),
    path('sp2/', views.sp2, name="product3"),
    path('sp3/', views.sp3, name="product4"),
    path('sp4/', views.sp4, name="product5"),
    path('sp5/', views.sp5, name="product6"),
    path('sp6/', views.sp6, name="product7"),
    path('sp7/', views.sp7, name="product8"),
    path('sp8/', views.sp8, name="product9"),
    path('sp9/', views.sp9, name="product10"),
    path('sp10/', views.sp10, name="product11"),
    path('sp11/', views.sp11, name="product12"),
    path('sp12/', views.sp12, name="product13"),
    path('sp13/', views.sp13, name="product14"),
    path('sp14/', views.sp14, name="product15"),
    path('review-items/', views.review_items, name='review_items'),
    path('enter_shipping_details/', views.enter_shipping_details, name='enter_shipping_details'),
    path('update_item/', views.updateItem, name="update_item"),
    path('order_items/', views.order_item_list, name='order_item_list'),
    path('order_items/<int:pk>/', views.order_item_detail, name='order_item_detail'),
    path('order_items/<int:pk>/update/', views.order_item_update, name='order_item_update'),
    path('order_items/<int:order_item_id>/delete/', views.order_item_delete, name='order_item_delete'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:customer_id>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/<int:warehouse_id>/', views.warehouse_detail, name='warehouse_detail'),
    path('warehouses/new/', views.warehouse_create, name='warehouse_create'),
    path('warehouses/<int:warehouse_id>/edit/', views.warehouse_update, name='warehouse_update'),
    path('warehouses/<int:warehouse_id>/delete/', views.warehouse_delete, name='warehouse_delete'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('EmployeeSignupPage/', views.EmployeeSignupPage, name='EmployeeSignupPage'),
    path('EmployeeLoginPage/', views.EmployeeLoginPage, name='EmployeeLoginPage'),
]