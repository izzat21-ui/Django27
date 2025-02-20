import os
from datetime import datetime
from django.utils.dateparse import parse_date

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()
from apps.models import Region, District

#===============================================================
# select_related() – JOIN ishlatadi va ForeignKey / One-to-One uchun eng yaxshi yechim

# prefetch_related() – alohida so‘rovlar ishlatadi va Many-to-Many / One-to-Many uchun optimal

# Django ORM ni tezlashtirish uchun N+1 muammolarni hal qiladiannotate() har bir obyekt uchun qo‘shimcha ustunlar yaratadi

# Q() – Murakkab filterlar (OR, AND, NOT) yaratish uchun

# F() – Modeldagi ustunlarni bir-biri bilan solishtirish va arifmetik amallar bajarish uchun

# only() – Faqat kerakli ustunlarni olish va ORM'ni tezlashtirish uchun





#+++++++++++++++++++++++++++=====================================

# qs = Region.objects.all().count()
# print(qs)

#=======================Regiondagi birinchisidagi sozni olib keladi=========================================
# qs = Region.objects.all().first()
# print(qs)

#=========================ORM truncate qilish=======================================

# qs = District.objects.all().delete()
# qv = District.objects.all().count()
# print(qs)
# print(qv)

# class Category(Model):
#     @classmethod
#     def truncate(cls):
#         with connection.cursor() as cursor:
#             cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


#=========================Stringni datetimega aylantirish =======================================

# user = Region.objects.get(id=1)
# date_str = "2018-03-11"
# temp_date = parse_date(date_str)
# a1 = District(headline="String converted to date", pub_date=temp_date, reporter=user)
# a1.save()
# datetime.date(2018, 3, 11)
# temp_date = datetime.strptime(date_str, "%Y-%m-%d").date()
# a2 = District(headline="String converted to date way 2", pub_date=temp_date, reporter=user)
# a2.save()
# print(a1)
# print(a2)

#=========================order_by qilish=======================================

# qs = Region.objects.order_by('name')
# print(qs)
#
# #=========================order_by qilish=======================================








