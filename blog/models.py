from django.conf import settings
from django.db import models
from django.utils import timezone


# #`class` is a special keyword that indicates that we are defining an object.
## `Post` is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
## `models.Model` means that the Post is a Django Model, so Django knows that it should be saved in the database.


class Post(models.Model):   ## this line defines our model (it is an object)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  ## models.ForeignKey – this is a link to another model.
    title = models.CharField(max_length=200) ## models.CharField – this is how you define text with a limited number of characters.
    text = models.TextField()  ## models.TextField – this is for long text without a limit. Sounds ideal for blog post content
    created_date = models.DateTimeField(default=timezone.now)  ## models.DateTimeField – this is a date and time.
    published_date = models.DateTimeField(blank=True, null=True)  ##

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
