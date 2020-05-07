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

        Filter the `BlogPost` queryset if there is a `tag` querystring sent as part
        of the request
        '''

        filter_kwargs = {}

        context = super().get_context_data(**kwargs)

        # If a valid `tag` querystring has been sent via the request, filter
        # `BlogPost` entries with this tag
        request_tag_name = self.request.GET.get('tag', None)

        # Filter `BlogPost` entries just by `live` by default
        filter_kwargs['live'] = True

        if request_tag_name:
            if Tag.objects.filter(name=request_tag_name).exists():
                filter_kwargs['tags__name__in'] = [request_tag_name]

        # Only show tags that have a page associated with them
        context['tags'] = Tag.objects.filter(blogpost__isnull=False)
        # Add `BlogPost` queryset to the context filtered using `filter_kwargs`
        context['posts'] = BlogPost.objects.filter(**filter_kwargs)

        return context
