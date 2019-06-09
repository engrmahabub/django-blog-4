from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from blog.models import Post


class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        post_qs = Post.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated:
            is_liked = Post.objects.like_toggle(request.user, post_qs.first())
            return Response({'liked': is_liked})
        return Response({"message": message}, status=400)
