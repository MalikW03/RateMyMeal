# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Review, User
from .forms import UserForm, MyUserCreationForm


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password is incorrect')

    return render(request, 'base/login_register.html', {'page': 'login'})


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Registration error')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') or ''
    reviews = Review.objects.filter(item_name__icontains=q)
    recent_reviews = Review.objects.all().order_by('-created')[:5]
    return render(request, 'base/home.html', {
        'reviews': reviews,
        'recent_reviews': recent_reviews
    })


@login_required(login_url='login')
def createReview(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        rating = request.POST.get('rating')
        description = request.POST.get('description')

        Review.objects.create(
            user=request.user,
            item_name=item_name,
            rating=rating,
            description=description,
        )
        return redirect('home')

    return render(request, 'base/review_form.html')


def reviewDetail(request, pk):
    review = get_object_or_404(Review, id=pk)
    return render(request, 'base/review_detail.html', {'review': review})


def userProfile(request, pk):
    user = get_object_or_404(User, id=pk)
    reviews = Review.objects.filter(user=user)
    return render(request, 'base/profile.html', {'user': user, 'reviews': reviews})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})


@login_required(login_url='login')
def updateReview(request, pk):
    review = get_object_or_404(Review, id=pk, user=request.user)

    if request.method == 'POST':
        review.item_name = request.POST.get('item_name')
        review.rating = request.POST.get('rating')
        review.description = request.POST.get('description')
        review.save()
        return redirect('review-detail', pk=review.id)

    return render(request, 'base/review_form.html', {'review': review})


@login_required(login_url='login')
def deleteReview(request, pk):
    review = get_object_or_404(Review, id=pk, user=request.user)

    if request.method == 'POST':
        review.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': review})
