from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatMessage, UserSession
from .serializers import ChatMessageSerializer
from .llm import generate_response

class ChatView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        session_id = request.data.get('session_id')
        session, _ = UserSession.objects.get_or_create(session_id=session_id)
        response_text = generate_response(prompt, session_id=session_id)

        ChatMessage.objects.create(session=session, is_user=True, text=prompt)
        message = ChatMessage.objects.create(session=session, is_user=False, text=response_text)

        serializer = ChatMessageSerializer(message)
        return Response({'response': response_text, 'message': serializer.data})
