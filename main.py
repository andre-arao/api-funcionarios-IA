from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/employees'  # Substitua com sua URI de banco de dados

try:
    conn = psycopg2.connect(
        dbname="employees",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa!")
except psycopg2.Error as e:
    print("Error al conectar a la base de datos:", e)

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'

    emp_no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Employee(emp_no={self.emp_no}, first_name='{self.first_name}', last_name='{self.last_name}', gender='{self.gender}')>"
    
    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender
        }
    
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees]), 200

if __name__ == '__main__':
    app.run(debug=True)
