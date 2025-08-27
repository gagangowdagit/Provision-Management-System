from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


with open('config.json','r') as c:
    params = json.load(c)["params"]


local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'



if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']


else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['proud_uri']

db = SQLAlchemy(app)


class orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arrival = db.Column(db.String, nullable=False)
    name = db.Column(db.String(500), nullable=False)
    items= db.Column(db.String(500), nullable=False)
    products = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    mid = db.Column(db.String(120), nullable=False)
    

class Posts(db.Model):
    mid = db.Column(db.Integer, primary_key=True)
    items_name = db.Column(db.String(80), nullable=False)
    owner_name = db.Column(db.String(200), nullable=False)
    phone_no = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(120), nullable=False)

class Addmp(db.Model):
    sno = db.Column(db.Integer,  primary_key=True)
    item = db.Column(db.String, nullable=False)

class Addpd(db.Model):
    sno = db.Column(db.Integer,  primary_key=True)
    product = db.Column(db.String, nullable=False)


class Logs(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.String, nullable=True)
    action = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(100), nullable=False)



@app.route("/")
def hello():
    if 'user' in session and session['user'] == params['user']:
        return render_template('index.html', params=params)
    else:
        flash("Please login first", "warning")
        return redirect('/login')



@app.route("/index")
def home():
    if 'user' in session and session['user'] == params['user']:
        return render_template('dashbord.html', params=params)
    else:
        flash("Please login first", "warning")
        return redirect('/login')


@app.route("/search", methods=['GET', 'POST'])
def search():
    if 'user' in session and session['user'] == params['user']:
        if request.method == 'POST':
            name = request.form.get('search')
            post = Addmp.query.filter_by(item=name).first()
            pro = Addpd.query.filter_by(product=name).first()

            if post or pro:
                flash("Item is available.", "primary")
            else:
                flash("Item is not available.", "danger")

        return render_template('search.html', params=params)
    else:
        flash("Please login first", "warning")
        return redirect('/login')


@app.route("/details", methods=['GET', 'POST'])
def details():
    if 'user' in session and session['user'] == params['user']:
        posts = Logs.query.all()
        return render_template('details.html', params=params, posts=posts)
    else:
        flash("Please login first", "warning")
        return redirect('/login')



@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html', params=params)


@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if 'user' in session and session['user'] == params['user']:
        if request.method == 'POST':
            # Add entry to the database
            mid = request.form.get('mid')
            items_name = request.form.get('items_name')
            owner_name = request.form.get('owner_name')
            phone_no = request.form.get('phone_no')
            address = request.form.get('address')

            push = Posts(mid=mid, items_name=items_name, owner_name=owner_name, phone_no=phone_no, address=address)
            db.session.add(push)
            db.session.commit()

            flash("Details have been submitted", "primary")

        return render_template('insert.html', params=params)
    else:
        flash("Please login first", "warning")
        return redirect('/login')



@app.route("/addmp", methods=['GET', 'POST'])
def addmp():
    if 'user' in session and session['user'] == params['user']:
        if request.method == 'POST':
            # Add entry to the database
            newitem = request.form.get('item')
            push = Addmp(item=newitem)
            db.session.add(push)
            db.session.commit()
            flash("Thanks for adding new items", "primary")
        return render_template('search.html', params=params)
    else:
        flash("Please login first", "warning")
        return redirect('/login')



@app.route("/addpd", methods = ['GET','POST'])



@app.route("/addpd", methods=['GET', 'POST'])
def addpd():
    if 'user' in session and session['user'] == params['user']:
        if request.method == 'POST':
            # Add entry to the database
            newproduct = request.form.get('product')
            push = Addpd(product=newproduct)
            db.session.add(push)
            db.session.commit()
            flash("Items (Products) added successfully", "primary")
        return render_template('search.html', params=params)
    else:
        flash("Please login first", "warning")
        return redirect('/login')


@app.route("/list", methods=['GET','POST'])
def post():
    if 'user' in session and session['user'] == params['user']:
        posts = orders.query.all()
        return render_template('post.html', params=params, posts=posts)
    else:
        flash("Please login first", "warning")
        return redirect('/login')



@app.route("/items", methods=['GET', 'POST'])
def items():
    if 'user' in session and session['user'] == params['user']:
        posts = Addmp.query.all()
        return render_template('items.html', params=params, posts=posts)
    else:
        flash("Please login first", "warning")
        return redirect('/login')


@app.route("/items2", methods=['GET', 'POST'])
def items2():
    if 'user' in session and session['user'] == params['user']:
        posts = Addpd.query.all()
        return render_template('items2.html', params=params, posts=posts)
    else:
        flash("Please login first", "warning")
        return redirect('/login')

@app.route("/sp", methods=['GET', 'POST'])
def sp():
    if 'user' in session and session['user'] == params['user']:
        posts = orders.query.all()
        return render_template('store.html', params=params, posts=posts)
    else:
        flash("Please login first", "warning")
        return redirect('/login')


@app.route("/logout")
def logout():

    session.pop('user')
    flash("You are logout", "primary")

    return redirect('/login')


@app.route("/login",methods=['GET','POST'])
def login():

    if ('user' in session and session['user'] == params['user']):
        posts = Posts.query.all()
        return render_template('dashbord.html',params=params,posts=posts)

    if request.method=='POST':

        username=request.form.get('uname')
        userpass=request.form.get('password')
        if(username==params['user'] and userpass==params['password']):

            session['user']=username
            posts=Posts.query.all()
            flash("You are Logged in", "primary")

            return render_template('index.html',params=params,posts=posts)
        else:
            flash("wrong password", "danger")

    return render_template('login.html', params=params)


@app.route("/edit/<string:mid>",methods=['GET','POST'])

def edit(mid):
    if('user' in session and session['user']==params['user']):
        if request.method =='POST':
            items_name=request.form.get('items_name')
            owner_name=request.form.get('owner_name')
            phone_no=request.form.get('phone_no')
            address=request.form.get('address')


            if mid==0:
                posts=Posts(items_name=items_name,owner_name=owner_name,phone_no=phone_no,address=address)

                db.session.add(posts)
                db.session.commit()
            else:
                post=Posts.query.filter_by(mid=mid).first()
                post.items_name=items_name
                post.owner_name=owner_name
                post.phone_no=phone_no
                post.address=address
                db.session.commit()
                flash("data updated ", "success")

                return redirect('/edit/'+mid)
        post = Posts.query.filter_by(mid=mid).first()
        return render_template('edit.html',params=params,post=post)


#         if user is logged in
#delete

@app.route("/delete/<string:mid>", methods=['GET', 'POST'])
def delete(mid):
    if ('user' in session and session['user']==params['user']):
        post=Posts.query.filter_by(mid=mid).first()
        db.session.delete(post)
        db.session.commit()
        flash("Deleted Successfully", "warning")

    return redirect('/login')

@app.route("/deletemp/<string:id>", methods=['GET', 'POST'])
def deletemp(id):
    if ('user' in session and session['user']==params['user']):
        post=orders.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()
        flash("Deleted Successfully", "primary")

    return redirect('/list')

@app.route("/orders", methods=['GET', 'POST'])
def medicine():
    if 'user' in session and session['user'] == params['user']:
        if request.method == 'POST':
            # Add entry to the database
            mid = request.form.get('mid')
            name = request.form.get('name')
            items = request.form.get('items')
            products = request.form.get('products')
            email = request.form.get('email')
            arrival = request.form.get('arrival')
            entry = orders(mid=mid, name=name, items=items, products=products, email=email, arrival=arrival)
            db.session.add(entry)
            db.session.commit()
            flash("Data Added Successfully", "primary")

        return render_template('orders.html', params=params)
    else:
        flash("Please login first", "warning")
        return redirect('/login')



app.run(debug=True)