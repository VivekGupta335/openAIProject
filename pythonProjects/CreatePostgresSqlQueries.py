import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

text = input("prompt")

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


prompt = f"""
### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
Create Query based on query, which is delimited with triple brackets
query: '''{text}'''
"""

response = get_completion(prompt)
print(response)


#sample response

#text=A query to create all tables
# CREATE TABLE Employee (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(50) NOT NULL,
#   department_id INTEGER REFERENCES Department(id)
# );

# CREATE TABLE Department (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(50) NOT NULL,
#   address VARCHAR(100) NOT NULL
# );

# CREATE TABLE Salary_Payments (
#   id SERIAL PRIMARY KEY,
#   employee_id INTEGER REFERENCES Employee(id),
#   amount DECIMAL(10,2) NOT NULL,
#   date DATE NOT NULL
# );

#text=A query to list the names of the departments which employed more than 10 employees in the last 3 months
# SELECT Department.name 
# FROM Department 
# INNER JOIN Employee ON Department.id = Employee.department_id 
# INNER JOIN Salary_Payments ON Employee.id = Salary_Payments.employee_id 
# WHERE Salary_Payments.date >= NOW() - INTERVAL '3 months' 
# GROUP BY Department.name 
# HAVING COUNT(Employee.id) > 10;



