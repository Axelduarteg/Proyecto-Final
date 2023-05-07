from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message
from .forms import SendMessageForm

User = get_user_model()

@login_required
def chatroom(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            receiver_id = form.cleaned_data['receiver_id']
            message = form.cleaned_data['message']
            receiver = User.objects.get(id=receiver_id)
            Message.objects.create(sender=request.user, receiver=receiver, message=message)
            return redirect('chatroom')
    else:
        form = SendMessageForm()
    return render(request, 'chat_room.html', {'users': users, 'form': form})

