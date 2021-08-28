# from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import generics
from django.contrib import auth
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .decorators import *
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view

from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from api.models import *


@unauthenticated_user
def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboardMainPage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username taken")
            elif User.objects.filter(email=email).exists():
                print("email already exist ")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            print("Password is not matched")

    else:
        return render(request, 'login/signup.html')


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # IsAdminUser

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in CustomUser.objects.all()]
        return Response(usernames)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            data_saved = serializer.save()
            data['response'] = "Successfully registered"
            data['email'] = data_saved.email
            data['user_id'] = data_saved.id
            data['username'] = data_saved.username
            token = Token.objects.get(user=data_saved).key
            data['token'] = token
            uid = data['username']
            getuser = CustomUser.objects.get(username = uid)
            UserWallet.objects.create(UserWalletID = getuser , Wallet = 10000)
        else:
            data = serializer.errors
        return Response(data)
