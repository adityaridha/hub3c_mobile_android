import pytest
import os

@pytest.fixture()
def reset_app():
    print("Reset App Data")
    os.system("adb shell pm clear au.geekseat.com.hub3candroid")
