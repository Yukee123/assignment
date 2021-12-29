from django.shortcuts import render
from assignmentapp.models import Types_Of_Games
from django.db import connection
# Create your views here.
def insert_operation(request):
    try:
        my_cursor = connection.cursor()
        records = Types_Of_Games.objects.all()
        my_dict = {'records':records}

    except Exception as msg:
        print(msg)

    finally:
        my_cursor.close()
        connection.close()

    return render(request,'assignmentapp/Types_Of_Games.html',context=my_dict)