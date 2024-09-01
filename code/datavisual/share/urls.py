from . import views
from django.urls import path,include
urlpatterns = [
   path('',views.share_list,name='share_list'),
   path('<int:share_id>/delete/',views.share_delete,name='share_delete'),
   path('<int:share_id>/edit/',views.share_edit,name='share_edit'),
   path('create/',views.share_create,name='share_create'),
   path('register/',views.register,name='register'),
   path('<int:share_id>/see/',views.see,name='see_data'),

]




