# Chatgpt python 

#Install openai using pip

```
pip install openai
```

#Install python-dotenv

```
pip install python-dotenv
```

#Create env file .env
#Place your api_key as 

```
OPENAI_API_KEY= <api_key>
```

#Helper function 

```
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

```
