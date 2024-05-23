from django.db import models

class CHSource(models.Model):
    src_file = models.CharField(db_column='src_file', max_length=255, default='')
    src_name = models.CharField(db_column='src_name', max_length=255, default='')
    src_link = models.CharField(db_column='src_link', max_length=1024, default='')
    result_text = models.CharField(db_column='result_text', max_length=4096, default='')
    status = models.CharField(db_column='status', max_length=10, default='0')
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')
    created_at = models.DateTimeField(db_column='created_at', )

    class Meta:
        managed = False
        db_table = 'ch_source'