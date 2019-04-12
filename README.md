Main Purpose:
	Main purpose of this project is to show how to simple crud works in Django. We are using following software:
	
	Django 2.2
	Postgres
	
	Operating System: 
	
	Ubuntu 18
	
In order to get it to work - you will need to install Postgres on your Ubuntu server
You will need to create a database (free to name whatever you want). 
Once your database is up and running, you will need to set django project's setting. In our cash Django Project is called oscarecom and application is called lswebapi. 

Settings.py file exists in oscarecom/oscarecom/settings.py

Set the host (IP address / Cname) under ALLOWED_HOSTS

	ALLOWED_HOSTS = ['<YOUR IP ADDRESS / HOST NAME>']

Put your database information here:

	DATABASES = {
 	   	'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': '',
		'USER': '',
		'PASSWORD': '',
		'HOST':''
	    	}
	}
	
You can access the application by browsing to http://<YOUR IP ADDRESS / CNAME>/

Let me know if you have any questions/feedback
