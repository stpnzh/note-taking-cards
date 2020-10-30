# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from notes.models import Note, Tag
from notes.serializers import NoteSerializer, TagSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def note_list(req):
  if req.method == 'GET':
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
  
  elif req.method == 'POST':
    serializer = NoteSerializer(data = req.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)