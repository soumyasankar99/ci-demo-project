from app.etl import transform


def test_transform():
    assert transform([1, 2, 3]) == [2, 4, 6]
