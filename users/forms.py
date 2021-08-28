from django import forms


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser

from django.contrib.auth.forms import UserCreationForm




class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    # email = forms.CharField(widget=forms.EmailInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # first_name = forms.CharField(label='Firstname', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Firstname'}))
    # last_name = forms.CharField(label='Lastname', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Lastname'}))
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    # # Dealership = forms.ModelChoiceField(queryset=Dealership.objects.all())

    class Meta():
        model = CustomUser
        # fields = "__all__"
        fields = ['username', 'password1', 'email',
                  'first_name', 'last_name', 'password2']

    # def save(self, commit=True):
    # 	user = super().save(commit=False)
    # 	user.username = self.cleaned_data['username']
    # 	user.email = self.cleaned_data['email']
    # 	user.first_name = self.cleaned_data['first_name']
    # 	user.last_name = self.cleaned_data['last_name']
    # 	user.groups = self.cleaned_data['groups']
    # 	user.password1 = self.cleaned_data['password1']
    # 	user.password2 = self.cleaned_data['password2']

    # 	if commit:
    # 		user.save()
    # 		return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
