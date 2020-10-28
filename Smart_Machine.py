from Fonctional_machine import machine_Joue, switching_O, switching_X

# La Machine Reflechie, comment Gagner le jeu
# ou au pire, comment contrer le Joueur

def Reflexion_Machine(pygame,fenetre,case,choixUser,MachineCase,playedCase,PlayingMachine,PlayingJoueur,machine_Joue,switching_O,switching_X,random):
            # S'il existe au moins une case vide | Tour Machine
            if ((case[1] == True or case[2] == True or case[3] == True or case[4] == True 
                or case[5] == True or case[6] == True or case[7] == True or case[8] == True or
                case[9] == True) and PlayingMachine == True and PlayingJoueur == False):
                    listeIndiceCaseVide = []
                    listeIndiceRandomise = []
                    a = 1
                    # Liste Case Vide
                    for a in range(len(case)):
                        if(case[a] == True):
                            listeIndiceCaseVide.append(a) # indice : 2,4,7...
                    while PlayingMachine == True :
                        # Verifie si son prochain jeu peut faire d'elle vainqueur | Sinon, il contre le joueur
                        if (((case[1] == False and MachineCase[1]) and (case[2] == False and MachineCase[2]) and case[3]) or 
                            ((case[1] == False and MachineCase[1]) and (case[3] == False and MachineCase[3]) and case[2]) or
                            ((case[2] == False and MachineCase[2]) and (case[3] == False and MachineCase[3]) and case[1])):
                            i = 1
                            while i<=3:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=1
                        elif (((case[1] == False and MachineCase[1]) and (case[4] == False and MachineCase[4]) and case[7]) or 
                            ((case[1] == False and MachineCase[1]) and (case[7] == False and MachineCase[7]) and case[4]) or
                            ((case[4] == False and MachineCase[4]) and (case[7] == False and MachineCase[7]) and case[1])):
                            i = 1
                            while i<=7:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=3
                        elif (((case[1] == False and MachineCase[1]) and (case[5] == False and MachineCase[5]) and case[9]) or 
                            ((case[1] == False and MachineCase[1]) and (case[9] == False and MachineCase[9]) and case[5]) or
                            ((case[5] == False and MachineCase[5]) and (case[9] == False and MachineCase[9]) and case[1])):
                            i = 1
                            while i<=9:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=4
                        elif (((case[3] == False and MachineCase[3]) and (case[5] == False and MachineCase[5]) and case[7]) or 
                            ((case[3] == False and MachineCase[3]) and (case[7] == False and MachineCase[7]) and case[5]) or
                            ((case[5] == False and MachineCase[5]) and (case[7] == False and MachineCase[7]) and case[3])):
                            i = 3
                            while i<=7:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=2
                        elif (((case[3] == False and MachineCase[3]) and (case[6] == False and MachineCase[6]) and case[9]) or 
                            ((case[3] == False and MachineCase[3]) and (case[9] == False and MachineCase[9]) and case[6]) or
                            ((case[6] == False and MachineCase[6]) and (case[9] == False and MachineCase[9]) and case[3])):
                            i = 3
                            while i<=7:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=3
                        elif (((case[2] == False and MachineCase[2]) and (case[5] == False and MachineCase[5]) and case[8]) or 
                            ((case[2] == False and MachineCase[2]) and (case[8] == False and MachineCase[8]) and case[5]) or
                            ((case[5] == False and MachineCase[5]) and (case[8] == False and MachineCase[8]) and case[2])):
                            i = 2
                            while i<=8:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=3
                        elif (((case[4] == False and MachineCase[4]) and (case[5] == False and MachineCase[5]) and case[6]) or 
                            ((case[4] == False and MachineCase[4]) and (case[6] == False and MachineCase[6]) and case[5]) or
                            ((case[5] == False and MachineCase[5]) and (case[6] == False and MachineCase[6]) and case[4])):
                            i = 4
                            while i<=6:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=1
                        elif (((case[7] == False and MachineCase[7]) and (case[8] == False and MachineCase[8]) and case[9]) or 
                            ((case[7] == False and MachineCase[7]) and (case[9] == False and MachineCase[9]) and case[8]) or
                            ((case[8] == False and MachineCase[8]) and (case[9] == False and MachineCase[9]) and case[7])):
                            i = 7
                            while i<=9:
                                machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                PlayingMachine = machinePlayed[0]
                                PlayingJoueur = machinePlayed[1]
                                arretWhile = machinePlayed[2]
                                if (arretWhile == True):
                                    MachineCase[i] = True
                                    break
                                i+=1
                        else:
                            # La Machine essaye de contrer l'action du joueur
                            if (((case[1] == False and playedCase[1]) and (case[2] == False and playedCase[2]) and case[3]) or 
                                ((case[1] == False and playedCase[1]) and (case[3] == False and playedCase[3]) and case[2]) or
                                ((case[2] == False and playedCase[2]) and (case[3] == False and playedCase[3]) and case[1])):
                                i = 1
                                while i<=3:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=1
                            elif (((case[1] == False and playedCase[1]) and (case[4] == False and playedCase[4]) and case[7]) or 
                                ((case[1] == False and playedCase[1]) and (case[7] == False and playedCase[7]) and case[4]) or
                                ((case[4] == False and playedCase[4]) and (case[7] == False and playedCase[7]) and case[1])):
                                i = 1
                                while i<=7:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=3
                            elif (((case[1] == False and playedCase[1]) and (case[5] == False and playedCase[5]) and case[9]) or 
                                ((case[1] == False and playedCase[1]) and (case[9] == False and playedCase[9]) and case[5]) or
                                ((case[5] == False and playedCase[5]) and (case[9] == False and playedCase[9]) and case[1])):
                                i = 1
                                while i<=9:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=4
                            elif (((case[3] == False and playedCase[3]) and (case[5] == False and playedCase[5]) and case[7]) or 
                                ((case[3] == False and playedCase[3]) and (case[7] == False and playedCase[7]) and case[5]) or
                                ((case[5] == False and playedCase[5]) and (case[7] == False and playedCase[7]) and case[3])):
                                i = 3
                                while i<=7:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=2
                            elif (((case[3] == False and playedCase[3]) and (case[6] == False and playedCase[6]) and case[9]) or 
                                ((case[3] == False and playedCase[3]) and (case[9] == False and playedCase[9]) and case[6]) or
                                ((case[6] == False and playedCase[6]) and (case[9] == False and playedCase[9]) and case[3])):
                                i = 3
                                while i<=7:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=3
                            elif (((case[2] == False and playedCase[2]) and (case[5] == False and playedCase[5]) and case[8]) or 
                                ((case[2] == False and playedCase[2]) and (case[8] == False and playedCase[8]) and case[5]) or
                                ((case[5] == False and playedCase[5]) and (case[8] == False and playedCase[8]) and case[2])):
                                i = 2
                                while i<=8:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=3
                            elif (((case[4] == False and playedCase[4]) and (case[5] == False and playedCase[5]) and case[6]) or 
                                ((case[4] == False and playedCase[4]) and (case[6] == False and playedCase[6]) and case[5]) or
                                ((case[5] == False and playedCase[5]) and (case[6] == False and playedCase[6]) and case[4])):
                                i = 4
                                while i<=6:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=1
                            elif (((case[7] == False and playedCase[7]) and (case[8] == False and playedCase[8]) and case[9]) or 
                                ((case[7] == False and playedCase[7]) and (case[9] == False and playedCase[9]) and case[8]) or
                                ((case[8] == False and playedCase[8]) and (case[9] == False and playedCase[9]) and case[7])):
                                i = 7
                                while i<=9:
                                    machinePlayed = machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur)
                                    PlayingMachine = machinePlayed[0]
                                    PlayingJoueur = machinePlayed[1]
                                    arretWhile = machinePlayed[2]
                                    if (arretWhile == True):
                                        MachineCase[i] = True
                                        break
                                    i+=1
                            else:
                                # Randomiser la liste
                                while len(listeIndiceCaseVide) != 0 :
                                    tailleListe = len(listeIndiceCaseVide)
                                    chiffreRandom = random.randint(0,tailleListe-1)
                                    IndiceRandom = listeIndiceCaseVide[chiffreRandom] # 2,4,7...
                                    listeIndiceRandomise.append(IndiceRandom)
                                    del listeIndiceCaseVide[chiffreRandom]
                                # Demander à la machine de Jouer
                                # Prendre une case au hasard et coché
                                if (len(listeIndiceRandomise) != 0):
                                    indiceCaseRandom = random.choice(listeIndiceRandomise)
                                    # Verifier si la case et occupé ou pas
                                    if case[indiceCaseRandom] == True:
                                        if choixUser == "X":
                                            switching_O(pygame,fenetre,indiceCaseRandom)
                                            case[indiceCaseRandom] = False
                                            MachineCase[indiceCaseRandom] = True
                                            PlayingMachine = False
                                            PlayingJoueur = True
                                            break
                                        elif choixUser == "O":
                                            switching_X(pygame,fenetre,indiceCaseRandom)
                                            case[indiceCaseRandom] = False
                                            MachineCase[indiceCaseRandom] = True
                                            PlayingMachine = False
                                            PlayingJoueur = True
                                            break
                                        else:
                                            PlayingMachine = True
                                            print("Je ne sais pas sur quelle case dessinée")
            # A Qui le prochain tour @see return
            return [PlayingMachine,PlayingJoueur]