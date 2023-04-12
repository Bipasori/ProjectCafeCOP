from django.db import models

class Member(models.Model):
    member_no = models.AutoField(db_column='member_no', primary_key=True)
    member_id = models.CharField(db_column='member_id', max_length=20)
    member_pwd = models.CharField(db_column='member_pwd', max_length=20)
    member_name = models.CharField(db_column='member_name', max_length=50)
    member_email = models.CharField(db_column='member_email', max_length=50)
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')
    register_date = models.DateTimeField(db_column='register_date', )
    access_latest = models.DateTimeField(db_column='access_latest', )

    class Meta:
        managed = False
        db_table = 'member'

    def __str__(self):
        return "이름 : " + self.member_name + ", 이메일 : " + self.member_email
