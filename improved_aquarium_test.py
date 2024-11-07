import streamlit as st
import random

# Initialize question pool
def generate_question_pool():
    return [
        ("I enjoy having clear targets to aim for.", "Doing", "I am known for my warmth and approachability.", "People"),
        ("I find excitement in taking charge of new projects.", "Doing", "I like to test new approaches methodically.", "Planning"),
        ("I am quick to act when faced with a challenge.", "Doing", "I often find myself empathizing with others' emotions.", "People"),
        ("I prefer to have a clear plan before starting any task.", "Planning", "I am excited when exploring new possibilities and ideas.", "Vision"),
        ("I set ambitious goals for myself and work hard to achieve them.", "Doing", "I value teamwork and group harmony.", "People"),
        ("I am systematic in how I approach issues.", "Planning", "I enjoy looking for creative and innovative solutions to problems.", "Vision"),
        ("I am confident in making decisions independently.", "Doing", "I make an effort to listen carefully and build rapport.", "People"),
        ("I like having multiple tasks going on at once.", "Doing", "I ensure every step in a process is carefully followed.", "Planning"),
        ("I often think outside the box.", "Vision", "I strive to understand what motivates the people around me.", "People"),
        ("I like to maintain a fast-paced work environment.", "Doing", "I rely on evidence and proof to validate my thoughts.", "Planning"),
        # Add more question pairs as needed to reach 52 total pairs (104 selections)
    ]

# Function to administer the test
def administer_test(questions):
    scores = {"Vision": 0, "People": 0, "Planning": 0, "Doing": 0}
    if 'responses' not in st.session_state:
        st.session_state.responses = scores

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    current_index = st.session_state.current_question

    if current_index < len(questions):
        q1, style1, q2, style2 = questions[current_index]
        st.write(f"**Question {current_index + 1}:**")
        
        # Display radio buttons for the current question
        choice = st.radio(
            "Choose the statement that best suits you:",
            (f"A: {q1}", f"B: {q2}"),
            key=f"choice_{current_index}"
        )
        
        # Ensure the choice is recorded only when the "Next" button is clicked
        if st.button("Next"):
            if choice:
                if choice.startswith("A"):
                    st.session_state.responses[style1] += 1
                elif choice.startswith("B"):
                    st.session_state.responses[style2] += 1
                st.session_state.current_question += 1
                # Advance without refreshing
                
    else:
        primary_style, sorted_scores = determine_primary_style(st.session_state.responses)
        display_results(primary_style, sorted_scores)

# Function to determine the primary style
def determine_primary_style(scores):
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    primary, secondary, third, fourth = [item[0] for item in sorted_scores]
    score_values = [item[1] for item in sorted_scores]

    # Check for Blend if all scores are within 3 points of each other
    if max(score_values) - min(score_values) <= 3:
        return "Blend", sorted_scores
    return primary, sorted_scores

# Function to display results with descriptions and colored circles
def display_results(primary_style, sorted_scores):
    st.subheader("Results:")

    # Display color-coded circle based on primary style
    if primary_style == "Vision":
        st.markdown("<div style='width: 50px; height: 50px; background-color: yellow; border-radius: 50%;'></div>", unsafe_allow_html=True)
    elif primary_style == "People":
        st.markdown("<div style='width: 50px; height: 50px; background-color: green; border-radius: 50%;'></div>", unsafe_allow_html=True)
    elif primary_style == "Planning":
        st.markdown("<div style='width: 50px; height: 50px; background-color: blue; border-radius: 50%;'></div>", unsafe_allow_html=True)
    elif primary_style == "Doing":
        st.markdown("<div style='width: 50px; height: 50px; background-color: red; border-radius: 50%;'></div>", unsafe_allow_html=True)
    elif primary_style == "Blend":
        st.markdown("<div style='width: 50px; height: 50px; background: conic-gradient(red, blue, green, yellow); border-radius: 50%;'></div>", unsafe_allow_html=True)

    # Display descriptions for each style
    if primary_style == "Vision":
        st.write("**Vision (Why?)**: You are a forward-thinking individual who thrives on possibilities and creativity. You focus on the big picture and are known for your innovative ideas and ability to inspire others.")
    elif primary_style == "People":
        st.write("**People (Who?)**: You are empathetic, warm, and relationship-focused. You excel in collaborative environments and value team harmony and effective communication.")
    elif primary_style == "Planning":
        st.write("**Planning (How?)**: You are detail-oriented, logical, and structured. You approach problems systematically and are skilled at creating and following plans to achieve goals.")
    elif primary_style == "Doing":
        st.write("**Doing (What?)**: You are action-oriented, decisive, and results-driven. You focus on getting things done efficiently and are often seen as a pragmatic and energetic leader.")
    elif primary_style == "Blend":
        st.write("**Blend**: You have a balanced profile, equally drawing on strengths from all four styles. This allows you to be versatile, adapting your approach to fit different situations and challenges.")

    st.write("\n**Score breakdown:**")
    for style, score in sorted_scores:
        st.write(f"{style}: {score}")

# Main Streamlit app
def main():
    st.title("The Improved Aquarium Test")
    st.write("Select the statement that best describes you for each question.")

    question_pool = generate_question_pool()
    random.shuffle(question_pool)
    questions = question_pool[:52]  # Display 52 pairs (104 selections)

    if 'responses' not in st.session_state:
        st.session_state.responses = {"Vision": 0, "People": 0, "Planning": 0, "Doing": 0}

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    administer_test(questions)

if __name__ == "__main__":
    main()

