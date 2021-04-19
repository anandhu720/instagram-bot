from instapy import InstaPy
from time import sleep

session = InstaPy(username="gjsjjsb16782", password="**********").login()
session.login()
#session.follow_by_tags(tags=["chsslyf"],amount=5)
#session.follow_user_followers(["a_na_ndhu__"],amount=5)
#session.follow_user_following(["a_na_ndhu"],amount=5)
#session.join_pods(topic='travel',engagement_mode='normal')  confusing
#session.interact_by_users(['a_na_ndhu__'],amount=2)
#session.story_by_tags(tags=['marvel'])
session.validate_user_call('a_na_ndhu__')
session.end()
