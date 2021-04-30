from file_mgmt.views.file_mgmt_file_show import show_files
from file_mgmt.models import UploadFile,OwnerName
import os
from django.contrib.auth.decorators import login_required


@login_required()
def delete_file(request, file_id):
    try:
        # 获取对应ID的文件
        m = UploadFile.objects.get(id=file_id, file_owner_name=OwnerName.objects.get(name=request.user.get_username()))
        # 获取关联的hashhex对象
        m_hash = m.hash_hex
        # 从数据库中删除设备条目
        m.delete()

        # 如果确实没有任何文件关联到这个hashhex, 就可以删除了
        if not m_hash.related_upload_files():
            os.remove(m_hash.full_path())
            m_hash.delete()

        return show_files(request, successmessage="文件删除成功")
    except UploadFile.DoesNotExist:
        return show_files(request, errormessage="文件未找到!或者已经被删除!")