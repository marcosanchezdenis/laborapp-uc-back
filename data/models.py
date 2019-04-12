from django.db import models






class PropertyType(models.Model):
    name =  models.CharField(max_length=300)

    def __str__(self):
        return '%s' % (self.name)
class Property(models.Model):
    CONTROL_TYPE = (
        ('text-input', 'Entrada de texto'),
        ('date-input', 'Entrada de fecha'),
        ('paragraph-input', 'Entrada de texto multilinea'),
        ('image-input', 'Entrada de imagen'), # debe tener referenciado un request 
 
    )
    name = models.CharField(max_length=200)
    description =  models.TextField()
    type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    control_type =  models.CharField(max_length=200,choices=CONTROL_TYPE)
    required = models.BooleanField(default=False)
    visibility_set =  models.ManyToManyField('privacy.Visibility',blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s, %s' % (self.name, self.type)