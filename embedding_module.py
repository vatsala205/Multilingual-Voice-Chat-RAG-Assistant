from sentence_transformers import SentenceTransformer
import faiss
import os
import numpy as np

class SemanticSearch:
    def __init__(self, corpus_dir="corpus"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.docs = []
        self.embeddings = []
        self.index = None
        self.load_corpus(corpus_dir)

    def load_corpus(self, dir_path):
        for file in os.listdir(dir_path):
            with open(os.path.join(dir_path, file), "r", encoding="utf-8") as f:
                text = f.read()
                self.docs.append(text)
                self.embeddings.append(self.model.encode(text))

        self.index = faiss.IndexFlatL2(len(self.embeddings[0]))
        self.index.add(np.array(self.embeddings))

    def query(self, question, top_k=3):
        q_embedding = self.model.encode([question])
        _, indices = self.index.search(np.array(q_embedding), top_k)
        return [self.docs[i] for i in indices[0]]
