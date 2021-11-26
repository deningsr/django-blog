from django.shortcuts import render
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class BlogListView(ListView):
    queryset = Post.objects.order_by("-published_date").exclude(published_date=None)
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"


class LatestEntriesFeed(Feed):
    title = "Latest Posts"
    link = "/posts/"
    description = "Updates when new posts are added"

    def posts(self):
        return Post.objects.order_by("-published_date")

    def post_title(self, post):
        return post.title

    def item_description(self, item):
        return item.description

    def item_link(self, post):
        return reverse("post", args=[post.pk])
