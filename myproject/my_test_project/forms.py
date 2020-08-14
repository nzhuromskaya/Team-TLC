from django import forms


class userP1form(forms.Form):
    '''
    Input forms for userP1 page
    '''
    content = forms.CharField()

class searchPageform(forms.Form):
    '''
    Inputp forms for searchPageform page
    '''
    searchVal = forms.CharField()

