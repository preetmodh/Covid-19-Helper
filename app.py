from flask import Flask,render_template,request
import requests
app = Flask(__name__, template_folder='template')
@app.route("/",methods=["GET"])
def index():
    res=requests.get('https://corona.lmao.ninja/v2/all?yesterday')
    data=res.json()
    cases="{:,}".format(data['cases'])
    deaths="{:,}".format(data['deaths'])
    todaycases="{:,}".format(data['todayCases'])
    todaydeaths="{:,}".format(data['todayDeaths'])
    todayrecovered="{:,}".format(data['todayRecovered'])
    activecases="{:,}".format(data['active'])
    recovered="{:,}".format(data['recovered'])
    critical="{:,}".format(data['critical'])
    mild="{:,}".format(data['active']-data['critical'])
    outcome="{:,}".format(data['recovered']+data['deaths'])
    return render_template("index.html",todayrecovered=todayrecovered,outcome=outcome,mild=mild,critical=critical,data=data,cases=cases,deaths=deaths,todaycases=todaycases,todaydeaths=todaydeaths,activecases=activecases,recovered=recovered)

@app.route("/Allcountries",methods=["GET","POST"])
def Allcountries():
    res=requests.get('https://corona.lmao.ninja/v2/countries?yesterday&sort')
    datas=res.json()
    return render_template("Allcountries.html",datas=datas)

@app.route("/scountries",methods=["GET","POST"])
def scountries():
    country=''
    country=request.form.get("name")
    res=requests.get('https://corona.lmao.ninja/v2/countries/'+country+'?yesterday')
    data=res.json()
    country=data['country']
    country=country.upper()
    if res.status_code!=200:
        return render_template("error.html")
    else:
        cases="{:,}".format(data['cases'])
        deaths="{:,}".format(data['deaths'])
        todaycases="{:,}".format(data['todayCases'])
        todaydeaths="{:,}".format(data['todayDeaths'])
        todayrecovered="{:,}".format(data['todayRecovered'])
        activecases="{:,}".format(data['active'])
        recovered="{:,}".format(data['recovered'])
        critical="{:,}".format(data['critical'])
        mild="{:,}".format(data['active']-data['critical'])
        outcome="{:,}".format(data['recovered']+data['deaths'])
        return render_template("country.html",country=country,todayrecovered=todayrecovered,outcome=outcome,mild=mild,critical=critical,data=data,cases=cases,deaths=deaths,todaycases=todaycases,todaydeaths=todaydeaths,activecases=activecases,recovered=recovered)
