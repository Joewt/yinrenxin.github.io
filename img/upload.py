from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
access_key = 'gb-pd5ReYGwaY0pTdHFGstOHBZyYMNVOulstOlZ3'
secret_key = '3Xn8cpiUB7dMCtHLcsT_6ZqwcItZxaAYLsPuvS1K'
q = Auth(access_key, secret_key)
bucket_name = 'yrapp'
key = 'swoole-install-finish.png';
token = q.upload_token(bucket_name, key, 3600)
localfile = './1.png'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)