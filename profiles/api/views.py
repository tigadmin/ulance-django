from rest_framework import generics, permissions, mixins
from rest_framework.parsers import FileUploadParser
from .serializers import ( ProfileSerializer, SkillSerializer, LinkSerializer, PortfolioSerializer, LevelSerializer, CertificationSerializer, ProfilePictureSerializer, EducationSerializer, MajorSerializer )
from profiles.models import ProfileModel, SkillModel, LinkModel, PortfolioModel, LevelModel, CertificationModel, EducationModel, MajorModel
from ulance import pagination
from ulance.custom_permissions import MyUserPermissions
from django.contrib.auth import get_user_model
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MajorFilter, SkillFilter

User = get_user_model()

#PROFILES
class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'

class ProfileDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    parser_classes = (FileUploadParser,)
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'
    permission_classes = [MyUserPermissions]
  #  parser_classes = [FileUploadParser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class ProfilePictureDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfilePictureSerializer
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

#SKILLS
class SkillListAPIView(generics.ListAPIView):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all().order_by('name')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SkillFilter
    pagination_class = pagination.StandardResultsPagination

class SkillCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all()
    permission_classes = [permissions.IsAdminUser]

class SkillDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

#LINKS
# class LinkListAPIView(generics.ListAPIView):
#     serializer_class = LinkSerializer
#     queryset = LinkModel.objects.all()

class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer
    queryset = LinkModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)

class LinkDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = LinkSerializer
    queryset = LinkModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class UserLinkListAPIView(generics.ListAPIView):
    serializer_class = LinkSerializer
    model = LinkModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = LinkModel.objects.filter(user=user)
        return qs
#PORTFOLIOS

class PortfolioCreateAPIView(generics.CreateAPIView):
    serializer_class = PortfolioSerializer
    queryset = PortfolioModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)

class PortfolioDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = PortfolioSerializer
    queryset = PortfolioModel.objects.all()
    lookup_field = 'user__username'
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

#LEVELS

class LevelCreateAPIView(generics.CreateAPIView):
    serializer_class = LevelSerializer
    queryset = LevelModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        skill_name = serializer.validated_data['skill']
        skill = SkillModel.objects.get(name__iexact=skill_name)
        serializer.save(user=self.request.user, skill=skill)


class LevelDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = LevelSerializer
    queryset = LevelModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class UserLevelListAPIView(generics.ListAPIView):
    serializer_class = LevelSerializer
    model = LevelModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = LevelModel.objects.filter(user=user)
        return qs

# CERTIFICATIONS

class CertificationCreateAPIView(generics.CreateAPIView):
    serializer_class = CertificationSerializer
    queryset = CertificationModel.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)

class CertificationDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = CertificationSerializer
    queryset = CertificationModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class UserCertificationListAPIView(generics.ListAPIView):
    serializer_class = CertificationSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = CertificationModel.objects.filter(user=user)
        return qs

# EDUCATION

class EducationCreateAPIView(generics.CreateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)

class MajorCreateAPIView(generics.CreateAPIView):
    queryset = MajorModel.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [permissions.IsAdminUser]


class MajorListAPIView(generics.ListAPIView):
    queryset = MajorModel.objects.all().order_by('major_name')
    serializer_class = MajorSerializer
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MajorFilter
    #     filter_backends = (filters.SearchFilter,)
    # search_fields = ('major_name',)

    # def get_queryset(self, *args, **kwargs):
    #     qs = MajorModel.objects.all().order_by('major_name')
    #     query = self.request.GET.get("major", None)
    #     if query is not None:
    #         qs = qs.filter(
    #             Q(major_name__icontains=query)
    #         )
    #     return qs


class UserEducationLisAPIView(generics.ListAPIView):
    serializer_class = EducationSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = EducationModel.objects.filter(user=user)
        return qs

class EducationDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = CertificationSerializer
    queryset = EducationModel.objects.all()

    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)






