import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from Account.models import Account


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True, validators=[UniqueValidator(queryset=Account.objects.all())])

    class Meta:
        model = Account
        fields = ('username', 'password')

    def create(self, validated_data):
        validated_data['date_joined'] = datetime.datetime.today()
        validated_data['is_active'] = True
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
