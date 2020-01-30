from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import RegistrationForm,CheckForm
from .models import Registration
from face.detect import face_detect
import MySQLdb

def home(request):
	return render(request,template_name='home.html')

def reg(request):

	if request.method=='POST':
		form = RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			name=form.cleaned_data.get('name')
			email=form.cleaned_data.get('email')
			mobile=form.cleaned_data.get('mobile')
			image = form.cleaned_data.get('image')
			r=Registration(name=name,email=email,mobile=mobile,image=image)
			r.save()
			form = RegistrationForm()
			return render(request,'reg.html',{'form':form})
		else:
			return render(request,'reg.html',{'form':form})
			
	else:
		form=RegistrationForm()
		return render(request,'reg.html',{'form':form})

def check(request):


	if request.method=='POST':
		form = CheckForm(request.POST, request.FILES)
		if form.is_valid():
			
			image = form.cleaned_data.get('image')
			result = face_detect(image)
			# print(result)
			
			db = MySQLdb.connect(host="localhost",
			                     user="naresh",
			                     passwd="naresh24",
			                     db="mydb") 

			cur = db.cursor()
			cur.execute("select *from face_registration where image='%s'"%result)
			res = cur.fetchone()
			db.close()
							
			try:
				res1 = {'Name':res[1],'Email':res[2],'Phone':res[3]}
				img = res[4]
				
				return render(request,'result.html',{'data':res1,'data1':'/media/'+img})
			except:
				return HttpResponse('No Data Found....!')
		else:
			return render(request,'log.html',{'form':form})
			
	else:
		form=CheckForm()
		return render(request,'log.html',{'form':form})

