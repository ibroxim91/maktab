from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def page_views(request, page_name):
	return render(request, 'pages/{}.html'.format(page_name))

def ajax_test(request):
	numbers = range(1,16)
	print(numbers)
	context = {'numbers':numbers}
	return render(request,'pages/test.html', context)	