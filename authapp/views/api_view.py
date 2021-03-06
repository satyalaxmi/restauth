from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from authapp.models.profile import Profile
from authapp.serializers.profile_serializer import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import logout


class ProfileView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_object_by_id(pk):
    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        profile = None
    return profile


class ProfileDetails(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        profile = get_object_by_id(pk)
        if profile is None:
            return Response(
                {"msg": "Record is not availabe try again"},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        profile = get_object_by_id(pk)
        if profile:
            data = ProfileSerializer(profile, data=request.data)
            if data.is_valid():
                data.save()
                return Response(data.data, status=status.HTTP_200_OK)
            else:
                return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
                {"msg": "record is not availabel to update"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, pk):
        profile = self.get_objects_by_id(pk)
        if profile is None:
            return Response(
                {"msg": "record is not availabe to delete"},
                status=status.HTTP_404_NOT_FOUND,
            )
        profile.delete()
        return Response(
            {"msg": "record deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class LogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        
        logout(request)
        return Response({"msg": "logout successfully"}, status=status.HTTP_200_OK)
