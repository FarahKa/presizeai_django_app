# Size ID app


Hello,
This is my presize.ai technical test app!
It's an app aimed to generate unique, usable size ids for users.
It has a simple HTML template hooked up with views. The views communicate with the models and size id generation algorithm.


I made it using the following :
Python 3.9.1, Django and the configparser library.
```
pip install  Django == 3.2.8
pip install configparser
```

The app you need to run is the shop app.
Go to the manage.py root and run

```
python3 manage.py runserver
```

This should run the server seamlessly.
Then access http://127.0.0.1:8000/ to check out the index page:

The index page gives you 2 options:

![index](https://imgur.com/AdzdEDP.png)

- You already have a size id and input it:
It looks for the scans that correspond to that size id in the database and gives them back to you. If that size ID does not exist, or if it has expired, you will not be able to retrieve a scan.

![yes](https://imgur.com/VdVXfhB.png)
![no](https://imgur.com/lwwDPBr.png)
- You do not have a size id yet: It generates a size id for you and displays it.
![gen](https://imgur.com/DxvXLx2.png)

For the SizeID generation, I did some research and found that, cryptography wise, the most safe and random function to use would be os.urandom(). So, I made sure to use random.SystemRandom() which has an underlying os.urandom() and therefore is very random. I randomized the length of the SizeID and its contents seperately to make it harder to crack.
In order to make the SizeID generation scalable, I created a config.ini file. This file contains 3 variables : MIN, MAX & TRIALS.
MIN (currently set to 3) = the minimum length of the SizeID.
MAX (currently set to 6) = the maximum length of the SizeID.
TRIALS (currently set to 10) = the number of times that the algorithm would try to create a unique & random ID, before deciding to create a random ID with the length MAX+1 (which is garanteed to be unique) and then incrementing MAX globally.
I hope my work is to your liking. Please do not hesitate to give me feedback.
