'''
Custom tags for the project

https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/
'''


from django import template

from taggit.models import Tag


register = template.Library()


@register.inclusion_tag('tags/tag_links.html')
def tag_links():
    '''
    Returns a queryset of valid `Tag` entries to use as links on the home page

    Only show tags that have a page associated with them
    '''

    return {'tags': Tag.objects.filter(blogpost__isnull=False).distinct()}
