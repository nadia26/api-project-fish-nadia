from flask import Flask,request,url_for,redirect,render_template
import json, urllib2

app=Flask(__name__)

@app.route("/")
def index():
    return "hi"
    #return render_template("index.html")

#weird urllib2 error
@app.route("/q")
@app.route("/q/<query>")
def q(query="Dynamite"):
    url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=re8z35f3uhrea4vc46jz4wcg&q=%s"
    url = url%(query)
    request = urlllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    page = ""
    for r in d['movies']:
        if 'ratings' in r.keys():
            page = page + (r['ratings'][0])#returns critics score
    return page

if __name__=="__main__":
   app.debug=True
   app.run()
