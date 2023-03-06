from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Track
from .serializers import TrackSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_tracks': '/',
        'Search by Id': '/?id=id_name',
        'Search by Activity': '/?activity=activity_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/track/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_tracks(request):
    track = TrackSerializer(data=request.data)

    # validating for already existing data
    if Track.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if track.is_valid():
        track.save()
        return Response(track.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_tracks(request):

    # checking for the parameters from the URL
    if request.query_params:
        tracks = Track.objects.filter(**request.query_params.dict())
    else:
        tracks = Track.objects.all()

    # if there is something in tracks else raise error
    if tracks:
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_tracks(request, pk):
    track = Track.objects.get(pk=pk)
    data = TrackSerializer(instance=track, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_tracks(request, pk):
    track = get_object_or_404(Track, pk=pk)
    track.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
