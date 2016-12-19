from todos.models import ToDo
from rest_framework import serializers

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = (
                'time_created',
                'time_finished',
                'last_modified',
                'text',
                'finished',
            )
