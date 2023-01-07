from django.utils import timezone
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializer import RegisterSerializer, UserSerializer

RESEND_EMAIL_MINUTES = 5


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        refresh = RefreshToken.for_user(serializer.instance)
        response = serializer.data
        response['refresh'] = str(refresh)
        response['access'] = str(refresh.access_token)

        return Response(response, status=status.HTTP_201_CREATED)


class ConfirmEmailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request):
        """
           Sends a new confirmation email to the user, if the user is not already confirmed.
        """
        user = request.user
        if user.status.is_confirmed:
            return Response({'detail': 'This user is already confirmed.', 'success': True},
                            status=status.HTTP_200_OK)

        if user.status.last_sent_time and timezone.now() < user.status.token_key_expires:
            time_difference_from_last_sent_time = timezone.now() - user.status.last_sent_time
            time_gap = timezone.timedelta(minutes=RESEND_EMAIL_MINUTES)
            if time_difference_from_last_sent_time < time_gap:
                time_left_in_minutes = (time_gap - time_difference_from_last_sent_time).seconds // 60
                return Response({'detail': f'You can send a new confirmation email in {time_left_in_minutes} minutes.',
                                 'time_left_in_minutes': time_left_in_minutes,
                                 'success': True}, status=status.HTTP_200_OK)

        user.status.set_token()
        token = user.status.token_key

        user.email_user(
            'Confirm your email',
            f'Please click on the link to confirm your email: https://shazam.blog/confirm/{token}',
            'no-reply@shazam.blog',
        )

        success, message = user.status.set_confirm_sent()
        if success:
            return Response({'detail': message, 'success': success}, status=status.HTTP_200_OK)
        return Response({"error": message, "success": success}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: Request):
        confirmation_token = request.data['confirmationToken']
        user = request.user

        if user.status.is_confirmed:
            return Response({'detail': 'This user is already confirmed.', 'success': True},
                            status=status.HTTP_200_OK)

        if not user.status.token_key_expires:
            return Response({'detail': 'This user has no token.', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        if timezone.now() > user.status.token_key_expires:
            print("user.status.token_key_expires", user.status.token_key_expires)
            print("timezone.now()", timezone.now())
            return Response({'detail': 'This token has expired.', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        if user.status.token_key != confirmation_token:
            return Response({'detail': 'This token is invalid.', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        success, message = user.status.set_confirmed(confirmation_token)
        if success:
            return Response({'detail': message, 'success': success}, status=status.HTTP_200_OK)
        return Response({"error": 'Not able to set user status to confirmed.', 'success': False},
                        status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
