from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import UserHealPoint


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserHealPoint
        fields = ['id', 'phone_number']
        
class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    Handles user creation with hashed password using validated data.
    """
    password = serializers.CharField(write_only = True)

    class Meta:
        model = UserHealPoint
        fields = ["id","phone_number", "password"]
        read_only_fields = ["id"]
        
    def create(self, validated_data):
        """
        Create a new user instance with the provided validated data.
        The password is hashed before saving the user instance.
        """
        password = validated_data.pop("password")
        user = UserHealPoint(**validated_data)
        user.set_password(password)
        user.save()
        return user    

class LoginSerializer(serializers.Serializer):
    
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        
        user = authenticate(username=data["phone_number"], password=data["password"])
        
        if user and user.is_active:
            return user
        
        raise serializers.ValidationError("Invalid Credentials")
