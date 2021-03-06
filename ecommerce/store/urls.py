from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),

	path('login/', views.loginPage, name="loginn"),
	#path('register/', views.registerPage, name="register"),
	path('register/', views.registerPage, name="register"),
	path('edit/<id>/', views.editPage, name="edit"),
	path('delete/', views.deletePage, name="delete"),
	path('logout/', views.registerPage, name="logout"),

	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('checkoutfact/', views.checkoutfact, name="checkoutfact"),
	path('update_items/', views.updateItems, name="update_items"),
	path('process_order/', views.processOrder, name="process_order"),
	path('process_orderfact/', views.processOrderFact, name="process_orderfact"),
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
	path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
	path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
	path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
	path('adm-producto/', views.adm_productos, name="adm-producto"),
	path('agregar-producto/', views.agregar_producto, name="agregar-producto"),

	path('edit-product/<id>/', views.editProductPage, name="edit-product"),
	path("id_producto",views.id_producto, name='id_producto'),
	path("adm-producto/delete/<pk>/",views.eliminar_producto, name='eliminar_producto'),

	path("store/enviar-orden/<pk>", views.send_order, name='send_order'),
	path("store/aprobar/<pk>/", views.aprobarOrden, name='aprobarOrden'),
	path("store/rechazar/<pk>/", views.rechazarOrden, name='rechazarOrden'),

	path('admin/listado_usuarios/',views.listUser, name="listado_usuarios"),
	path('admin/users/edit/<pk>/' ,views.editUser, name='edit_user'),
	path('admin/users/delete/<pk>/',views.deleteUser, name='delete_user'),
	path("admin/users/registerclient/",views.registerClient, name='register_client'),
	path("admin/users/registerseller/",views.registerSeller, name='register_seller'),
	path("admin/users/registersupplier/",views.registerSupplier, name='register_supplier'),
	path("admin/users/registeremployee/",views.registerEmployee, name='register_employee'),


	path("admin/users/registerclient",views.registerClient, name='register_client'),
	path("admin/users/registerseller",views.registerSeller, name='register_seller'),
	path("admin/users/registersupplier",views.registerSupplier, name='register_supplier'),
	path("admin/users/registeremployee",views.registerEmployee, name='register_employee'),

	path("adm-factura",views.adm_facturas, name='adm-factura'),
	path("adm-boleta",views.adm_boletas, name='adm-boleta'),
	path("adm-ordencompra",views.adm_ordencompra, name='adm-ordencompra'),
	path('consultar_orden', views.vista_proveedor, name='proveedor-ordencompra'),
	path('check_order/<pk>/', views.check_order, name='check_order'),
	path('generar-ordencompra',views.orden_compra, name='generar-ordencompra'),
	path('eliminar-ordencompra/<pk>/',views.eliminar_orden_compra, name='eliminar-ordencompra'),
	path('revisar-ordencompra/<pk>/',views.review_order, name='review_order'),
	path('delete_bill/<pk>/',views.delete_bill, name='delete_bill'),
	path('edit_bill/<pk>/' ,views.edit_bill, name='edit_bill'),
	path('edit_receipt/<pk>/', views.edit_receipt, name='edit_receipt'),
	path('edit_order/<pk>/',views.edit_order, name='edit_order'),
	path('eliminar_factura/<pk>/' ,views.eliminar_factura, name='eliminar-factura'),
	path('export/csv/productos', views.exportar_productos, name='exportar_productos'),
	path('export/csv/boletas', views.exportar_boletas, name='exportar_boletas'),
	path('export/csv/facturas', views.exportar_facturas, name='exportar_facturas'),
	path('export/csv/ordenes', views.exportar_ordenes, name='exportar_ordenes'),
    path('export/csv/usuarios', views.exportar_usuarios, name='exportar_usuarios'),
	

	path('page_not_found', views.page_not_found, name='page_not_found'),

	path('store/cat/<pk>', views.storeCategories, name="storeCategories"),
	path('store/type/<pk>', views.storeTypes, name="storeTypes"),

	path('admin/filter/clients', views.userClients, name="userClients"),
	path('admin/filter/employees', views.userEmployees, name="userEmployees"),
	path('admin/filter/suppliers', views.userSuppliers, name="userSuppliers"),
	path('admin/filter/sellers', views.userSellers, name="userSellers"),

	path('agregar-familia/', views.addFamily, name="agregar-familia"),
	path('agregar-tipo/', views.addType, name="agregar-tipo")
	
]
