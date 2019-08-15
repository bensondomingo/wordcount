from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'website_name': 'Word Counter'})

def count(request):
    word_str = request.GET['words']
    word_set = set(word_str.split(' '))

    word_count_dict = dict(
        zip(word_set, map(word_str.count, word_set))
    )

    word_sorted = sorted(word_count_dict, key=word_count_dict.get, reverse=True)
    word_sorted = [(word, word_count_dict[word]) for word in word_sorted]
    return render(
        request, 
        'count.html', 
        {'word_str': word_str, 'word_sorted': word_sorted},
    )

def about(request):
    return render(request, 'about.html')