


from flask import Flask, render_template, request,redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  #class object

# def test(st):
# route(path)

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
    

@app.route('/viewplayers')
def viewplayers():
    players = Player.query.all()
    return render_template("viewplayer.html",players=players)

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