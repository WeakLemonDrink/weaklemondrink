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
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogIndexPage(Page):
    '''
    Index page for `BlogPage` entries
    '''

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]


class BlogPostTag(TaggedItemBase):
    '''
    List of tags we can use for `BlogPage` entries
    '''

    content_object = ParentalKey(
        'blog.BlogPage', on_delete=models.CASCADE, related_name='tagged_items'
    )


class BlogPage(Page):
    '''
    Defines database table structure for `BlogPage` entries
    '''

    body = RichTextField()
    date = models.DateField('Post date')
    tags = ClusterTaggableManager(through=BlogPostTag, blank=True)
    preview_img = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='blogpage_preview_img')

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        FieldPanel('tags'),
        ImageChooserPanel('preview_img'),
    ]
