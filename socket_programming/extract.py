from PyPDF2 import PdfFileReader, PdfFileWriter


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

def put_watermark(file_path, watermark,output):
    #output here is the destination file we which to write our result
    pdf_reader = PdfFileReader(file_path)
    pdf_writer = PdfFileWriter()
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getpage(0)
    for page in range(pdf_reader.getPageNumber()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)
        with open(output) as f:
            pdf_writer.write(f)