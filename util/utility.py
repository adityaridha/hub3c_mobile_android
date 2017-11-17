class Helper():

    def __init__(self, driver):
        self.driver = driver

    def tap_first_result_auto_complete(self, element):
        x = element.location['x']
        y = element.location['y']
        height = element.size['height']
        width = element.size['width']
        target_x = x + (int(width/2))
        suggestion_cord = []
        suggestion_cord.append((target_x, y+height+40))
        suggestion_cord.append((target_x, y+height+50))

        self.driver.tap(suggestion_cord)

    def swipe_to_buttom(self):
        try:
            self.driver.swipe(522, 800, 495, 100, 1000)
            print("swipe success")
        except :
            print("swipe failed")

