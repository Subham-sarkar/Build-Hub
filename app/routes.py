from app import app
from flask import render_template, flash, request, redirect, url_for, session
from cms import CONTENT, INDEXP, DASHBOARD, CHART_DATA, CHART_WEEK
from dbconnect import connection
import os
from functools import wraps
import gc
from stringht import mstr, dstr
from DHash import makeHash, findHash
from firstpage import First
from mypro import mypro
from deletefile import deletef
from searchbyl import search_language

@app.route('/', methods = ["GET", "POST"])
@app.route('/index/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        key = request.form['search']
        author = request.form['author']
        code = findHash(key, author)
        if(code == False):
            flash("File Not found")
            return redirect(url_for('search'))
        code = dstr(code)
        return render_template('searchFile.html', code = code, key = key, CONTENT = CONTENT, DASHBOARD = DASHBOARD)
    l = list()
    l = First()
    return render_template('index.html',CONTENT = CONTENT, INDEXP = INDEXP,l = l)

@app.errorhandler(404)
def erroepage(e):
    return render_template('404.html') 

@app.errorhandler(500)
def erroepages(e):
    return render_template('500.html')

@app.route('/login/', methods = ["GET", "POST"])
def login_page():
 
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # check the credentials

            fname = open("reg.txt","r")
            data = fname.read()
            d = dict()
            data = data.split("$")
            data = data[1:]
            for record in data:
                temp = record.split(',')
                user = temp[0].split('=')[1]
                passwd = temp[1].split('=')[1]
                d[user] = passwd
            if username in d.keys():
                #valid user
                if d[username] == password:
                    session['logged_in'] = True
                    session['username'] = username
                    flash("Successfully logged in as "+username)
                    return redirect(url_for('home'))
                    
                else:
                    flash("wrong credentils")
                    return redirect(url_for('login_page'))
            else:
                #username not exist
                flash("wrong credentials")
                return redirect(url_for('login_page'))
            
                
            
            # if username == 'Nishchal' and password == 'Nishchal':
            #     file = open("name.txt","w")
            #     string = "test this"
            #     file.write(string)
            #     file.close()
            #     return redirect(url_for('home'))
            # else:
            #     flash('Incorrect Credentials')
            #     return render_template('login.html')
            
            # c.close()
            # conn.close()
            # gc.collect()

        return render_template('login.html')
    except:
        return render_template('login.html')

@app.route('/signup/', methods = ["GET", "POST"])
def signup_page():
 
    try:
        if request.method == 'POST':
            username = request.form['email']
            password = request.form['password']
            city = request.form['city']
            address = request.form['address']
            zp = request.form['zip']
            # checking if user exist
            fname = open("reg.txt","r")
            data = fname.read()
            d = dict()
            data = data.split("$")
            data = data[1:]
            for record in data:
                temp = record.split(',')
                user = temp[0].split('=')[1]
                passwd = temp[1].split('=')[1]
                d[user] = passwd
            if username in d.keys():
                flash("Username taken choose another :(")
                return redirect(url_for('signup_page'))
            fname = open("reg.txt", 'a')
            string = "$username="+username+",password="+password
            fname.write(string)
            fname.close()
            os.chdir("files")
            #os.mkdir(username)
            #os.chdir(username)
            filenam = open("basicInfo.txt","a")
            string = username+" "+password+" "+city+" "+address+" "+zp+"\n"
            filenam.write(string)
            filenam.close()
            os.chdir('./..')
            flash("login now using the credentials")
            return redirect(url_for('login_page'))
        
        return render_template('signup.html',CONTENT = CONTENT)
    except:
        return render_template('signup.html', CONTENT = CONTENT)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("you are required to login first")
            return redirect(url_for("login_page"))
    return wrap


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    flash("Successfully logged out")
    return redirect(url_for('home'))

@app.route('/dashboard/', methods = ["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        key = request.form['search']
        author = session['username']
        code = findHash(key, author)
        if(code == False):
            flash("File Not found")
            return redirect(url_for('search'))
        code = dstr(code)
        return render_template('searchFile.html', code = code, key = key, CONTENT = CONTENT, DASHBOARD = DASHBOARD)
    l = list()
    l = mypro(session['username'])
    return render_template('myprojects.html', CONTENT = CONTENT, DASHBOARD = DASHBOARD, l = l)

@app.route('/coding/', methods = ["GET", "POST"])
@login_required
def coding():
    if request.method == 'POST':
        key = request.form['nameoffile']
        code = request.form['code']
        code = mstr(code)
        #string = "{Name="+nameoffile+"}"+"{code="+code+"}"
        author = session['username']
        count = makeHash(key, code, author)
        
        
       
        #flash("File Saved Successfully")
        flash("Collission occured "+str(count)+" times")
        return redirect(url_for('coding'))

    return render_template('coding.html', CONTENT=CONTENT, DASHBOARD=DASHBOARD)

# @app.route('/myactivities/')
# @login_required
# def myactivities():
#     return render_template('activity.html', CONTENT=CONTENT, DASHBOARD=DASHBOARD, CHART_DATA= CHART_DATA, CHART_WEEK=CHART_WEEK)

@app.route('/search/', methods = ['GET', 'POST'])
@login_required
def search():
    if request.method == "POST":
        key = request.form['search']
        author = session['username']
        code = findHash(key, author)
        if(code == False):
            flash("File Not found")
            return redirect(url_for('search'))
        code = dstr(code)
        return render_template('searchFile.html', code = code, key = key, CONTENT = CONTENT, DASHBOARD = DASHBOARD)
    return render_template('search.html', CONTENT = CONTENT,DASHBOARD = DASHBOARD)

@app.route('/delete/', methods = ["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        name = request.form['delete']
        deletef(name, session['username'])
        l = list()
        l = mypro(session['username'])
        return render_template('delete.html', CONTENT = CONTENT, DASHBOARD = DASHBOARD, l = l)
    l = list()
    l = mypro(session['username'])
    return render_template('delete.html', CONTENT = CONTENT, DASHBOARD = DASHBOARD, l = l)


@app.route('/slang/', methods = ['GET', 'POST'])
def slang():
    if request.method == "POST":
        key = request.form['search']
        l = search_language(key)
        if(l==0):
            flash('Files with .'+key+' extension not found')
            return render_template('searchlang.html', CONTENT = CONTENT,DASHBOARD = DASHBOARD) 

        session['key']=key
        return redirect(url_for('slangs'))

    return render_template('searchlang.html', CONTENT = CONTENT,DASHBOARD = DASHBOARD)

@app.route('/slangs/', methods = ['GET', 'POST'])
def slangs():
    if request.method == "POST":
        key = request.form['search']
        author =  request.form['author']
        code = findHash(key, author)
        if(code == False):
            flash("File Not found")
            return redirect(url_for('search'))
        code = dstr(code)
        return render_template('searchFile.html', code = code, key = key, CONTENT = CONTENT, DASHBOARD = DASHBOARD)

    l=list()
    key = session['key']
    l = search_language(key)
    return render_template('slang.html', CONTENT = CONTENT,DASHBOARD = DASHBOARD, l=l,key=key)
