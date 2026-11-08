from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):
    def visible(self):
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        ).select_related('author', 'category', 'location')
