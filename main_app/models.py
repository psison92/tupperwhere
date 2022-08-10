from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

LOCATIONS = (
  ('R', 'Refrigerator'),
  ('L', 'Freezer')
)

# Create your models here.

class Leftover(models.Model):
  name = models.CharField(max_length=50)
  expiration = models.DateField()
  storage = models.CharField(
    max_length=1,
    choices=LOCATIONS,
    default=LOCATIONS[0][0]
  )
  servings = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("leftovers_detail", kwargs={"leftover_id": self.id})
  