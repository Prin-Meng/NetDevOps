from django.shortcuts import render
from file_mgmt.models import UploadFile, OwnerName


def show_files(request, successmessage=None, errormessage=None):
    # 查询整个数据库的信息 object.all()
    result = UploadFile.objects.filter(file_owner_name=OwnerName.objects.get(name=request.user.get_username()))
    # 最终得到设备清单devices_list,清单内部是每一个设备信息的字典
    files_list = []
    for x in result:
        # 产生学员信息的字典
        file_dict = {
            'file_raw_name': x.file_raw_name,
            'upload_datetime': x.upload_datetime,
            'delete_url': "/file_mgmt/delete_file/" + str(x.id),
            'download_url': "/file_mgmt/download_file/" + str(x.id),
        }

        # 提取学员详细信息,并写入字典
        files_list.append(file_dict)
    return render(request, 'file_mgmt_show.html', {'files_list': files_list,
                                                   'successmessage': successmessage,
                                                   'errormessage': errormessage,
                                                   })
