from rest_framework import routers

from auth.api.views import SkillViewSet, SocialViewSet, UserViewSet

auth_router = routers.SimpleRouter()

auth_router.register("social", SocialViewSet, "social")
auth_router.register("skill", SkillViewSet, "skill")
auth_router.register("social", UserViewSet, "social")
