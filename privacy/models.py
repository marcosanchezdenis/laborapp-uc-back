from django.db import models


from data.models import *



#el tipo de abstraccion tendra un nombre, que ayudara al usuario a saber que datos se hara publico
# la descripcion explicara el proceso
# cada abstraccion estara ligada una clase especifica de propiedad, para el caso de ejemplo sera el 
#fecha de nacimiento y localizacion 

class Abstraction(models.Model):
    name =  models.CharField(max_length=200)
    description =  models.TextField()
    property = models.ForeignKey(Property,on_delete=models.CASCADE, blank=True)
    level = models.IntegerField()
    process_id = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Visibility(models.Model):

   
    CONTEXT = (

        ('public', 'Publico'),
        ('onlyme', 'Solo yo'),
        ('contacts', 'Solo mis contactos'),
        ('service', 'Para un servicio'), # debe tener referenciado un request 
        ('custom-list-customers', ' Lista de Clientes'),
        ('custom-list-providers', ' Lista de Proveedores'),
    )
    context_type = models.CharField(
        max_length=100,
        choices=CONTEXT,
        default='onlyme',
    )


    abstraccion =  models.ForeignKey(Abstraction,on_delete=models.CASCADE,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)