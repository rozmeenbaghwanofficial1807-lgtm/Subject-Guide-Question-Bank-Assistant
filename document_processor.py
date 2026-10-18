
from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract readable text from a PDF file."""

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Please select a PDF file.")

    reader = PdfReader(str(path))
    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            extracted_pages.append(
                f"--- Page {page_number} ---\n{text}"
            )

    if not extracted_pages:
        return (
            "No readable text was found. "
            "This PDF may be scanned and require OCR."
        )

    return "\n\n".join(extracted_pages)
