import streamlit as st
import pandas as pd
from ml_engine import predict_study_hours, cluster_subjects
from scheduler import generate_weekly_schedule
from weekly_report import generate_report
from ai_assistant import chat_response

st.set_page_config(page_title="Smart Study Scheduler", layout="wide")

st.title("📚 Smart Study Scheduler with ML + Gemini AI")
st.markdown("""
Welcome to your intelligent study planning assistant.
""")

# Step 1: User Input
st.header("📝 Step 1: Enter your study details")
subjects_input = st.text_area("Subjects (comma-separated)", "Math, Physics, Chemistry")
grades_input = st.text_area("Grades (0–100, comma-separated)", "85, 90, 80")
priorities_input = st.text_area("Priorities (1–5, comma-separated)", "3, 4, 2")

if st.button("Generate Schedule"):
    try:
        subjects = [s.strip() for s in subjects_input.split(",")]
        grades = [float(g.strip()) for g in grades_input.split(",")]
        priorities = [float(p.strip()) for p in priorities_input.split(",")]

        if not (len(subjects) == len(grades) == len(priorities)):
            st.error("Mismatch in number of subjects, grades, or priorities.")
        else:
            # Predict hours
            hours = predict_study_hours(grades, priorities)
            schedule_df = pd.DataFrame({
                "Subject": subjects,
                "Grade": grades,
                "Priority": priorities,
                "Predicted Study Hours": [round(h, 2) for h in hours]
            })
            st.subheader("📊 Personalized Study Plan")
            st.dataframe(schedule_df, use_container_width=True)

            # Weekly Schedule
            weekly_df = generate_weekly_schedule(subjects, list(hours))
            st.subheader("📅 Weekly Calendar View")
            st.dataframe(weekly_df.fillna(""), use_container_width=True)

            # Clustering
            clusters = cluster_subjects(subjects, grades)
            st.subheader("🔍 Subject Clustering (based on difficulty)")
            for cluster_id, subs in clusters.items():
                st.write(f"Cluster {cluster_id + 1}: {', '.join(subs)}")

            # Weekly report
            # st.subheader("📈 Weekly Study Report")
            # report = generate_report(subjects, grades, [round(h, 2) for h in hours])
            # st.dataframe(report, use_container_width=True)

            # Export
            st.download_button("📤 Download Schedule as CSV", schedule_df.to_csv(index=False), file_name="study_schedule.csv")

    except Exception as e:
        st.error(f"Error: {e}")

# AI Chat Assistant
st.header("🧠 Gemini AI Study Assistant")
question = st.text_input("Ask anything related to study planning, topics, revision, etc.")
if question:
    with st.spinner("Thinking..."):
        reply = chat_response(question)
    st.markdown(f"**🧑‍🧠 Assistant:** {reply}")
