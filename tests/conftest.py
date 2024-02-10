import pytest
from alttester import AltDriver, By, AltObject



@pytest.fixture(scope='session')
def alt_driver():
    driver = AltDriver()
    yield driver
    driver.stop()


@pytest.fixture(scope='function')
def load_scene(alt_driver: AltDriver):
    alt_driver.load_scene('Game')


@pytest.fixture(scope='session')
def player(alt_driver: AltDriver) -> AltObject:
    return alt_driver.find_object(By.NAME, 'Player')
