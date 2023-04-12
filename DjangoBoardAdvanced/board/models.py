from django.db import models

class Board(models.Model):
    b_no = models.AutoField(db_column='b_no', primary_key=True)
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_note = models.TextField(db_column='b_note', )
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    parent_no = models.IntegerField(db_column='parent_no', default=0)
    b_count = models.IntegerField(db_column='b_count', default=0)
    b_date = models.DateTimeField(db_column='b_date', )
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'board'

    def __str__(self):
        return "제목 : " + self.b_title + ", 작성자 : " + self.b_writer

# class Person(models.Model):
#     name = models.CharField(db_column='name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'person'
#
#     def __str__(self):
#         return "이름 : " + self.name
