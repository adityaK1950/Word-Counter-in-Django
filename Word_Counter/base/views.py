from django.shortcuts import render

def home(request):
    if request.method == "POST":
        text = request.POST.get('words', '')
        words = str(text).strip()
        
        if words:
            number_of_words = len(words.split())
        else:
            number_of_words = 0

        return render(request, 'index.html', {
            'n_words': number_of_words,
            'words': words,
        })

    return render(request, 'index.html')
