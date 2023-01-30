import os

from flask import Flask, request, render_template

from app.models.answer_retriever import AnswerRetriever
import logging

from app.models.embeddings_service import EmbeddingsService

app_path = os.getcwd() + '/app'
templates_path = app_path + '/templates'
static_path = app_path + '/static'
print('templates_path: ' + templates_path)
app = Flask(__name__, template_folder=templates_path, static_folder=static_path)


@app.route("/")
def root():
    documents = os.listdir(os.getcwd() + '/app/assets/raw')
    print('documents: ' + str(documents))
    return render_template('documents.html', documents=documents)


@app.route("/document/<param>")
def get_answer(param):
    document = param
    return render_template('ask.html', document=document)


@app.route("/submit_question", methods=['GET', 'POST'])
def submit_question():
    query = request.form['question']
    document = request.form['document']
    embeddings = EmbeddingsService.load_embeddings(document)
    results = AnswerRetriever().get_answer(embeddings, query)
    answer = results['answer']
    sources = results['sources']
    response = {'query': query, 'answer': answer, 'sources': sources, 'document': document}
    logging.info('document: ' + document + ', query: ' + query + ', answer: ' + answer)
    return render_template('answer.html', response=response)


@app.context_processor
def utility_processor():
    def display_format(string):
        # Split the string by "_"
        words = string.split("_")
        # Capitalize the first letter of each word
        words = [word.capitalize() for word in words]
        # Join the words with space
        display_str = " ".join(words)
        # remove file extension
        display_str = display_str.split(".")[0]
        return display_str
    return dict(display_format=display_format)
