from django.db import models

class Subscription(models.Model):
    title = models.CharField(max_length = 100, blank = True, default = '')
    price = models.IntegerField()
    frequency = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Tea(models.Model):
    subscription = models.ManyToManyField('Subscription', related_name='teas', blank=True)
    title = models.CharField(max_length = 100, blank = True, default = '')
    description = models.TextField()
    temperature = models.IntegerField()
    brew_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Customer(models.Model):
    subscriptions = models.ManyToManyField(Subscription, through='CustomerSubscription')
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class CustomerSubscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    active = models.BooleanField(help_text = 'Active status', default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

