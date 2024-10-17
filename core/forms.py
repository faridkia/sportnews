from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(max_length=75)

    def clean_text(self):
        text = self.cleaned_data['text']
        lst = ['عوضی','بی شخصیت']
        for i in lst:
            if i in text:
                raise forms.ValidationError('متن شامل حرفای ناسزا است.')
        if len(text) < 4 :
            raise forms.ValidationError('متن کوتاه است.')
        return text
