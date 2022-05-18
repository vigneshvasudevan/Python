'''
Setting up Django env

1. To install Django: python3 -m pip3 install Django or pip3 install Django
2. To check Django ver : python3 -m django --version
3. Add Django binaries to PATH environment variable : export PATH=$PATH:/Users/vigneshv/Library/Python/3.8/bin/
4. To create a sample project: cd <DjangoProjectPath>;
        python3 -m django-admin startproject myFirstWebsite (or)
        django-admin startproject myFirstWebsite


5. Now run the webserver:
        django-admin runserver myFirstWebsite <optionallyPortNumber>
        
        or 
        cd <pathToYourDjangoProject>
        python3 manage.py runserver <optionallyPortNumber>
        
        Note: Default port 8000


6. Update DB from SQLite to PostgreSQL
        By default, Django is configured to use SQLite as its backend. 
        To use Postgres instead, <PathToDjangoProject>/settings.py” needs to be updated:


        DATABASES = {

                'default': {

                        'ENGINE': 'django.db.backends.postgresql_psycopg2',

                        'NAME': ‘<db_name, make sure this DB exists in postgres>’,

                        'USER': '<db_username>',

                        'PASSWORD': '<password>',

                        'HOST': '<db_hostname_or_ip>',

                        'PORT': '<db_port>',

                }
        }
        
        e.g)
        
        DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': "mock2",
                        'USER': 'vigneshv',
                        'PASSWORD': 'password',
                        'HOST': 'localhost',
                        'PORT': '5432',
                }
        }
        
    
8. Add superuser to your website 
        run this command
                python manage.py createsuperuser
        
        and provide below details
                Username (leave blank to use 'root'): <somename>

                Email address: <youremail@gmail.com>

                Password: <somepassword>

                Password (again): <somepassword>

                Superuser created successfully.
                
9. Now start the server again

        python3 manage.py runserver <optionallyPortNumber>
        
        
10. Now to verify super user works
        visit url : “127.0.0.1:8000/admin
        
        Note: 8000 here refers to the default port
        
        Login page should appear
        
        
11. Migrate database from SQLite to PostgreSQL:
        Django was designed with user access in mind, so by default a Django application will create a database schema involving users, groups, and permissions. 
        To create the schema, generate a migration and run it.

        python3 manage.py makemigrations
        python3 manage.py migrate       
        
12. runserver now to check everything is intact
        python3 manage.py runserver
        Let’s make the app for 'User'
        
        Syntax: python manage.py startapp <AppNameGoesHere>
        Example : python3 manage.py startapp User
        
        This will create a folder 'User' with few files

13. Add 'User' application to settings.py
        e.g) 'User.apps.UserConfig'
 
14. Create the register form
        cd to  <projectPath>/<AppName>/forms.py 
        create a new file with name forms.py
        Create a user registration form here


15. Create a register.html file
        cd to  <projectPath>/<AppName>/
        mkdir templates 
        cd templates
        create a new file with name register.html
        
16. Add function at <projectPath>/<AppName>/views.py to register user

17. Now create an end point and add the function created at step16 as callback function
        cd <projectPath>
        At urls.py, add 
                urlpatterns = [
                        ...
                        path('register/', views.register_request),
                        ...
                ]
                
18. pip3 install django-crispy-forms

19. runServer and navigate to localhost/register


'''


# Mini-project ideas:
# 
# 1. Add login and logout support
# 2. After user successfully logs in, allow users to download an image
# 3. Create a page where admin can add products
# 4. Allow users to view the products
# 5. Allow users to place orders (without handling concurrency)
# 6. Create a page to show user order history
# 