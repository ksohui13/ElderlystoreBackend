from django.db import models
from mainshop.models import TimeStampModel

class Businesspage(TimeStampModel):
    order_detail_number = models.IntegerField()

    class Meta:
        db_table = 'businesspage'

class deliver(TimeStampModel):
    deliver_number = models.AutoField(primary_key=True)
    deliver_status = models.CharField(max_length=50)
    deliver_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'deliver'
