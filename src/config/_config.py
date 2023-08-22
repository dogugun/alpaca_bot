import os
from enum import Enum
from typing import List, Literal

import yaml
from pydantic import BaseModel
from pydantic.types import SecretStr, constr

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class Api(BaseModel):
    apca_api_key_id: str
    apca_api_secret_key: str


class Model(BaseModel):
    name: str
    fields: List[str]


class Config(BaseModel):
    Api: Api

def get_config():
    config_path = os.path.join(BASEDIR, "config.yaml")
    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)

    config = Config.parse_obj(config_dict)
    return config

