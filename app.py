from flask import Flask,render_template,request,jsonify
import requests
app = Flask(__name__, template_folder='template')
@app.route("/",methods=["GET"])
def index():
    res=requests.get('https://disease.sh/v3/covid-19/all?yesterday=true')
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
    res=requests.get('https://disease.sh/v3/covid-19/countries?yesterday=true&sort')
    datas=res.json()
    return render_template("Allcountries.html",datas=datas)

@app.route("/scountries",methods=["GET","POST"])
def scountries():
    country=''
    country=request.form.get("name")
    res=requests.get('https://disease.sh/v3/covid-19/countries/'+country+'?yesterday=true')
    data=res.json()
    country=data['country']
    if res.status_code!=200:
        return render_template("error.html")
    else:
        country=country.upper()
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

@app.route("/api/world",methods=["GET"])
def API_index():
    res=requests.get('https://disease.sh/v3/covid-19/all?yesterday=true')
    data=res.json()
    new_data={}
    new_data['cases']="{:,}".format(data['cases'])
    new_data['deaths']="{:,}".format(data['deaths'])
    new_data['todayCases']="{:,}".format(data['todayCases'])
    new_data['todayDeaths']="{:,}".format(data['todayDeaths'])
    new_data['todayRecovered']="{:,}".format(data['todayRecovered'])
    new_data['active']="{:,}".format(data['active'])
    new_data['recovered']="{:,}".format(data['recovered'])
    new_data['critical']="{:,}".format(data['critical'])
    new_data['mild']="{:,}".format(data['active']-data['critical'])
    new_data['outcome']="{:,}".format(data['recovered']+data['deaths'])
    return jsonify(new_data)

@app.route("/api/allcountries",methods=["GET","POST"])
def API_Allcountries():
    res=requests.get('https://disease.sh/v3/covid-19/countries?yesterday=true&sort')
    data=res.json()
    return jsonify(data)

@app.route("/api/scountries/<country>",methods=["GET","POST"])
def API_scountries(country):
    res=requests.get('https://disease.sh/v3/covid-19/countries/'+country+'?yesterday=true')
    data=res.json()
    country=data['country']
    if res.status_code!=200:
        return render_template("error.html")
    else:
        new_data={}
        new_data['country']=country.upper()
        new_data['cases']="{:,}".format(data['cases'])
        new_data['deaths']="{:,}".format(data['deaths'])
        new_data['todayCases']="{:,}".format(data['todayCases'])
        new_data['todayDeaths']="{:,}".format(data['todayDeaths'])
        new_data['todayRecovered']="{:,}".format(data['todayRecovered'])
        new_data['active']="{:,}".format(data['active'])
        new_data['recovered']="{:,}".format(data['recovered'])
        new_data['critical']="{:,}".format(data['critical'])
        new_data['mild']="{:,}".format(data['active']-data['critical'])
        new_data['outcome']="{:,}".format(data['recovered']+data['deaths'])
        return jsonify(new_data)
        


@app.route("/api/vaccination",methods=["GET","POST"])
def API_vacination():
    res=requests.get('https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=30&fullData=false')
    data=res.json()
    return jsonify(data)

@app.route('/api/vaccination/<country>',methods=["GET","POST"])
def API_single_vacination(country):
    res=requests.get('https://disease.sh/v3/covid-19/vaccine/coverage/countries/'+country+'?lastdays=30&fullData=false')
    data=res.json()
    return jsonify(data)

@app.errorhandler(500)
def page_not_found():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=False)