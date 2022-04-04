from FileSystem.celery import app as celery_app
from celery import shared_task
from PIL import Image
from fpdf import FPDF

@celery_app.task(bind=True)
# @shared_task(bind=True)
def pdfMaker(self, *args, **kwargs):
    print("I am here")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    print("args: ",args)
    for image in args[0]:
        cover = Image.open(image)
        X, Y = cover.size
        if X > Y:
            cover = cover.rotate(-90, expand=True)  
            cover.save(image)
        pdf.image(image, 0,0,w=210)
        pdf.add_page()  
    pdf.output("test.pdf", "F")