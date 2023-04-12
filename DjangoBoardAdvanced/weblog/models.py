from django.db import models

class Weblog(models.Model):
    member_no = models.IntegerField(db_column='member_no', default=0)
    server_desc = models.CharField(db_column='server_desc', max_length=255)
    useragent = models.CharField(db_column='useragent', max_length=255)
    url_desc = models.CharField(db_column='url_desc', max_length=255)
    log_date = models.DateTimeField(db_column='log_date', )

    class Meta:
        managed = False
        db_table = 'weblog'

class WeblogUrl(models.Model):
    url_desc = models.CharField(db_column='url_desc', max_length=255)
    yyyymmdd = models.CharField(db_column='yyyymmdd', max_length=255)
    click_cnt = models.IntegerField(db_column='click_cnt', default=0)

    class Meta:
        managed = False
        db_table = 'weblog_url'
