#from asyncio.windows_events import NULL
#from asyncio.windows_events import NULL
from distutils.command.clean import clean
from flask import Flask
from flask import Flask, request, render_template
from flask import session
import os
import requests

requests.get('https://www.huggingface.co')
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("summerizer.html")
    
my_value = ""

@app.route('/', methods=['POST','GET'])
def text_summerize():
    
    #text = request.form.get('input_text_name')
    #item = str(request.form.get('input_text_name'))
    text=  request.form['input_text_name'] or "please enter text"
    

    max_words = int(request.form['word_max_length_name'] or "130")
    min_words = int(request.form['word_min_length_name']or "1")


    
        



    #if max_words == NULL:
        #max_words = 130

    #if min_words == NULL:
         #min_words == 1

    #if text == NULL:
        #text= "enter text"


    output_text = summerizer(text, max_words, min_words)
    input_text = text

    #if request.form['clear_data'] == 'clear':
        #input_text == " "
        #output_text ==" "

    


    return render_template("summerizer.html", output_text=output_text, input_text= input_text)

#os.environ["CURL_CA_BUNDLE"]=""

model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
tokenizer = AutoTokenizer.from_pretrained("t5-base")



#inputs = tokenizer("summarize: " + ARTICLE, return_tensors="pt", max_length=512, truncation=True)
#outputs = model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True )


def summerizer(text, max_words, min_words):
    
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=max_words, min_length = min_words,length_penalty=2.0, num_beams=4, early_stopping=True )

    clean_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return clean_text


if __name__ == '__main__':
    app.run(debug = True, host= '0,0,0,0')
