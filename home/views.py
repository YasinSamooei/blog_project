from django.views.generic import TemplateView

# local
from blog.models import Blog,Comment

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        # context['comments'] = Comment.objects.all().order_by("-created_at")[:3]

        blogs=Blog.objects.order_by('-created_at')
        context['blogs'] = blogs[:6]
         
        return context


