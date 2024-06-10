from flask import Flask, render_template, request, redirect, url_for
from pony.orm import Database, Required, db_session, select, PrimaryKey

app = Flask(__name__)

# Konfiguracija baze podataka
db = Database()
db.bind(provider='sqlite', filename='databases.sqlite', create_db=True)


class Let(db.Entity):
    id_let = PrimaryKey(int, auto=True)
    id_odredište = Required(int)
    datumPolaska = Required(str)
    trajanjeLeta = Required(int)
    duljinaLeta = Required(float)


class Odredište(db.Entity):
    id_Odredišta = PrimaryKey(int, auto=True)
    nazivOdrredišta = Required(str)
    državaOdredišta = Required(str)


db.generate_mapping(create_tables=True)


# Rute
@app.route('/')
@db_session
def index():
    sort_letovi = request.args.get('sort_letovi', 'id_let')
    sort_odredista = request.args.get('sort_odredista', 'id_Odredišta')

    letovi_query = Let.select()
    if sort_letovi == 'datumPolaska':
        letovi_query = letovi_query.order_by(Let.datumPolaska)
    elif sort_letovi == 'trajanjeLeta':
        letovi_query = letovi_query.order_by(Let.trajanjeLeta)
    elif sort_letovi == 'duljinaLeta':
        letovi_query = letovi_query.order_by(Let.duljinaLeta)
    elif sort_letovi == 'odrediste':
        letovi_query = letovi_query.order_by(Let.id_odredište)
    else:
        letovi_query = letovi_query.order_by(Let.id_let)

    odredista_query = Odredište.select()
    if sort_odredista == 'nazivOdrredišta':
        odredista_query = odredista_query.order_by(Odredište.nazivOdrredišta)
    elif sort_odredista == 'državaOdredišta':
        odredista_query = odredista_query.order_by(Odredište.državaOdredišta)
    else:
        odredista_query = odredista_query.order_by(Odredište.id_Odredišta)

    letovi = letovi_query[:]
    odredista = odredista_query[:]

    return render_template('index.html', letovi=letovi, odredista=odredista, sort_letovi=sort_letovi,
                           sort_odredista=sort_odredista)


@app.route('/letovi', methods=['GET', 'POST'])
@db_session
def letovi():
    if request.method == 'POST':
        data = request.form
        Let(id_odredište=int(data['id_odredište']),
            datumPolaska=data['datumPolaska'], trajanjeLeta=int(data['trajanjeLeta']),
            duljinaLeta=float(data['duljinaLeta']))
        return redirect(url_for('letovi'))

    odredista = Odredište.select()[:]
    letovi = Let.select()[:]
    return render_template('letovi.html', letovi=letovi, odredista=odredista)


@app.route('/letovi/edit/<int:id_let>', methods=['GET', 'POST'])
@db_session
def edit_let(id_let):
    let = Let.get(id_let=id_let)
    if request.method == 'POST':
        data = request.form
        let.id_odredište = int(data['id_odredište'])
        let.datumPolaska = data['datumPolaska']
        let.trajanjeLeta = int(data['trajanjeLeta'])
        let.duljinaLeta = float(data['duljinaLeta'])
        return redirect(url_for('letovi'))

    odredista = Odredište.select()[:]
    return render_template('edit_let.html', let=let, odredista=odredista)


@app.route('/odredista', methods=['GET', 'POST'])
@db_session
def odredista():
    if request.method == 'POST':
        data = request.form
        Odredište(nazivOdrredišta=data['nazivOdrredišta'],
                  državaOdredišta=data['državaOdredišta'])
        return redirect(url_for('odredista'))
    odredista = Odredište.select()[:]
    return render_template('odredista.html', odredista=odredista)


@app.route('/odredista/edit/<int:id_odrediste>', methods=['GET', 'POST'])
@db_session
def edit_odrediste(id_odrediste):
    odrediste = Odredište.get(id_Odredišta=id_odrediste)
    if request.method == 'POST':
        data = request.form
        odrediste.nazivOdrredišta = data['nazivOdrredišta']
        odrediste.državaOdredišta = data['državaOdredišta']
        return redirect(url_for('odredista'))
    return render_template('edit_odrediste.html', odrediste=odrediste)


@app.route('/letovi/delete/<int:id_let>', methods=['POST'])
@db_session
def delete_let(id_let):
    let = Let.get(id_let=id_let)
    if let:
        let.delete()
    return redirect(url_for('letovi'))


@app.route('/odredista/delete/<int:id_odrediste>', methods=['POST'])
@db_session
def delete_odrediste(id_odrediste):
    odrediste = Odredište.get(id_Odredišta=id_odrediste)
    if odrediste:
        odrediste.delete()
    return redirect(url_for('odredista'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)