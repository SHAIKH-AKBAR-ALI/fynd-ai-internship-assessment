# ======================================================================
# Task 2 - AI Feedback System (User + Admin Dashboards)
# Single Streamlit app with tabs, CSV storage, OpenAI GPT-4o-mini
# ======================================================================

import os
import datetime as dt
from pathlib import Path

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------
# 1. Config & Setup
# ---------------------------

load_dotenv()

# Try to get API key from multiple sources
OPENAI_API_KEY = None

# First try Streamlit secrets (for Streamlit Cloud)
try:
    import streamlit as st
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except:
    # Fallback to environment variable (for local development)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# If still no key, ask user to input it
if not OPENAI_API_KEY:
    st.warning("⚠️ OpenAI API Key Required")
    OPENAI_API_KEY = st.text_input(
        "Please enter your OpenAI API Key:", 
        type="password",
        help="Get your API key from https://platform.openai.com/api-keys"
    )
    
    if not OPENAI_API_KEY:
        st.info("👆 Please enter your OpenAI API key above to use the application")
        st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)

FEEDBACK_FILE = Path("feedback.csv")

# Columns we will store
FEEDBACK_COLUMNS = [
    "timestamp",
    "user_name",
    "rating",
    "review_text",
    "user_llm_response",
]


# ---------------------------
# 2. Data Helpers (CSV)
# ---------------------------

def load_feedback() -> pd.DataFrame:
    """Load feedback CSV if exists, else empty DataFrame."""
    if FEEDBACK_FILE.exists() and FEEDBACK_FILE.stat().st_size > 0:
        try:
            df = pd.read_csv(FEEDBACK_FILE)
            # ensure expected columns
            missing = [c for c in FEEDBACK_COLUMNS if c not in df.columns]
            for c in missing:
                df[c] = np.nan
            return df[FEEDBACK_COLUMNS]
        except (pd.errors.EmptyDataError, pd.errors.ParserError):
            return pd.DataFrame(columns=FEEDBACK_COLUMNS)
    else:
        return pd.DataFrame(columns=FEEDBACK_COLUMNS)


def append_feedback(record: dict) -> None:
    """Append single feedback record (dict) to CSV."""
    df = load_feedback()
    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    df.to_csv(FEEDBACK_FILE, index=False)


# ---------------------------
# 3. LLM helper functions
# ---------------------------

def call_openai(prompt: str, max_tokens: int = 300) -> str:
    """Simple wrapper to call GPT-4o-mini."""
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=max_tokens,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"[LLM error: {e}]"


def generate_user_response(user_name: str, rating: int, review_text: str) -> str:
    """Generate a polite, short reply to the user's feedback."""
    name_part = user_name if user_name else "there"
    prompt = f"""
You are a polite customer support assistant.

A customer named {name_part} left this feedback:
Rating: {rating} / 5
Review: \"\"\"{review_text}\"\"\"

Write a short, friendly reply (2-3 sentences) that:
- Thanks them for the feedback
- Acknowledges their sentiment based on rating
- If rating <= 3, apologize briefly and say you'll work to improve
- If rating >= 4, appreciate their support

Don't add any JSON, just natural language.
"""
    return call_openai(prompt, max_tokens=150)


def generate_admin_summary(df: pd.DataFrame) -> str:
    """Summarize overall feedback for admin."""
    # to avoid huge prompts, limit to first 50 reviews
    sample = df.tail(50)
    reviews_text = "\n\n".join(
        [f"Rating {row.rating}: {row.review_text}" for _, row in sample.iterrows()]
    )

    prompt = f"""
You are helping a business owner understand customer feedback.

Here are recent customer reviews (rating and text):

{reviews_text}

Your tasks:
1. Provide a concise summary (4-6 bullet points) of what customers like and dislike.
2. Mention any repeated themes (e.g., staff, waiting time, price, quality).
3. Comment on overall satisfaction (low/medium/high).

Return the answer in markdown with sections:
## Summary
- ...

## Overall Satisfaction
- ...
"""
    return call_openai(prompt, max_tokens=350)


def generate_admin_actions(df: pd.DataFrame) -> str:
    """Suggest actionable improvements for admin."""
    sample = df.tail(50)
    reviews_text = "\n\n".join(
        [f"Rating {row.rating}: {row.review_text}" for _, row in sample.iterrows()]
    )

    prompt = f"""
You are a customer experience consultant.

Based on these customer reviews:

{reviews_text}

Suggest 5-8 practical, specific actions the business can take to improve.
- Mix quick wins and long-term changes
- Focus on things that actually appear in the reviews
- Prioritize impact

Return as a markdown bullet list, no JSON.
"""
    return call_openai(prompt, max_tokens=350)


# ---------------------------
# 4. Streamlit App Layout
# ---------------------------

st.set_page_config(
    page_title="AI Feedback System",
    page_icon="💬",
    layout="wide",
)

st.title("💬 AI-Powered Customer Feedback System")
st.markdown("<div style='text-align: center; color: #666; margin-bottom: 20px;'>Made by SHAIKH AKBAR ALI</div>", unsafe_allow_html=True)

tab_user, tab_admin = st.tabs(["🙋 User Feedback", "🛠️ Admin Dashboard"])

# ---------------------------
# 5. User Feedback Tab
# ---------------------------

with tab_user:
    st.header("Share your feedback")

    with st.form(key="feedback_form"):
        col1, col2 = st.columns(2)
        with col1:
            user_name = st.text_input("Your Name (optional)")
        with col2:
            rating = st.slider("Rating (1 = worst, 5 = best)", min_value=1, max_value=5, value=5)

        review_text = st.text_area("Your Feedback", height=150)

        submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        if not review_text.strip():
            st.error("Please write some feedback before submitting.")
        else:
            # generate LLM response for user
            with st.spinner("Generating AI response..."):
                user_reply = generate_user_response(user_name, rating, review_text)

            # save to CSV
            record = {
                "timestamp": dt.datetime.utcnow().isoformat(),
                "user_name": user_name,
                "rating": rating,
                "review_text": review_text,
                "user_llm_response": user_reply,
            }
            append_feedback(record)

            st.success("Thank you! Your feedback has been recorded.")
            st.subheader("Our Response")
            st.write(user_reply)

# ---------------------------
# 6. Admin Dashboard Tab
# ---------------------------

with tab_admin:
    st.header("Admin Dashboard")

    df_fb = load_feedback()

    if df_fb.empty:
        st.info("No feedback received yet.")
    else:
        # Basic stats
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Total Feedback", len(df_fb))
        with col_b:
            avg_rating = df_fb["rating"].mean()
            st.metric("Average Rating", f"{avg_rating:.2f} / 5")
        with col_c:
            latest_time = pd.to_datetime(df_fb["timestamp"]).max()
            st.metric("Last Feedback At (UTC)", str(latest_time))

        st.markdown("---")

        # Rating distribution chart
        st.subheader("Rating Distribution")
        rating_counts = df_fb["rating"].value_counts().sort_index()
        chart_df = pd.DataFrame({"rating": rating_counts.index, "count": rating_counts.values})
        fig = px.bar(chart_df, x="rating", y="count", labels={"rating": "Rating", "count": "Count"}, title="Ratings Histogram")
        st.plotly_chart(fig, use_container_width=True)

        # Show raw table
        st.subheader("Raw Feedback Data")
        st.dataframe(df_fb.sort_values("timestamp", ascending=False), use_container_width=True, height=300)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("AI Summary of Feedback")
            if st.button("Generate Summary"):
                with st.spinner("Analyzing feedback..."):
                    summary_text = generate_admin_summary(df_fb)
                st.markdown(summary_text)

        with col2:
            st.subheader("AI Recommended Actions")
            if st.button("Generate Actionable Suggestions"):
                with st.spinner("Generating recommendations..."):
                    actions_text = generate_admin_actions(df_fb)
                st.markdown(actions_text)

        st.markdown("> ⚠️ Note: AI-generated insights are suggestions. Please review before acting.")
