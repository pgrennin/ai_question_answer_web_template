# AI Question Answer Web Template

A Python Flask web app template for doing AI Question and Answering with sources using Langchain. Optimized for minimal developer
setup by running in a Docker container, and provides a framework for adding
and embedding documents. Already contains several embedded documents preloaded and more can
be added easily using a script.


# Demo
![Demo](https://raw.githubusercontent.com/pgrennin/ai_question_answer_web_template/demo-ai-template2.gif)


# Quick Start

1) To get started, clone this repository.

   `git clone https://github.com/pgrennin/ai_question_answer_web_template.git`

2) Add your OPENAI API KEY to app/config/config.py

3) Run the following command to build the Docker image and run the container.  (This script requires Docker. Please
   install if you don't have it already.)

   `bash run.dev.sh`


4) Go to http://localhost:8000/ to see the application and run questions and answers on one of the documents already
   pre-created.


# Upload your own document for doing question and answers (optional)

Create embeddings on a document of your choice by doing the following:

1) Create a `.txt` file and place in the app/assets/raw directory.

example:

`curl https://www.gutenberg.org/cache/epub/3755/pg3755.txt -o app/assets/raw/thomas_paine_common_sense.txt`

2) Run the create embeddings script

`bash create_embeddings.sh`

**What this script does.**
This will create new embeddings for all files in app/assets/raw. If an embedding file has already been created for a
file, it will not be recreated. It checks if embedding was already created in /app/assets/embeddings.

3) Go to http://localhost:8000/ view your document and ask questions on it.

## Notes

* Please feel free to open a PR if you have any suggestions or improvements.
* Only tested with txt documents but could be extended to other file types.
* Errors may occur uploading very large documents.
* After starting this project I found Langchain has already created something similar with a chatbot
  template. (https://blog.langchain.dev/langchain-chat/)

### The tools used in this project are:

- Python 3.11
- LangChain
- Flask
- OpenAI API
- FAISS
- Docker
- Bootstrap
