'''
Models for the `blog` app
'''


from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField


class BlogPostTag(TaggedItemBase):
    '''
    List of tags we can use for `BlogPost` entries
    '''

    content_object = ParentalKey(
        'blog.BlogPost', on_delete=models.CASCADE, related_name='tagged_items'
    )


class BlogPost(Page):
    '''
    Defines database table structure for `BlogPost` entries
    '''

    body = RichTextField()
    date = models.DateField('Post date')
    tags = ClusterTaggableManager(through=BlogPostTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        FieldPanel('tags'),
    ]
