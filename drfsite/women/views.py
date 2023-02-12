# createAPIView - создание данных по POST-запросу
# ListAPIView - чтение списка данных по GET-запросу
# RetrieveAIView - чтение конкретных данных(записи) по GET-запросу
# DestroyAIView - удаление данных(записи) по DELETE-запросу
# UpdateAIView - изменение записи по PUT- или PATCH-запросу
# ListCreateAIView - для чтения (по GET-запросу) и создания списка данных(по POST-запросу)
# RetrieveUpdateAIView - чтение и изменение отдельноц записи(GET- POST-запрос)
# RetrieveDestroyAIView - чтение(GET-запрос) и удаление(DELETE-запрос) отдельной записи
# RetrieveUpdateDestroyAIView - чтение, изменение и добавление отдельной записи(GET-, PUT-, PATCH- и DELETE-запросы)



from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.views import APIView


class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    #queryset = Women.objects.all()  #если мы переопределили get_queryset, то эту строку можно убрать, но добавить в urls.py поле basename='women'
    serializer_class = WomenSerializer

    #Если мы хотим вернуть не все записи, а только первые 3(например), тогда надо переопределить метод get_queryset(self):
    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True) #detail = False (Выводится список) || detail=True (Выводится конкретная запись)
    def category(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

    # @action(methods=['get'], detail=False) #detail = False (Выводится список) || detail=True (Выводится конкретная запись)
    # def category(self, request):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})

# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#-----------------------------------------------------------------------
#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#----------------------------------------------------------------------------

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         #Код для удаления записи с переданным pk
#         try:
#             record = Women.objects.filter(pk=pk)
#             record.delete()
#         except:
#             return Response({"error": "Objects does not delete"})
#
#         return Response({"post": "delete post" + str(pk)})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

