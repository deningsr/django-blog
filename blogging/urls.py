from django.urls import path
from blogging.views import stub_view
from blogging.views import ListView, BlogListView, BlogDetailView, LatestEntriesFeed


urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("latest/feed/", LatestEntriesFeed()),
]
