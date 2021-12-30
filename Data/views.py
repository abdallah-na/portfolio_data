from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

"""
    ABOUT ME
"""

@api_view(['GET', 'POST'])
def AboutMe(request):
    """
    about me or create it.
    """
    if request.method == 'GET':
        aboutme = AboutMe.objects.all()
        serializer = AboutMeSerializer(aboutme, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AboutMeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
    PROJECT views 
"""
@api_view(['GET','POST'])
def project(request):
    """
    Retrieve all project or create a new one 
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, slug):
    """
    Retrieve, update or delete a project.
    """
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(Project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
    Work views 
"""
@api_view(['GET','POST'])
def work(request):
    """
    Retrieve all work or create a new one 
    """
    if request.method == 'GET':
        work = Work.objects.all()
        serializer = WorkSerializer(work, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
def work_detail(request, slug):
    """
    Retrieve, update or delete a work.
    """
    try:
        work = Work.objects.get(slug=slug)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorkSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WorkSerializer(Project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        work.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
    Education views 
"""
@api_view(['GET','POST'])
def Education(request):
    """
    Retrieve all education history or create a new one 
    """
    if request.method == 'GET':
        education = Education.objects.all()
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
def Education_detail(request, slug):
    """
    Retrieve, update or delete a education history.
    """
    try:
        education = Education.objects.get(slug=slug)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EducationSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EducationSerializer(Project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)