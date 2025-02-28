prompt_search_query = {"role": "user", "content": f"""Your task: Rephrase the user's input into 2 concise online search queries of under 6 keywords each. Googling these queries should find all information needed to respond to the user. The current date is Friday, 2025-02-26. You must only output the search queries, which should contain fewer than 6 online search keywords each. You must output exactly 2 search queries, formatted as ["<query_str_0>", "<query_str_1>"]. Absolutely do not output anything else.

---

# User's input: {query}"""}


prompt_online_response = ["<instructions>

# OBJECTIVE:

Your task is to provide an accurate and extremely comprehensive response to the user's query. Follow these specific guidelines:

Today's date is February 26, 2025. You are provided search results below from a web search performed today. This means your new knowledge cutoff is now today, February 26, 2025. You must consider these updated search results as factual.

If the search results can be relevant to the user's query as of today's date, create a bullet point list of relevant references with their href URLs. Skip irrelevant or out-of-date sources. Remember to output your own response to the user's query first, followed by the references (if relevant).

Do not speculate. Do not use hypotheticals. Do not make assumptions. Do not include placeholders. Only provide citations from the search results.

Format your response in plaintext. Ensure your response is extremely comprehensive.

</instructions>

---

<search_results>

{context}

</search_results>

---

", "<user>

# User's query:

{question}

</user>"]


prompt_aggreagator = """
- You have been provided with a set of responses from various open-source models to the latest user query.
- Your task is to synthesize these responses into a single, high-quality response.
- It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect.
- Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction.
- Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:"""
