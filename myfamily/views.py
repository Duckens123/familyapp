from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member
from .serializer import MemberSerializer

# Create your views here.
@api_view(['GET'])
def getMember(request):
    member=Member.objects.all()
    serializer=MemberSerializer(member,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def postMember(request):
    serializer=MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
