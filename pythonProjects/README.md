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


summarize.py -> This will summarize paragraph to few lines text which contain only important information

formatConversion -> This will convert json text into html code

inferSentiment.py  -> This will infer the sentiment of the text, is it negative, positive or neutral

generateCustomizedEmailReply -> This will generate email reply on the basis of customer's text tone and takes information from customer's                                    email to generate reply

languageTransistion -> This will translate english text to different language based on user input

CreatePostgresSqlQueries.py -> This will create postgres sql queries based on text

TranslateAllTextToOneLanguage.py -> This will translate paragraph which contains texts from many different language to English





