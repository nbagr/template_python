from template_code.sum import sum


def test_sum():
    assert sum(2, 3) == 5
    assert sum(0, 4) == 4
    assert sum(100, 200) == 300
