from upyun.upyun import UpYun

# # huiwing
# http://huiwing.test.upcdn.net/test/BeetAnGeSample.mxl
# # 需要填写自己的服务名，操作员名，密码
# service = ""
# username = ""
# password = ""
#
# # 需要填写上传文件的本地路径和云存储路径，目录
# local_file = "BeetAnGeSample.mxl"
# remote_file = "/test/BeetAnGeSample.mxl"
# remote_dir = "test"

# local-dev
# https://upyun.dev.moicen.com/music-room/trans_test_mxl.mxl
# 需要填写自己的服务名，操作员名，密码
service = ""
username = ""
password = ""

# 需要填写上传文件的本地路径和云存储路径，目录
local_file = "trans_test_mxl.mxl"
remote_file = "/music-room/trans_test_mxl.mxl"
remote_dir = "test"

up = UpYun(service, username=username, password=password, debug=True)

# Get remote file info
remote_file_info = up.getinfo(remote_file)
print(f"Remote file info : {remote_file_info}")

# Download file
with open(local_file, 'wb') as f:
    up.get(remote_file, f)

# Upload file
with open(local_file, "rb") as f:
    # headers 可选，见rest上传参数
    headers = None
    up.put(remote_file, f)