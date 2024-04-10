from alttester import AltDriver, AltKeyCode, By


def test_player_can_move(alt_driver: AltDriver, load_scene):
    player = alt_driver.find_object(By.NAME, 'Player')
    start_pos = player.x

    alt_driver.press_key(AltKeyCode.D, duration=1)

    player = alt_driver.find_object(By.NAME, 'Player')
    new_pos = player.x
    assert start_pos != new_pos


def test_player_can_jump(alt_driver: AltDriver, load_scene):
    player = alt_driver.find_object(By.NAME, 'Player')
    start_pos = player.y
    
    alt_driver.press_key(AltKeyCode.Space)

    player = alt_driver.find_object(By.NAME, 'Player')
    new_pos = player.y
    assert start_pos != new_pos
