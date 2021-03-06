from .settings import *

# mysql 数据库
import pymysql

pymysql.install_as_MySQLdb()
# DEBUG=False 不会用自带的 server 去 server js/css 等静态文件
# 需要用 nginx 之类的去做静态文件的 server.
DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS += INTERNAL_IPS
ALLOWED_HOSTS.append('localhost')

# 重置 setting 里的 STATIC_ROOT 配置
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# static 目录配置
# 如果 DEBUG 为 False 这里就会失效，需要用 NGIX 代理
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
    os.path.join(PROJECT_ROOT, 'frontend/dist/static'),
]

# 开发环境开启跨域
CORS_ORIGIN_ALLOW_ALL = True

#INSTALLED_APPS.append('debug_toolbar')
#MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# 请按照你开发时本机的数据库名字，密码，端口填写
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tripitaka',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4', 'init_command': 'SET default_storage_engine=InnoDB'}
    },
}