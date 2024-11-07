import streamlit as st
import random

# Initialize question pool
def generate_question_pool():
    return [
        ("I enjoy having clear targets to aim for.", "Doing", "I am known for my warmth and approachability.", "People"),
        ("I find excitement in taking charge of new projects.", "Doing", "I like to test new approaches methodically.", "Planning"),
        # Add more question pairs as needed
    ]

# Function to administer the test
def administer_test(questions):
    scores = {"Vision": 0, "People": 0, "Planning": 0, "Doing": 0}
    for index, (q1, style1, q2, style2) in enumerate(questions):
        st.write(f"**Question {index + 1}:**")
        choice = st.radio(f"Choose the statement that best suits you:", (f"A: {q1}", f"B: {q2}"), key=index)
        if choice.startswith("A"):
            scores[style1] += 1
        elif choice.startswith("B"):
            scores[style2] += 1
    return scores

# Function to determine the primary style
def determine_primary_style(scores):
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    primary, secondary, third, fourth = [item[0] for item in sorted_scores]
    score_values = [item[1] for item in sorted_scores]

    # Check for Blend if all scores are within 3 points of each other
    if max(score_values) - min(score_values) <= 3:
        return "Blend", sorted_scores
    return primary, sorted_scores

# Main Streamlit app
def main():
    st.title("The Improved Aquarium Test")
    st.write("Select the statement that best describes you for each question.")

    question_pool = generate_question_pool()
    random.shuffle(question_pool)
    questions = question_pool[:30]  # Display 30 pairs (60 questions)

    if st.button("Submit Test"):
        scores = administer_test(questions)
        primary_style, sorted_scores = determine_primary_style(scores)

        st.subheader("Results:")
        if primary_style == "Blend":
            st.write("You have a balanced profile and fall into the 'Blend' category.")
        else:
            st.write(f"Your primary style is: {primary_style}")

        st.write("\n**Score breakdown:**")
        for style, score in sorted_scores:
            st.write(f"{style}: {score}")

if __name__ == "__main__":
    main()
