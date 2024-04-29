#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Countries
from .serializers import CountriesSerializer
from django.http import Http404
import pdb
import sys

class CountriesViewSet(viewsets.ModelViewSet):
  queryset = Countries.objects.all()
  serializer_class = CountriesSerializer

  #all get paths
  def get_queryset(self):
    if self.action == 'list':
      countries = Countries.objects.all()

      # Intercept incoming query parameters
      alpha2 = self.request.query_params.get('alpha2', None)
      if alpha2 is not None:
        countries = countries.filter(alpha2=alpha2)  
      
      alpha3 = self.request.query_params.get('alpha3', None)
      if alpha3 is not None:
        countries = countries.filter(alpha3=alpha3)
      
      include_deleted = self.request.query_params.get('include_deleted', None)
      if include_deleted is None or include_deleted != '1':
        countries = countries.filter(is_deleted=False)

      return countries

    # If the action is not 'list', return an empty queryset
    return Countries.objects.none()

  def get_object(self, deleted_state=False):
    pk = self.kwargs.get('pk')  # Get the primary key from the URL parameters
    obj = Countries.objects.filter(pk=pk).first()  # Manually fetch the object from the database
    
    # If the country is deleted, raise a Http404 error
    if obj is None:
      raise Http404("No Countries matches the given query.")
    elif deleted_state: #i want to delete
      if obj.is_deleted:
        raise Http404("No Countries matches the given query.")
      
    elif not deleted_state: #want to un-delete (get)
      if not obj.is_deleted:
        raise Http404("No Countries matches the given query.")

    return obj  # Return the country

  # Un-delete Country (Update)
  @action(detail=True, methods=['put'], url_path='undelete')
  def undelete(self, request, pk=None):
    country = self.get_object(False)
    country.is_deleted = False
    country.save()

    return Response({'status': 'Country un-deleted'}, status=status.HTTP_200_OK)

  # Soft Delete Country (Update)
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object(True)
    instance.is_deleted = True
    instance.save()

    return Response({"status":"Country deleted."},status=status.HTTP_204_NO_CONTENT)
