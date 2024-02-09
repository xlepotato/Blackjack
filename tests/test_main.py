import pytest
from main import display_banner

@pytest.fixture
def mocked_player(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mocked_dealer(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mocked_game(mocker, mocked_player, mocked_dealer):
    return mocker.MagicMock(player=mocked_player, dealer=mocked_dealer)

def test_display_banner(mocker):
    mock_print = mocker.patch("builtins.print")
    display_banner()
    # Ensure that the banner is printed correctly
    assert mock_print.call_count == 4  # The banner consists of 4 lines
