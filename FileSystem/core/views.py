import os
from fpdf import FPDF
from .forms import DocumentForm
from django.views.generic.edit import FormView
from tempfile import NamedTemporaryFile
from PIL import Image

def pdfMaker(images):
    print("I am here")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for image in images:
        cover = Image.open(image)
        X, Y = cover.size
        if X > Y:
            cover = cover.rotate(-90, expand=True)  
            cover.save(image)
        pdf.image(image, 0,0,w=210)
        pdf.add_page()  
    pdf.output("test.pdf", "F")

class DocumentFormView(FormView):
    form_class = DocumentForm
    template_name = 'test.html'
    success_url = '/test'
    def post(self, request, *args, **kwargs):
        form=DocumentForm(request.POST or None,request.FILES or None)
        files = request.FILES.getlist('image')
        extentions = ('jpg', 'png', 'jpeg')
        if form.is_valid():
            fls = []
            for file in files:
                ext = file.name.split('.')[-1]
                if ext.lower() in extentions:
                    newfile = NamedTemporaryFile(delete=False, suffix='.'+ext)
                    newfile.write(file.read())
                    fls.append(newfile.name)
                    newfile.close()

            pdfMaker(fls)
            # delete the temporary files
            for file in fls:
                os.remove(file)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    


 


