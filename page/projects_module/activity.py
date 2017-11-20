from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class Activity():

    search_textbox = "android:id/search_src_text"
    activity_card = "(//*[@id='rv_activities_project']/*/*[@class='android.widget.LinearLayout' and @width>0 and @height>0 and ./*[./*[./*[@id='text_tittle_activity']]]])[1]"
    activity_title = "au.geekseat.com.hub3candroid:id / text_tittle_activity"
    activity_assignee_name = "au.geekseat.com.hub3candroid:id / tv_name"
    activity_assignee_picture = "( // * [ @ id = 'rv_activities_project'] / * / * / * / * / *[ @class ='android.widget.ImageView' and @ width > 0 and @ height > 0 and./ preceding-sibling::*[ @ id = 'skill_container']])[1]"
    activity_progress_bar = "au.geekseat.com.hub3candroid:id / materialProgress"
    activity_due_date = "au.geekseat.com.hub3candroid:id / text_due_date"
    activity_more_button = "au.geekseat.com.hub3candroid:id / ib_action_more"
    add_activity = "au.geekseat.com.hub3candroid:id / fab"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"

    ''' option more button '''
    more_activity_name = "au.geekseat.com.hub3candroid:id/text_tittle"
    more_alert_me = "au.geekseat.com.hub3candroid:id/btn_edit"
    more_mark_complete = "au.geekseat.com.hub3candroid:id/btn_complete"
    more_delete = "au.geekseat.com.hub3candroid:id/btn_delete"