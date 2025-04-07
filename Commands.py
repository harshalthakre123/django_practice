# create Folder:
    # cmd:- mkdir django

# inside folder :
# Create env (virtual environment)by:
    # py -m venv myenv #
# now inside scripts in terminal activate it by: cd tab-button then enter
    # ./activate
# come to rootfolder by:
    # cd ../../
# installing django by:
    # pip install django
        # some packages installed

#come to root folder:

#Creating project by:  
    #django-admin startproject <projectname>

#so, now inside project: to create app or runserver etc.
    #py manage.py startapp <app_name>
    #and
    #py manage.py runserver 
# 




# for dom in django.

# Now in settings inside installed Apps register your app.
# add---->"App name"

# now in urls.py inside urls path
# set path
# path("rootname", views.<fun/class name>, name="root name")

# now on views.py write your functions/classes or code
# to get response
# 1. HttpResponse for html codes
# 2. JsonResponse for json data
# 3. render for html page transfer 
# render(request, index.html(htmlpage), data inside html page(only transfer data in the form of dictionary))
# #data from db cames in the form of list of distionary or  , 
# 4. redirect url page or links.