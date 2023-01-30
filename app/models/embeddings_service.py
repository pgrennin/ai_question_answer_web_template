import os
import pickle

from langchain import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

from app.config.config import OPEN_AI_API_KEY


class EmbeddingsService:
    CURRENT_DIRECTORY = os.path.dirname(__file__)
    FILE_PATH_ASSETS = os.path.join(CURRENT_DIRECTORY, "../assets")
    EMBEDDINGS_PATH = FILE_PATH_ASSETS + '/embeddings/'

    def get_embedded_file_path(document_name):
        return EmbeddingsService.EMBEDDINGS_PATH + '/' + document_name + '.embedding.pkl'

    def get_raw_file_path(document_name):
        return EmbeddingsService.FILE_PATH_ASSETS + '/raw/' + document_name

    @staticmethod
    def create_embeddings(file_name):
        if file_name == 'ALL':
            # iterate over all files in app/assets/raw, and create embeddings for each
            for file in os.listdir(EmbeddingsService.FILE_PATH_ASSETS + '/raw'):
                EmbeddingsService.create_embeddings_for_file(file)

    @staticmethod
    def create_embeddings_for_file(file_name):
        # check if embedding file already exists.  It would exist in the folder app/assets/embeddings with filename +
        # .embedding.pkl.  If it exists, then skip it.  If it does not exist, then create it.
        embedded_file_path = EmbeddingsService.get_embedded_file_path(file_name)
        if os.path.exists(embedded_file_path):
            print('Embeddings file already exists.  Skipping...' + embedded_file_path)
            return
        else:
            raw_file_path = EmbeddingsService.get_raw_file_path(file_name)
            print('Creating embeddings for file: ' + raw_file_path + ' and saving to: ' + embedded_file_path)
            EmbeddingsService.create_embeddings_and_save(raw_file_path, embedded_file_path)
            print('Embeddings created successfully for: ' + embedded_file_path)
            return

    @staticmethod
    def create_embeddings_and_save(raw_file_path, embedded_file_path):
        print('Creating embeddings...')
        os.environ["OPENAI_API_KEY"] = OPEN_AI_API_KEY
        with open(raw_file_path) as f:
            file_to_split = f.read()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_text(file_to_split)
        embeddings = OpenAIEmbeddings()

        # Vector store.  Object which stores the embeddings and allows for fast retrieval.
        docsearch = FAISS.from_texts(texts, embeddings, metadatas=[{"source": i} for i in range(len(texts))])

        v = [docsearch, texts]

        # save to pickle
        with open(embedded_file_path, 'wb') as f:
            pickle.dump(v, f)

    @staticmethod
    def load_embeddings(document_name):
        os.environ["OPENAI_API_KEY"] = OPEN_AI_API_KEY
        embedded_file_path = EmbeddingsService.get_embedded_file_path(document_name)
        if os.path.exists(embedded_file_path):
            print('Loading embeddings from file...')
            with open(embedded_file_path, 'rb') as f:
                docsearch, texts = pickle.load(f)
        else:
            raise Exception('Embeddings file does not exist.  Please create embeddings file first.')
        return {'docsearch': docsearch, 'texts': texts}
