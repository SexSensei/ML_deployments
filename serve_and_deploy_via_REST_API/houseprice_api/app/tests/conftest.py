import sys
from xml.etree.ElementPath import prepare_descendant

sys.path.append('C:\\KV_AI_JLR_26\\ML_deployments\\serve_and_deploy_via_REST_API\\houseprice_api\\')

from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from regression_model.config.core import config
from regression_model.processing.data_manager import load_dataset

from app.main import app

@pytest.fixture(scope='module')
def test_data() -> pd.DataFrame:
    return load_dataset(file_name=config.app_config.test_data_file)

@pytest.fixture()
def client() -> Generator:
    with testClient(app) as _client:
        yield _client
        app.dependecy_overrides = {}