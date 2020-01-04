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
            if (int(request.POST['id'])//10000==10):
             g=game_list(game_id=request.POST['id'],team1_score="0/0",team2_score="0/0")
            else:
                 g=game_list(game_id=request.POST['id'])
            g.save()
        if( request.POST['type']=="clock"):
            obj=match_list.objects.filter(game_id=request.POST['id'])[0]
            obj.ac_start_time=request.POST['data']
            obj.save()
        if( request.POST['type']=="end"):
            obj=match_list.objects.filter(game_id=request.POST['id'])[0]
            obj.live_status=False
            obj.end_status=True
            obj.final_discription=request.POST['comments']
            obj.winner=request.POST['winner']
            g=game_list.objects.filter(game_id=request.POST['id']).order_by('-id')[0]
            obj.final_team1=g.team1_score
            obj.final_team2=g.team2_score
            obj.save()
            return redirect("/logedin")   
    else:
        return redirect("/login/vol/logedin")        
    return HttpResponse("null")

def update(request):#for cricket and basketball(10 and 11)
    p=request.POST
    
    if(User.is_authenticated and request.method=='POST'):
        
        if(p['request'] == '1' and int(p['id'])//10000!=12):
            ch=game_list.objects.filter(game_id=p['id']).order_by('-id')[0]
            a=0
            b=0    
            if(p['team']=='1'):
             
             team1_score=ch.team1_score.split('/')
             ch.team1_score=str(int(p['value'])+int(team1_score[0]))
             if(int(p['id'])//10000==10):
                wkt=str(int(team1_score[1])+int(p['wicket']))
                ch.team1_score=ch.team1_score+"/"+wkt
                ch.overs_1=p['overs']
             a=ch.team1_score
             b=ch.overs_1
            if(p['team']=='2'):
             team2_score=ch.team1_score.split('/')
             ch.team2_score=str(int(p['value'])+int(team2_score[0]))
             if(int(p['id'])//10000==10):
                wkt=str(int(team2_score[1])+int(p['wicket']))
                ch.team2_score=ch.team2_score+"/"+wkt
                ch.overs_2=p['overs']
            
             a=ch.team2_score
             b=ch.overs_2
            

            obj=game_list(game_id=ch.game_id,team1_score=ch.team1_score,team2_score=ch.team2_score,overs_1=ch.overs_1,overs_2=ch.overs_2)
            obj.save()
            return JsonResponse({'status':"success",'score1':ch.team1_score,'score2':ch.team2_score,'overs':b})

        if(p['request']=='1' and int(p['id'])//10000==12):
            ch=game_list.objects.filter(game_id=p['id']).order_by('-id')[0]
            set1=ch.team1_score.split(' ')
            set2=ch.team2_score.split(' ')
            if(p['team']=='1'):
                n=len(set1)-1
                set1[n]= int(set1[n])+int(request.POST['value'])
                ch.team1_score=set1[0]
                for i in range(1,n+1):
                   ch.team1_score+=(" "+set1[i])
                a=ch.team1_score
                c=ch.set
            if(p['team']=='2'):
                n=len(set2)-1
                set2[n]= int(set2[n])+int(request.POST['value'])
                ch.team2_score=""
                for i in range(0,n+1):
                   ch.team2_score+=(" "+str(set2[i]))
                a=ch.team2_score
                c=ch.set
            obj=game_list(game_id=ch.game_id,team1_score=ch.team1_score,team2_score=ch.team2_score,set=ch.set)
            obj.save()
            return JsonResponse({'status':"success",'score1':ch.team1_score,'score2':ch.team2_score,'set':c})
        if(p['request']=='2'):
            ch=game_list.objects.filter(game_id=p['id']).order_by('-id')[0]
            ch.delete()
            ch=game_list.objects.filter(game_id=p['id']).order_by('-id')[0]
            if(p['team']=='1'):
             a=ch.team1_score
             b=ch.overs_1
            if(p['team']=='2'):
             a=ch.team2_score
             b=ch.overs_2
            c=ch.set
            return JsonResponse({'status':"success",'score1':ch.team1_score,'score2':ch.team2_score,'overs':b,'set':c})
        if(p['request'] == '3'):
            print("oo")
            ch=game_list.objects.filter(game_id=p['id']).order_by('-id')[0]
            ch.set=int(ch.set)+1
            ch.team1_score+=" 0"
            ch.team2_score+=" 0"
            obj=game_list(game_id=ch.game_id,team1_score=ch.team1_score,team2_score=ch.team2_score,set=ch.set)
            obj.save()
            return JsonResponse({'status':"success",'score1':ch.team1_score,'score2':ch.team2_score,'set':ch.set})
def vol_logedin(request):
    User=request.user
    
    if(User.is_authenticated and request.method!='POST'):
        game=match_list.objects.filter(assignment_to=User.username)
        
        return render(request,"admin.html",{'dat':User,'type':"volunteer",'assign':game})
    if(User.is_authenticated and request.method=='POST'):
        
        c=int(request.POST['id'])//10000
        ch=game_list.objects.filter(game_id=request.POST['id']).order_by('-id')
        dat=0
        if(len(ch)):
            dat=ch[0]
        game=match_list.objects.filter(game_id=request.POST['id'])[0]
        
        return render(request,"games.html",{'c': c,'game':game,'dat':dat})

def live(request):

    daw = match_list.objects.filter(live_status=True,end_status=False)
    if(request.method=='POST'):
        l=[]
        for  i in daw:
            obj=game_list.objects.filter(game_id=i.game_id).order_by('-id')[0]
            l.append({'id':i.game_id,'score1':obj.team1_score,'score2':obj.team2_score})
        return JsonResponse(l,safe=False)
    return render(request,"livematch.html",{'daw':daw,'ldaw':len(daw)})    


def login(request):
     if(request.method=='POST'):
      username=request.POST['username']
      password=request.POST['pass']
      user=auth.authenticate(username=username,password=password)
      
      if(user is not None):
         auth.login(request,user)
         return redirect('/login/vol/logedin')
      else:
            return render(request,'adminlogin.html',{'error':'True'})
     else:
          return render(request,'adminlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'adminlogin.html')
