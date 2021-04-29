from django.shortcuts import render
from file_mgmt.models import FileDir, UploadFile, HashHex, OwnerName
import hashlib
import os

file_os_path = FileDir.objects.get(id=1).file_dir


def upload_files(request):
    if request.method == 'POST':  # 如果请求method为POST, 上传文件都是用POST
        messages = []  # 由于并不是所有的文件都能成功上传, 所以这里做了一个给客户回显每一个文件上传状态信息的清单messages
        files_list = request.FILES.getlist('files[]')  # 得到多个文件的清单
        for file in files_list:
            # file.name 文件名
            # file.content_type 文件类型
            # file.size 文件大小(可以考虑对文件大小进行限制)
            ext_name = os.path.splitext(file.name)[1]
            if ext_name != '.docx' and ext_name != '.doc':
                # 把此文件的错误信息, 放入messages清单, 并使用continue跳过此文件
                messages.append(file.name + ":文件格式并不是doc或者docx!")
                continue

            # 读取二进制数据
            bit_file = file.file.read()
            # 产生HASH,用HASH作为写入OS的文件名
            hash_hex_value = hashlib.sha3_256(bit_file).hexdigest()

            try:
                # 确认是否重复上传相同文件，相同的话直接进入下一个循环，如果没有找到对应的值，则继续后续的操作
                uploaded = UploadFile.objects.get(hash_hex__hash_hex=hash_hex_value,
                                                  file_owner_name__name=request.user.get_username())
                messages.append(f"{file.name}:文件, 与已有文件:{uploaded.file_raw_name}重复!")
                continue
            except UploadFile.DoesNotExist:
                pass

            file_raw_name = file.name
            owner_username = request.user.get_username()
            print(owner_username)
            try:
                # 如果hash值相同，但不存在相应的用户名，则不用保存新的文件，直接将相关信息写入数据库
                hash_hex_obj = HashHex.objects.get(hash_hex=hash_hex_value)
                # 向ownerName表中写入拥有者用户名
                owner = OwnerName(name=owner_username)
                owner.save()

                s = UploadFile(file_raw_name=file_raw_name,
                               owner_username=owner,
                               hash_hex=hash_hex_obj,
                               )
                s.save()
                messages.append(file.name + ":快速上传成功!")

            except Exception:
                # 如果hash值不同，也不存在相应的用户名，则在更新数据库的同时，还需要将文件写入文件系统
                # 把文件写入, 文件系统, 文件名为Hash Hex
                checked_file = open(file_os_path + hash_hex_value, 'wb')
                # 在FileDir数据库中写入文件路径
                file_path = FileDir(file_dir=file_os_path + hash_hex_value)
                file_path.save()
                # 写入文件系统
                checked_file.write(bit_file)
                checked_file.close()

                # 将hash和用户名，写入HashHex和OwnerName表中
                h = HashHex(hash_hex=hash_hex_value)
                h.save()
                owner = OwnerName(name=owner_username)
                owner.save()

                # 保存到数据库
                s = UploadFile(file_raw_name=file_raw_name,
                               owner_username=owner,
                               hash_hex=h,
                               )
                s.save()
                messages.append(file_raw_name + ":上传成功!")
        return render(request, 'file_mgmt_upload.html', {'messages': messages})

    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        return render(request, 'file_mgmt_upload.html')
