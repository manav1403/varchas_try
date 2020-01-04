from django.db import models
from datetime import date

# Create your models here


class match_list(models.Model):
    team1=models.CharField(max_length=100)
    team2=models.CharField(max_length=100)
    game_name=models.CharField(max_length=20)
    game_type=models.CharField(max_length=20)
    game_date=models.DateField(default=date.today)
    game_time=models.TimeField(default='00:00')
    ac_start_time=models.IntegerField(default=0)
    live_status=models.BooleanField(default=False)##false means match not done yet//true match done
    match_place=models.CharField(max_length=100)
    end_status=models.BooleanField(default=False)##false means match not started//true means match started
    game_id=models.IntegerField(default=0000)#code aabbcc
    assignment_to=models.CharField(max_length=100,default="NIL")
    final_discription=models.CharField(max_length=100,blank=True)
    winner=models.CharField(max_length=100,blank=True,null=True)
    final_team1=models.CharField(max_length=20,blank=True,null=True) 
    final_team2=models.CharField(max_length=20,blank=True)
    invisble_comments=models.CharField(max_length=100,blank=True,null=True)


class team_data(models.Model): #list of all teams
    team_name=models.CharField(max_length=100)
    team_game=models.CharField(max_length=100)

###########     table for matches    ####################################

class game_list(models.Model):
    game_id=models.IntegerField(default=0)
    team1_score=models.CharField(max_length=40,default="0")
    overs_1=models.DecimalField(default=0.0,max_digits=4,decimal_places=2)
    team2_score=models.CharField(max_length=40,default="0")
    overs_2=models.DecimalField(default=0.0,max_digits=4,decimal_places=2)
    set=models.IntegerField(default=1)
    comments=models.CharField(max_length=40)
 

