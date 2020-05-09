'''
Models for the `base` app
'''


from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField


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

    pass
