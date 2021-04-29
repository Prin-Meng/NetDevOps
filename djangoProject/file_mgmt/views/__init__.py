import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()
from file_mgmt.models import FileDir

file_os_path = FileDir.objects.get(id=1).file_dir

print(file_os_path)