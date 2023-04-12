from django.db import models

# # SQLAlchemy
# from sqlalchemy import Sequence, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

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

# class Board2(Base):
#     __tablename__ = 'board'
#     b_no = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     b_title = Column(String(50))
#     b_note = Column(String(50))
#     b_writer = Column(String(50))
#     b_count = Column(Integer)
#     usage_flag = Column(String(10))
#
#     def __repr__(self):
#         return "<User(Title='%s', Writer='%s')>" % (self.b_title, self.b_writer)