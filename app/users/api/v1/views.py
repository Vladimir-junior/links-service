from django.db import connection
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from users.api.v1.serializers import (
    SignUpSerializer,
    PasswordResetSerializer,
    SignInSerializer,
    ChangePasswordSerializer,
    UserSerializer
)
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return self.queryset.none()
        return self.queryset.filter(id=self.request.user.id)

    @action(
        detail=False,
        methods=['post'],
        url_path='sign-up'
    )
    def sig_nup(self, request: Request) -> Response:
        serializer = SignUpSerializer(data=request.data)
        result = {"status": "ok"}
        response_status = status.HTTP_201_CREATED

        if serializer.is_valid():
            serializer.save()
        else:
            result = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(result, status=response_status)

    @action(
        detail=False,
        methods=['post'],
        url_path='sign-in'
    )
    def sign_in(self, request: Request) -> Response:
        serializer = SignInSerializer(data=request.data)
        response_status = status.HTTP_200_OK

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            result = {'token': token.key}
        else:
            result = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(result, status=response_status)

    @action(
        detail=False,
        methods=['post'],
        url_path='sign-out',
        permission_classes=[IsAuthenticated]
    )
    def sign_out(self, request: Request) -> Response:
        request.user.auth_token.delete()
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['post'],
        url_path='change-password',
        permission_classes=[IsAuthenticated]
    )
    def change_password(self, request: Request) -> Response:
        serializer = (ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        ))
        result = {"status": "ok"}
        response_status = status.HTTP_201_CREATED
        if serializer.is_valid():
            serializer.save()
        else:
            result = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(result, status=response_status)

    @action(
        detail=False,
        methods=['post'],
        url_path='reset-password'
    )
    def reset_password(self, request: Request) -> Response:
        serializer = PasswordResetSerializer(data=request.data)
        response_status = status.HTTP_201_CREATED
        if serializer.is_valid():
            result = {"message": f"Message sent to this email {serializer.validated_data['email']}"}
        else:
            result = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(result, status=response_status)


class TopUsersView(APIView):
    def get(self, request):
        query = """
            SELECT 
                u.id, 
                u.email, 
                COUNT(l.id) AS link_count
            FROM 
                users_user AS u
            LEFT JOIN 
                links_link AS l ON u.id = l.owner_id
            GROUP BY 
                u.id
            ORDER BY 
                link_count DESC, 
                u.date_joined ASC
            LIMIT 10;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        users_data = [
            {"id": row[0], "email": row[1], "link_count": row[2]} for row in rows
        ]
        return Response(users_data)
