import os
import PyPDF2
import docx


def extract_text_from_file(file_path: str) -> str:
    """
    Extracts and returns text from a given PDF or DOCX file path.

    Args:
        file_path (str): The absolute or relative path to the resume file.

    Returns:
        str: The extracted text content, or an error message if extraction fails.
    """
    if not os.path.exists(file_path):
        return f"Error: The file at '{file_path}' was not found."

    file_extension = os.path.splitext(file_path)[1].lower()
    extracted_text = ""

    try:
        if file_extension == '.pdf':
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        extracted_text += text + "\n"

        elif file_extension == '.docx':
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                extracted_text += para.text + "\n"

        elif file_extension == '.txt':
            with open(file_path, 'r', encoding='utf-8') as file:
                extracted_text = file.read()

        else:
            return f"Error: Unsupported file format '{file_extension}'. Please provide a PDF, DOCX, or TXT file."

        if not extracted_text.strip():
            return "Error: The file was read successfully, but no text could be extracted (it might be a scanned image)."
        print("My extracted resume", extracted_text.strip())
        return extracted_text.strip()

    except Exception as e:
        return f"Error during file extraction: {str(e)}"


def save_optimized_resume(content: str, output_path: str) -> str:
    """
    Saves the tailored resume content to the specified output path.

    Args:
        content (str): The optimized resume text (usually in Markdown format).
        output_path (str): The desired file path to save the document.

    Returns:
        str: A success or error message for the orchestrator to log.
    """
    try:
        # Ensure the output directory exists before trying to write to it
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the content as a Markdown/Text file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)

        return f"Success! Optimized resume saved securely to {output_path}"

    except Exception as e:
        return f"Error saving the optimized resume: {str(e)}"