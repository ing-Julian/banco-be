from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#from authApp.serializers.userSerializer import UserSerializer 
from authApp.serializers import UserSerializer 

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs): 
        #print(request.data)
        serializer = UserSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        serializer.save()

        tokenData = {"username":request.data["username"], 
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData) 
        tokenSerializer.is_valid(raise_exception=True)
 
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
      #  return Response('Creado', status=status.HTTP_200_OK)