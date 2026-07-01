import streamlit as st
from agents.interviewer import ask_question
from agents.mentor import mentor_tip
from agents.evaluator import evaluate_answer
from services.resume_parser import parse_resume
from services.session_manager import save_session

st.title("Multi-Agent Mock Interview")

# Company selection
company = st.selectbox(
    "Choose Company",
    ["Amazon", "Google", "Meta"]
)

# Role input
role = st.text_input("Enter Role")

# Resume upload
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["txt", "pdf"]
)
resume = ""

if uploaded_file:
    resume = parse_resume(uploaded_file)

# Start interview
if st.button("Start Interview"):
    question = ask_question(company, role, resume)
    st.session_state.question = question

# Display question
if "question" in st.session_state:
    st.subheader("Interviewer")
    st.write(st.session_state.question)

# User answer
answer = st.text_area("Your Answer")

# Submit answer
if st.button("Submit Answer"):
    tip = mentor_tip(st.session_state.question, answer)
    score = evaluate_answer(answer)

    st.subheader("Mentor Whisper")
    st.write(tip)

    st.subheader("Evaluation")
    st.write(score)

    save_session({
        "company": company,
        "role": role,
        "question": st.session_state.question,
        "answer": answer,
        "score": score
    })
