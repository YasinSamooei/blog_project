from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('blog/<str:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog-search', views.SearchView.as_view(), name='blog-search'),
    path('blog-list', views.BlogListView.as_view(), name='blog-list'),
    path('tag/<str:slug>', views.TagDetailView.as_view(), name='tag-detail'),
    path("remove/<int:pk>", views.RemoveCommentView.as_view(), name='remove_comment'),
    path('delete-notif/<int:pk>',views.DeleteNotif.as_view(),name="delete-notif"),
    path('delete-public-notif/<int:pk>',views.DeletePublicNotif.as_view(),name="delete-public-notif"),
    path('add-notif-system',views.AddNotificationSystem.as_view(),name="add-notif-system"),
    path('remove-notif-system',views.RemoveNotificationSystem.as_view(),name="remove-notif-system"),
    path("add-favorite/<int:pk>", views.AddFavoriteView.as_view(), name="favorite_add"),
    
    
]