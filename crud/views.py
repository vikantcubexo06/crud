from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from jangoPro1 import settings
from .ModelForm import UserForm, RegistrationForm
from .models import Information, Profile
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail


@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        user = request.POST['username']
        print(request.POST)
        print(request.FILES)
        imag = request.FILES['pic']
        try:
            v = Profile.objects.get(user=User.objects.get(username=user))
            if v:
                v.imag = request.FILES["pic"]
                v.save()
                # messages.success(request, 'Profile updated successfully')
                return redirect('user_profile')
        except:
            update_form = Profile.objects.create(user=User.objects.get(username=user), imag=imag)
            update_form.save()
            # messages.success(request, 'Profile updated successfully')
            return redirect('user_profile')
    else:
        user = {}
        user['username'] = request.session['username']
        user1 = Profile.objects.filter(user=User.objects.get(username=user['username']))
        if user1:
            return render(request, 'profile.html', context={'username': user,"pic": user1[0]})

    return render(request, 'profile.html', context={'username': user})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = authenticate(request, username=username, password=password)
        if user1 is not None:
            login(request, user1)
            messages.success(request, 'welcome user ')

            request.session['username'] = username

            context = {
                "username": username
            }

            # return render(request, 'create_view.html', context)
            return redirect('create_view')
        else:
            fm = AuthenticationForm()
            return render(request, 'login.html', {'form': fm, "msg": "invalid details"})
    fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


@login_required(login_url='login')
def create_view(request):
    if User.objects.get(username=request.user.username).get_username() == 'vikrant':

        if request.method == 'POST':
            f = UserForm(request.POST)

            if f.is_valid():
                f.save()

            return HttpResponseRedirect(reverse(create_view))
        else:
            f = UserForm()
            data = Information.objects.all()

            context = {
                "form": f,
                'data': data

            }

            return render(request, 'create_view.html', context)
    else:
        if request.method == 'POST':
            username = request.POST['User_name']
            first_name = request.POST['First_name']
            last_name = request.POST['Last_name']
            email = request.POST['Email']
            age = request.POST['Age']

            # obj = User.objects.filter(email=email)
            # print(obj)
            obj = Information.objects.create(User_name=User.objects.get(username=username), First_name=first_name,
                                             Last_name=last_name, Email=email, Age=age)
            obj.save()

            # add = Information.objects.get(id=newKey.pk)
            # add.user = obj
            # add.save()

            return HttpResponseRedirect(reverse(create_view))
        else:
            # obj = User.objects.get(pk=request.user.id)

            data = Information.objects.filter(User_name=request.user)
            # data1 = Information.objects.all()
            # print("data1")
            f = UserForm()
            # f.id = obj

            # print(f.id)

            # f = UserForm()
            # def name():
            # if data.first().User_name == request.session['username']:
            #     return data.first().User_name_id

            context = {
                "form": f,
                'data': data,
                'username': data.first().User_name_id
            }
            print(context.get('username'))
            return render(request, 'create_view.html', context)


def Update(request, id):
    if request.method == "POST":
        obj = Information.objects.get(id=id)
        obj.First_name = request.POST['first_name']
        obj.Last_name = request.POST['last_name']
        obj.Email = request.POST['email']
        obj.Age = request.POST['age']
        obj.save()
        return redirect(create_view)

    else:
        data = Information.objects.get(id=id)

        context = {
            'data': data
        }
        return render(request, 'update_view.html', context)


def delete(request, id):
    obj = Information.objects.get(id=id)
    obj.delete()
    return redirect(create_view)


def boot(request):
    return render(request, "boot.html")


def register_view(request):
    ''' for registration of user'''

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST["username"]
        password = request.POST['password1']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Already exits')
            return redirect("register")
        else:
            hash = make_password(password)
            fm = User.objects.create(username=username, email=email, password=hash,
                                     first_name=first_name, last_name=last_name)
            fm.save()
            messages.error(request, 'Account Created')
            return redirect("register")
    # else:
    #     fm = User.objects.all()
    #     context={
    #         'form':fm
    #     }
    #     print(context)
    #     return render(request, 'registration.html', context=context)

    #     fm = UserCreationForm(request.POST)
    #     print(fm)
    #     if fm.is_valid():
    #         fm.save()
    #         messages.success(request, 'Account Created Successfully')
    #
    #         subject = 'welcome to the site'
    #         message1 = ' thanks for registration'
    #         send_mail(subject, message1, settings.EMAIL_HOST_USER, [request.POST['email']], fail_silently=False)
    #         return redirect(login_view)
    #     else:
    #         messages.success(request, 'Invalid data entry')
    #         return redirect(register_view)
    else:
        fm = RegistrationForm()
        context = {
            'form': fm
        }
        # print(context)
        return render(request, 'registration.html', context=context)


def logoutPage(request):
    logout(request)
    messages.error(request, 'user logged out successfully')
    return redirect('create_view')


def pass_reset(request):
    # obj= user.objects.get(id=id)
    # obj
    # print('hiii')
    return render(request, "password_reset_view.html")


def forget_pass(request):
    if request.method == 'POST':
        domain = request.headers['HOST']
        # print('hello')
        # if User.objects.filter(email=request.POST['email']).exists():
        # otp = random.randint(1111, 9999)
        # print(otp)
        # subject = 'Reset password'
        # message = otp
        # print([request.POST['email'], ])
        # send_mail(subject, str(message), settings.EMAIL_HOST_USER, [request.POST['email'], ], fail_silently=False)
        associated_user = User.objects.filter(email=request.POST['email'])
        if associated_user.exists():
            for i in associated_user:
                subject = 'Reset password'
                c = {

                    "email": i.email,
                    'domain': domain,

                    "uid": urlsafe_base64_encode(force_bytes(i.pk)),

                    "token": default_token_generator.make_token(i),
                    'protocol': 'http',
                }

                email = render_to_string('pass_email.txt', c)
                send_mail(subject, email, settings.EMAIL_HOST_USER, [request.POST['email']], fail_silently=False)
                return render(request, "password_reset_done.html")
        # print('none happing')
    # print('not sending')
