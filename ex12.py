import csv
import sqlite3

with open('players.csv', encoding="utf-8-sig") as csvfile: 
    csv_reader = csv.DictReader(csvfile) 
    fields = csv_reader.fieldnames 
    data = list(csv_reader) 

with open('player_career.csv', encoding="utf-8-sig") as csvfile: 
    csv_reader2 = csv.DictReader(csvfile) 
    fields2 = csv_reader2.fieldnames 
    data2 = list(csv_reader2) 


conn = sqlite3.connect("data_player.db")

cursor = conn.cursor()
# cursor.execute("create table players(ilkid text, firstname text, lastname text, position text, firstseason text, lastseason text, h_feet text, h_inches text, weight)")
# cursor.execute("create table player_career(ilkid text,firstname text,lastname text,leag text,gp text,minutes text,pts text,oreb text,dreb text,reb text,asts text,stl text,blk text,turnover text,pf text,fga text,fgm text,fta text,ftm text,tpa text,tpm text)")

for i in data:
    cursor.execute("insert into players(ilkid, firstname, lastname, position, firstseason, lastseason, h_feet, h_inches, weight) values(:ilkid, :firstname, :lastname, :position, :firstseason, :lastseason, :h_feet, :h_inches, :weight)", i)

for j in data2:
    cursor.execute("insert into player_career(ilkid,firstname,lastname,leag,gp,minutes,pts,oreb,dreb,reb,asts,stl,blk,turnover,pf,fga,fgm,fta,ftm,tpa,tpm) values(:ilkid,:firstname,:lastname,:leag,:gp,:minutes,:pts,:oreb,:dreb,:reb,:asts,:stl,:blk,:turnover,:pf,:fga,:fgm,:fta,:ftm,:tpa,:tpm)", j)

cursor.execute("""select distinct players.firstname, 
 players.lastname, 
 players.h_feet, 
 players.h_inches, 
 player_career.pts 
from players, player_career 
where trim(players.ilkid) = trim(player_career.ilkid) 
and players.h_feet >= 7 
and players.h_inches >= 5 
""")

for row in cursor:
    print(row)

conn.commit()