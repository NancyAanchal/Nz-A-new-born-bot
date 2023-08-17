from django.shortcuts import render
from django.http import HttpResponse
from . import Nz_the_bot
import os


def index(request):
    return render(request, 'shop/index.html')
    


def getResponse(request):
    user_input = request.GET.get('user_input')
   
    f=open("Chat/support_files/need_to_learn.txt","r")
    need_to_learn=f.readline()
    f.close()
        
    if need_to_learn=="True":
       
        f=open("Chat/support_files/last_input.txt","r")
        last_input=f.readline()
        f.close()
        response= Nz_the_bot.new_ans(last_input, user_input)
        os.remove("Chat/support_files/last_input.txt")

        f=open("Chat/support_files/need_to_learn.txt","w")
        f.write("False")
        f.close()

    else:
        response= Nz_the_bot.chat_bot(user_input)

        if response==("I don't know the response. Can you teach me?"):
            
            f=open("Chat/support_files/need_to_learn.txt","w")
            f.write("True")
            f.close()
            
            f=open("Chat/support_files/last_input.txt","w")
            f.write(user_input)
            f.close()

    return HttpResponse(response)
    