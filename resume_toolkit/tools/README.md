# Tools

Document processing utilities for resume extraction and handling.

## Functions

### extract_text_from_file(file_path: str) → str

Extracts text content from resume files.

**Supported Formats**:
- PDF (.pdf) - Uses PyPDF2
- Word (.docx) - Uses python-docx

**Parameters**:
- `file_path`: Absolute or relative path to the file

**Returns**:
- Extracted text content as string
- Error message if file not found or extraction fails

**Example**:
```python
from resume_toolkit.tools.document_tools import extract_text_from_file

text = extract_text_from_file("resume.pdf")
```

## Dependencies

- PyPDF2 - PDF text extraction
- python-docx - DOCX text extraction
