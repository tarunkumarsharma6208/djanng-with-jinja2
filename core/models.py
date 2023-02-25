from django.db import models

# Create your models here.
class Base(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

TYPE = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C')
)

class Book(Base):
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(choices=TYPE,max_length=2, default='A')
    def __str__(self):
	    return self.name
