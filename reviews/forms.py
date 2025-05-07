from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={
                    'class': 'block w-full pl-3 pr-10 py-2 border-2 border-gray-500 !important rounded-lg shadow-sm focus:ring-2 focus:ring-blue-600 focus:border-blue-600 sm:text-sm bg-white text-gray-900 appearance-none',
                    'style': 'background-image: url(\"data:image/svg+xml;utf8,<svg fill=\'gray\' height=\'24\' viewBox=\'0 0 24 24\' width=\'24\' xmlns=\'http://www.w3.org/2000/svg\'><path d=\'M7 10l5 5 5-5z\'/><path d=\'M0 0h24v24H0z\' fill=\'none\'/></svg>\"); background-repeat: no-repeat; background-position: right 0.75rem center;'
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'rows': 5,
                    'class': 'block w-full p-3 border-2 border-gray-500 !important rounded-lg shadow-sm focus:ring-2 focus:ring-blue-600 focus:border-blue-600 sm:text-sm min-h-[120px]',
                    'placeholder': 'Share your thoughts about the product...'
                }
            ),
        }