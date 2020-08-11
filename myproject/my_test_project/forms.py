from django import forms


class userP1form(forms.Form):
    content = forms.CharField()

class searchPageform(forms.Form):
    searchVal = forms.CharField()

