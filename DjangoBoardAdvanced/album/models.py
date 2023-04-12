from django.db import models

class Album(models.Model):
    a_no = models.AutoField(db_column='a_no', primary_key=True)
    a_type = models.CharField(db_column='a_type', max_length=50)
    a_title = models.CharField(db_column='a_title', max_length=255)
    a_note = models.CharField(db_column='a_note', max_length=4096)
    a_image = models.CharField(db_column='a_image', max_length=1000)
    a_count = models.IntegerField(db_column='a_count', default=0)
    a_datetime = models.DateTimeField(db_column='a_datetime', )
    a_usage = models.CharField(db_column='a_usage', max_length=10)

    class Meta:
        managed = False
        db_table = 'album'

    def __str__(self):
        return "제목 : " + self.a_title + ", 유형 : " + self.a_type