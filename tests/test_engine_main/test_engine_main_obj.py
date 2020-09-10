import pytest
from kaalia.game import kaaliaMain

def test_engine_main_obj_type(kaalia_engine):
    assert type(kaalia_engine) is kaaliaMain
