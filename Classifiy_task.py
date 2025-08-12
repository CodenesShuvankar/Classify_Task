import re

def classify_and_respond(question: str) -> str:
    # Normalize the question to lowercase for easier matching
    lower_question = question.lower()

    # --- Classification Logic ---

    # 1. Check for math-related questions
    math_keywords = ['calculate', 'what is', 'how much is', 'Total of']
    math_operators = ['+', '-', '*', '/']
    if any(keyword in lower_question for keyword in math_keywords) or \
            any(op in lower_question for op in math_operators) or \
            re.search(r'\d', lower_question):
        classification = "Math"

        return f"Classification: {classification}\n"

    # 2. Check for opinion-based questions
    opinion_keywords = ['think', 'believe', 'choose' ,'feel', 'opinion', 'best', 'worst', 'should i', 'following', 'which of the following']
    if any(keyword in lower_question for keyword in opinion_keywords):
        classification = "Opinion"

        return f"Classification: {classification}\n"

    # 3. Default to factual question
    classification = "Factual"
    return f"Classification: {classification}\n"

##---------------------Integrate API/LLM Support ------------------------------#
# def llm(question:str) -> str:
#     import google.generativeai as genai
#
#     try:
#         genai.configure(api_key="GOOGLE_API_KEY")
#     except KeyError:
#         print("Error: GOOGLE_API_KEY environment variable not set.")
#         exit()
#     model = genai.GenerativeModel('gemini-2.5-flash')
#     prompt = f"""
#     Classify the following user question as either 'Factual', 'Opinion', or 'Math'.
#     Respond with only one of those three words. Do not add any other text or punctuation.
#
#     Question: "{question}"
#     Classification:
#     """
#     try:
#         response = model.generate_content(prompt)
#         classification = response.text.strip()
#
#         if classification in ["Factual", "Opinion", "Math"]:
#             return classification
#         else:
#             return "Factual"
#
#     except Exception as e:
#         print(f"An error occurred with the Gemini API: {e}")
#         return "Factual"


# --- Example Usage ---
if __name__ == "__main__":
    # Example questions to test the classifier
    q1 = "What do you think about Python as a programming language?"
    q2 = "What is the capital of France?"
    q3 = "Can you calculate 5 * 10?"
    q4 = "which of the following are the best practice - 1.comment 2.Update comment?"

    print(f"User Question: \"{q1}\"")
    print(classify_and_respond(q1))
    print("-" * 20)

    print(f"User Question: \"{q2}\"")
    print(classify_and_respond(q2))
    print("-" * 20)

    print(f"User Question: \"{q3}\"")
    print(classify_and_respond(q3))
    print("-" * 20)

    print(f"User Question: \"{q4}\"")
    print(classify_and_respond(q4))
    print("-" * 20)
