from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField,StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail import blocks

from django.contrib.auth.models import User

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractForm


class BlogIndexPage(Page):
            intro = RichTextField(blank=True)

            content_panels = Page.content_panels + [
                FieldPanel('intro')
            ]
            
            def get_context(self, request):
                # Update context to include only published posts, ordered by reverse-chron
                context = super().get_context(request)
                blogpages = self.get_children().live().order_by('-first_published_at')
                context['blogpages'] = blogpages
                return context

class BlogPage(Page):
            date = models.DateField("Post date")
            intro = models.CharField(max_length=250)
            body = StreamField([
                ('heading', blocks.CharBlock(form_classname="title", on_delete=models.CASCADE, blank=True, null=True)),
                ('paragraph', blocks.RichTextBlock(on_delete=models.CASCADE, blank=True, null=True)),
                ])
            author = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)

            search_fields = Page.search_fields + [
                index.SearchField('intro'),
                index.SearchField('body'),
            ]

            content_panels = Page.content_panels + [
                FieldPanel('date'),
                FieldPanel('intro'),
                StreamFieldPanel('body'),
                FieldPanel('author', classname="full"),
                InlinePanel('gallery_images', label="Gallery images"),
            ]
            
class GalleryImage(Orderable):
            page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
            image = models.ForeignKey(
                'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
            )
            caption = models.CharField(blank=True, max_length=250)

            panels = [
                FieldPanel('image'),
                FieldPanel('caption'),
            ]
            

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birthday = models.CharField(max_length=100)