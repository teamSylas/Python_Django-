from django.shortcuts import render

# Create your views here.
def list(request):
  # posts = []
    # nous allons passer de la liste au dictionnaire 
   # posts = ['First Post', 'Seconde article','le troisieme table']
   posts = [
       {'id':1,'title': 'First Post','body':'this is my 1eme poste where i am use'},
       {'id':2,'title': 'Second Post','body':'this is my 2eme poste where i am use'},
       {'id':3,'title': 'Third Post','body':'this is my 3 eme poste where am use'},
       {'id':4,'title': 'First Post','body':'this is my 4 eme poste where i am use'},
       {'id':5,'title': 'First Post','body':'this is my 4eme poste where i am use'},
   ]
   return render (request,'blog/index.html',{'posts':posts})

def show(request,id):
    return render (request, 'blog/show.html')