from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Account)
admin.site.register(Report)
admin.site.register(Interval)
admin.site.register(Frequency)
admin.site.register(IntradayFrequency)