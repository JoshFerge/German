# -*- coding: iso-8859-15 -*-

import os, sys
class Translate:

	
	to = {
'nope':'Nein, das ist nicht ein Wort.',
'yellow':'gelb',
'purple':'lila',
'pink':'rosa',
'black':'schwartz', 
'green':'grün',
'door':'die Tür',
'crazy':'verrückt',
'white':'weiß',
'blue':'blau',
'the':'der die das',
'a':'ein, eine',
'jump':'springen',
'wall':'der wand',
'ceiling':'die decke',
'laptop':'der laptop',
'book':'der buch',
'hello':'hallo, Guten Tag',
'goodbye':'Tschüss, Auf Weidersein',
'belly':'der Bauch',
'head':'der kopf',
'mouth':'der Mund',
'back':'der Rücken',
'eye': 'das Auge',
'face':'das Gesicht',
'foot':'der Fuß',
'hair':'das Haar',
'finger':'der Finger',
'watch':'eine Armbanduhr',
'glasses':'eine Brille'


}
	def Dict(self):
		g = True
		while g == True:
			fruit = set(self.to) 
			word = raw_input("what word would you like to translate?\n")
			if word == "out":
				print "YOLO"
				break
			if word not in self.to:
				word = "nope"
				g = False
			
			
			
			print self.to[word]

	def Game(self):
			count = 0
			outof = 0
			fruit = list(self.to)
			for i in range (0 ,len(fruit)):
				print fruit[i]
				test = raw_input("Translate to German!\n")
				if test != self.to[fruit[i]]:
					print "wrong!\n"
					print self.to[fruit[i]]
					outof = outof+1

					
				else:
					print "right!\n"
					outof=outof+1
					count=count+1
			print count, "/", outof





german = Translate()



german.Game()


