# for i in range(5):
#     f = open(f'file_{i}.txt', 'w+')
#     f.write(f'{i} File')
#     f.close()
import os
# import zipfile
#
# compressed_file = zipfile.ZipFile('zipped2.zip', 'w', zipfile.ZIP_DEFLATED)
# for i in range(5):
#     compressed_file.write(f'file_{i}.txt')
# compressed_file.close()
#
# zip_object = zipfile.ZipFile('zipped2.zip', 'r')
# zip_object.extractall('extracted')

import zipfile
import shutil

shutil.make_archive('zipped_1', 'zip', 'extracted')
shutil.unpack_archive('zipped_1.zip', 'final_unzip', 'zip')