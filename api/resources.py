from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.contrib.auth.models import User


class AllUsers(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        authorization = Authorization()
