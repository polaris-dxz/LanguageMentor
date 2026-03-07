# tests/test_scenario_tab.py
from unittest.mock import patch

import pytest


def test_get_page_desc_returns_content_when_file_exists():
    """当场景页面 md 存在时返回其内容"""
    from tabs.scenario_tab import get_page_desc

    out = get_page_desc("job_interview")
    assert "目标" in out or "面试" in out
    assert "场景介绍文件未找到" not in out


def test_get_page_desc_returns_error_message_when_file_not_found():
    """当场景页面 md 不存在时返回错误提示"""
    from tabs.scenario_tab import get_page_desc

    out = get_page_desc("nonexistent_scenario_xyz")
    assert out == "场景介绍文件未找到。"
