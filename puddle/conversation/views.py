from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
# Create your views here.

from item.models import Item
from .models import Conversation
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])