#!/usr/bin/env python

# Web2Hunter			    		  -- Abhishek Mishra <ideamonk at gmail.com>
#
#			a web 2.0 name generator extension to domainhunter.py
#
# 	usage -
#		$ python web2hunter.py

import domainhunter as DH
import random

A = ["Anti", "Aero", "Babble", "Buzz", "Blog", "Blue", "Brain", "Bright", "Browse", "Bubble", "Chat", "Chatter", "Dab", "Dazzle", "Dev", "Digi", "Edge", "Feed", "Five", "Flash", "Flip", "Gab", "Giga",  "Inno", "Jabber", "Jax", "Jet", "Jump", "Link", "Live", "My", "N", "Photo", "Pod", "Real", "Riff", "Shuffle", "Snap", "Skip", "Tag", "Tek", "Thought", "Top", "Topic", "Twitter", "Word", "You", "Zoom"]
B = ["bean", "beat", "bird", "blab", "box", "bridge", "bug", "buzz", "cast", "cat", "chat", "club", "cube", "dog", "drive", "feed", "fire", "fish", "fly", "ify", "jam", "links", "list", "lounge", "mix", "nation", "opia", "pad", "path", "pedia", "point", "pulse", "set", "space", "span", "share", "shots", "sphere", "spot", "storm",  "ster", "tag", "tags", "tube", "tune", "type", "verse", "vine", "ware", "wire", "works", "XS", "Z", "zone", "zoom"]
C = ["Ai", "Aba", "Agi", "Ava", "Awesome", "Cami", "Centi", "Cogi", "Demi", "Diva", "Dyna", "Ea", "Ei", "Fa", "Ge", "Ja", "I", "Ka", "Kay", "Ki", "Kwi", "La", "Lee", "Mee", "Mi", "Mu", "My", "Oo", "O", "Oyo", "Pixo", "Pla", "Qua", "Qui", "Roo", "Rhy", "Ska", "Sky", "Ski", "Ta", "Tri", "Twi", "Tru", "Vi", "Voo", "Wiki", "Ya", "Yaki", "Yo", "Za", "Zoo"]
D = ["ba", "ble", "boo", "box", "cero", "deo", "del", "do", "doo", "gen", "jo", "lane", "lia", "lith", "loo", "lium", "mba", "mbee", "mbo", "mbu", "mia", "mm", "nder", "ndo", "ndu", "noodle", "nix", "nte", "nti", "nu", "nyx", "pe", "re", "ta", "tri", "tz", "va", "vee", "veo", "vu", "xo", "yo", "zz", "zzy", "zio", "zu"]

def genName():
	output = ""

	random.shuffle(A)
	random.shuffle(B)
	random.shuffle(C)
	random.shuffle(D)
	
	if (random.randint(0,1) == 1):
		awesomename = A[0] + B[0]
	else:
		awesomename = C[0] + D[0]
	
	random.shuffle(DH.tlds)
	tld = DH.tlds[0]

	if ( DH.domainSearch(awesomename + tld) ):
		output = awesomename + tld
			
	return output
