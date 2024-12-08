


from flask import Flask, render_template, request,redirect,flash
from flask import url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user


app = Flask(__name__)  #class object

# def test(st):
# route(path)

app.secret_key = 'MITS@123'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db=SQLAlchemy(app)

@app.route('/home')
def home():
    print("This route is being called!")
    return render_template("home.html")

@app.route('/about')
def about():
    name= "joel"
    age = 344
    runs= [20,30,40,68,13]
    return render_template("index.html",name=name,age=age,runs=runs)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/base')
def base():
    return render_template("base.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/addplayer',methods=['GET','POST'])
def addplayer():
    if request.method== 'POST':
        name=request.form['name']
        age=request.form['age']
        #print(name,age)
        #players.append({"name":name,"age":age})
        p=Player(name=name, age=age)
        db.session.add(p)
        db.session.commit()

        return redirect(url_for('viewplayers'))
        return name + " " + age
    else:
        return render_template("addplayer.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exist")
            return redirect(url_for('login'))
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    else:
        return render_template('signup.html')   


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password")
            return redirect(url_for('login')) 
    return render_template('login.html')

@app.route('/profile')
def profile():
    print(current_user.username)
    return render_template('profile.html',user=current_user) 

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/viewplayers')
def viewplayers():
    players = Player.query.all()
    return render_template("viewplayer.html",players=players)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

app.app_context().push()
db.create_all()
#@app.route('/addplayer',method=['POST'])

@app.route('/editplayer/<int:id>',methods=['GET','POST'])
def editplayer(id):
    player = Player.query.get(id)
    if request.method == 'POST':
        player=Player.query.get(id)
        player.name = request.form['name']
        player.age = request.form['age']
        db.session.commit()
        return redirect(url_for('viewplayers'))
    return render_template('editplayer.html', player=player)

@app.route('/deleteplayer/<int:id>')
def deleteplayer(id):
    player = Player.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('viewplayers'))
app.run(debug=True)