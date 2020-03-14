from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webbot import Browser

from flask import Flask, request, render_template
import time

from waitress import serve

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route('/act', methods=['POST'])
def act():
  # GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
  # CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
  # chrome_options = webdriver.ChromeOptions()
  # chrome_options.add_argument('--disable-gpu')
  # chrome_options.add_argument('--no-sandbox')
  # chrome_options.binary_location = GOOGLE_CHROME_PATH
  # browser = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)
  url = request.form['url']
  user = request.form['username']
  password = request.form['password']
  #browser.get(url)
  web = Browser()
  web.go_to(url)
  web.type(user , into='Email')
  web.type(password , into='Password', xpath = "//*[@id='tblActivityTleDesc']/tbody/tr[4]/td[1]/table[2]/tbody/tr[4]/td[3]/input") # specific selection
  web.click(xpath= "//*[@id='tblActivityTleDesc']/tbody/tr[4]/td[1]/table[2]/tbody/tr[4]/td[4]/input") # you are logged in ^_^
  while True:
    web.click(xpath = "//*[@id='cardDiv']")

  return render_template("home.html")

if __name__ == "__main__":
  serve(app, host = '0.0.0.0', port = 8080)
  # app.run(debug=True)