# tests/test_logger.py


def test_log_exists():
    """utils.logger 导出 LOG 且可调用 debug/info/error"""
    from utils.logger import LOG

    assert LOG is not None
    LOG.debug("test debug")
    LOG.info("test info")
    LOG.error("test error")
