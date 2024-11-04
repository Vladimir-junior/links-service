from typing import Any, Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data: Dict[str, Any]) -> User:
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")
        data['user'] = user
        return data


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['current_password', 'new_password', 'confirm_password']

    def validate_current_password(self, value: str) -> str:
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Current password is incorrect.")
        return value

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("New passwords do not match.")
        return data

    def save(self, **kwargs: Any) -> User:
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value: str) -> str:
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User not found.')
        return value
