
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView


from rest_framework.authtoken.models import Token



class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    #kullanıcı register olduğunda siteye hemen girişinin yapılması için gerekli  create methodu overread ettik. Buna token'ı eklemiş olduk
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token = Token.objects.create(user_id=response.data['id'])
        response.data['token'] = token.key
        # print(response.data)
        return response

# ----------- Kullanıcı Çıkış yaptığında token silme işlemi  ------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Kullanıcı Çıkış (Token Sil)
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})