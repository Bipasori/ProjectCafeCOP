from django.db import models

class Boardtype(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    type_name = models.CharField(db_column='type_name', max_length=50)

    class Meta:
        managed = False
        db_table = 'boardtype'


class Boardnew(models.Model):
    b_no = models.AutoField(db_column='b_no', primary_key=True)
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_note = models.TextField(db_column='b_note', blank=True, null=True)
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    type = models.ForeignKey(Boardtype, on_delete=models.CASCADE, default=1)
    parent_no = models.IntegerField(db_column='parent_no', default=0)
    b_count = models.IntegerField(db_column='b_count', default=0)
    b_date = models.DateTimeField(db_column='b_date', )
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'boardnew'