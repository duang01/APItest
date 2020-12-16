

# 测试版本
def test_version():
    from apitest import __version__
    assert isinstance(__version__, str)  # 测试__version__是否为字符串

