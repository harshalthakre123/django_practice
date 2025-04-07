# Current Version- django-5.1.7 
#c python compiler is bydefault  compiler for python.
#Django is a Framework (Predefined Structure) used for web development.
#
#def of django:- Danjgo free open source, high level web framework#

#Virtual Environment:- created a virual environment to prevent problems came from versions upgrade.
#   Resolves the problem of no. of pc requirement.
#   permission for multiple version installation.
#   prevent the version upgrade and while upgrading global environment.
#   to create virtual environment OS is responsible and internet is not required.


# Django
#   |--->Create Virtual Environment.
#       |-->open command prompt(cmd)
#       |-->cd.desktop. or if on cloud onedrive.
#               .same directory(folder)
#               ../previous drive
#               D: for d drive
#       |--> mkdir django
#       |-->cd django
#       |-->python -m venv virtualenv(directory name)
#       |-->Virtual environment created.

#   |--->Activation of virtual environment# 
#        in script we have to activate
#cmd           use 1. ./activate
#               2. .\activate
#               3. activate
#cmd       pip install django#
#               Interview Question:- django dependent package
#                   1. asgiref(asyncronous server gateway interface) multiple req at a time is async. ex.websocket
                        # django bydefault work synchronous one req at a time.
#                   2. sqlparse( query related from database and parse is used to convert python to  )
#                   3. tzdata- timezone (worldwide) database
#                   4. django#

# to check the no of packages installed in the django cmd is 
#       pip freeze

# to create a file with requirements printed in it cmd is 
        #pip freeze > requirement.txt(recommended name we can use anything)





#command to create project 
        # command is:- django-admin startproject project(project name)
            # 1. project is outer project folder structure
                    #a. it includes inner project folder structure.
                    #b. manage.py is commandline utility tool used to handle every command of django

# then cd project 
# inside project directory
# in terminal
# py (tab) or file name .\manage.py.
# 
# 
# next command 
# py manage.py runserver 

# note there are two typesz of server which is development(local server) and deployment server
# (default port) code 8000 for django ande 3000 is of react.
# we can change the code no by two ways 
        # static(manually change sourcecode default port) 
        # and dynamic, it is used to run multiple project on different port number. (cmd is:-  py manage.py runserver 6050)


#cmd:- history for previous command list
#  


# Inner project directory 
        #        
                # __init__.py (empty file)
        # servers
                # asgi.py (multiple request or project (asynchronous server gateway -interface).) use web socket.
                #wsgi.py (by default server work on single request(web server gateway(synchronous)interface).)
        
        #settings.py
                #port no.
                # applications
                # authentications
                # database
                #timezone
                #static
                #media, etc etc.
                         #if we type or print (print("Base Information",BASE_DIR)) in settings.py(17th line the address of current project is printed)
        # urls
        # after project run on server (browser) 8000/admin/ 
                # py manage.py runserver
                # py manage.py migrate (for table creation and storing data of superuser, related to sqlite.)
                # py manage.py  createsuperuser (to create main user)
                # py manage.py runserver (and login through admin and pass-admin)



# App Creation commands.


















# created app
# inside app


# ORM (object Relational mapple) conversion of both process migrations 
# 
# 
#                                                                     cmd-  py mangange.py migrate
#                                                               (conversion of query to db table creation)  
                                                                                #      |
# modals.py(responsible fortable structure)        initial0001.py
# (file name, work related to database)             (file name)
# python code----------------|------------------->query--------------------------------|--------->dbsqlite
#                            |
#        cmd-  py manage.py makemigrations
#            (query Creation to respected db different compilers)





# admin.py=====it is responsible for admin panel , you have to register your work.
# 
# apps.py-==== confriguration file we dont have to work on it. confriguration between app and project
# 
# note:- do not rename folder name created by command.
# 
# text.py ==== testing regarding files 
# 
# views.py ==== logic implementation (any operations ) 






#App is used to create particular sections and it do not affect the other part while upgrading
# after activating django 
#       py manage.py startapp <appname>















# to on server
# =================================================================================================
# commandline--LIFE CYCLE===============================================================================
# 
# life cycle of command line
# commandline entry point---  [manage.py]----->[settings.py]------>[urls.py]------>[wsgi.py] 
# 
# now for request response the entry point/exit point is---[wsgi.py]
# 
# 
# to break server control+c.
# 



# random module--kand krne k liye




# life cycle for request response.
# Request response/Django --Life cycle.

#[wsgi.py]  req entry point as wel as exit point (jha se req aayege vhi pe response bhi diya jayega)

#[wsgi.py]-------[settings.py]--------[urls.py]---------------[views.py]<--------------->[modules.py] #
#                                                               |-->[templates/]

# this is MVT-- Model View Template Pattern.
# [views.py]<--------------->[modules.py] #
#                                                               |-->[templates/](dtl django templating language)








#
# 
# 
# 
# 
# settings me installed app me app register kiya then,
# urls me jayege, in path
# path(route, fun name or class name(from views.py), temp.related ) 

# route after 8000/home




#types of responses.
# 
# |--HttpResponse()---->text-content(html)
# |--JsonResponse()---->Json-Content
# |--render()----> HTML-Page
# |--redirect()---->URL- Page
# | #