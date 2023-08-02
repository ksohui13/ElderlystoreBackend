from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Maincategories(models.Model):
    main_category_id = models.AutoField(primary_key=True)
    main_category = models.CharField()

    class Meta:
        db_table = 'main_categories'