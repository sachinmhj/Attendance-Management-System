from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import StudentCreateForm, TeacherCreateForm, AdminCreateForm, UserEditFrom
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
# from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            ath = AuthenticationForm(request=request, data=request.POST)
            if ath.is_valid():
                uname = ath.cleaned_data.get('username')
                pw = ath.cleaned_data.get('password')
                checkuser = authenticate(username=uname, password=pw)
                if checkuser != None:
                    login(request, checkuser)
                    # print(request.user.pk)
                    # print(checkuser.pk)
                    return redirect(f'/dashboard-page/{checkuser.user_slug}/')
        else:
            ath = AuthenticationForm()
        context = {'authenticate':ath}
        return render(request, 'users/authentication/login.html', context)
    messages.warning(request, 'Please logout first.')
    return redirect('/')

def dashboardpage(request, sg):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.role=='admin':
            return redirect('/admin/')
        # registereduser = User.objects.get(id=sg)
        registereduser = CustomUser.objects.get(user_slug=sg)
        return render(request, 'users/dashboardpg.html', {'reguser':registereduser})
    messages.warning(request, 'Please login first to visit Dashboard Page.')
    return redirect('/')

def registerpage(request, user_role):
    # if request.method == "POST":
    #     usercreate = AdminCreateForm(request.POST, request.FILES)
    #      # if usercreate.is_valid():
    #         # print(usercreate.cleaned_data)
    #         # username = usercreate.cleaned_data.get('username')
    #         # firstname = usercreate.cleaned_data.get('first_name', 'empty')
    #         # lastname = usercreate.cleaned_data.get('last_name', 'empty')
    #         # email = usercreate.cleaned_data.get('email', 'empty')
    #         # active = usercreate.cleaned_data.get('is_active', True)
    #         # staff = usercreate.cleaned_data.get('is_staff', False)
    #         # dob = usercreate.cleaned_data.get('date_of_birth', 'empty')
    #         # userimage = usercreate.cleaned_data.get('user_image')
    #         # role = usercreate.cleaned_data.get('role')
    #         # datejoined = usercreate.cleaned_data.get('date_joined', timezone.now())
    #         # if role == 'student':
    #         #     stu = Student(username=username,first_name=firstname,last_name=lastname,email=email,is_active=active,is_staff=staff,date_of_birth=dob,user_image=userimage,role=role,date_joined=datejoined)
    #         #     stu.save()
    #         # elif role == 'teacher':
    #         #     teach = Teacher(username=username,first_name=firstname,last_name=lastname,email=email,is_active=active,is_staff=staff,date_of_birth=dob,user_image=userimage,role=role,date_joined=datejoined)
    #         #     teach.save()
    #         # else:
    #         #     print('admin')
    #     if usercreate.is_valid():
    #         usercreate.save()
    #         messages.success(request, 'Thanks for registering, you can now login.')
    #         return HttpResponseRedirect('/')
    # else:
    #     usercreate = AdminCreateForm()
    if request.method == "POST":
        if user_role == 'student':
            usercreate = StudentCreateForm(request.POST,request.FILES)
        elif user_role == 'teacher':
            usercreate = TeacherCreateForm(request.POST,request.FILES)
        else:
            usercreate = AdminCreateForm(request.POST,request.FILES)
        if usercreate.is_valid():
            usercreate.instance.role = user_role
            if usercreate.instance.role == 'admin':
                usercreate.instance.is_staff = True
                usercreate.instance.is_superuser = True
            if usercreate.instance.role == 'teacher':
                usercreate.instance.is_staff = True
            usercreate.save()
            messages.success(request, 'Thanks for registering, you can now login.')
            return redirect('/')
    else:
        if user_role == 'student':
            usercreate = StudentCreateForm()
        elif user_role == 'teacher':
            usercreate = TeacherCreateForm()
        elif user_role == 'admin':
            usercreate = AdminCreateForm()
        else:
            return redirect('/')
    context = {'createform':usercreate}
    return render(request, 'users/authentication/register.html', context)

def selectrole(request):
    return render(request, 'users/authentication/selectrole.html')

def editpage(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            editform = UserEditFrom(request.POST, request.FILES, instance=request.user)
            if editform.is_valid():
                editform.save()
                return redirect(f'/dashboard-page/{request.user.user_slug}/')
        else:
            editform = UserEditFrom(instance=request.user)
        return render(request, 'users/useredit/editprofile.html',{'editform':editform})
    messages.warning(request, 'Please login first to visit Profile Page.')
    return redirect('/')

def changepw(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pw = PasswordChangeForm(user=request.user, data=request.POST)
            if pw.is_valid():
                pw.save()
                update_session_auth_hash(request, pw.user)
                return redirect(f'/dashboard-page/{request.user.user_slug}/')
        else:
            pw = PasswordChangeForm(user=request.user)
        return render(request, 'users/useredit/changepw.html', {'pw':pw})
    messages.warning(request, 'Please login first to visit the Page.')
    return redirect('/')

def logoutpage(request):
    logout(request)
    return redirect('/')

