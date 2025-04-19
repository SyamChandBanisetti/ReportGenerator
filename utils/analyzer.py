from sentence_transformers import SentenceTransformer, util

# Load the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def score_answer(answer_text, target_label):
    # Predefined target descriptions for scoring (to be modified as needed)
    descriptions = {
        "Precision": "Precision is the fraction of relevant instances among the retrieved instances. It's a measure of how many of the results your model retrieved are relevant.",
        "Recall": "Recall is the fraction of relevant instances that have been retrieved over the total amount of relevant instances. It measures how many relevant results your model missed.",
        "F1 Score": "F1 Score is the harmonic mean of Precision and Recall. It balances the two metrics, rewarding models that have both high precision and high recall."
    }

    # Encode the answer and description
    description = descriptions.get(target_label, "")
    answer_embedding = model.encode(answer_text, convert_to_tensor=True)
    description_embedding = model.encode(description, convert_to_tensor=True)

    # Calculate cosine similarity
    similarity = util.pytorch_cos_sim(answer_embedding, description_embedding)[0][0].item()

    # Score based on similarity (scaled to 5)
    score = max(0, min(5, int(similarity * 5)))
    return score
