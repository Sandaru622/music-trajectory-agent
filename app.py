import streamlit as st

from agents.trajectory_agent import TrajectoryAgent
from agents.interpreter_agent import InterpreterAgent

st.set_page_config(
    page_title="Music Trajectory Agent",
    page_icon="🎵",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================

with st.sidebar:
    st.title("🎵 Music Trajectory Agent")

    st.markdown("""
### Technologies Used

- 🤖 Groq LLM
- 📚 Retrieval-Augmented Generation (RAG)
- 🗂️ Chroma Vector Database
- 🔎 LangChain Retriever
- 📊 Music Dataset
""")

    st.markdown("---")

    st.info(
        "Enter an artist name and click Analyze to generate an AI-powered music trajectory report."
    )

# ==========================
# Main Page
# ==========================

st.title("🎵 Music Trajectory Agent")

st.write(
    "Analyze an artist's music career using Artificial Intelligence, "
    "Retrieval-Augmented Generation (RAG), and Music Trend Analysis."
)

artist = st.text_input("🎤 Enter Artist Name")

if st.button("Analyze"):

    if artist.strip() == "":
        st.warning("Please enter an artist name.")
        st.stop()

    with st.spinner("Analyzing artist... Please wait..."):

        trajectory = TrajectoryAgent()
        interpreter = InterpreterAgent()

        summary = trajectory.run(artist)

        if summary:

            result = interpreter.run(summary)

            answer = result["answer"]
            knowledge = result["knowledge"]

            st.success("✅ Analysis Completed Successfully!")

            # ==========================
            # Statistics
            # ==========================

            st.subheader("📊 Artist Statistics")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Songs", summary["songs"])

            with col2:
                st.metric(
                    "Highest Views",
                    f"{summary['highest_views']:,}"
                )

            with col3:
                st.metric(
                    "Average Views",
                    f"{summary['average_views']:,}"
                )

            col4, col5, col6, col7 = st.columns(4)

            with col4:
                st.metric("First Release", summary["first_year"])

            with col5:
                st.metric("Latest Release", summary["latest_year"])

            with col6:
                st.metric(
                    "Career Span",
                    f"{summary['career_span']} Years"
                )

            with col7:
                st.metric("Trend", summary["trend"])

            st.divider()

            # ==========================
            # AI Report
            # ==========================

            st.subheader("🤖 AI Career Interpretation")

            with st.expander("View AI Report", expanded=True):
                st.write(answer)

            # ==========================
            # Chart
            # ==========================

            st.subheader("📈 YouTube Views Over Time")

            chart_data = summary["chart_data"][["Release Year", "Youtube Views"]]
            chart_data = chart_data.sort_values("Release Year")

            st.line_chart(
                chart_data.set_index("Release Year")["Youtube Views"]
            )

            # ==========================
            # Retrieved Knowledge
            # ==========================

            st.subheader("📚 Retrieved Knowledge")

            with st.expander("View Retrieved Knowledge"):
                st.write(knowledge)

            # ==========================
            # Download Report
            # ==========================

            st.download_button(
                label="📥 Download AI Report",
                data=answer,
                file_name=f"{artist}_AI_Report.txt",
                mime="text/plain"
            )

        else:
            st.error("❌ Artist not found in the dataset.")

# ==========================
# Footer
# ==========================

st.markdown("---")

st.caption(
    "Developed for IT41043 – Intelligent Systems | Music Trajectory Agent"
)