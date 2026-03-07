# tests/test_agent_base.py
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


@patch("agents.agent_base.ChatOllama")
@patch("agents.agent_base.RunnableWithMessageHistory")
def test_load_prompt_success(MockRunnable, MockOllama):
    """load_prompt 能正确读取提示文件内容"""
    from agents.agent_base import AgentBase

    class ConcreteAgent(AgentBase):
        def create_chatbot(self):
            self.chatbot = MagicMock()
            self.chatbot_with_history = MagicMock()

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write("Hello system prompt\n")
        prompt_path = f.name
    try:
        agent = ConcreteAgent(
            name="test",
            prompt_file=prompt_path,
            session_id="test_session",
        )
        assert agent.prompt == "Hello system prompt"
    finally:
        os.unlink(prompt_path)


def test_load_prompt_file_not_found():
    """提示文件不存在时抛出 FileNotFoundError"""
    from agents.agent_base import AgentBase

    with patch.object(AgentBase, "create_chatbot", lambda self: None):
        with pytest.raises(FileNotFoundError, match="找不到提示文件"):
            AgentBase(
                name="test",
                prompt_file="nonexistent_prompt_xyz.txt",
                session_id="test",
            )


@patch("agents.agent_base.ChatOllama")
@patch("agents.agent_base.RunnableWithMessageHistory")
def test_load_intro_success(MockRunnable, MockOllama):
    """load_intro 能正确读取 JSON 初始消息列表"""
    from agents.agent_base import AgentBase

    class ConcreteAgent(AgentBase):
        def create_chatbot(self):
            self.chatbot = MagicMock()
            self.chatbot_with_history = MagicMock()

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as pf:
        pf.write("prompt")
        prompt_path = pf.name
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as jf:
        json.dump(["msg1", "msg2"], jf, ensure_ascii=False)
        intro_path = jf.name
    try:
        agent = ConcreteAgent(
            name="test",
            prompt_file=prompt_path,
            intro_file=intro_path,
            session_id="test_session",
        )
        assert agent.intro_messages == ["msg1", "msg2"]
    finally:
        os.unlink(prompt_path)
        os.unlink(intro_path)


def test_load_intro_invalid_json():
    """intro 文件内容非合法 JSON 时抛出 ValueError"""
    from agents.agent_base import AgentBase

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write("not valid json {")
        bad_path = f.name
    try:
        with patch.object(AgentBase, "create_chatbot", lambda self: None):
            with patch.object(AgentBase, "load_prompt", return_value="dummy"):
                with pytest.raises(ValueError, match="无效的 JSON"):
                    AgentBase(
                        name="test",
                        prompt_file="prompts/conversation_prompt.txt",
                        intro_file=bad_path,
                        session_id="test",
                    )
    finally:
        os.unlink(bad_path)


def test_load_intro_file_not_found():
    """intro 文件不存在时抛出 FileNotFoundError"""
    from agents.agent_base import AgentBase

    with patch.object(AgentBase, "create_chatbot", lambda self: None):
        with patch.object(AgentBase, "load_prompt", return_value="dummy"):
            with pytest.raises(FileNotFoundError, match="找不到初始消息文件"):
                AgentBase(
                    name="test",
                    prompt_file="prompts/conversation_prompt.txt",
                    intro_file="content/intro/nonexistent.json",
                    session_id="test",
                )


@patch("agents.agent_base.ChatOllama")
@patch("agents.agent_base.RunnableWithMessageHistory")
def test_session_id_defaults_to_name(MockRunnable, MockOllama):
    """未传 session_id 时使用 name 作为 session_id"""
    from agents.agent_base import AgentBase

    class ConcreteAgent(AgentBase):
        def create_chatbot(self):
            self.chatbot = MagicMock()
            self.chatbot_with_history = MagicMock()

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write("p")
        prompt_path = f.name
    try:
        agent = ConcreteAgent(
            name="my_agent",
            prompt_file=prompt_path,
            session_id=None,
        )
        assert agent.session_id == "my_agent"
    finally:
        os.unlink(prompt_path)
