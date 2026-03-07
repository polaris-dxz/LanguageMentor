# tests/test_vocab_tab.py


def test_get_page_desc_returns_content_when_file_exists():
    """当词汇页面 md 存在时返回其内容"""
    from tabs.vocab_tab import get_page_desc

    out = get_page_desc("vocab_study")
    assert "词汇" in out or "目标" in out or "介绍" in out
    assert "未找到" not in out or out == "词汇学习介绍文件未找到。"


def test_get_page_desc_returns_error_message_when_file_not_found():
    """当词汇页面 md 不存在时返回错误提示"""
    from tabs.vocab_tab import get_page_desc

    out = get_page_desc("nonexistent_feature_xyz")
    assert out == "词汇学习介绍文件未找到。"
