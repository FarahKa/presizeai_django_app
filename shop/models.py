from django.db import models

# The body scan information and size ID
class Scan(models.Model):
    #this is the size ID
    sizeid = models.CharField(max_length=6)
    #we assume this model also contains the scan information
    #last activity lets us know if this scan is still usable. If it exceeds 60 days ago
    #we can not use this scan anymore and need to create a new one
    last_activity = models.DateField()
    


