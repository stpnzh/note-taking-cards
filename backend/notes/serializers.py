from rest_framework import serializers
from notes.models import Note, Tag


class TagSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tag
    fields = ('__all__')


class NoteSerializer(serializers.ModelSerializer):
  tag = TagSerializer(read_only=True)

  class Meta:
    model = Note
    fields = ('__all__')
