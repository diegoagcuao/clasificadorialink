from app import create_app, database as db  # Cambiar a 'database'

app = create_app()

if __name__ == '__main__':
<<<<<<< HEAD
    #with app.app_context():
        #db.drop_all()
        #db.create_all()  # Usar 'database' en lugar de 'db'
=======
    with app.app_context():
        #db.drop_all()
        db.create_all()  # Usar 'database' en lugar de 'db'
>>>>>>> bea17413e07e1b0f4a193a8a83213fef4bdd08ac
    app.run(debug=True, host='0.0.0.0', port=8080)
