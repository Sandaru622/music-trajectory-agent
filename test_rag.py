from utils.rag import load_documents, create_vector_store

# ======================================================
# STEP 1 - Test Document Loading and Chunking
# ======================================================

chunks = load_documents()

print("Number of Chunks:", len(chunks))
print()

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}")
    print(chunk.page_content)
    print("-" * 50)


# ======================================================
# STEP 2 - Create Chroma Vector Database
# ======================================================

vector_store = create_vector_store(chunks)

print("\n✅ Chroma Database Created Successfully!")