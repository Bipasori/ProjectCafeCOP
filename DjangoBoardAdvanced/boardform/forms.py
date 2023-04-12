from django import forms

from .models import Boardnew

class BoardForm(forms.ModelForm):
    b_title = forms.CharField(label='', widget=forms.TextInput(attrs={
                                        "placeholder":"제목을 넣어주세요"
                                    }
                                )
                              )
    b_note = forms.CharField(required=False, widget=forms.Textarea(
                                    attrs={
                                        "placeholder":"내용을 넣어주세요",
                                        "class":"newclass",
                                        "id":"textid",
                                        "rows":20,
                                        "cols":60
                                    }
                                )
                             )
    b_writer = forms.CharField(initial='홍길동')

    class Meta:
        model = Boardnew
        fields = [
            'b_title',
            'b_note',
            'b_writer'
        ]

    def clean_b_title(self, *args, **kwargs):
        title = self.cleaned_data.get("b_title")
        if not "good" in title:
            raise forms.ValidationError("Not a valid title... include 'good' ")
        if not "title" in title:
            raise forms.ValidationError("Not a valid title... include 'title' ")
        else:
            return title



# standard Django form
class RawBoardForm(forms.Form):
    b_title = forms.CharField(label='', widget=forms.TextInput(attrs={
                                        "placeholder":"제목을 넣어주세요"
                                    }
                                )
                              )
    b_note = forms.CharField(required=False, widget=forms.Textarea(
                                    attrs={
                                        "placeholder":"내용을 넣어주세요",
                                        "class":"newclass",
                                        "id":"textid",
                                        "rows":20,
                                        "cols":60
                                    }
                                )
                             )
    b_writer = forms.CharField(initial='홍길동')