from minicas.log import Log


def test_logs_do_not_share_lines():
    a, b = Log(), Log()
    a.write("x")
    assert b.lines == []
