def Reflexion_Joueur(pygame,event,fenetre,case,choixUser,playedCase,PlayingJoueur,PlayingMachine,rec,
font_info,rouge,blanc,dodger_blue,joueurWin,score):
            monScore = "Score : " + str(score)
    # S'il existe au moins une case vide | Tour Joeur
            if ((case[1] == True or case[2] == True or case[3] == True or case[4] == True 
            or case[5] == True or case[6] == True or case[7] == True or case[8] == True or
            case[9] == True or joueurWin) and PlayingJoueur == True and PlayingMachine == False):
                # Affichage du choix de l'Utilisateur
                maCouleur = (0,0,0)
                if(choixUser == "X"):
                    maCouleur = rouge
                else:
                    maCouleur = dodger_blue
               
                texte = font_info.render(monScore,True,blanc,maCouleur) 
                # create a rectangular object for the 
                # text surface object 
                textRect = texte.get_rect()
                # copying the text surface object 
                # to the display surface object 
                fenetre.blit(texte, textRect) 
                UserPlayed = False # l'Utilisateur n'a pas encore joué
                #LOGIQUE DU JEU
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos, " - Choix Rectangle")

                    # rec[1] à rec[9] correspondent aux rectangles
                    if rec[1].collidepoint(pos) and case[1]:
                        if choixUser == "X":
                                pygame.draw.line(fenetre, rouge,[35,25],[165,174], 20)
                                pygame.draw.line(fenetre, rouge,[165,25],[35,174], 20)
                        else:
                            # (100,100) le centre du circle, 50 rayon )        
                            pygame.draw.ellipse(fenetre, dodger_blue, [35,35,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[1] = True
                        case[1] = False
                    
                    if rec[2].collidepoint(pos) and case[2]:
                        if choixUser == "X":
                            pygame.draw.line(fenetre, rouge,[210,25],[339,174], 20)
                            pygame.draw.line(fenetre, rouge,[339,25],[210,174], 20)
                        else:
                            # on ajoute 100 + 175 =275
                            pygame.draw.ellipse(fenetre, dodger_blue, [210,35,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[2] = True
                        case[2] = False
                    
                    if rec[3].collidepoint(pos) and case[3] :
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[385,25],[514,174], 20)
                                pygame.draw.line(fenetre, rouge,[515,25],[384,174], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [385,35,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[3] = True
                        case[3] = False
                            
                    if rec[4].collidepoint(pos) and case[4] :
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[35,200],[165,349], 20)
                                pygame.draw.line(fenetre, rouge,[165,200],[35,349], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [35,210,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[4] = True
                        case[4] = False
                        
                    if rec[5].collidepoint(pos) and case[5]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[210,200],[339,349], 20)
                                pygame.draw.line(fenetre, rouge,[339,200],[210,349], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [210,210,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[5] = True
                        case[5] = False
                    
                    if rec[6].collidepoint(pos) and case[6]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[385,200],[514,349], 20)
                                pygame.draw.line(fenetre, rouge,[514,200],[384,349], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [385,210,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[6] = True
                        case[6] = False
                        
                    if rec[7].collidepoint(pos) and case[7]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[35,375],[164,524], 20)
                                pygame.draw.line(fenetre, rouge,[164,375],[35,524], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [35,385,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[7] = True
                        case[7] = False
                    
                    if rec[8].collidepoint(pos) and case[8]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[210,375],[339,524], 20)
                                pygame.draw.line(fenetre, rouge,[339,375],[210,524], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [210,385,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[8] = True
                        case[8] = False

                    if rec[9].collidepoint(pos) and case[9]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[385,375],[514,524], 20)
                                pygame.draw.line(fenetre, rouge,[514,375],[384,524], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [385,385,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        playedCase[9] = True
                        case[9] = False
            return [PlayingMachine,PlayingJoueur]