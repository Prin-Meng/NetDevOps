from django.contrib import admin

from file_mgmt.models import FileDir
from file_mgmt.models import UploadFile
from file_mgmt.models import OwnerName
from file_mgmt.models import HashHex


admin.site.register(FileDir)
admin.site.register(UploadFile)
admin.site.register(OwnerName)
admin.site.register(HashHex)

