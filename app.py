## set FLASK_APP=adoption_site.py - Włącza migracje
## flask db init - Tworzy folder migracji
## flask db migrate -m 'Napis potwierdzający miracje tabeli których brakuje'
## flask db upgrade  "Dodaje Tabele lub rzeczy których nie było w DB"

# APP.PY
from blog import app

if __name__ == '__main__':
    app.run(debug=True)
