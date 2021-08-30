
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json
import get_data
from apicall import call
import decimal

app = Flask(__name__, )

db_name = 'mydb'
client = None
db = None


# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

def get_list(inp):
    final=[]
    for i in inp:
        final.append(inp[0])
    return final

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/city",methods=['GET','POST'])
def city():
    db=get_data.connect()
    if db!=False:
        teams=get_data.ret_data(db,'SELECT DISTINCT "team1" FROM "matches" WHERE "team1" IS NOT NULL AND "season"=2019 ORDER BY "team1"')
        teams2=get_data.ret_data(db,'SELECT DISTINCT "team1" FROM "matches" WHERE "team1" IS NOT NULL AND "season"=2019 ORDER BY "team1"')
        venue=get_data.ret_data(db,'SELECT DISTINCT "venue","city" FROM "matches" WHERE "venue" IS NOT NULL ORDER BY "city"')
        umpire1=get_data.ret_data(db,'SELECT DISTINCT "umpire1" FROM "matches" WHERE "umpire1" IS NOT NULL ORDER BY "umpire1"')
        umpire2=get_data.ret_data(db,'SELECT DISTINCT "umpire2" FROM "matches" WHERE "umpire2" IS NOT NULL ORDER BY "umpire2"')
        umpire3=get_data.ret_data(db,'SELECT DISTINCT "umpire3" FROM "matches" WHERE "umpire3" IS NOT NULL ORDER BY "umpire3"')
        toss_winner=get_data.ret_data(db,'SELECT DISTINCT "toss_winner" FROM "matches" WHERE "toss_winner" IS NOT NULL AND "season"=2019 ORDER BY "toss_winner"')
        toss_decision=get_data.ret_data(db,'SELECT DISTINCT "toss_decision" FROM "matches" WHERE "toss_decision" IS NOT NULL ORDER BY "toss_decision"')
        cities=get_data.ret_data(db,'SELECT DISTINCT "city" FROM "matches" WHERE "city" IS NOT NULL ORDER BY "city"')
    return render_template("predictor.html",cities=cities,teams=teams,teams2=teams2,venue=venue,umpire1=umpire1,umpire2=umpire2,umpire3=umpire3,toss_winner=toss_winner,toss_decision=toss_decision)

@app.route("/submit",methods=['POST','GET'])
def submit():
    if request.method=="POST":
        data=request.form
        data=data.to_dict(flat=False)
    winner,score=call(data)
    decimal.getcontext().rounding = decimal.ROUND_DOWN
    score = decimal.Decimal(score)
    score=float(round(score,4))
    return render_template("output.html",winner=winner, score=score)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
