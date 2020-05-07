'''
Views for the `home` app
'''


from django.views.generic import TemplateView

from taggit.models import Tag


class AboutView(TemplateView):
    '''
    Provides a basic view for `about`
    '''

    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        '''
        Provide a queryset of `Tag` entries to the context for rendering on the
        page header
        '''

        context = super().get_context_data(**kwargs)

        # Only show tags that have a page associated with them
        context['tags'] = Tag.objects.filter(blogpost__isnull=False)

        return context
