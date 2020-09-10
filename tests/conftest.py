import pytest
from kaalia.game import kaaliaMain


@pytest.fixture(scope='module')
def kaalia_engine():
    engine_obj = kaaliaMain()
    yield engine_obj
