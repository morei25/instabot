from instapy import InstaPy

session = InstaPy(username="danielmoreira.dm49@gmail.com", password="DerBot25", headless_browser=True).login()
session.like_by_tags(["bmw","mercedes"], amount=5)
session.set_dont_like(["porshe", "naked"])
session.set_do_follow(True, percentage=45)

