from utils.retriever import retrieve

results = retrieve("How does tempo affect popularity?")

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print(doc.page_content)