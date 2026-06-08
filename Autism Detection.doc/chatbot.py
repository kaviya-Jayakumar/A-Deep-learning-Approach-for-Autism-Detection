import difflib
import random
from knowledge_base import faq_data, doctor_recommendations


def get_best_match(query, choices, cutoff=0.6):
    """
    Returns the best matching key from choices based on similarity.
    """
    matches = difflib.get_close_matches(query, choices, n=1, cutoff=cutoff)
    return matches[0] if matches else None

def chatbot_response(user_input):
    user_input_lower = user_input.lower()

    faq_keys = list(faq_data.keys())
    best_match = get_best_match(user_input_lower, faq_keys)
    if best_match:
        return faq_data[best_match]

    # Doctor recommendation matching
    doctor_keys = list(doctor_recommendations.keys())
    best_match = get_best_match(user_input_lower, doctor_keys)
    if best_match:
        symptom = best_match
        return f"Based on what you mentioned ({symptom}), it is recommended to consult a **{doctor_recommendations[symptom]}**."

    # Default fallback
    fallback = [
        "I'm not sure about that. Could you ask differently?",
        "I don’t know exactly, but I suggest consulting a healthcare professional.",
        "That’s an interesting question. I recommend you note your symptoms for a doctor’s review."
    ]
    return random.choice(fallback)