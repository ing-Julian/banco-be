from authApp.models.account import Account 
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Account
        fields = ['balance', 'lastChangeDate', 'isActive']

    def create(self, validated_data):
        account_data =validated_data.pop('account')
        print (account_data)
        return {}