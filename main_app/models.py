from django.db import models

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

  def __str__(self):
    return self.name