import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from file_mgmt.models import FileDir, HashHex, OwnerName, UploadFile



# 删除现有的数据
FileDir.objects.all().delete()
HashHex.objects.all().delete()
OwnerName.objects.all().delete()
UploadFile.objects.all().delete()
