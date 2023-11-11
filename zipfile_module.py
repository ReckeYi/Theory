import os
import zipfile

'''
Single File
'''
# zipped_files = zipfile.ZipFile('D:\\Projects\\temp\\test_zip\\zipped_file.zip', 'w')
# zipped_files.write('D:\\Projects\\temp\\test_zip\\files\\file.txt',
#                    compress_type=zipfile.ZIP_DEFLATED)
# zipped_files.close()
'''
#Several Files + saving catalog structure
'''
zipped_files = zipfile.ZipFile('D:\\Projects\\temp\\test_zip\\zipped_files_result.zip', 'w')

for folder, subfolders, files in os.walk('D:\\Projects\\temp\\test_zip\\files'):
    for file in files:
        if file.endswith('.txt') or file.endswith('.py'):
            zipped_files.write(os.path.join(folder, file),
                               os.path.relpath(os.path.join(folder, file), 'D:\\Projects\\temp\\test_zip\\files'),
                               compress_type = zipfile.ZIP_DEFLATED)
zipped_files.close()
'''
Several Files + without saving catalog structure
'''
# zipped_files = zipfile.ZipFile('D:\\Projects\\temp\\test_zip\\zipped_files_result_2.zip', 'w')
#
# for folder, subfolders, files in os.walk('D:\\Projects\\temp\\test_zip\\files'):
#     for file in files:
#         if file.endswith('.txt') or file.endswith('.py'):
#             zipped_files.write(os.path.join(folder, file),
#                                file,
#                                compress_type = zipfile.ZIP_DEFLATED)
# zipped_files.close()

'''
Extract ALL Files
'''

# zipped_files = zipfile.ZipFile('D:\\Projects\\temp\\test_zip\\zipped_files_result.zip')
# zipped_files.extractall('D:\\Projects\\temp\\unzipped')
# zipped_files.close()

'''
Extract Single File
'''

zipped_file = zipfile.ZipFile('D:\\Projects\\temp\\test_zip\\zipped_files_result_2.zip')
zipped_file.extract('file.txt', 'D:\\Projects\\temp\\unzipped\\single_file')
zipped_file.close()