from django.views import generic
from . import models

class HomeView(generic.ListView):
    """ Home page view """
    model = models.Post
    context_object_name = 'posts'
    template_name = 'main/index.html'


class ForumCategoriesView(generic.ListView):
    """ Forum categories page view """
    model = models.ForumCategory
    context_object_name = 'categories'
    template_name='main/forum_category_list.html'


class ForumCategoryDetailView(generic.DetailView):
    """ Forums page view """
    model = models.ForumCategory
    template_name='main/forum_category_detail.html'


class ForumsDetailView():
    pass


class PostDetailView():
    pass


class AboutUsView(generic.TemplateView):
    """ About-Us page view """
    template_name = "main/about_us.html"

