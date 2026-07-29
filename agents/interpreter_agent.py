from utils.retriever import retrieve
from utils.llm import llm
from utils.openrouter_llm import openrouter_llm


class InterpreterAgent:

    def run(self, summary):

        query = f"{summary['artist']} music trend"

        docs = retrieve(query)

        context = "\n".join(doc.page_content for doc in docs)

        prompt = f"""
You are a music trend analyst.

Analysis:
Artist: {summary['artist']}
Total Songs: {summary['songs']}
First Release: {summary['first_year']}
Latest Release: {summary['latest_year']}
Highest Views: {summary['highest_views']}
Average Views: {summary['average_views']}
Trend: {summary['trend']}

Knowledge Base:
{context}

Write a clear explanation of the artist's career trajectory.
"""

        # First model - Groq
        groq_response = llm.invoke(prompt)

        # Second model - OpenRouter
        review_prompt = f"""
Improve the following analysis.
Make it professional, natural and easy to understand.

{groq_response.content}
"""

        try:
            final_response = openrouter_llm.invoke(review_prompt)
            final_answer = final_response.content
        except Exception:
            # If OpenRouter has any temporary issue,
            # fall back to the Groq response.
            final_answer = groq_response.content

        return {
            "answer": final_answer,
            "knowledge": context
        }