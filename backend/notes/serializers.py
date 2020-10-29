from rest_framework import serializers
from notes.models import Note, Tag

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = ['id', 'category', 'description', 'code', 'pub_date']


