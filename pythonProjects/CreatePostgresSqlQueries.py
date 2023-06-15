import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

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
### A query to create all 3 tables:
"""

response = get_completion(prompt)
print(response)


#sample response
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

