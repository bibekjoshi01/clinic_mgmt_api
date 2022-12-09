from django.db import models

# Create your models here.

class Service(models.Model):
    img = models.ImageField(null=True, upload_to='images/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Doctor(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    fa_link = models.URLField(max_length=500, blank=True, null=True)
    tw_link = models.URLField(max_length=500, blank=True, null=True)
    in_link = models.URLField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Health_Package(models.Model):
    img = models.ImageField(null=True, upload_to='images/')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    description = models.TextField()
    note = models.CharField(max_length=250, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Test(models.Model):
    img = models.ImageField(null=True, upload_to='images/')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    img = models.ImageField(null=True, upload_to='images/')
    name = models.CharField(max_length=50)
    profession = models.CharField(blank=True, null=True, max_length=100)
    feedback = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Accreditation(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100)
    img = models.ImageField(null=True, upload_to='images/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Payment_Method(models.Model):
    title = models.CharField(blank=True, null=True, max_length=30)
    img = models.ImageField(null=True, upload_to='images/')
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class FAQs(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQs"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question[:50]
    

#-------------------------------------------------------------------------------------------------------
