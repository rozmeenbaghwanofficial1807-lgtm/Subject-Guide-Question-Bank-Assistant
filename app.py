
from document_processor import extract_text_from_pdf


def main():
    pdf_path = input(
        "Enter the full path of your PDF file: "
    ).strip().strip('"')

    try:
        text = extract_text_from_pdf(pdf_path)

        print("\n===== EXTRACTED PDF TEXT =====\n")
        print(text)

        with open(
            "extracted_text.txt", "w", encoding="utf-8"
        ) as file:
            file.write(text)

        print("\nText saved to extracted_text.txt")

    except (FileNotFoundError, ValueError) as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
