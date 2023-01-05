

from .pagination import CustomPageNumberPagination
from django.shortcuts import render

# my imports
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

# rest framework imports
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


#AUTH
#from rest_framework.permissions import IsAuthenticated #kullanıcı LOGİN ise işlem yetkisi tanıyoruz.

from rest_framework.permissions import IsAdminUser #Sadece  Admin ise İşlem yetkisi tanıyoruz.

from rest_framework.permissions import IsAuthenticatedOrReadOnly #Kullanıcı login ise CRUD yapsın değilse sadece GET yapsın anlamındadır.


#!#################### FUNCTION BASED VIEWS ########################################

@api_view()  # default GET
def home(requst):
    return Response({'home': 'This is home page...'})



#concrete Methodu ile Endpoint Oluşturma

class StudentMVS(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # permission_classes = [IsAuthenticated] # kullanıcıya yetki vermiş oluyoruz. Login ise işlem yapabilir.

    permission_classes = [IsAdminUser] #tüm işlemleri yapmaya sadece Admin olanlar yetkilendirilir.

    #permission_classes = [IsAuthenticatedOrReadOnly] #kullanıcı login ise crud işlemlerini yapsın değilse sadece GET işlemi yapabilir.


    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

    # toplam öğrenci sayısını verir.
    @action(detail=False, methods=["GET"])
    def student_count(self, request):
        count = {
            "student-count": self.queryset.count()
        }
        return Response(count)


class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer

 
