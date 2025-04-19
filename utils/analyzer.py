# analyzer.py

def score_answer(answer, formula_type):
    """
    This function scores the answer for the Precision, Recall, and F1 Score questions.
    It looks for relevant keywords and gives a score based on how well the answer matches.
    """
    if formula_type == "Precision":
        correct_keywords = ["true positive", "false positive", "positive"]
        score = sum(keyword in answer.lower() for keyword in correct_keywords)
    elif formula_type == "Recall":
        correct_keywords = ["true positive", "false negative", "positive"]
        score = sum(keyword in answer.lower() for keyword in correct_keywords)
    elif formula_type == "F1 Score":
        correct_keywords = ["precision", "recall", "harmonic mean"]
        score = sum(keyword in answer.lower() for keyword in correct_keywords)
    else:
        score = 0
    return score
