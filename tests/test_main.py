from alttester import AltDriver, AltKeyCode, AltObject


def test_player_can_move(alt_driver: AltDriver, player: AltObject, load_scene):
    start_pos = player.x
    alt_driver.press_key(AltKeyCode.D, duration=1)
    player.update_object()
    new_pos = player.x
    assert start_pos != new_pos


def test_player_can_jump(alt_driver: AltDriver, player: AltObject, load_scene):
    start_pos = player.y
    alt_driver.press_key(AltKeyCode.Space)
    player.update_object()
    new_pos = player.y
    assert start_pos != new_pos
