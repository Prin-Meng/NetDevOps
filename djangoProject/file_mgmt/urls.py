from django.urls import path
from file_mgmt.views.file_mgmt_file_show import show_files
from file_mgmt.views.file_mgmt_file_delete import delete_files
from file_mgmt.views.file_mgmt_file_upload import upload_files
from file_mgmt.views.file_mgmt_file_download import download_files

urlpatterns = [
    path('upload_files', upload_files),
    path('delete_files', delete_files),
    path('show_files', show_files),
    path('download_files', download_files),
]
