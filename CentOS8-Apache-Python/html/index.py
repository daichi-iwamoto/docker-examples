from docx import Document

document = Document()

document.add_paragraph("test")

# word 書込み
document.save("test.docx")
