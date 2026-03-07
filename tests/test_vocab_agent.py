# tests/test_vocab_agent.py
from unittest.mock import MagicMock, patch

import pytest


@patch("agents.vocab_agent.AgentBase.__init__", return_value=None)
def test_restart_session_clears_history_and_returns(MockBaseInit):
    """restart_session 清除该 session 历史并返回 history 对象"""
    from agents.vocab_agent import VocabAgent

    mock_history = MagicMock()
    with patch("agents.vocab_agent.get_session_history", return_value=mock_history):
        with patch.object(VocabAgent, "load_prompt", return_value="p"):
            with patch.object(VocabAgent, "create_chatbot", return_value=None):
                agent = VocabAgent(session_id="vocab_test")
                agent.session_id = "vocab_test"

    result = agent.restart_session()
    mock_history.clear.assert_called_once()
    assert result is mock_history


@patch("agents.vocab_agent.AgentBase.__init__", return_value=None)
def test_restart_session_uses_instance_session_id_when_none(MockBaseInit):
    """restart_session(session_id=None) 使用实例的 session_id"""
    from agents.vocab_agent import VocabAgent

    mock_history = MagicMock()
    with patch("agents.vocab_agent.get_session_history", return_value=mock_history) as MockGet:
        with patch.object(VocabAgent, "load_prompt", return_value="p"):
            with patch.object(VocabAgent, "create_chatbot", return_value=None):
                agent = VocabAgent(session_id=None)
                agent.session_id = "vocab_study"

    agent.restart_session(session_id=None)
    MockGet.assert_called_with("vocab_study")
