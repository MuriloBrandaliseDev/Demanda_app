from django import forms
from .models import Demanda
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['titulo', 'descricao', 'data_demanda']
    
    def __init__(self, *args, **kwargs):
        super(DemandaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Removendo labels
        self.fields['titulo'].label = ''
        self.fields['descricao'].label = ''
        self.fields['data_demanda'].label = ''

        # Adicionando classes e placeholders
        self.fields['titulo'].widget.attrs.update({'placeholder': 'Título', 'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'placeholder': 'Descrição', 'class': 'form-control'})
        self.fields['data_demanda'].widget.attrs.update({'placeholder': 'Data da demanda', 'class': 'form-control'})

        # Definindo layout do Crispy Forms sem os labels
        self.helper.layout = Layout(
            'titulo',
            'descricao',
            'data_demanda',
            ButtonHolder(
                Submit('submit', 'Salvar', css_class='btn btn-pink')
            )
        )
