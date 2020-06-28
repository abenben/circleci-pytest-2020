import pytest

@pytest.fixture()
def fix01():
    # 前処理
    print('[start]fixture')

    # ここでテストを実行
    yield

    # 後処理
    print('[end]fiture')

def test_fixture(fix01):
    print('test!')
    assert True