
from rest_framework import routers

from users.api import RegisterView, VerifyEmail

router = routers.DefaultRouter()
router.register(r'register', RegisterView, 'register'),
router.register(r'verify', VerifyEmail, 'verify')

