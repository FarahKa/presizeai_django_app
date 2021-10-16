from django.shortcuts import render
from shop.models import Scan
from datetime import date
from django.shortcuts import render
import os
import random 
import string
import configparser

# put configuration from config.ini file into variables
cwd= os.getcwd()
config = configparser.ConfigParser()
config.read(cwd + '/config.ini')
MAX = int(config.get('id_config', 'MAX'))
MIN = int(config.get('id_config', "MIN"))
TRIALS = int(config.get("id_config", "TRIALS"))


def get_id_with_fixed_size(size):
    id =  ''
    # loop and get one random alphanumeric character at a time
    for _ in range(size):
        id = id + (random.SystemRandom().choice(string.ascii_lowercase + string.digits))
    return id

def get_unique_id(MAX, MIN, TRIALS):
    # loop trial times 
    for _ in range(TRIALS):
        # get cryptographly safe random int (underlying os.urandom()) for the size of the id
        N = random.SystemRandom().randint(MIN, MAX)
        # get random id with N size 
        id =  get_id_with_fixed_size(N)
        # check if id is unique or not
        scan = Scan.objects.filter(sizeid = id).first()
        if scan is None:
            return id
    id = get_id_with_fixed_size(N+1)
    MAX = MAX +1;
    increment_max(MAX)
    return id
        
def increment_max(MAX):
    MAX = MAX +1
    config.set("id_config", "MAX", MAX)

def basic(request):
    #just return the user to the index page
    return render(request,"shopfront.html",{'result':''})  

# View used to create the size id.

def createScan(request):
    #creating the id
    id = get_unique_id(MAX, MIN , TRIALS)
    scan = Scan.objects.create(sizeid=id, last_activity=date.today())
    return render(request,"shopfront.html", {'result':'Your new size ID is %s'%(scan.sizeid)} )


def getScan(request):
    #checks if the scan exists and if it is still usable

    #get the desired scan
    scan = Scan.objects.filter(sizeid = request.POST.get('sizeid_input')).first()
    if scan is None:
        return render(request,"shopfront.html", {'result':'This size id was not found'})

    #check if the scan is usable
    #get number of days between today and last use
    difference = date.today() - scan.last_activity
    days = difference.days
    if days > 60:
        #return unusable template
        return render(request,"shopfront.html", {'result':'This size id has expired. Create a new one.'})
    else:
        #update last activity
        scan.last_activity = date.today()
        scan.save()
        #return scan
        return render(request,"shopfront.html", {'result':'Awesome, here is your scan information for the size id you provided ...'})


    
