# PDF to Speech Converter

A Python-based tool that converts PDF documents to speech, with support for OCR (Optical Character Recognition) for scanned documents.

## Features

- PDF text extraction
- OCR support for scanned documents using OCR.space API
- Text-to-speech conversion using gTTS (Google Text-to-Speech)
- Support for multiple languages
- Automatic audio playback
- Handles multi-page PDFs
- Text file output option

## Prerequisites

- Python 3.x
- OCR.space API key (for OCR functionality)

## Installation

1. Clone this repository
2. Install required packages:

```bash
pip install requests gtts PyPDF2 Pillow
```

## Usage

### Simple Text-to-Speech Conversion

For PDFs with extractable text:

```python
from d.tts import pdf_to_speech

pdf_to_speech("your_file.pdf", lang='en', slow=False)
```

### OCR and Speech Conversion

For scanned PDFs requiring OCR:

```python
from final_working import perform_ocr_on_pdf, text_to_speech

# Replace with your OCR.space API key
api_key = "your_api_key"

# Extract text using OCR
text = perform_ocr_on_pdf("your_file.pdf", api_key)

# Convert to speech
text_to_speech(text, "output.mp3", lang='en', slow=False)
```

### Simple Text File to Speech

To convert a text file directly to speech:

```python
from simpletts import main
# Place your text in input.txt and run
main()
```

## Configuration

- `lang`: Language code (default: 'en' for English)
- `slow`: Speech speed (default: False for normal speed)
- OCR Engine: Set to 2 for better PDF processing
- Supported file formats: PDF, TXT

## Error Handling

The tool includes comprehensive error handling for:
- File not found errors
- OCR processing errors
- Text-to-speech conversion issues
- Audio playback problems

## Output Files

- `output.mp3`: Generated audio file
- `output.txt`: Extracted text (when using OCR)

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Acknowledgments

- OCR.space for OCR API
- Google Text-to-Speech (gTTS) for speech synthesis
