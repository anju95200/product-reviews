from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Review

@shared_task
def send_review_notification(review_id):
    try:
        review = Review.objects.get(id=review_id)
        subject = f'New Review for {review.product.name}'
        message = f"""
        A new review has been submitted for {review.product.name}.
        
        Reviewer: {review.user.username}
        Rating: {review.rating}/5
        Comment: {review.comment}
        
        Please login to the admin panel to view details.
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
    except Review.DoesNotExist:
        pass