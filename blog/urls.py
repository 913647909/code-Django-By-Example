from django.contrib.sitemaps.views import sitemap
from django.urls import path

from blog import views
from blog.feeds import LatestPostFeed
from blog.sitemaps import PostSitemap

app_name = 'blog'

sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [
    # 非Class-view 方式
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
