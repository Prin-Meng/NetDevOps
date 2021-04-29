from django.urls import path
from file_mgmt.views.file_mgmt_file_show import show_files
from file_mgmt.views.file_mgmt_file_delete import delete_file
from file_mgmt.views.file_mgmt_file_upload import upload_files
from file_mgmt.views.file_mgmt_file_download import download_file

urlpatterns = [
    path('upload_files', upload_files),
    path('delete_file/<int:file_id>', delete_file),
    path('show_files', show_files),
    path('download_file/<int:file_id>', download_file),
]
