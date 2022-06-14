import os


def get_databases_object(config_dict: dict, base_dir) -> dict:
    if config_dict["PRODUCTION"]:
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': config_dict['SERVER_DB']['NAME'],
                'USER': config_dict['SERVER_DB']['USER'],
                'PASSWORD': config_dict['SERVER_DB']['PASSWORD'],
                'HOST': config_dict['SERVER_DB']['HOST'],
                'PORT': config_dict['SERVER_DB']['PORT'],
            }
        }
    else:
        if config_dict["USING_LOCAL_DOCKER"]:
            return {
                'default': {
                    'ENGINE': os.environ.get(config_dict['LOCAL_DB_DOCKER']['ENGINE_ENV'],
                                             'django.db.backends.sqlite3'),
                    'NAME': os.environ.get(config_dict['LOCAL_DB_DOCKER']['NAME_ENV'],
                                           os.path.join(base_dir, 'db.sqlite3')),
                    'USER': os.environ.get(config_dict['LOCAL_DB_DOCKER']['USER_ENV'], 'user'),
                    'PASSWORD': os.environ.get(config_dict['LOCAL_DB_DOCKER']['PASSWORD_ENV'], 'password'),
                    'HOST': os.environ.get(config_dict['LOCAL_DB_DOCKER']['HOST_ENV'], 'localhost'),
                    'PORT': os.environ.get(config_dict['LOCAL_DB_DOCKER']['PORT_ENV'], '5432'),
                }
            }
        else:
            return {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': config_dict['LOCAL_DB_NO_DOCKER']['NAME'],
                    'USER': config_dict['LOCAL_DB_NO_DOCKER']['USER'],
                    'PASSWORD': config_dict['LOCAL_DB_NO_DOCKER']['PASSWORD'],
                    'HOST': config_dict['LOCAL_DB_NO_DOCKER']['HOST'],
                    'PORT': config_dict['LOCAL_DB_NO_DOCKER']['PORT'],
                }
            }
