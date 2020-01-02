from django.shortcuts import render,redirect
from django.http import HttpResponse,request,JsonResponse
from .models import match_list,game_list
from datetime import datetime
from django.contrib.auth.models import User,auth
import copy


def game(request):
    if(request.method=='POST'):
        if( request.POST['type']=="start"):
            obj=match_list.objects.filter(game_id=request.POST['id'])[0]
            obj.live_status=True
            obj.save()
            g=game_list(game_id=request.POST['id'])
            g.save()
        if( request.POST['type']=="clock"):
            obj=match_list.objects.filter(game_id=request.POST['id'])[0]
            obj.ac_start_time=request.POST['data']
            obj.save()
    else:
        request.redirect("/logedin")        
    return HttpResponse("null")

def update(request):
    p=request.POST
    
    if(User.is_authenticated and request.method=='POST'):
        print(p['request'])
        if(p['request'] == '1'):

            ch=game_list.objects.filter(game_id=p['id']).order_by('-id')[0]
        
            if(p['team']=='1'):
             ch.team1_score=int(p['value'])+int(ch.team1_score)
             a=ch.team1_score
            if(p['team']=='2'):
             ch.team2_score=int(p['value'])+int(ch.team2_score)
             a=ch.team2_score
            obj=game_list(game_id=ch.game_id,team1_score=ch.team1_score,team2_score=ch.team2_score)
            obj.save()
            return JsonResponse({'status':"success",'score':a})

def vol_logedin(request):
    User=request.user
    
    if(User.is_authenticated and request.method!='POST'):
        game=match_list.objects.filter(assignment_to=User.username)
        
        return render(request,"admin.html",{'dat':User,'type':"volunteer",'assign':game})
    if(User.is_authenticated and request.method=='POST'):
        
        c=int(request.POST['id'])//10000
        ch=game_list.objects.filter(game_id=request.POST['id']).order_by('-id')[0]
        game=match_list.objects.filter(game_id=request.POST['id'])[0]
        return render(request,"games.html",{'c':11,'game':game,'dat':ch})

def live(request):
    daw = match_list.objects.filter(live_status=True,end_status=False)
    if(request.method=='POST'):
        l=[]
        for  i in daw:
            obj=game_list.objects.filter(game_id=i.game_id)[0]
            l.append({'id':i.game_id,'score1':obj.team1_score,'score2':obj.team2_score})
        return JsonResponse(l,safe=False)
    return render(request,"livematch.html",{'daw':daw,'ldaw':len(daw)})    

