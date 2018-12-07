from django import forms
from blog.models import Post
from blog.models import Komentarz

class PostForm(forms.ModelForm):

#utworzenie meta-klasy w celu użycia widget-ów do strony
    class Meta():
        model = Post
        fields = ('autor', 'tytul', 'text')

#utworzenie widgetów za pomoca slownika
# kazdy widget jest w formie klucz-wartosc gdzie wartosciami są słowniki atrybutow i klasy CSS np. klasatextowa, editable
        widgets = {
            'tytul': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
            #editable medium-editor-textarea to nie są moje klasy

        }

class KomentarzForm(forms.ModelForm):
    class Meta():
        model = Komentarz
        fields = ('autor', 'text')

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
            #editable medium-editor-textarea to nie są moje klasy

    }
