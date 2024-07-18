# 1st option without using model, my(Nazgul) suggest isto use this function for MVP
def get_recommended_events(events, interests):
    """
    Selects events suitable for the user based on their interests.

    Args:
    events (QuerySet): QuerySet of Events objects to filter from.
    interests (list of str): List of interests of the user.

    Returns:
    list: Array of event IDs recommended for the user.
    """
    # TODO: Write finding suitable events. Add parameters if needed.
    interests_set = set(interests)
    scored_events = []

    for event_id, tags in events:
        tags_set = set(tags)
        common_tags = interests_set & tags_set
        score = len(common_tags)
        scored_events.append((event_id, score))

    sorted_events = sorted(scored_events, key=lambda x: x[1], reverse=True)

    sorted_event_ids = [event_id for event_id, _ in sorted_events]
    return sorted_event_ids


# 2nd option + need to add in requirements.txt: scikit-learn==0.24.1
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# from typing import List, Tuple, Any
#
# def get_recommended_events(events: List[Tuple[Any, List[str]]], interests: List[str]) -> List[Any]:
#     """
#     Selects events suitable for the user based on their interests.
#
#     Args:
#     events (list of tuples): List of tuples where each tuple contains an event ID and a list of tags.
#     interests (list of str): List of interests of the user.
#
#     Returns:
#     list: Array of event IDs recommended for the user.
#     """
#     # Combine tags into a single string for each event
#     event_descriptions = [" ".join(tags) for _, tags in events]
#
#     # Create the TF-IDF matrix for the event descriptions
#     vectorizer = TfidfVectorizer()
#     event_tfidf_matrix = vectorizer.fit_transform(event_descriptions)
#
#     # Combine user interests into a single string
#     interests_combined = " ".join(interests)
#
#     # Create the TF-IDF matrix for the user interests
#     user_tfidf_matrix = vectorizer.transform([interests_combined])
#
#     # Compute cosine similarity between user interests and event descriptions
#     similarity_scores = cosine_similarity(user_tfidf_matrix, event_tfidf_matrix).flatten()
#
#     # Get the indices of the events sorted by similarity scores in descending order
#     sorted_indices = np.argsort(similarity_scores)[::-1]
#
#     # Get the sorted event IDs
#     sorted_event_ids = [events[i][0] for i in sorted_indices]
#
#     return sorted_event_ids
