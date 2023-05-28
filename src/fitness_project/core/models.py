from django.db import models
import uuid
from django.db import models
class Workouts(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4)
    picture = models.ImageField(upload_to='picture')