# tests/test_scenario_agent.py
from unittest.mock import MagicMock, patch

import pytest


@patch("agents.scenario_agent.get_session_history")
@patch("agents.scenario_agent.AgentBase.__init__", return_value=None)
def test_start_new_session_returns_random_intro_when_history_empty(MockBaseInit, MockGetHistory):
    """历史为空时 start_new_session 返回随机一条 intro 并写入历史"""
    from agents.scenario_agent import ScenarioAgent

    mock_history = MagicMock()
    mock_history.messages = []
    MockGetHistory.return_value = mock_history

    with patch.object(ScenarioAgent, "load_prompt", return_value="prompt"):
        with patch.object(ScenarioAgent, "load_intro", return_value=["intro1", "intro2"]):
            with patch.object(ScenarioAgent, "create_chatbot", return_value=None):
                agent = ScenarioAgent("job_interview")
                agent.intro_messages = ["intro1", "intro2"]
                agent.session_id = "sid"

    with patch("agents.scenario_agent.random") as MockRandom:
        MockRandom.choice.return_value = "intro1"
        out = agent.start_new_session()
    assert out == "intro1"
    mock_history.add_message.assert_called_once()
    MockRandom.choice.assert_called_once_with(["intro1", "intro2"])


@patch("agents.scenario_agent.get_session_history")
@patch("agents.scenario_agent.AgentBase.__init__", return_value=None)
def test_start_new_session_returns_last_message_when_history_not_empty(MockBaseInit, MockGetHistory):
    """历史非空时 start_new_session 返回最后一条消息"""
    from agents.scenario_agent import ScenarioAgent

    mock_last = MagicMock()
    mock_last.content = "last message"
    mock_history = MagicMock()
    mock_history.messages = [MagicMock(), mock_last]
    MockGetHistory.return_value = mock_history

    with patch.object(ScenarioAgent, "load_prompt", return_value="prompt"):
        with patch.object(ScenarioAgent, "load_intro", return_value=[]):
            with patch.object(ScenarioAgent, "create_chatbot", return_value=None):
                agent = ScenarioAgent("job_interview")
                agent.session_id = "sid"

    out = agent.start_new_session()
    assert out == "last message"
    mock_history.add_message.assert_not_called()
