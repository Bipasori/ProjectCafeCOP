from django.db import models


class Entity(models.Model):
    entity_name = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = "myapp_entity"


class Meta(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=50)
    column_type = models.CharField(max_length=20)
    column_length = models.IntegerField(default=0)
    order_no = models.IntegerField(default=1)

    class Meta:
        db_table = "myapp_meta"