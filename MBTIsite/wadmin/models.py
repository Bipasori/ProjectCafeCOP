from django.db import models

class WMHeader(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    pname = models.CharField(db_column='pname', max_length=50)
    pdesc = models.CharField(db_column='pdesc', max_length=255)
    qask = models.CharField(db_column='qask', max_length=1024)
    level_max = models.IntegerField(db_column='level_max', default=1)

    class Meta:
        managed = False
        db_table = 'wm_qheader'

class WMQuestion(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    header = models.ForeignKey(WMHeader, on_delete=models.CASCADE)
    parent_id = models.IntegerField(db_column='parent_id', default=0)
    qlevel = models.IntegerField(db_column='qlevel', default=1)
    order_no = models.IntegerField(db_column='order_no', default=1)
    qask = models.CharField(db_column='qask', max_length=1024)
    qname = models.CharField(db_column='qname', max_length=50)
    qdesc = models.CharField(db_column='qdesc', max_length=255)

    class Meta:
        managed = False
        db_table = 'wm_question'


class WHEvent(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    header = models.ForeignKey(WMHeader, on_delete=models.CASCADE)
    event_id = models.CharField(db_column='event_id', max_length=50)
    user_answer = models.CharField(db_column='user_answer', max_length=255)
    user_note = models.CharField(db_column='user_note', max_length=4096)
    event_result = models.CharField(db_column='event_result', max_length=255)
    level_max = models.IntegerField(db_column='level_max', default=1)

    class Meta:
        managed = False
        db_table = 'wh_event'


class WHResult(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    header = models.ForeignKey(WMHeader, on_delete=models.CASCADE)
    result_code = models.CharField(db_column='result_code', max_length=255)
    result_link = models.CharField(db_column='result_link', max_length=1024)
    image_link = models.CharField(db_column='image_link', max_length=1024)
    result_desc = models.CharField(db_column='result_desc', max_length=1024)

    class Meta:
        managed = False
        db_table = 'wh_result'