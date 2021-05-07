from django.views import generic
from django.shortcuts import get_object_or_404
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
    """ Forum category page view"""
    model = models.ForumCategory
    template_name='main/forum_category_detail.html'

class PostListView(generic.ListView):
    """ Post List view based on a particular forum """
    paginated_by = 10
    template_name = "main/post_list.html"
    
    def get_queryset(self, **kwargs):
        self.forum = get_object_or_404(models.Forum, name=self.kwargs['forum'])
        return models.Post.objects.filter(forum = self.forum)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['forum'] = self.forum
        return context


class AboutUsView(generic.TemplateView):
    """ About-Us page view """
    template_name = "main/about_us.html"

