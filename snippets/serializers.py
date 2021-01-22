from .models import ScippetModel
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model= ScippetModel
		fields=['id', 'title', 'content', 'author']

	def create(self, validate_data):
		return ScippetModel.objects.create(**validate_data)

	def update(self,instance, validate_data):
		instance.title=validate_data.get('title', instance.title)
		instance.content=validate_data.get('content', instance.content)
		instance.author=validate_data.get('author', instance.author)
		instance.save()
		return instance
