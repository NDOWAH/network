from PyPDF2 import PdfFileReader


def extract_infomation(document_path):
    with open(document_path,'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        page_number = pdf.getPageNumber()
        doc = f'''information about{document_path}.
        author: {info.author}
        title: {info.title}
        creator: {info.creator}
        page_number: {page_number}'''
    print(doc)
    return info

