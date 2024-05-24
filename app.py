from flask import Flask, render_template, request, redirect, url_for
from pony.orm import Database, Required, db_session

app = Flask(__name__)

# Konfiguracija baze podataka
db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

class Let(db.Entity):
    id_let = Required(int, unique=True)
    id_odredište = Required(int)
    datumPolaska = Required(str)
    trajanjeLeta = Required(int)
    duljinaLeta = Required(float)

class Odredište(db.Entity):
    id_Odredišta = Required(int, unique=True)
    nazivOdrredišta = Required(str)
    državaOdredišta = Required(str)

db.generate_mapping(create_tables=True)

# Rute
@app.route('/')
@db_session
def index():
    letovi = Let.select()[:]
    odredista = Odredište.select()[:]
    return render_template('index.html', letovi=letovi, odredista=odredista)

@app.route('/letovi', methods=['GET', 'POST'])
@db_session
def letovi():
    if request.method == 'POST':
        data = request.form
        Let(id_let=int(data['id_let']), id_odredište=int(data['id_odredište']),
            datumPolaska=data['datumPolaska'], trajanjeLeta=int(data['trajanjeLeta']),
            duljinaLeta=float(data['duljinaLeta']))
        return redirect(url_for('letovi'))
    letovi = Let.select()[:]
    return render_template('letovi.html', letovi=letovi)

@app.route('/odredista', methods=['GET', 'POST'])
@db_session
def odredista():
    if request.method == 'POST':
        data = request.form
        Odredište(id_Odredišta=int(data['id_Odredišta']), nazivOdrredišta=data['nazivOdrredišta'],
                  državaOdredišta=data['državaOdredišta'])
        return redirect(url_for('odredista'))
    odredista = Odredište.select()[:]
    return render_template('odredista.html', odredista=odredista)


if __name__ == '__main__':
    app.run(debug=True)
