from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    # 非Class-view 方式
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

]
