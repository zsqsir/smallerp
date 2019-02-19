from django.db import models

# Create your models here.

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    publisher=models.CharField("出版社",max_length=100)

    class Meta:
        db_table="publisher"
        verbose_name="出版社"
        verbose_name_plural = verbose_name

class Writer(models.Model):
    id = models.AutoField(primary_key=True)
    writer=models.CharField("作者",max_length=100)

    class Meta:
        db_table="writer"
        verbose_name="作者"
        verbose_name_plural = verbose_name

class Translator(models.Model):
    id = models.AutoField(primary_key=True)
    translator = models.CharField("译者",max_length=100)

    class Meta:
        db_table="Translator"
        verbose_name="译者"
        verbose_name_plural = verbose_name


class Kind(models.Model):
    id = models.AutoField(primary_key=True)
    kind=models.CharField("分类",max_length=250)

    class Meta:
        db_table="kind"
        verbose_name="种类"
        verbose_name_plural = verbose_name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    # 书名
    title=models.CharField("书名",max_length=250)
    # 出版社 外键至出版社类
    publisher = models.ForeignKey(to="Publisher",to_field="id",default ="",on_delete=models.CASCADE)
    date=models.DateField("出版日期",null=True, blank=True)
    # 作者 外键至作者类
    writer = models.ForeignKey(to="Writer",to_field="id",default ="",on_delete=models.CASCADE)
    # 译者 外键至译者类
    translator = models.ForeignKey(to="Translator",to_field="id",default ="",on_delete=models.CASCADE) 

    wordsCount=models.IntegerField("字数统计",null=True, blank=True,)
    price=models.DecimalField("书籍价格",max_digits=9, decimal_places=2)
    # 书籍分类 外键至 kind类
    kind = models.ForeignKey(to="Kind",to_field="id",default ="",on_delete=models.CASCADE) 
    
    series=models.CharField("系列",null=True, blank=True,max_length=250)
    size=models.CharField("尺寸",max_length=250)
    pages = models.IntegerField("页码数")
    turn=models.CharField("版次",null=True, blank=True,max_length=90)
    brief=models.TextField("简介",null=True, blank=True)
    isbn=models.CharField("ISBN",max_length=90)
    catalog=models.TextField("目录",null=True, blank=True)
    # old_id=models.IntegerField("oldid")

    class Meta:
        # db_table="book"
        verbose_name="书籍"
        verbose_name_plural = verbose_name

