import os
from .forms import DocumentForm
from django.views.generic.edit import FormView
from tempfile import NamedTemporaryFile
from .tasks import pdfMaker

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
                    newfile = NamedTemporaryFile(suffix='.'+ext, delete=False)
                    # print(newfile.tempdir)
                    newfile.write(file.read())
                    fls.append(newfile.name)
                    newfile.close()

            pdfMaker.delay(fls)
            # delete the temporary files
            print("It's done man")
            for file in fls:
                os.remove(file)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    


 


