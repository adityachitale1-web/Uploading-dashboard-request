import streamlit as st
from pathlib import Path
from text_utils import to_upper, to_lower, strip_text, replace_text, count_substring, add_timestamp

st.set_page_config(page_title="Text Helper", page_icon="📝", layout="wide")

# Load custom style
with open("style.css") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

st.title("📝 Text Helper App")
st.write("Upload, view, edit, and process your text files easily.")

st.sidebar.header("Upload & Mode Selection")
uploaded_file = st.sidebar.file_uploader("Upload a .txt file", type=["txt"])
mode = st.sidebar.selectbox("Select Mode", ["Read", "Append"])

if uploaded_file:
    if Path(uploaded_file.name).suffix != ".txt":
        st.error("❌ Only .txt files are supported.")
    else:
        text = uploaded_file.read().decode("utf-8")
        lines = text.splitlines()
        st.subheader("📄 File Preview (first 20 lines)")
        preview = "\n".join(lines[:20])
        st.code(preview, language="text")

        # Display basic stats
        line_count = len(lines)
        word_count = len(text.split())
        char_count = len(text)
        st.markdown(f"**Lines:** {line_count} | **Words:** {word_count} | **Characters:** {char_count}")

        # String operations
        st.subheader("✏️ String Operations")
        col1, col2, col3 = st.columns(3)

        if col1.button("UPPERCASE"):
            text = to_upper(text)
        if col1.button("lowercase"):
            text = to_lower(text)
        if col2.button("strip (trim)") :
            text = strip_text(text)

        with col2:
            old = st.text_input("Replace: old value")
            new = st.text_input("Replace: new value")
            if st.button("Apply Replace"):
                text = replace_text(text, old, new)

        with col3:
            substring = st.text_input("Count substring")
            if st.button("Count"):
                count = count_substring(text, substring)
                st.info(f"'{substring}' appears **{count}** times.")

        st.subheader("🔍 Updated Preview")
        st.code("\n".join(text.splitlines()[:20]), language="text")

        if mode == "Append":
            st.subheader("💾 Save & Append Mode")
            extra_text = st.text_area("Extra text to append")
            if st.button("Save File"):
                final_text = add_timestamp(text + "\n" + extra_text)
                st.download_button(
                    label="📥 Download Processed File",
                    data=final_text,
                    file_name=f"processed_{uploaded_file.name}",
                    mime="text/plain"
                )
        else:
            st.warning("Saving is disabled in Read mode.")
else:
    st.info("👆 Please upload a .txt file to get started.")
