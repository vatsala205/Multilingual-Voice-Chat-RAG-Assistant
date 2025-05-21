import openai
openai.api_key = "your-openai-key"

def generate_answer(context_docs: list, query: str) -> str:
    context = "\n".join(context_docs)
    prompt = f"Use the following documents to answer the question.\n\nDocuments:\n{context}\n\nQuestion: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response['choices'][0]['message']['content']
