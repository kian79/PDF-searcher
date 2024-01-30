import PyPDF2
import nltk
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')

def convert_pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text.replace('\n', ' ')


def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))

    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, num_sentences)

    summary_text = ' '.join(str(sentence) for sentence in summary)

    return summary_text

