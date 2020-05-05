'''
Views for the `home` app
'''


from django.views.generic import TemplateView

from taggit.models import Tag

from blog.models import BlogPost


class HomeView(TemplateView):
    '''
    Provides a basic view for `home`
    '''

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        '''
        Provide a queryset of `BlogPost` entries to the context for rendering on the
        home page
        '''

        context = super().get_context_data(**kwargs)

        # Add `BlogPost` queryset to the context
        context['tags'] = Tag.objects.all()
        context['posts'] = BlogPost.objects.filter(live=True)

        return context
