from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from members.management.commands.createsu import Command

User = get_user_model()

class SettingsBackend:
	def authenticate(self, request, username=None, password=None):
		login_valid = (settings.ADMIN_USERNAME == username)
		pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
		if login_valid and pwd_valid:
			try:
				user = User.objects.get(
					username=username,
				)
			except User.DoesNotExist:
				user = User(username=username)
				user.is_staff = True
				user.is_superuser = True
				user.save()
			return user
		return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoseNotExist:
			return None