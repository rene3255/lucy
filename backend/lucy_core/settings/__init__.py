from decouple import config

env_settings = config("DJANGO_ENV", default="dev")

if env_settings == "prod":
    print("AMBIENTE", env_settings)
    from .prod import *
else:
    from .dev import *
