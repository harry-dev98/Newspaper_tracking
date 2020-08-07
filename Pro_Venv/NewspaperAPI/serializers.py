from rest_framework import serializers
from .models import Newspaper, Intake, User,Consumer#,Order#,Daily_Cart,Regi
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ('id','newspaper','language','wh_price','sa_price','description','company','publication')

class ConsumerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumer
        fields = ('id', 'name', 'address', 'telephone', 'email', 'ac_no')

class IntakeSerializer(serializers.ModelSerializer):
    newspaper = serializers.StringRelatedField(many=True)
    class Meta:
        model = Intake
        fields = ('id','added_date','newspaper','qty','qty_return','total')

