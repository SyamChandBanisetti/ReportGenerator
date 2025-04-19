from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def score_answer(student_answer, correct_answer):
    """
    Score the student's answer based on cosine similarity to the correct answer.
    """
    # Use TF-IDF vectorization to convert text to vectors
    vectorizer = TfidfVectorizer().fit_transform([student_answer, correct_answer])
    
    # Calculate cosine similarity between student answer and correct answer
    similarity_matrix = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
    
    # The cosine similarity score ranges from 0 to 1; we scale it to be between 0 and 5
    score = similarity_matrix[0][0] * 5  # Scaling the similarity to a 5-point scale
    return round(score, 2)
