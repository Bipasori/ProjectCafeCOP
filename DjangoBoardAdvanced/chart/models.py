from django.db import models

class salesPredict(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    yyyymm = models.CharField(db_column='yyyymm', max_length=20)
    sales_amt = models.IntegerField(db_column='sales_amt', default=0)
    sales_predict = models.IntegerField(db_column='sales_predict', default=0)

    class Meta:
        managed = False
        db_table = 'sales_predict'

    def __str__(self):
        return self.yyyymm + "," + str(self.sales_amt) + "," + str(self.sales_predict)