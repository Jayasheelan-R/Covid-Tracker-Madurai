from flask import Flask,render_template
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://twitter.com/Vijayabaskarofl?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
tweets = soup.find_all("li", attrs={"class":"js-stream-item"})

eee =  []
for tweet in tweets:
    if tweet.find('p',{"class":'tweet-text'}):
        tweet_user = tweet.find('span',{"class":'username'}).text.strip()
        eee.append(tweet.find('p',{"class":'tweet-text'}).text.strip())
        tweet_reply = tweet.find('span',{"class":"ProfileTweet-actionCount"}).text.strip()
        retweets = tweet.find('span', {"class" : "ProfileTweet-action--retweet"}).text.strip()

link = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Tamil_Nadu'
data = urlopen(link).read()
Asoup = BeautifulSoup(data ,'lxml')
lol=Asoup.find_all('table', class_='wikitable plainrowheaders sortable')

A=lol[0].text.split()
tn_recovered = A[27]
tn_cases = A[30]
tn_death = A[28]
tn_active = A[29]
recovered = A[183]
cases = A[181]
death = A[182]
active = A[184]

app = Flask(__name__)

@app.route('/news')
def index():
    return render_template('index.html',eee = eee)

@app.route('/')
def home():
    return render_template('home.html',tn_recovered=tn_recovered,tn_cases=tn_cases,tn_death=tn_death,tn_active=tn_active,recovered=recovered,cases=cases,death=death,active=active)

@app.route('/lol')
def lol():
    return render_template('lol.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/virus')
def virus():
    return render_template('virus.html')

if __name__=="__main__":
    app.run()
