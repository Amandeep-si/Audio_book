import pyttsx3
import PyPDF2
book=open('SWOC Analysis.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print("Number of pages in this pdf are: ",pages)
speaker=pyttsx3.init()
p=('total number of pages in this pdf are',pages)
speaker.say(p)
for i in range(pages):
    page=pdfReader.getPage(i)
    text=page.extractText()
    page_no=i+1
    tell=('Page number is',page_no)
    speaker.say(tell)
    speaker.say(text)
    speaker.runAndWait()