import ga2
import random
import time
from ga2.cloud import reporter
import os
from ga2.device.device import DeviceType

def random_travel(device, rounds=10):
    engine = device.engine_connector()
    visited = []
    for i in range(rounds):
        time0 = time.time()
        uielements = engine.get_touchable_uielements()
        print("get touchable elements cost: " + str(time.time() - time0))
        if not uielements or len(uielements)==0:
            print("no uielements found... for now")
            continue
        elem = random.sample(uielements, 1)[0]
        for e in uielements:
            if e.element in visited:
                uielements.remove(e)
                print("remove visited elem...")
        if len(uielements) > 0:
            elem = random.sample(uielements, 1)[0]
        visited.append(elem.element)
        time.sleep(1)
        ga2.touch_element(ga2.By.ELEMENT_IN_ENGINE, elem.element, sleep_after=1)


def uiconfig_test(device):
    assert (ga2.load_uiconfig("uiconfig.yml"))
    device.home()
    ga2.click_element(ga2.By.ID_IN_UICONFIG, "CLOCK_ICON")
    ga2.click_element(ga2.By.ID_IN_UICONFIG, "TIMER")
    ga2.click_element(ga2.By.ID_IN_UICONFIG, "TIMER_START")
    time.sleep(3)
    ga2.click_element(ga2.By.ID_IN_UICONFIG, "TIMER_STOP")
    device.home()
    assert (ga2.ErrType.ERR_SUCCEED == device.launch_app(os.environ.get("PKGNAME", "com.tencent.wetest.demo")))
    time.sleep(5)
    if ga2.is_cloud_mode():
        reporter.Reporter().screenshot()
    # assert(device.init_engine_sdk()==ga2.ERR_SUCCEED) # lazy init when calling engine connector (if not init)
    assert (ga2.wait_element(ga2.By.ID_IN_UICONFIG, "FindElements", timeout=20))
    assert (ga2.touch_element(ga2.By.ID_IN_UICONFIG, "FindElements"))
    assert (ga2.touch_element(ga2.By.ID_IN_UICONFIG, "Level4"))
    print(device.display_size())
    assert (ga2.touch_element(ga2.By.ID_IN_UICONFIG, "Planet"))
    assert (ga2.touch_element(ga2.By.ID_IN_UICONFIG, "Game_Back"))
    assert (ga2.wait_element(ga2.By.ID_IN_UICONFIG, "FindElements"))
    assert (ga2.touch_element(ga2.By.ID_IN_UICONFIG, "FindElements"))
    assert (ga2.wait_element(ga2.By.ID_IN_UICONFIG, "Planet_Test"))
    assert (ga2.touch_element(ga2.By.ID_IN_UICONFIG, "Planet_Test"))



device_type = ga2.DeviceType.DEVICE_ANDROID
if ga2.is_cloud_mode() and os.environ.get("IOS_SERIAL"):
    device_type = ga2.DeviceType.DEVICE_IOS
device = ga2.init_device(device_type)
assert (device)
assert(ga2.ErrType.ERR_SUCCEED == device.launch_app(os.environ.get("PKGNAME", "com.tencent.wetest.demo")))
time.sleep(5)
if ga2.is_cloud_mode():
    reporter.Reporter().screenshot()
random_travel(device)
device.kill_app(os.environ.get("PKGNAME", "com.tencent.wetest.demo"))
uiconfig_test(device)

