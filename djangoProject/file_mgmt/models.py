from django.db import models
import os


# Create your models here.
class FileDir(models.Model):
    file_dir = models.CharField(max_length=999, verbose_name='文件目录')

    def __str__(self):
        return f"{self.__class__.__name__}(文件目录:{self.file_dir})"


class HashHex(models.Model):
    hash_hex = models.CharField(max_length=999, verbose_name='hash hex字符串')
    create_datetime = models.DateTimeField(null=True, auto_now_add=True, verbose_name='创建时间')

    def full_path(self):
        return FileDir.objects.get(id=1).file_dir + self.hash_hex

    def related_upload_files(self):
        try:
            return len(self.upload_files.all())
        except Exception:
            return

    def remove_file(self):
        os.remove(self.full_path())

    def __str__(self):
        return f"{self.__class__.__name__}(Hash值:{self.hash_hex})"


class OwnerName(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, verbose_name='拥有者用户名')

    def __str__(self):
        return f"{self.__class__.__name__}(拥有者用户名:{self.name})"


class UploadFile(models.Model):
    # 文件原始名称
    file_raw_name = models.CharField(max_length=999, verbose_name='文件原始名称')
    # 关联拥有人名称数据库
    file_owner_name = models.ForeignKey(OwnerName,
                                        related_name='files_name',
                                        on_delete=models.CASCADE,
                                        verbose_name='拥有者用户名')
    # hash hex字符串
    hash_hex = models.ForeignKey(HashHex,
                                 related_name='upload_files',
                                 on_delete=models.CASCADE,
                                 verbose_name='hash hex字符串')
    # 上传时间
    upload_datetime = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return f"{self.__class__.__name__}(拥有者:{self.file_owner_name.name}" \
               f"| 原始名称:{self.file_raw_name}" \
               f"| HASH值:{self.hash_hex.hash_hex})"
