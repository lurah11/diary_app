from .models import Entry
from django.forms import ModelForm, Textarea

class EntryForm(ModelForm):
    class Meta: 
        model = Entry 
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
            'text':'Tulislah!!'
        }
    # def __init__(self,*args,**kwargs):
    #  super().__init__(*args,**kwargs)
    #  self.fields['text'].widget.attrs.update({'class':'Textarea','placeholder':'tulis apa yang ada di hatimu :D'})





