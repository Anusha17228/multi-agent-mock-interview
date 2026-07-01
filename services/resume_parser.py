from pypdf import PdfReader
import io


def parse_resume(uploaded_file):
    file_type = uploaded_file.name.split(".")[-1].lower()

    # Handle TXT files
    if file_type == "txt":
        return uploaded_file.read().decode("utf-8")

    # Handle PDF files
    elif file_type == "pdf":
        pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
        text = ""

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text

    else:
        raise ValueError("Unsupported file format. Upload TXT or PDF.")
