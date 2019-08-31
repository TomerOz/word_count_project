from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
	return render(request, 'home.html')
	# Example : return render(request, 'home.html', {'key' : 'value'})

def about(request):
	return render(request, 'about.html')

def count(request):
	full_text = request.GET['fulltext']
	words = full_text.split()
	words_ammount = len(words)
	
	words_dict = {}
	for w in words:
		words_dict.setdefault(w, 0)
		words_dict[w] += 1
		
	words_freq_list = words_dict.items() # convert dict to tupple pairs list
	sorted_words = sorted(words_freq_list, key=operator.itemgetter(1), reverse=True)
	
	return render(request, 'count.html', {
										'fulltext':full_text, 
										'wordsAmmount': words_ammount,
										'wordsDict': sorted_words,
										})