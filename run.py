from app import app, db

# Crear la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)