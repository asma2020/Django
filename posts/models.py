from django.db import models # pyright: ignore[reportMissingModuleSource]

class PostLiveManager(models.Manager):
    def get_querryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_enable = True)
        return queryset

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    is_enable = models.BooleanField(default=False)
    publish_date = models.DateField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now= True)
    def __str__(self):
        # return self.title
        return '{} - {}'.format(self.pk, self.title)
    objects = models.Manager()
    live = PostLiveManager()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField(blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now= True)
