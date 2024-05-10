from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import google.generativeai as genai

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/employees'

try:
    conn = psycopg2.connect(
        dbname="employees",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Conexão com banco de dados ok!")
except psycopg2.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'

    emp_no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    contract = db.Column(db.String, nullable=False)
    salary = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Employee(emp_no={self.emp_no}, first_name='{self.first_name}', last_name='{self.last_name}', gender='{self.gender}', contract={self.contract}, salary={self.salary})>"
    
    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'contract': self.contract,
            'salary': self.salary
        }
    
@app.route('/api/funcionarios', methods=['GET', 'POST'])
def funcionarios():
    if request.method == 'GET':
        employees = Employee.query.all()
        return jsonify([employee.to_dict() for employee in employees]), 200
    elif request.method == 'POST':
        mensagem = request.json
        pergunta = mensagem['perguntaFuncionarios']

        todosFuncionarios = Employee.query.all()

        # Coloque sua API key no valor da variavel a baixo
        GOOGLE_API_KEY="AIzaSyA5h_qD6_jrvcQHwfhDidOa5n3d_ENzD7g"
        genai.configure(api_key=GOOGLE_API_KEY)
        generation_config = {
        "candidate_count": 1,
        "temperature": 0.5,
        }
        safety_settings={
            'HATE': 'BLOCK_NONE',
            'HARASSMENT': 'BLOCK_NONE',
            'SEXUAL' : 'BLOCK_NONE',
            'DANGEROUS' : 'BLOCK_NONE'
            }
        model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                        generation_config=generation_config,
                                        safety_settings=safety_settings,)
        
        perguntaData = f"{pergunta}\n\n{todosFuncionarios}"
        response = model.generate_content(perguntaData)

        return jsonify({'response': response.text}), 200


@app.route('/api/criar/funcionarios', methods=['POST'])
def create_employee():
    if request.method == 'POST':
        data = request.json
        new_employee = Employee(
            first_name=data['first_name'],
            last_name=data['last_name'],
            gender=data['gender'],
            contract=data['contract'],
            salary=data['salary']
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Novo funcionário criado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
