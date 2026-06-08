from rapidfuzz import process
import random

faq_data = {
    "what is autism": "Autism Spectrum Disorder (ASD) is a developmental condition affecting communication and behavior.",
    "symptoms of autism": "Common symptoms include challenges in communication, social interaction, and repetitive behaviors.",
    "treatment for autism": "Therapies like behavioral therapy, speech therapy, and occupational therapy can help manage ASD.",
    "can autism be cured": "Autism is not curable, but early intervention can improve quality of life and outcomes."
}

doctor_recommendations = {
    "speech delay": "speech therapist",
    "repetitive behavior": "behavioral therapist",
    "social difficulty": "psychologist",
    "learning issues": "developmental pediatrician"
}


def chatbot_response(user_input, threshold=70):
    user_input_lower = user_input.lower()

    #  Check FAQ with fuzzy matching
    faq_keys = list(faq_data.keys())
    best_match = process.extractOne(user_input_lower, faq_keys)
    if best_match and best_match[1] >= threshold:
        return faq_data[best_match[0]]

    #  Check doctor recommendations with fuzzy matching
    doctor_keys = list(doctor_recommendations.keys())
    best_match = process.extractOne(user_input_lower, doctor_keys)
    if best_match and best_match[1] >= threshold:
        symptom = best_match[0]
        return f"Based on what you mentioned ({symptom}), it is recommended to consult a **{doctor_recommendations[symptom]}**."

    #  Default fallback
    fallback = [
        "I'm not sure about that. Could you ask differently?",
        "I don’t know exactly, but I suggest consulting a healthcare professional.",
        "That’s an interesting question. I recommend you note your symptoms for a doctor’s review."
    ]
    return random.choice(fallback)