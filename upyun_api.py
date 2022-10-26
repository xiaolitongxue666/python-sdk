# Imports
from upyun import UpYun, ED_AUTO, UpYunServiceException, UpYunClientException

from settings import *


def check_mxl_file_url_endswith(download_file_url):
    if download_file_url.lower().endswith(('.mxl', 'MXL')):
        print('This is a mxl file url')
        return 'mxl'
    else:
        print('Not a mxl file url')
        return None


def new():
    upyun_entity = UpYun(UPYUN_SERVICE, UPYUN_USERNAME, UPYUN_PASSWORD, timeout=30, endpoint=ED_AUTO)
    return upyun_entity


def upload(entity, local_file, upyun_path):
    try:
        with open(local_file, 'rb') as upload_file:
            upload_result = entity.put(upyun_path, upload_file)
    except UpYunServiceException as se:
        print('Except an UpYunServiceException ...')
        print(f'Request Id: {se.request_id}')
        print(f'HTTP Status Code: {str(se.status)}')
        print(f'Error Message: {se.msg}')
        return None
    except UpYunClientException as ce:
        print('Except an UpYunClientException ...')
        print(f'Error Message: {ce.msg}')
        return None

    return upload_result


def download(entity, local_file, upyun_path):
    try:
        res = entity.getinfo(upyun_path)
        print(f'Download file info is {res}')
        with open(local_file, 'wb') as f:
            entity.get(upyun_path, f)

    except UpYunServiceException as se:
        print('Except an UpYunServiceException ...')
        print(f'Request Id: {se.request_id}')
        print(f'HTTP Status Code: {str(se.status)}')
        print(f'Error Message: {se.msg}')
        return None
    except UpYunClientException as ce:
        print('Except an UpYunClientException ...')
        print(f'Error Message: {ce.msg}')
        return None

    return True


def main():
    # Create new upyun entity
    up = new()

    # huiwing
    # http://huiwing.test.upcdn.net/test/BeetAnGeSample.mxl

    # # Download mxl file
    # download_file = 'BeetAnGeSample.mxl'
    # upyun_path = '/test/BeetAnGeSample.mxl'
    # download_result = download(up, download_file, upyun_path)
    # if download_result is not None:
    #     print(f'Download file {download_file} success')
    # else:
    #     print(f'Download file {download_file} fail')

    # Upload mxl file
    # upload_file = 'BeetAnGeSample.mxl'
    # upyun_path = '/test/BeetAnGeSample.mxl'
    # upload_result = upload(up, upload_file, upyun_path)
    # print(f'Upload mxl file {upload_file} result is : {upload_result}')


    # local-dev
    # https://upyun.dev.moicen.com/music-room/trans_test_mxl.mxl

    # Download mxl file
    download_file = 'trans_test_mxl.mxl'
    upyun_path = '/music-room/trans_test_mxl.mxl'
    download_result = download(up, download_file, upyun_path)
    if download_result is not None:
        print(f' =====>>> Download file {download_file} success')
    else:
        print(f' =====>>> Download file {download_file} fail')

    # Upload mxl file
    upload_file = 'trans_test_mxl.mxl'
    upyun_path = '/music-room/trans_test_mxl.mxl'
    upload_result = upload(up, upload_file, upyun_path)
    print(f' =====>>> Upload mxl file {upload_file} result is : {upload_result}')


if __name__ == "__main__":
    main()
