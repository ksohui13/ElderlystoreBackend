from rest_framework import serializers

from review.models import ProdcutReview

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdcutReview
        fields = '__all__'