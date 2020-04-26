from instapy import InstaPy

session = InstaPy(username="danielmoreira.dm49@gmail.com", password="DerBot25").login()
session.like_by_tags(["bmw","mercedes"], amount=5)
seesion.set_dont_like(["porshe", "naked"])

