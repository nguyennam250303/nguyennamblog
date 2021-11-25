from django.urls import path
from .views import BlogList, BlogDetail, Introduce, BlogCreate, BlogUpdate, BlogDelete, BlogLogin

app_name = 'Theblog'

urlpatterns = [
    path('',Introduce,name = 'infor'),
    path('posts',BlogList.as_view(),name= 'home'),
    path('detail/<int:pk>',BlogDetail.as_view(),name = 'detail'),
    path('detail/create/',BlogCreate.as_view(), name = 'create'),
    path('detail/update/<int:primarykey>',BlogUpdate.as_view(),name = 'update'),
    path('detail/delete/<int:primarykey>',BlogDelete.as_view(),name = 'delete'),
    path('login/',BlogLogin.as_view(),name = 'login')
]