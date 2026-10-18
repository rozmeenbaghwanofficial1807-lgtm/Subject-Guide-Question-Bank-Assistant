
import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="Subject Guide & Question Bank Assistant",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Subject Guide & Question Bank Assistant")
st.write(
    "Upload your syllabus, study notes, or previous question papers "
    "in PDF format."
)

st.info(
    "Current feature: PDF text extraction. "
    "AI-based question answering will be added in a later stage."
)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
)

if uploaded_file is not None:
    try:
        reader = PdfReader(uploaded_file)
        extracted_pages = []

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            if text.strip():
                extracted_pages.append(
                    f"--- Page {page_number} ---\n{text}"
                )

        if extracted_pages:
            extracted_text = "\n\n".join(extracted_pages)

            st.success("PDF uploaded and text extracted successfully!")
            st.write(f"**Pages in PDF:** {len(reader.pages)}")

            st.subheader("Extracted Text")

            st.text_area(
                "PDF content",
                value=extracted_text,
                height=350,
            )

            st.download_button(
                label="Download Extracted Text",
                data=extracted_text,
                file_name="extracted_text.txt",
                mime="text/plain",
            )
        else:
            st.warning(
                "No readable text found. "
                "This PDF may contain scanned images and need OCR."
            )

    except Exception as error:
        st.error(f"Could not process this PDF: {error}")
