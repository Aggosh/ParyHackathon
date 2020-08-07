from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Profile, Review
from .forms import ReviewForm


def profile(request, nickname):
    user = get_object_or_404(Profile, nickname=nickname)
    review = Review.objects.filter(profile=user.id)
    context = {"profile": user, "reviews": review}

    # Это плохой код, но другого у меня нет
    if request.user.is_authenticated:
        if request.method == 'POST':
            review_form = ReviewForm(data=request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)

                new_review.profile = user
                new_review.author = Profile.objects.get(pk=user.id)

                new_review.save()
                context.update({"new_review": True})
        else:
            review_form = ReviewForm()
            context.update({"review_form": review_form})

    return render(request, "profile.html", context=context)
