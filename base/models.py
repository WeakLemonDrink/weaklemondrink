'''
Models for the `base` app
'''


from taggit.models import Tag
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from blog.models import BlogPage


class AboutPage(Page):
    '''
    The about page
    '''

    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class HomePage(Page):
    '''
    The home page
    '''

    def get_context(self, request, *args, **kwargs):
        '''
        Override default `get_context` to add blog posts to the context for rendering
        on the homepage
        '''

        filter_kwargs = {}

        context = super().get_context(request, *args, **kwargs)

        # If a valid `tag` querystring has been sent via the request, filter
        # `BlogPage` entries with this tag
        request_tag_name = request.GET.get('tag', None)

        # Filter `BlogPage` entries just by `live` by default
        filter_kwargs['live'] = True

        if request_tag_name:
            if Tag.objects.filter(name=request_tag_name).exists():
                filter_kwargs['tags__name__in'] = [request_tag_name]

        # Add `BlogPage` queryset to the context filtered using `filter_kwargs`
        context['pages'] = BlogPage.objects.filter(**filter_kwargs)

        return context
