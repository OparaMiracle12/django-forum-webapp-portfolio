from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # example: wwww.website.com/
    path('', views.HomeView.as_view(), name = "index"),
    # example: www.website.com/forum-categories/
    path('forum-categories/', views.ForumCategoriesView.as_view(), name = "forum_categories"),
    # example: www.website.com/forum-category/entertainment/
    path('forum-categories/<int:pk>/<slug:category>/', views.ForumCategoryDetailView.as_view(), name = "forum_category"),
    # example: www.website.com/posts/programming/
    path('posts/<forum>/', views.PostListView.as_view(), name = "post_list"),
    # # example: www.website.com/posts/2/hello-world/
    # path('posts/<int:pk>/<slug:post>/', views.post_detail, name = "post_detail"),
    # example: www.website.com/about-us/
    path('about-us/', views.AboutUsView.as_view(), name = "about_us"),
]