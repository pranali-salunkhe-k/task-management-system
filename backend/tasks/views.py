from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])

def get_tasks(request):

    tasks = Task.objects.filter(created_by=request.user)

    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])

def create_task(request):

    data = request.data

    task = Task.objects.create(

        title=data['title'],
        description=data['description'],
        created_by=request.user

    )

    serializer = TaskSerializer(task)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    task.delete()

    return Response({

        'message':'Task deleted'

    })