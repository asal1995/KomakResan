from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=45, required=True)
    last_name = serializers.CharField(max_length=45, required=True)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password'
        )

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VerifySerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']
