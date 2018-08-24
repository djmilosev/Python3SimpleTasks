#!/usr/bin/env python3

## import modula
import random


## 1. Meni
def stampaj():
	print("Izaberite program koji želite iz menija: ")
	print("================")
	print("1. Loto ")
	print("2. Broj ocena ")
	print("3. Kviz iz istorije ")
	print("4. Izlaz ")
	print("================")


## 2. Loto
def kombinacije():
	listaKomb = []
	brojKombinacija = input("Unesite broj kombinacija: ")
	for i in range(1, int(brojKombinacija) +1):
		podlista = []
		for y in range (7):
			broj = random.randint(1,39)
			podlista.append(broj)
		listaKomb.append(podlista)
	print("Broj unetih kombinacija je: " + str(brojKombinacija))
	for x in listaKomb :
		print (x)
		
## 3. Ocene
def brojocena():
	brojOcena = input("Unesite broj ocena: ")
	listaOcena = []
	for i in range(1, int(brojOcena) +1):
		pojedinacneOcene=input("Unesite pojedinačne ocene: ")
		listaOcena.append(pojedinacneOcene)
	print("Broj unetih ocena je: " + str(brojOcena))
	print("Unete ocene su: " + str(listaOcena))


## 4. Kviz iz istorije
def pitanja():
	
	ispadni = False
	def pitanje1():
		odgovori1 = [ "a) 1803", "b) 1806", "c) 1804" ]
		print (odgovori1)
		while (True) :
			odgovor= input("Unesite slovo koje stoji pored tačnog odgovora: ") 
			if (odgovor == "C" or odgovor == "c"):
				print (" Odgovor je tačan!")
				ispadni = True
				return (ispadni)
				
			elif (odgovor == "A" or odgovor == "a" or odgovor == "B" or odgovor == "b") :
				print(" Sram te bilo! Netačno! >:( !")
				ispadni = True
				return (ispadni)
			else:
				print(" Neodgovarajući unos, pokušajte ponovo!\n")

	def pitanje2():
		odgovori2 = [ " a) 1768 b) 1769 c) 1777 "]
		print (odgovori2)
		while (True):
			odgovor= input("Unesite slovo koje stoji pored tačnog odgovora: ") 
			if (odgovor == "a" or odgovor == "A"):
				print (" Odgovor je tačan!")
				ispadni = True
				return (ispadni)
				
			elif (odgovor == "b" or odgovor == "B" or odgovor == "C" or odgovor == "c") :
				print(" Sram te bilo! Netačno! >:( !")
				ispadni = True
				return (ispadni)
			else:
				print(" Neodgovarajući unos, pokušajte ponovo! \n")
	
	def pitanje3():
		odgovori3 = [ " a) 1809 b) 1810 c) 1805 "]
		print (odgovori3)
		while (True):
			odgovor= input("Unesite slovo koje stoji pored tačnog odgovora: ") 
			if (odgovor == "a" or odgovor == "A"):
				print (" Tačno!")
				ispadni = True
				return (ispadni)
				
			elif (odgovor == "b" or odgovor == "B" or odgovor == "C" or odgovor == "c") :
				print(" Sram te bilo! Netačno! >:( !")
				ispadni = True
				return (ispadni)
			else:
				print(" Neodgovarajući unos, pokušajte ponovo! \n")

	def pitanje4():
		odgovori4 = [ " a) 1805 b) 1806 c) 1808 "]
		print (odgovori4)
		while (True):
			odgovor= input("Unesite slovo koje stoji pored tacnog odgovora: ") 
			if (odgovor == "b" or odgovor == "B"):
				print (" Tačno!")
				ispadni = True
				return (ispadni)
				
			elif (odgovor == "a" or odgovor == "A" or odgovor == "C" or odgovor == "c") :
				print(" Sram te bilo! Netačno! >:( !")
				ispadni = True
				return (ispadni)
			else:
				print(" Neodgovarajući unos, pokušajte ponovo! \n")


	def stampaj_pitanja():
		pitanje = [ "Kada je bio prvi Srpski ustanak?", "Kada je rođen Vožd Karađorđe?",
			"Kada je bila bitka na Čegru?", "Kada je Beograd oslobođen od Turaka?"]
		i = 0
		for x in pitanje:
			i+=1
			print(i,")",x)
		print ('\n') 

	while (True):
		stampaj_pitanja()
		unos = input("Izaberite pitanje ili unesite \"q\" za povratak u glavni meni:  ")
		if (unos == "1" ):
			print("izabrali ste prvo pitanje ")
			pitanje1()
			continue
			
		elif (unos == "2" ):
			print("izabrali ste drugo pitanje ")
			pitanje2()
			continue

		elif (unos == "3" ):
			print("izabrali ste treće pitanje ")
			pitanje3()
			continue

		elif (unos == "4" ):
			print("izabrali ste četvrto pitanje ")
			pitanje4()
			continue
			 

		elif (unos == "Q" or unos == "q"):
			return  


		else:
			print("Pogrešan unos!")
			
## (5, 6, 7) : output
while (True) :
	stampaj()	
	izbor = input("Unesite svoj izbor (1,2,3 ili 4): ")
	if izbor == "1" :
		kombinacije()

	elif izbor == "2":
		brojocena()

	elif izbor == "3":
		pitanja()

	elif izbor == "4":
		print("Prekidam, pozdrav!")
		break

	else :
		print("Pogrešan unos! Unesite ponovo!")
		

