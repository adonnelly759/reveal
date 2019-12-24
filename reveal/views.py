from django.shortcuts import render
from .models import Codes, Question, Answer
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    show = datetime(2019, 12, 25)
    today = datetime.today()

    if show < today:
        c = Codes.objects.get(pk=1)
        code = c.code[:c.sub]

        allAns = len(Answer.objects.all())
        corAns = len(Answer.objects.filter(correct=True))

        try:
            ans = Answer.objects.filter(correct=False)[:1].get()
        except Answer.DoesNotExist:
            ans = None


        if ans:
            if request.method == "POST":
                i = request.POST.get("answer")
                if ans.title == i:
                    ans.correct = True
                    ans.save()
                    sub = c.sub
                    c.sub = sub+1
                    c.save()
                    messages.success(request, 'That answer was correct! Good job :)')
                else: 
                    messages.warning(request, 'Oops! Nice try, but not quite')
        else:
            messages.success(request, "Awesome work! You got all the questions right!")

        context = {'code': code, 'ans': ans, 'allAns': allAns, 'corAns': corAns}
        return render(request, 'reveal/index.html', context)
    else:
        return render(request, 'reveal/notready.html', {})
