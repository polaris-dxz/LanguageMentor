# tests/test_session_history.py
import pytest
from agents.session_history import get_session_history, store


def test_get_session_history_creates_new():
    """新 session_id 会创建新的历史实例"""
    sid = "test_session_new_123"
    if sid in store:
        del store[sid]
    history = get_session_history(sid)
    assert history is not None
    assert sid in store
    assert store[sid] is history


def test_get_session_history_returns_same_for_same_id():
    """相同 session_id 返回同一历史对象"""
    sid = "test_session_same"
    if sid in store:
        del store[sid]
    h1 = get_session_history(sid)
    h2 = get_session_history(sid)
    assert h1 is h2


def test_history_starts_empty():
    """新历史初始无消息"""
    sid = "test_session_empty"
    if sid in store:
        del store[sid]
    history = get_session_history(sid)
    assert len(history.messages) == 0
