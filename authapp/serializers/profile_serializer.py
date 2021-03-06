from rest_framework import serializers
from authapp.models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    skills = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = "__all__"
