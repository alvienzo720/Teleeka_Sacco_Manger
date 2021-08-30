from django.shortcuts import render, redirect 

from django.http import HttpResponse

from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth.models import User

from django.forms.utils import ErrorList

from .forms import  CreateClientForm, CreateDepositForm, CreateWithdrawlForm, CreateSavingGroupForm, LoginForm, SignUpForm

from django.contrib.auth import authenticate, login , logout 

from django.contrib.auth.decorators import login_required

from .decorators import unauthnticated_user, admin_only

from django.contrib.auth.models import Group

from .models import *


def loginPage(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "teleeka/login.html", {"form": form, "msg" : msg})


def reigsterPage(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "teleeka/register.html", {"form": form, "msg" : msg, "success" : success })


# Create your views here.

# @unauthnticated_user
# def reigsterPage(request):
# 	form = CreateUserForm()

# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')

# 			group = Group.objects.get(name='clients')

# 			user.groups.add(group)

# 			messages.success(request, 'Account was created for '+ username)
# 			return redirect('login')

# 	context = {'form':form}
# 	return render(request, 'teleeka/register.html', context)


# Login View
# @unauthnticated_user
# def loginPage(request):

# 	username = request.POST.get('username')
# 	password = request.POST.get('password')

# 	user = authenticate(request, username=username, password=password)
# 	if user is not None:
# 		login(request, user)
# 		return redirect('home')

# 	else:
# 		messages.info(request, 'Username or Password is Incorrect')

# 	context = {}
# 	return render(request, 'teleeka/login.html',context)





# home view
@login_required(login_url='login')
@admin_only
def home(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	context = {'clients':clients,'client_count':client_count,'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls, 'count_withdrawls':count_withdrawls}

	return render(request, 'teleeka/index.html', context)


# Logout View
@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')



def profile(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}


	return render(request, 'teleeka/profile.html',context)


def deposit(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	

	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}
	

	return render(request, 'teleeka/deposit.html', context)


def withdrawl(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}

	return render(request, 'teleeka/withdrawl.html', context)



def transactions(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}
	
	return render(request, 'teleeka/transactions.html', context)


# clients view
def clientPage(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()
	
	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}

	return render(request, 'teleeka/clientspage.html', context)



def createClient(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	if request.method == 'POST':
		form = CreateClientForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('clientpage')
			except:
				pass
	else:
		form = CreateClientForm()
	
	
	context = {'form':form,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}


	return render(request, 'teleeka/createClient.html',context)
					

#edit Client View

def editClient(request, pk):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()
	client = Client.objects.get(id=pk)
	formset = CreateClientForm(instance=client)
	if request.POST == 'POST':
		print("Printing POST: ", request.POST)
		formset = CreateClientForm(request.POST, instance=client)
		if formset.is_valid():
			formset.save()
				# model = formset.instance
			return redirect('clientpage')
			# except Exception as e:
			# 	pass
	context = {'formset':formset,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}
	return render(request, 'teleeka/editClient.html', context)



# delete Client View
def deleteClient(request,pk):
	client = Client.objects.get(id=pk)
	if request.method == 'POST':
		client.delete()
		return redirect('clientpage')
	context = {'client':client}
	return render(request, 'teleeka/delteClient.html', context)


def createDeposit(request):

	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	if request.method == 'POST':
		form = CreateDepositForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('deposit')
			except:
				pass
	else:
		form = CreateDepositForm()
	
	context = {'form':form,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}


	
	return render(request, 'teleeka/createDeposit.html', context)


def deleteDeposit(request,pk):
	deposit = Deposit.objects.get(id=pk)
	if request.method == 'POST':
		deposit.delete()
		return redirect('deposit')
	context = {'deposit':deposit}
	return render(request, 'teleeka/deleteDeposit.html', context)



def createWithdraw(request):

	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	if request.method == 'POST':
		form = CreateWithdrawlForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('withdrawl')
			except:
				pass
	else:
		form = CreateWithdrawlForm()
	
	context = {'form':form,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups,'count_groups':count_groups}


	
	return render(request, 'teleeka/createWithdraw.html', context)



def deleteWithdrawl(request,pk):
	withdrawl = Withdrawl.objects.get(id=pk)
	if request.method == 'POST':
		withdrawl.delete()
		return redirect('withdrawl')
	context = {'withdrawl':withdrawl}
	return render(request, 'teleeka/deleteWithdrawl.html', context)



def groupPage(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()
	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups, 'count_groups':count_groups}

	return render(request, 'teleeka/groupPage.html', context)



def createGroup(request):

	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	groups = SavingGroup.objects.all()
	count_groups = groups.count()

	if request.method == 'POST':
		form = CreateSavingGroupForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('groupPage')
			except:
				pass
	else:
		form = CreateSavingGroupForm()
	
	context = {'form':form,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'groups':groups, 'count_groups':count_groups}


	
	return render(request, 'teleeka/createGroup.html', context)





def deleteGroup(request,pk):
	group = SavingGroup.objects.get(id=pk)
	if request.method == 'POST':
		group.delete()
		return redirect('groupPage')
	context = {'group':group}
	return render(request, 'teleeka/deleteGroup.html', context)






