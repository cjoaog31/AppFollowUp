from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class IntradayFrequency(models.Model):
	intraday_frecuency_name = models.CharField(max_length=20)

	def __str__(self):
		return self.intraday_frecuency_name

class Interval(models.Model):
	interval_name = models.CharField(max_length=20)
	initial_time = models.TimeField('interval ini')
	end_time = models.TimeField('Interval end')

	def __str__(self):
		return self.interval_name

class Frequency(models.Model):
	frecuency_name = models.CharField(max_length=20)

	def __str__(self):
		return self.frecuency_name

class Report(models.Model):
	report_name = models.CharField(max_length=50)
	report_format = models.CharField(max_length=50)
	weekly_frecuency = models.ForeignKey(Frequency, null=True, on_delete=models.SET_NULL, default=True)
	interval = models.ForeignKey(Interval, null=True, on_delete=models.SET_NULL)
	frequency = models.ForeignKey(IntradayFrequency, null=True, on_delete=models.SET_NULL)
	account = models.ForeignKey('Account',on_delete=models.CASCADE)

	def __str__(self):
		return self.report_name

class FollowUp(models.Model):
	follow_date = models.DateField('follow date')
	report = models.ForeignKey(Report, on_delete=models.CASCADE)
	report_interval = models.ForeignKey(Interval, on_delete=models.CASCADE)
	report_time = models.TimeField('report time')
	reported_on_time = models.BooleanField()


	def __str__(self):
		return self.follow_date + " " + self.on_time

class Account(models.Model):
	account_name = models.CharField(max_length=50)

	def __str__(self):
		return self.account_name

class Email(models.Model):
	subject = models.CharField(max_length=60)
	received_date_time = models.DateTimeField('received date time')
	sender = models.CharField(max_length=30)

	def __str__(self):
		return self.subject
