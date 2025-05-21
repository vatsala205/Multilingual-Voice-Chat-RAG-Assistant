from modules.stt_module import transcribe_audio
from modules.embedding_module import SemanticSearch
from modules.generation_module import generate_answer

# Step 1: Transcribe
transcribed = transcribe_audio("audio_inputs/input1.wav", language="hi")
print("Transcribed:", transcribed)

# Step 2: Retrieve
retriever = SemanticSearch("corpus")
top_docs = retriever.query(transcribed)
print("Retrieved Docs:", top_docs)

# Step 3: Generate Answer
response = generate_answer(top_docs, transcribed)
print("Generated Answer:", response)
