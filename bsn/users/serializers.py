from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username',]


class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=True, validators=[validate_password])
    password2 = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data.get('username'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

"""
{
"username":"user1",
"password":"user1",
"password2":"user1"
}
"""