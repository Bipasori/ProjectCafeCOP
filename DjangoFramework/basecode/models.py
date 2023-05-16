from django.db import models

class CBCodeHdr(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    type_name = models.CharField(db_column='type_name', max_length=50)
    register_date = models.DateTimeField(db_column='register_date', )
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'cb_code_hdr'

    def __str__(self):
        return "Code Type : " + self.type_name

class CBCodeDtl(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    code_cd = models.CharField(db_column='code_cd', max_length=20)
    code_name = models.CharField(db_column='code_name', max_length=50)
    register_date = models.DateTimeField(db_column='register_date', )
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'cb_code_dtl'

    def __str__(self):
        return "Code : " + self.code_name

class CMFactory(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    factory_cd = models.CharField(db_column='factory_cd', max_length=20)
    factory_name = models.CharField(db_column='factory_name', max_length=50)

    class Meta:
        managed = False
        db_table = 'cm_factory'

    def __str__(self):
        return "공장 : " + self.factory_name


class CBItemgrp(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    itemgrp_cd = models.CharField(db_column='itemgrp_cd', max_length=20)
    itemgrp_name = models.CharField(db_column='itemgrp_name', max_length=50)

    class Meta:
        managed = False
        db_table = 'cb_itemgrp'

    def __str__(self):
        return "품목그룹 : " + self.itemgrp_name

class CMItemaccnt(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    itemaccnt_cd = models.CharField(db_column='itemaccnt_cd', max_length=20)
    itemaccnt_name = models.CharField(db_column='itemaccnt_name', max_length=50)

    class Meta:
        managed = False
        db_table = 'cm_itemaccnt'

    def __str__(self):
        return "품목계정 : " + self.itemaccnt_name

class CMItem(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    factory = models.ForeignKey(CMFactory, on_delete=models.CASCADE)
    itemgrp = models.ForeignKey(CBItemgrp, on_delete=models.CASCADE)
    itemaccnt = models.ForeignKey(CMItemaccnt, on_delete=models.CASCADE)
    unit_id = models.IntegerField(db_column='unit_id', default=0)
    item_cd = models.CharField(db_column='item_cd', max_length=20)
    item_name = models.CharField(db_column='item_name', max_length=50)
    item_spec = models.CharField(db_column='item_spec', max_length=255)
    register_date = models.DateTimeField(db_column='register_date', )
    bom_flag = models.CharField(db_column='bom_flag', max_length=10, default='0')
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'cm_item'

    def __str__(self):
        return "품목 : " + self.item_name

class CMBOM(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    bom_type = models.CharField(db_column='bom_type', max_length=20)
    item = models.ForeignKey(CMItem, on_delete=models.DO_NOTHING)
    parent_id = models.IntegerField(db_column='parent_id', default=0)
    top_id = models.IntegerField(db_column='top_id', default=0)
    bom_order = models.IntegerField(db_column='bom_order', default=0)
    bom_level = models.IntegerField(db_column='bom_level', default=0)
    leaf_flag = models.CharField(db_column='leaf_flag', max_length=10, default='1')
    moitem_base = models.FloatField(db_column='moitem_base', default=0.0)
    jaitem_base = models.FloatField(db_column='jaitem_base', default=0.0)
    unit_product = models.CharField(db_column='unit_product', max_length=50)
    free_flag = models.CharField(db_column='free_flag', max_length=10, default='1')
    loss_product = models.FloatField(db_column='loss_product', default=0.0)
    demand_amt = models.FloatField(db_column='demand_amt', default=0.0)
    start_date = models.CharField(db_column='start_date', max_length=8)
    end_date = models.CharField(db_column='end_date', max_length=8)
    register_date = models.DateTimeField(db_column='register_date', )
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'cm_bom'

    def __str__(self):
        return "BOM id : " + str(self.id) + " Type : " + self.bom_type
