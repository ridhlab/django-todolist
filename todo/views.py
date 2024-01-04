from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TodoSerializer
from .models import Todo


# Create your views here.
class TodoViews(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        todos = Todo.objects.all()
        serialize = TodoSerializer(todos, many=True)
        return Response(
            {"status": "success", "data": serialize.data}, status=status.HTTP_200_OK
        )


class TodoViewsDetail(APIView):
    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        serialize = TodoSerializer(todo)
        return Response(
            {"status": "success", "data": serialize.data}, status=status.HTTP_200_OK
        )

    def patch(self, request, id):
        todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(instance=todo, data=request.data)
        print("isvalid", serializer.is_valid())
        print(serializer.errors)
        print(request.data)
        print(todo)
