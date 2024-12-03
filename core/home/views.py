from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUser(APIView):

    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':400,'errors':serializer.errors})
        serializer.save()
        user = User.objects.get(username = serializer.data["username"])
        refresh = RefreshToken.for_user(user)
        return Response({'status':200,'refresh': str(refresh),
        'access': str(refresh.access_token),'payload':serializer.data,'message':'you send data'})


# Create your views here.
@api_view(['GET'])
def get_books(request):
    books_obj = Book.objects.all()
    serializer = BookSerializer(books_obj,many=True)
    return Response({"status":200,"payload":serializer.data})


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs,many=True)
        return Response({'status':200,'paylod': serializer.data})
    
    def post(self,request):
        data = request.data
        serializer = StudentSerializer(data = request.data)
        print(data)
        if not serializer.is_valid():
            return Response({'status':400,'errors':serializer.errors})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'you send data'})
    
    def patch(self,request,pk):
        try:
            student_obj = Student.objects.get(pk = pk)
            serializer = StudentSerializer(student_obj,data = request.data,partial=True)
            if not serializer.is_valid():
                return Response({'status':400,'errors':serializer.errors})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'you send data'})
        except Exception as e:
            return Response({'status':400,'message':'Invalid id'})
        
    def delete(self,request,pk):
        try:
            student_obj = Student.objects.get(pk = pk)
            student_obj.delete()
            return Response({'status':200,'message':'Deleted successfully'})
        except Exception as e:
            return Response({'status':400,'message':'Invalid id'})




# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs,many=True)
#     return Response({'status':200,'paylod': serializer.data})

# @api_view(['POST'])
# def student_post(request):
#     data = request.data
#     serializer = StudentSerializer(data = request.data)
#     print(data)
#     if not serializer.is_valid():
#         return Response({'status':400,'errors':serializer.errors})
#     serializer.save()
#     return Response({'status':200,'payload':serializer.data,'message':'you send data'})

# @api_view(['PUT'])
# def update_student(request,id):
#     try:
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializer(student_obj,data = request.data)
#         if not serializer.is_valid():
#             return Response({'status':400,'errors':serializer.errors})
#         serializer.save()
#         return Response({'status':200,'payload':serializer.data,'message':'you send data'})
#     except Exception as e:
#         return Response({'status':400,'message':'Invalid id'})
    

# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
#         student_obj = Student.objects.get(id = id)
#         student_obj.delete()
#         return Response({'status':200,'message':'Deleted successfully'})
#     except Exception as e:
#         return Response({'status':400,'message':'Invalid id'})