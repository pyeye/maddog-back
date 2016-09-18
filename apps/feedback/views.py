from rest_framework.generics import CreateAPIView

from .serializers import FeedbackSerializer


class FeedbackAPIView(CreateAPIView):
    serializer_class = FeedbackSerializer
