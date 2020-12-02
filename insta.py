from instapy import InstaPy
from time import sleep

session = InstaPy(username="gjsjjsb16782", password="*********").login()
session.login()
session.like_by_tags([ "chsslyf"],amount=1)
session.set_dont_like(["fashion",'sexy'])
session.set_do_follow(True,percentage=100)
session.set_do_comment(True, percentage=100)
session.set_comments(["nice","sweet","awsome",])
session.end()
