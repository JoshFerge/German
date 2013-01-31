# -*- coding: iso-8859-15 -*-
g = True
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
'wall':'der want',
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
'ear':'das Ohr',
'hand':'die Hand',
'shoulder':'die Hand'


}




german = Translate

while g == True:
	fruit = set(german.to) 
	word = raw_input("what word would you like to translate\n")
	if word not in fruit:
		word = "nope"
		
	
	
	print german.to[word]


