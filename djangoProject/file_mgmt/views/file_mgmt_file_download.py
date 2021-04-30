from file_mgmt.models import UploadFile, OwnerName
from django.http import StreamingHttpResponse
from django.utils.http import urlquote
from file_mgmt.views.file_mgmt_file_show import show_files
from django.contrib.auth.decorators import login_required


@login_required()
def download_file(request, file_id):
    try:
        # 搜索请求用户名下的文件
        uploadfile = UploadFile.objects.get(id=file_id, file_owner_name=OwnerName.objects.get(name=request.user.get_username()))
        # 从文件系统读取文件
        uploadfile_bitfile = open(uploadfile.hash_hex.full_path(), 'rb')
        # 构建响应信息
        response = StreamingHttpResponse(uploadfile_bitfile)
        # 填写内容类型
        response['Content-Type'] = 'application/octet-stream'
        # 使用urlquote解决中文文件名问题, 是否火狐依然有问题
        response['Content-Disposition'] = 'attachment; filename={0}'.format(urlquote(uploadfile.file_raw_name))
        return response
    except UploadFile.DoesNotExist:
        return show_files(request, errormessage="文件未找到!或者无权删除!")