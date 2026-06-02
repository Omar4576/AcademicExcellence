from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from .forms import OrderForm

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    total = orders.count()
    pending = orders.filter(status='pending').count()
    in_progress = orders.filter(status='in_progress').count()
    completed = orders.filter(status='completed').count()
    delivered = orders.filter(status='delivered').count()
    context = {
        'orders': orders[:5],
        'total': total,
        'pending': pending,
        'in_progress': in_progress,
        'completed': completed,
        'delivered': delivered,
    }
    return render(request, 'orders/dashboard.html', context)

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_new(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, 'Sifarişiniz qəbul edildi!')
            return redirect('/dashboard/')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    steps = [
        ('pending', 'Gözləyir'),
        ('in_progress', 'İcradadır'),
        ('completed', 'Tamamlandı'),
        ('delivered', 'Çatdırıldı'),
    ]
    status_list = [s[0] for s in steps]
    step_index = status_list.index(order.status) + 1
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'steps': steps,
        'step_index': step_index,
    })