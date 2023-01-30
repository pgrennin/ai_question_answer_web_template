import re

from langchain import OpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain


class AnswerRetriever:
    def get_answer(self, embeddings, query):
        texts = embeddings['texts']
        docsearch = embeddings['docsearch']
        docs = docsearch.similarity_search(query)
        chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="stuff")
        answer = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
        sources_indexes = re.findall(r'\d+', answer['output_text'].splitlines()[-1])
        sources_indexes = [int(i) for i in sources_indexes]
        sources_list = []
        for idx in sources_indexes:
            sources_list.append(texts[idx])

        # remove sources from answer
        answer_str = answer['output_text'].split("\nSOURCES:")[0]

        response = {
            'answer': answer_str,
            'sources': sources_list
        }

        # code to load embeddings
        return response
