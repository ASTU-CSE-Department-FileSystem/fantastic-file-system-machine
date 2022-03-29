import os
from pydoc import Doc
from django.shortcuts import render
from fpdf import FPDF
from .forms import DocumentForm
from django.views.generic.edit import FormView
from tempfile import NamedTemporaryFile

def pdfMaker(images):
    print("I am here")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for image in images:
        pdf.image(image, 0,0,w=210, h=297)
        pdf.add_page()
    pdf.output("test.pdf", "F")

class DocumentFormView(FormView):
    form_class = DocumentForm
    template_name = 'test.html'
    success_url = '/test'
    def post(self, request, *args, **kwargs):
        form=DocumentForm(request.POST or None,request.FILES or None)
        files = request.FILES.getlist('image')
        print(files)
        if form.is_valid():
            fls = []
            for file in files:
                newfile = NamedTemporaryFile(delete=False, suffix='.png')
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
    


 


