import matplotlib.pyplot as plt
import time

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']

"""
Fonction qui prend en argument un texte "brut" (qui contient des accents,
des guillemets...) et retourne un texte dépourvu d'espaces, d'accents, de guillemets...
"""
def conv_character(char:str):
    final_char = ""
    l_char = list(char)
    l = len(l_char)

    for i in range(0,l_char.count(' ')):
        index = l_char.index(' ')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('é')):
        index = l_char.index('é')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('è')):
        index = l_char.index('è')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('à')):
        index = l_char.index('à')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count(':')):
        index = l_char.index(':')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('/')):
        index = l_char.index('/')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('§')):
        index = l_char.index('§')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('!')):
        index = l_char.index('!')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count(',')):
        index = l_char.index(',')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count(';')):
        index = l_char.index(';')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('.')):
        index = l_char.index('.')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('-')):
        index = l_char.index('-')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count(')')):
        index = l_char.index(')')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('(')):
        index = l_char.index('(')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('_')):
        index = l_char.index('_')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('–')):
        index = l_char.index('–')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count("'")):
        index = l_char.index("'")
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count("’")):
        index = l_char.index("’")
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('"')):
        index = l_char.index('"')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('“')):
        index = l_char.index('“')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('ù')):
        index = l_char.index('ù')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('ê')):
        index = l_char.index('ê')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('A')):
        index = l_char.index('A')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('B')):
        index = l_char.index('B')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('C')):
        index = l_char.index('C')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('D')):
        index = l_char.index('D')
        del l_char[index]
        l = len(l_char)

    for i in range(0,l_char.count('E')):
        index = l_char.index('E')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('F')):
        index = l_char.index('F')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('G')):
        index = l_char.index('G')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('H')):
        index = l_char.index('H')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('I')):
        index = l_char.index('I')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('J')):
        index = l_char.index('J')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('L')):
        index = l_char.index('L')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('M')):
        index = l_char.index('M')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('N')):
        index = l_char.index('N')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('O')):
        index = l_char.index('O')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('P')):
        index = l_char.index('P')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('Q')):
        index = l_char.index('Q')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('R')):
        index = l_char.index('R')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count("S")):
        index = l_char.index("S")
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count("T")):
        index = l_char.index("T")
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('U')):
        index = l_char.index('U')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('V')):
        index = l_char.index('V')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('W')):
        index = l_char.index('W')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('X')):
        index = l_char.index('X')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('Y')):
        index = l_char.index('Y')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('Z')):
        index = l_char.index('Z')
        del l_char[index]
        l = len(l_char)

    for i in range(0, l_char.count('â')):
        index = l_char.index('â')
        del l_char[index]
        l = len(l_char)

    for i in range(0,len(l_char)):
        final_char = final_char + l_char[i]

    print(final_char)

def cryptage(a: str, cle: str):
    txt = list(a)  # Transforme les arguments en liste.
    list_cle = list(cle)  #
    index_output = ''
    if len(list_cle) // len(txt) == 0:  # Si la clé est un diviseur de la chaine de caractère.
        for i in range(0, len(a) % len(list_cle) - 1):
            list_cle = list(cle) + list_cle
    else:
        for i in range(0, len(a) // len(list_cle) - 2):  # Si la clé est plus petite que la chaine de caractère.
            list_cle = list(cle) + list_cle[0:len(txt) % len(list_cle)]
    list_cle = list_cle + list(cle[0:len(a) % len(list_cle)])
    for i in range(0, len(txt)):
        if i >= 26:  # Si l'élément recherché dans la liste l est plus grand que la longueur de la liste.
            index_input = l.index(txt[i % 26]) + l.index(str(list_cle[i]))
            index_output = l[index_input] + index_output
        else:
            index_input = l.index(txt[i]) + l.index(str(list_cle[i]))
            index_output = l[index_input % 26] + index_output
    print("".join(reversed(index_output)))

def decryptage(a: str, cle: str):
    txt = list(a)  # Transforme les arguments en liste
    list_cle = list(cle)  #
    index_output = ''
    if len(list_cle) // len(txt) == 0:  # Si la clé est un diviseur de la chaine de caractère.
        for i in range(0, len(a) % len(list_cle) - 1):
            list_cle = list(cle) + list_cle
    else:
        for i in range(0, len(a) // len(list_cle) - 2):  # Si la clé est plus petite que la chaine de caractère.
            list_cle = list(cle) + list_cle[0:len(txt) % len(list_cle)]
    list_cle = list_cle + list(cle[0:len(a) % len(list_cle)])
    for i in range(0, len(txt)):
        if i >= 26:  # Si l'élément recherché dans la liste l est plus grand que la longueur de la liste.
            index_input = l.index(txt[i % 26]) - l.index(str(list_cle[i]))
            index_output = l[index_input] + index_output
        else:
            index_input = l.index(txt[i]) - l.index(str(list_cle[i]))
            index_output = l[index_input % 26] + index_output
    print("".join(reversed(index_output)))

"""
Fonctions qui génèrent les sous chaines de caratères
en déterminant pour chaqune d'elles 
"""

def IC1(a:int):
    str = ""
    sous_chaine = []
    for i in range(0,len(a)):
        str = str + a[i]
    sous_chaine.append(str)
    return sous_chaine

def IC2(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,2):
        for i in range(j,len(a),2):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC3(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,3):
        for i in range(j,len(a),3):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC4(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,4):
        for i in range(j,len(a),4):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC5(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,5):
        for i in range(j,len(a),5):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC6(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,6):
        for i in range(j,len(a),6):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC7(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,7):
        for i in range(j,len(a),7):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC8(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,8):
        for i in range(j,len(a),8):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def sous_chaines(chaine,k):
    str = ""
    sous_chaine = []
    for j in range(0, k):
        for i in range(j, len(chaine), k):
            str = str + chaine[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC9(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,9):
        for i in range(j,len(a),9):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC10(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,10):
        for i in range(j,len(a),10):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC11(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,11):
        for i in range(j,len(a),11):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

def IC12(a:int):
    str = ""
    sous_chaine = []
    for j in range(0,12):
        for i in range(j,len(a),12):
            str = str + a[i]
        sous_chaine.append(str)
        str = ""
    return sous_chaine

"""
Fonction qui génère la liste contenant les sous chaines pour un nombre d'indice donné
Autrement dit, la fonction prend en argument i; qui est le nombre de sous chaines que
l'on veut calculer. /!\ i ne peut pas être supérieur à 12
Autrement dit, la longueur de la clé ne doit pas dépasser 12 caractères
Elle prend aussi en argument a, qui est le texte à décrypter.
"""
def gen_IC(a:str,i:int):

    l_IC = [IC1(a),IC2(a),IC3(a),IC4(a),IC5(a),IC6(a),IC7(a),IC8(a),IC9(a),IC10(a),IC11(a),IC12(a)]
    l_sous_chaines = []
    for k in range(0,i):
        l_sous_chaines.append(l_IC[k])
    return l_sous_chaines

"""
Fonction qui crée un liste qui retourne le nombre de fois
qu'une lettre est dans le texte pour chaque d'elles
Ne prend en argument que des chaines de caratères
"""
def nq(a:str):
    alphab_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for element in a:
        for i in range(0, len(l)):
            if element == l[i]:
                alphab_num[i] = alphab_num[i] + 1
    return alphab_num

"""
Fonction qui compare les moyennes des IC et les compare à celui du français
et retourne uniquement l'IC le plus proche de celui du français
"""
def choice_IC(l_IC:list)->float:
    IC_fr = 0.0778

    global compare
    compare = l_IC[0]
    for i in range(1,len(l_IC)):
        if abs(l_IC[i] - 0.0778) < compare:
            compare = l_IC[i]
    return compare

"""
Calcule l'indice de coincidence du texte à partir du nombre de fois ou chaque lettres apparaissent dans le texte
puis fait la moyenne des indices de coîcidence de chaque sous_chaines 
"""
def calcul_IC(a:str,i:int):
    char = ""
    final_list = []
    l_moy = []

    # Calcul des IC

    l_nq = []
    l_nq = nq(gen_IC(a,i))
    for k in range(0,i):
        for element in l_nq[k]:
            l_IC.append((element*(element-1))/(len(a))*(len(nq(a))-1))
        final_list.append(l_IC)

    # Calcul des moyennes des IC

    for k in range(0, len(final_list)):
        count = 0
        for i in range(0, len(final_list[k])):
            count = count + final_list[k][i]
        l_moy.append(count / len(final_list[k]))

    choice_IC(l_moy)
    print(l_moy)
    print(choice_IC(l_moy))
    print(l)
    print(l_char)

"""
Fonction qui détermine la longueur de la clé 
"""
def lenght_key(a: str):
    key = ""
    l_ic = []
    l_ic.append(calcul_IC(a))


    return key

"""
Fonction qui retourne un graphique mettant en évidence les indices de coincidence calculés et celui du francçais
"""

def graphic():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = calcul_IC("ahuirrieyrereuyerayuearyeruyearyrereareerhththtrz", 12)[1]
    y.append(0.0778)
    plt.title("Courbe représentant les Indices de Coîcidence calculés et celui du français")
    plt.xlabel("Indices de Coîncidence")
    plt.ylabel("Moyenne des Indices de Coîcidence")
    plt.bar(x, y, width=0.1, color='r')
    plt.show()

def decryptage_auto(t:str):
    decryptage(t,lenght_key(t))

#gen_IC("abcdefghijklmopqrstuvwxyz",12)
#calcul_IC("nuitperduejesortaisduntheatreoutouslessoirsjeparaissaisauxavantscenesengrandetenuedesoupirantquelquefoistoutetaitpleinquelquefoistoutetaitvidepeumimportaitdarretermesregardssurunparterrepeupleseulementdunetrentainedamateursforcessurdeslogesgarniesdebonnetsoudetoilettessuranneesoubiendefairepartiedunesalleanimeeetfremissantecouronneeatoussesetagesdetoilettesfleuriesdebijouxetincelantsetdevisagesradieuxindifferentauspectacledelasalleceluidutheatrenemarretaitguereexceptelorsqualasecondeoualatroisiemescenedunmaussadechefdoeuvredalorsuneapparitionbienconnueilluminaitlespaceviderendantlaviedunsouffleetdunmotacesvainesfiguresquimentouraientjemesentaisvivreenelleetellevivaitpourmoiseulsonsouriremeremplissaitdunebeatitudeinfinielavibrationdesavoixsidouceetcependantfortementtimbreemefaisaittressaillirdejoieetdamourelleavaitpourmoitouteslesperfectionsellerepondaitatousmesenthousiasmesatousmescapricesbellecommelejourauxfeuxdelarampequileclairaitdenbaspalecommelanuitquandlarampebaisseelalaissaiteclaireedenhautsouslesrayonsdulustreetlamontraitplusnaturellebrillantdanslombredesaseulebeautecommelesheuresdivinesquisedecoupentavecuneetoileaufrontsurlesfondsbrunsdesfresquesdherculanumdepuisunanjenavaispasencoresongeaminformerdecequellepouvaitetredailleursjecraignaisdetroublerlemiroirmagiquequimerenvoyaitsonimageettoutauplusavaisjepreteloreilleaquelquesproposconcernantnonpluslactricemaislafemmejemeninformaisaussipeuquedesbruitsquiontpucourirsurlaprincessedelideousurlareinedetrebizondeundemesonclesquiavaitvecudanslesavantdernieresanneesduxviiiesieclecommeilfallaityvivrepourlebienconnaitremayantprevenudebonneheurequelesactricesnetaientpasdesfemmesetquelanatureavaitoubliedeleurfaireuncoeurilparlaitdecellesdecetempslasansdoutemaisilmavaitracontetantdhistoiresdesesillusionsdesesdeceptionsetmontretantdeportraitssurivoiremedaillonscharmantsquilutilisaitdepuisaparerdestabatierestantdebilletsjaunistantdefaveursfaneesenmenfaisantlhistoireetlecomptedefinitifquejemetaishabitueapensermaldetoutessanstenircomptedelordredestempsnousvivionsalorsdansuneepoqueetrangecommecellesquidordinairesuccedentauxrevolutionsouauxabaissementsdesgrandsregnescenetaitpluslagalanterieheroiquecommesouslafrondeleviceelegantetparecommesouslaregencelescepticismeetlesfollesorgiesdudirectoirecetaitunmelangedactivitedhesitationetdeparessedutopiesbrillantesdaspirationsphilosophiquesoureligieusesdenthousiasmesvaguesmelesdecertainsinstinctsderenaissancedennuisdesdiscordespasseesdespoirsincertainsquelquechosecommelepoquedeperegrinusetdapuleelhommematerielaspiraitaubouquetderosesquidevaitleregenererparlesmainsdelabelleisisladeesseeternellementjeuneetpurenousapparaissaitdanslesnuitsetnousfaisaithontedenosheuresdejourperdueslambitionnetaitcependantpasdenotreageetlavidecureequisefaisaitalorsdespositionsetdeshonneursnouseloignaitdesspheresdactivitepossiblesilnenousrestaitpourasilequecettetourdivoiredespoetesounousmontionstoujoursplushautpournousisolerdelafouleacespointselevesounousguidaientnosmaitresnousrespirionsenfinlairpurdessolitudesnousbuvionsloublidanslacoupedordeslegendesnousetionsivresdepoesieetdamouramourhelasdesformesvaguesdesteintesrosesetbleuesdesfantomesmetaphysiquesvuedepreslafemmereellerevoltaitnotreingenuiteilfallaitquelleapparutreineoudeesseetsurtoutnenpasapprocherquelquesunsdentrenousneanmoinsprisaientpeucesparadoxesplatoniquesetatraversnosrevesrenouvelesdalexandrieagitaientparfoislatorchedesdieuxsouterrainsquieclairelombreuninstantdesestraineesdetincellescestainsiquesortantdutheatreaveclameretristessequelaisseunsongeevanouijallaisvolontiersmejoindrealasocieteduncercleoulonsoupaitengrandnombreetoutoutemelancoliecedaitdevantlaverveintarissabledequelquesespritseclatantsvifsorageuxsublimesparfoistelsquilsenesttrouvetoujoursdanslesepoquesderenovationoudedecadenceetdontlesdiscussionssehaussaientacepointquelesplustimidesdentrenousallaientvoirparfoisauxfenetressileshunslesturcomansoulescosaquesnarrivaientpasenfinpourcoupercourtacesargumentsderheteursetdesophistesbuvonsaimonscestlasagessetelleetaitlaseuleopiniondesplusjeunesundeceuxlameditvoicibienlongtempsquejeterencontredanslememetheatreetchaquefoisquejyvaispourlaquelleyvienstupourlaquelleilnemesemblaitpasquelonputallerlapouruneautrecependantjavouaiunnomehbienditmonamiavecindulgencetuvoislabaslhommeheureuxquivientdelareconduireetquifideleauxloisdenotrecercleniralaretrouverpeutetrequapreslanuitsanstropdemotionjetournailesyeuxverslepersonnageindiquecetaitunjeunehommecorrectementvetudunefigurepaleetnerveuseayantdesmanieresconvenablesetdesyeuxempreintsdemelancolieetdedouceuriljetaitdelorsurunetabledewhistetleperdaitavecindifferencequemimportedisjeluioutoutautreilfallaitquilyeneutunetceluilameparaitdignedavoiretechoisiettoimoicestuneimagequejepoursuisriendeplusensortantjepassaiparlasalledelectureetmachinalementjeregardaiunjournalcetaitjecroispouryvoirlecoursdelaboursedanslesdebrisdemonopulencesetrouvaitunesommeassezforteentitresetrangerslebruitavaitcouruquenegligeslongtempsilsallaientetrereconnuscequivenaitdavoirlieualasuitedunchangementdeministerelesfondssetrouvaientdejacotestreshautjeredevenaisricheuneseulepenseeresultadecechangementdesituationcellequelafemmeaimeesilongtempsetaitamoisijevoulaisjetouchaisdudoigtmonidealnetaitcepasuneillusionencoreunefautedimpressionrailleusemaislesautresfeuillesparlaientdememelasommegagneesedressaitdevantmoicommelastatuedordemolochquediraitmaintenantpensaijelejeunehommedetoutalheuresijallaisprendresaplacepresdelafemmequilalaisseeseulejefremisdecettepenseeetmonorgueilserevoltanoncenestpasainsicenestpasamonagequelontuelamouravecdelorjeneseraipasuncorrupteurdailleursceciestuneideedunautretempsquimeditaussiquecettefemmesoitvenalemonregardparcouraitvaguementlejournalquejetenaisencoreetjyluscesdeuxlignesfetedubouquetprovincialdemainlesarchersdesenlisdoiventrendrelebouquetaceuxdeloisycesmotsfortsimplesreveillerentenmoitouteunenouvelleseriedimpressionscetaitunsouvenirdelaprovincedepuislongtempsoublieeunecholointaindesfetesnaivesdelajeunesselecoretletambourresonnaientauloindansleshameauxetdanslesboislesjeunesfillestressaientdesguirlandesetassortissaientenchantantdesbouquetsornesderubansunlourdchariottrainepardesboeufsrecevaitcespresentssursonpassageetnousenfantsdecescontreesnousformionscortegeavecnosarcsetnosflechesnousdecorantdutitredechevalierssanssavoiralorsquenousnefaisionsquerepeterdageenageunefetedruidiquesurvivantauxmonarchiesetauxreligionsnouvellesadriennejeregagnaimonlitetjenepusytrouverlereposplongedansunedemisomnolencetoutemajeunesserepassaitenmessouvenirscetetatoulespritresisteencoreauxbizarrescombinaisonsdusongepermetsouventdevoirsepresserenquelquesminuteslestableauxlesplussaillantsdunelongueperiodedelaviejemerepresentaisunchateaudutempsdehenriivavecsestoitspointuscouvertsdardoisesetsafacerougeatreauxencoignuresdenteleesdepierresjauniesunegrandeplaceverteencadreedormesetdetilleulsdontlesoleilcouchantperçaitlefeuillagedesestraitsenflammesdesjeunesfillesdansaientenrondsurlapelouseenchantantdevieuxairstransmisparleursmeresetdunfrançaissinaturellementpurquelonsesentaitbienexisterdanscevieuxpaysduvaloisoupendantplusdemilleansabattulecoeurdelafrancejetaisleseulgarçondanscetterondeoujavaisamenemacompagnetoutejeuneencoresylvieunepetitefilleduhameauvoisinsiviveetsifraicheavecsesyeuxnoirssonprofilregulieretsapeaulegerementhaleejenaimaisquellejenevoyaisquellejusquelaapeineavaisjeremarquedanslarondeounousdansionsuneblondegrandeetbellequonappelaitadriennetoutduncoupsuivantlesreglesdeladanseadriennesetrouvaplaceeseuleavecmoiaumilieuducerclenostaillesetaientpareillesonnousditdenousembrasseretladanseetlechoeurtournaientplusvivementquejamaisenluidonnantcebaiserjenepusmempecherdeluipresserlamainleslongsanneauxroulesdesescheveuxdoreffleuraientmesjouesdecemomentuntroubleinconnusemparademoilabelledevaitchanterpouravoirledroitderentrerdansladanseonsassitautourdelleetaussitotdunevoixfraicheetpenetrantelegerementvoileecommecelledesfillesdecepaysbrumeuxellechantaunedecesanciennesromancespleinesdemelancolieetdamourquiracontenttoujourslesmalheursduneprincesseenfermeedanssatourparlavolontedunperequilapunitdavoiraimelamelodieseterminaitachaquestanceparcestrilleschevrotantsquefontvaloirsibienlesvoixjeunesquandellesimitentparunfrissonmodulelavoixtremblantedesaieulesamesurequellechantaitlombredescendaitdesgrandsarbresetleclairdelunenaissanttombaitsurelleseuleisoleedenotrecercleattentifellesetutetpersonnenosaromprelesilencelapelouseetaitcouvertedefaiblesvapeurscondenseesquideroulaientleursblancsfloconssurlespointesdesherbesnouspensionsetreenparadisjemelevaienfincourantauparterreduchateauousetrouvaientdelauriersplantesdansdegrandsvasesdefaiencepeintsencamaieujerapportaideuxbranchesquifurenttresseesencouronneetnoueesdunrubanjeposaisurlatetedadriennecetornementdontlesfeuilleslustreeseclataientsursescheveuxblondsauxrayonspalesdelaluneelleressemblaitalabeatricededantequisouritaupoeteerrantsurlalisieredessaintesdemeuresadrienneselevadeveloppantsatailleelanceeellenousfitunsalutgracieuxetrentraencourantdanslechateaucetaitnousditonlapetitefilledelundesdescendantsdunefamilleallieeauxanciensroisdefrancelesangdesvaloiscoulaitdanssesveinespourcejourdefeteonluiavaitpermisdesemeleranosjeuxnousnedevionspluslarevoircarlelendemainellerepartitpouruncouventouelleetaitpensionnairequandjerevinspresdesylviejemaperçusquellepleuraitlacouronnedonneeparmesmainsalabellechanteuseetaitlesujetdeseslarmesjeluioffrisdenallercueilliruneautremaiselleditquellenytenaitnullementnelameritantpasjevoulusenvainmedefendreellenemeditplusunseulmotpendantquejelareconduisaischezsesparentsrappelemoimemeaparispouryreprendremesetudesjemportaicettedoubleimageduneamitietendretristementrompuepuisdunamourimpossibleetvaguesourcedepenseesdouloureusesquelaphilosophiedecollegeetaitimpuissanteacalmerlafiguredadriennerestaseuletriomphantemiragedelagloireetdelabeauteadoucissantoupartageantlesheuresdesseveresetudesauxvacancesdelanneesuivantejapprisquecettebelleapeineentrevueetaitconsacreeparsafamillealaviereligieuseresolutiontoutmetaitexpliqueparcesouvenirademirevecetamourvagueetsansespoirconçupourunefemmedetheatrequitouslessoirsmeprenaitalheureduspectaclepournemequitterqualheuredusommeilavaitsongermedanslesouvenirdadriennefleurdelanuiteclosealapaleclartedelalunefantomeroseetblondglissantsurlherbeverteademibaigneedeblanchesvapeurslaressemblancedunefigureoublieedepuisdesanneessedessinaitdesormaisavecunenettetesingulierecetaituncrayonestompeparletempsquisefaisaitpeinturecommecesvieuxcroquisdemaitresadmiresdansunmuseedontonretrouveailleursloriginaleblouissantaimerunereligieusesouslaformeduneactriceetsicetaitlamemeilyadequoidevenirfoucestunentrainementfataloulinconnuvousattirecommelefeufolletfuyantsurlesjoncsduneeaumortereprenonspiedsurlereeletsylviequejaimaistantpourquoilaijeoublieedepuistroisanscetaitunebienjoliefilleetlaplusbelledeloisyelleexisteellebonneetpuredecoeursansdoutejerevoissafenetreoulepampresenlaceaurosierlacagedefauvettessuspendueagauchejentendslebruitdesesfuseauxsonoresetsachansonfavoritelabelleetaitassisepresduruisseaucoulantellemattendencorequilauraitepouseeelleestsipauvredanssonvillageetdansceuxquilentourentdebonspaysansenblouseauxmainsrudesalafaceamaigrieauteinthaleellemaimaitseulmoilepetitparisienquandjallaisvoirpresdeloisymonpauvreonclemortaujourdhuidepuistroisansjedissipeenseigneurlebienmodestequilmalaisseetquipouvaitsuffireamavieavecsylviejelauraisconservelehasardmenrendunepartieilesttempsencoreacetteheurequefaitelleelledortnonellenedortpascestaujourdhuilafetedelarclaseuledelanneeoulondansetoutelanuitelleestalafetequelleheureestiljenavaispasdemontreaumilieudetouteslessplendeursdebricabracquiletaitdusagedereuniracetteepoquepourrestaurerdanssacouleurlocaleunappartementdautrefoisbrillaitduneclatrafraichiunedecespendulesdecailledelarenaissancedontledomedoresurmontedelafiguredutempsestsupportepardescariatidesdustylemedicisreposantaleurtoursurdeschevauxademicabresladianehistoriqueaccoudeesursoncerfestenbasreliefsouslecadranousetalentsurunfondnielleleschiffresemaillesdesheureslemouvementexcellentsansdoutenavaitpaseteremontedepuisdeuxsieclescenetaitpaspoursavoirlheurequejavaisachetecettependuleentourainejedescendischezleconciergesoncoucoumarquaituneheuredumatinenquatreheuresmedisjejepuisarriveraubaldeloisyilyavaitencoresurlaplacedupalaisroyalcinqousixfiacresstationnantpourleshabituesdescerclesetdesmaisonsdejeualoisydisjeauplusapparentoucelaestilpresdesenlisahuitlieuesjevaisvousconduirealaposteditlecochermoinspreoccupequemoiquelletristeroutelanuitquecetteroutedeflandrequinedevientbellequenatteignantlazonedesforetstoujourscesdeuxfilesdarbresmonotonesquigrimacentdesformesvaguesaudeladescarresdeverdureetdeterresremueesbornesagaucheparlescollinesbleuatresdemontmorencydecouendeluzarchesvoicigonesselebourgvulgairepleindessouvenirsdelaligueetdelafrondeplusloinquelouvresestuncheminbordedepommiersdontjaivubiendesfoislesfleurseclaterdanslanuitcommedesetoilesdelaterrecetaitlepluscourtpourgagnerleshameauxpendantquelavoituremontelescotesrecomposonslessouvenirsdutempsoujyvenaissisouventunvoyageacytherequelquesanneessetaientecouleeslepoqueoujavaisrencontreadriennedevantlechateaunetaitplusdejaquunsouvenirdenfancejemeretrouvaialoisyaumomentdelafetepatronalejallaidenouveaumejoindreauxchevaliersdelarcprenantplacedanslacompagniedontjavaisfaitpartiedejadesjeunesgensappartenantauxvieillesfamillesquipossedentencorelaplusieursdeceschateauxperdusdanslesforetsquiontplussouffertdutempsquedesrevolutionsavaientorganiselafetedechantillydecompiegneetdesenlisaccouraientdejoyeusescavalcadesquiprenaientplacedanslecortegerustiquedescompagniesdelarcapreslalonguepromenadeatraverslesvillagesetlesbourgsapreslamessealegliselesluttesdadresseetladistributiondesprixlesvainqueursavaienteteconviesaunrepasquisedonnaitdansuneileombrageedepeupliersetdetilleulsaumilieudelundesetangsalimentesparlanonetteetlathevedesbarquespavoiseesnousconduisirentaliledontlechoixavaitetedetermineparlexistenceduntempleovaleacolonnesquidevaitservirdesallepourlefestinlacommeaermenonvillelepaysestsemedecesedificeslegersdelafinduxviiiesiecleoudesmillionnairesphilosophessesontinspiresdansleursplansdugoutdominantdalorsjecroisbienquecetempleavaitduetreprimitivementdedieauranietroiscolonnesavaientsuccombeemportantdansleurchuteunepartiedelarchitravemaisonavaitdeblayelinterieurdelasallesuspendudesguirlandesentrelescolonnesonavaitrajeunicetteruinemodernequiappartenaitaupaganismedeboufflersoudechaulieuplutotquaceluidhoracelatraverseedulacavaiteteimagineepeutetrepourrappelerlevoyageacytheredewatteaunoscostumesmodernesderangeaientseulslillusionlimmensebouquetdelafeteenleveducharquileportaitavaiteteplacesurunegrandebarquelecortegedesjeunesfillesvetuesdeblancquilaccompagnentselonlusageavaitprisplacesurlesbancsetcettegracieusetheorierenouveleedesjoursantiquesserefletaitdansleseauxcalmesdeletangquilaseparaitduborddelilesivermeilauxrayonsdusoiravecseshalliersdepinesacolonnadeetsesclairsfeuillagestouteslesbarquesaborderentenpeudetempslacorbeilleporteeenceremonieoccupalecentredelatableetchacunpritplacelesplusfavorisesaupresdesjeunesfillesilsuffisaitpourceladetreconnudeleursparentscefutlacausequifitquejemeretrouvaipresdesylviesonfreremavaitdejarejointdanslafeteilmefitlaguerredenavoirpasdepuislongtempsrenduvisiteasafamillejemexcusaisurmesetudesquimeretenaientaparisetlassuraiquejetaisvenudanscetteintentionnoncestmoiquilaoublieeditsylvienoussommesdesgensdevillageetparisestsiaudessusjevouluslembrasserpourluifermerlabouchemaisellemeboudaitencoreetilfallutquesonfrereintervintpourquellemoffritsajouedunairindifferentjeneusaucunejoiedecebaiserdontbiendautresobtenaientlafaveurcardanscepayspatriarcaloulonsaluetouthommequipasseunbaisernestautrechosequunepolitesseentrebonnesgensunesurpriseavaitetearrangeeparlesordonnateursdelafetealafindurepasonvitsenvolerdufonddelavastecorbeilleuncygnesauvagejusquelacaptifsouslesfleursquidesesfortesailessoulevantdeslacisdeguirlandesetdecouronnesfinitparlesdisperserdetouscotespendantquilselançaitjoyeuxverslesderniereslueursdusoleilnousrattrapionsauhasardlescouronnesdontchacunparaitaussitotlefrontdesavoisinejeuslebonheurdesaisirunedesplusbellesetsylviesourianteselaissaembrassercettefoisplustendrementquelautrejecomprisquejeffaçaisainsilesouvenirdunautretempsjeladmiraicettefoissanspartageelleetaitdevenuesibellecenetaitpluscettepetitefilledevillagequejavaisdedaigneepouruneplusgrandeetplusfaiteauxgracesdumondetoutenelleavaitgagnelecharmedesesyeuxnoirssiseduisantsdessonenfanceetaitdevenuirresistiblesouslorbitearqueedesessourcilssonsourireeclairanttoutacoupdestraitsreguliersetplacidesavaitquelquechosedathenienjadmiraiscettephysionomiedignedelartantiqueaumilieudesminoischiffonnesdesescompagnessesmainsdelicatementallongeessesbrasquiavaientblanchiensarrondissantsatailledegageelafaisaienttoutautrequejenelavaisvuejenepusmempecherdeluidirecombienjelatrouvaisdifferentedellememeesperantcouvrirainsimonancienneetrapideinfidelitetoutmefavorisaitdailleurslamitiedesonfrerelimpressioncharmantedecettefetelheuredusoiretlelieumemeouparunefantaisiepleinedegoutonavaitreproduituneimagedesgalantessolennitesdautrefoistantquenouspouvionsnousechappionsaladansepourcauserdenossouvenirsdenfanceetpouradmirerenrevantadeuxlesrefletsducielsurlesombragesetsurleseauxilfallutquelefreredesylvienousarrachatacettecontemplationendisantquiletaittempsderetournerauvillageassezeloignequhabitaientsesparentslevillagecetaitaloisydanslanciennemaisondugardejelesconduisisjusquelapuisjeretournaiamontagnyoujedemeuraischezmononcleenquittantlecheminpourtraverserunpetitboisquisepareloisydesaintsjenetardaipasamengagerdansunesenteprofondequilongelaforetdermenonvillejemattendaisensuitearencontrerlesmursduncouventquilfallaitsuivrependantunquartdelieuelalunesecachaitdetempsaautresouslesnuageseclairantapeinelesrochesdegressombreetlesbruyeresquisemultipliaientsousmespasadroiteetagauchedeslisieresdeforetssansroutestraceesettoujoursdevantmoicesrochesdruidiquesdelacontreequigardentlesouvenirdesfilsdarmenexterminesparlesromainsduhautdecesentassementssublimesjevoyaislesetangslointainssedecoupercommedesmiroirssurlaplainebrumeusesanspouvoirdistinguerceluimemeousetaitpasseelafetelairetaittiedeetembaumejeresolusdenepasallerplusloinetdattendrelematinenmecouchantsurdestouffesdebruyeresenmereveillantjereconnuspeuapeulespointsvoisinsdulieuoujemetaisegaredanslanuitamagauchejevissedessinerlalonguelignedesmursducouventdesaintspuisdelautrecotedelavalleelabutteauxgensdarmesaveclesruinesebrecheesdelantiqueresidencecarlovingiennepresdelaaudessusdestouffesdeboisleshautesmasuresdelabbayedethiersdecoupaientsurlhorizonleurspansdemuraillepercesdetreflesetdogivesaudelalemanoirgothiquedepontarmeentouredeaucommeautrefoisrefletabientotlespremiersfeuxdujourtandisquonvoyaitsedresseraumidilehautdonjondelatournelleetlesquatretoursdebertrandfossesurlespremierscoteauxdemontmeliantcettenuitmavaitetedouceetjenesongeaisquasylviecependantlaspectducouventmedonnauninstantlideequecetaitceluipeutetrequhabitaitadrienneletintementdelaclochedumatinetaitencoredansmonoreilleetmavaitsansdoutereveillejeusuninstantlideedejeteruncoupdoeilpardessuslesmursengravissantlaplushautepointedesrochersmaisenyreflechissantjemengardaicommeduneprofanationlejourengrandissantchassademapenseecevainsouveniretnylaissaplusquelestraitsrosesdesylvieallonslareveillermedisjeetjereprislechemindeloisyvoicilevillageauboutdelasentequicotoielaforetvingtchaumieresdontlavigneetlesrosesgrimpantesfestonnentlesmursdesfileusesmatinalescoiffeesdemouchoirsrougestravaillentreuniesdevantunefermesylvienestpointavecellescestpresqueunedemoiselledepuisquelleexecutedefinesdentellestandisquesesparentssontrestesdebonsvillageoisjesuismonteasachambresansetonnerpersonnedejaleveedepuislongtempselleagitaitlesfuseauxdesadentellequiclaquaientavecundouxbruitsurlecarreauvertquesoutenaientsesgenouxvousvoilaparesseuxditelleavecsonsouriredivinjesuissurequevoussortezseulementdevotrelitjeluiracontaimanuitpasseesanssommeilmescoursesegareesatraverslesboisetlesrochesellevoulutbienmeplaindreuninstantsivousnetespasfatiguejevaisvousfairecourirencorenousironsvoirmagrandtanteaothysjavaisapeinereponduquelleselevajoyeusementarrangeasescheveuxdevantunmiroiretsecoiffadunchapeaudepaillerustiquelinnocenceetlajoieeclataientdanssesyeuxnouspartimesensuivantlesbordsdelatheveatraverslespressemesdemargueritesetdeboutonsdorpuislelongdesboisdesaintlaurentfranchissantparfoislesruisseauxetleshallierspourabregerlaroutelesmerlessifflaientdanslesarbresetlesmesangessechappaientjoyeusementdesbuissonsfrolesparnotremarcheparfoisnousrencontrionssousnospaslespervenchessicheresarousseauouvrantleurscorollesbleuesparmiceslongsrameauxdefeuillesaccoupleeslianesmodestesquiarretaientlespiedsfurtifsdemacompagneindifferenteauxsouvenirsduphilosophegenevoisellecherchaitçaetlalesfraisesparfumeesetmoijeluiparlaisdelanouvelleheloisedontjerecitaisparcoeurquelquespassagesestcequecestjoliditellecestsublimeestcemieuxquaugustelafontainecestplustendreohbienditelleilfautquejelisecelajediraiamonfreredemelapporterlapremierefoisquiliraasenlisetjecontinuaisareciterdesfragmentsdelheloisependantquesylviecueillaitdesfraisesothysausortirduboisnousrencontramesdegrandestouffesdedigitalepourpreeelleenfitunenormebouquetenmedisantcestpourmatanteelleserasiheureusedavoircesbellesfleursdanssachambrenousnavionsplusquunboutdeplaineatraverserpourgagnerothysleclocherduvillagepointaitsurlescoteauxbleuatresquivontdemontmeliantadammartinlathevebruissaitdenouveauparmilesgresetlescaillouxsamincissantauvoisinagedesasourceouellesereposedanslespresformantunpetitlacaumilieudesglaieulsetdesirisbientotnousgagnameslespremieresmaisonslatantedesylviehabitaitunepetitechaumierebatieenpierresdegresinegalesquerevetaientdestreillagesdehoublonetdevigneviergeellevivaitseuledequelquescarresdeterrequelesgensduvillagecultivaientpourelledepuislamortdesonmarisaniecearrivantcetaitlefeudanslamaisonbonjourlatantevoicivosenfantsditsylvienousavonsbienfaimellelembrassatendrementluimitdanslesbraslabottedefleurspuissongeaenfinamepresenterendisantcestmonamoureuxjembrassaiamontourlatantequiditilestgentilcestdoncunblondiladejolischeveuxfinsditsylviecelanedurepasditlatantemaisvousavezdutempsdevantvousettoiquiesbrunecelatassortitbienilfautlefairedejeunerlatanteditsylvieetelleallacherchantdanslesarmoiresdanslahuchetrouvantdulaitdupainbisdusucreetalantsanstropdesoinsurlatablelesassiettesetlesplatsdefaienceemaillesdelargesfleursetdecoqsauvifplumageunejatteenporcelainedecreilpleinedelaitounageaientlesfraisesdevintlecentreduserviceetapresavoirdepouillelejardindequelquespoigneesdecerisesetdegroseilleselledisposadeuxvasesdefleursauxdeuxboutsdelanappemaislatanteavaitditcesbellesparolestoutcelacenestquedudessertilfautmelaisserfaireapresentetelleavaitdecrochelapoeleetjeteunfagotdanslahautechemineejeneveuxpasquetutouchesaceladitelleasylviequivoulaitlaiderabimertesjolisdoigtsquifontdeladentelleplusbellequachantillytumenasdonneetjemyconnaisahouilatanteditesdoncsivousenavezdesmorceauxdelanciennecelameferadesmodelesehbienvavoirlahautditlatanteilyenapeutetredansmacommodedonnezmoilesclefsrepritsylviebahditlatantelestiroirssontouvertscenestpasvraiilyenaunquiesttoujoursfermeetpendantquelabonnefemmenettoyaitlapoeleapreslavoirpasseeaufeusylviedenouaitdespendantsdesaceintureunepetiteclefdunacierouvragequellemefitvoiravectriomphejelasuivismontantrapidementlescalierdeboisquiconduisaitalachambreojeunesseovieillessesaintesquidonceutsongeaternirlapuretedunpremieramourdanscesanctuairedessouvenirsfidelesleportraitdunjeunehommedubonvieuxtempssouriaitavecsesyeuxnoirsetsaboucherosedansunovaleaucadredoresuspendualatetedulitrustiqueilportaitluniformedesgardeschassedelamaisondecondesonattitudeademimartialesafigureroseetbienveillantesonfrontpursoussescheveuxpoudresrelevaientcepastelmediocrepeutetredesgracesdelajeunesseetdelasimplicitequelqueartistemodesteinviteauxchassesprincieressetaitappliquealepourtrairedesonmieuxainsiquesajeuneepousequonvoyaitdansunautremedaillonattrayantemaligneelanceedanssoncorsageouvertaechellederubansagaçantdesamineretrousseeunoiseauposesursondoigtcetaitpourtantlamemebonnevieillequicuisinaitencemomentcourbeesurlefeudelatrecelamefitpenserauxfeesdesfunambulesquicachentsousleurmasquerideunvisageattrayantquellesrevelentaudenouementlorsqueapparaitletempledelamouretsonsoleiltournantquirayonnedefeuxmagiquesobonnetantemecriaijequevousetiezjolieetmoidoncditsylviequietaitparvenueaouvrirlefameuxtiroirelleyavaittrouveunegranderobeentaffetasflambequicriaitdufroissementdesesplisjeveuxessayersicelamiraditelleahjevaisavoirlairdunevieillefeelafeedeslegendeseternellementjeunedisjeenmoimemeetdejasylvieavaitdegrafesarobedindienneetlalaissaittomberasespiedslarobeetoffeedelavieilletantesajustaparfaitementsurlataillemincedesylviequimeditdelagraferohlesmanchesplatesquecestridiculeditelleetcependantlessabotsgarnisdedentellesdecouvraientadmirablementsesbrasnuslagorgesencadraitdanslepurcorsageauxtullesjaunisauxrubanspassesquinavaitserrequebienpeulescharmesevanouisdelatantemaisfinissezenvousnesavezdoncpasagraferunerobemedisaitsylvieelleavaitlairdelaccordeedevillagedegreuzeilfaudraitdelapoudredisje",12)
calcul_IC("abcdefghijklmonpqrstuvwxyz",12)
#decryptage_auto("abcdefghijklmnopqrstu")
#cryptage("aaa", "sembat")
#decryptage("upmtsxhvqqamkm", "sembat")
#lenght_key("abcdefghi")
#decryptage('abcdefghi')
#choice_IC([1,156,51123,484656,565,0.1,0.56,0.01,0.02,0.078,0.02,1,5,5,5,6,0.07,0.07,2,0.0778])
#IC1("abcdefghijklmopqrstuvwxyz")
#IC2("abcdefghijklmopqrstuvwxyz")
#IC3("abcdefghijklmopqrstuvwxyz")
#IC4("abcdefghijklmopqrstuvwxyz")
#IC5("abcdefghijklmopqrstuvwxyz")
#IC6("abcdefghijklmopqrstuvwxyz")
#IC7("abcdefghijklmopqrstuvwxyz")
#IC8("abcdefghijklmopqrstuvwxyz")
#IC9("abcdefghijklmopqrstuvwxyz")
#IC10("abcdefghijklmopqrstuvwxyz")
#IC11("abcdefghijklmopqrstuvwxyz")
#IC12("abcdefghijklmopqrstuvwxyz")
#conv_character("C'est un long texte un très long texte que je pourrais écrire un long texte pour clore la journée saluer le coucher du soleil un long texte en lieu & place des milliers des millions d'autres très beaux textes et par là j'entends d'autres textes qui seraient très beaux alors que celui-ci n'est qu'un long texte lamentable oui un long texte trop long texte en lieu & place des centaines de textes qu'il me reste à retrouver à recopier à inventer à écrire un long long texte comme une longue fuite en avant la lâcheté de mes commissures un très long texte puisqu'il ne raconte ne dit rien tourne en rond un long texte qui ennuie désarçonne agace surtout agace puisque ce texte est long dès le premier mot il était très long puisque l'auteur en avait décidé ainsi et même s'il s'en était tenu aux quatre premiers d'une certaine façon ce texte eût été long très long trop long long long chemin comme une fuite en avant de lâche bavant des commissures à force de renâcler devant la tâche à force d'ahaner ses longs textes et donc ce très long texte dont je ne sais pourquoi je l'ai commencé si ce n'est pour m'occuper peut-être et dont je sais encore moins comment il finira ni quand il finira lâchement je me défilerai jusqu'à ne pas l'écrire si long que cela puisque j'ai déjà expliqué que ce texte qui ne raconte rien paraîtra toujours long même s'il est très court ce qu'il n'est déjà plus et même s'il est court ce qu'il est encore mais enfin même s'il est de longueur moyenne il sera toujours moins que médiocre et plein de longueurs il est plutôt la longueur et je me languis d'un beau texte d'un très long ou très court texte qui au moins ne serait pas d'une totale vacuité si je dois l'avouer et donc il paraîtra trop long bien trop long et ainsi s'accomplira la prophétie des quatre premiers mots de ce texte décidément très long dont je ne sais comment ni quand il finira si tant est même puisque je n'en sais rien si tant est que puisqu'il est long très long trop long si tant est disais-je avant cette avalanche d'incises que ne marque même pas la moindre parenthèse comme l'on s'est aperçu depuis longtemps que la ponctuation empêchait de se concentrer sur l'écriture preste qui va son cours et donc ce très long texte est très long lui dont je ne sais comment ni quand il finira si tant est même qu'il finisse à moinSans honneur que précaire, sans liberté que provisoire, jusqu’à la découverte du crime ; sans situation qu’instable, comme pour le poète la veille fêté dans tous les salons, applaudi dans tous les théâtres de Londres, chassé le lendemain de tous les garnis sans pouvoir trouver un oreiller où reposer sa tête, tournant la meule comme Samson et disant comme lui : “Les deux sexes mourront chacun de son côté” ; exclus même, hors les jours de grande infortune où le plus grand nombre se rallie autour de la victime, comme les juifs autour de Dreyfus, de la sympathie – parfois de la société – de leurs semblables, auxquels ils donnent le dégoût de voir ce qu’ils sont, dépeint dans un miroir, qui ne les flattant plus, accuse toutes les tares qu’ils n’avaient pas voulu remarquer chez eux-mêmes et qui leur fait comprendre que ce qu’ils appelaient leur amour (et à quoi, en jouant sur le mot, ils avaient, par sens social, annexé tout ce que la poésie, la peinture, la musique, la chevalerie, l’ascétisme, ont pu ajouter à l’amour) découle non d’un idéal de beauté qu’ils ont élu, mais d’une maladie inguérissable ; comme les juifs encore (sauf quelques-uns qui ne veulent fréquenter que ceux de leur race, ont toujours à la bouche les mots rituels et les plaisanteries consacrées) se fuyant les uns les autres, recherchant ceux qui leur sont le plus opposés, qui ne veulent pas d’eux, pardonnant leurs rebuffades, s’enivrant de leurs complaisances ; mais aussi rassemblés à leurs pareils par l’ostracisme qui les frappe, l’opprobre où ils sont tombés, ayant fini par prendre, par une persécution semblable à celle d’Israël, les caractères physiques et moraux d’une race, parfois beaux, souvent affreux, trouvant (malgré toutes les moqueries dont celui qui, plus mêlé, mieux assimilé à la race adverse, est relativement, en apparence, le moins inverti, accable celui qui l’est demeuré davantage), une détente dans la fréquentation de leurs semblables, et même un appui dans leur existence, si bien que, tout en niant qu’ils soient une race (dont le nom est la plus grande injure), ceux qui parviennent à cacher qu’ils en sont, ils les démasquent volontiers, moins pour leur nuire, ce qu’ils ne détestent pas, que pour s’excuser, et allant chercher comme un médecin l’appendicite l’inversion jusque dans l’histoire, ayant plaisir à rappeler que Socrate était l’un d’eux, comme les Israélites disent de Jésus, sans songer qu’il n’y avait pas d’anormaux quand l’homosexualité était la norme, pas d’anti-chrétiens avant le Christ, que l’opprobre seul fait le crime, parce qu’il n’a laissé subsister que ceux qui étaient réfractaires à toute prédication, à tout exemple, à tout châtiment, en vertu d’une disposition innée tellement spéciale qu’elle répugne plus aux autres hommes (encore qu’elle puisse s’accompagner de hautes qualités morales) que de certains vices qui y contredisent comme le vol, la cruauté, la mauvaise foi, mieux compris, donc plus excusés du commun des hommes ; formant une franc-maçonnerie bien plus étendue, plus efficace et moins soupçonnée que celle des loges, car elle repose sur une identité de goûts, de besoins, d’habitudes, de dangers, d’apprentissage, de savoir, de trafic, de glossaire, et dans laquelle les membres mêmes, qui souhaitent de ne pas se connaître, aussitôt se reconnaissent à des signes naturels ou de convention, involontaires ou voulus, qui signalent un de ses semblables au mendiant dans le grand seigneur à qui il ferme la portière de sa voiture, au père dans le fiancé de sa fille, à celui qui avait voulu se guérir, se confesser, qui avait à se défendre, dans le médecin, dans le prêtre, dans l’avocat qu’il est allé trouver; tous obligés à protéger leur secret, mais ayant leur part d’un secret des autres que le reste de l’humanité ne soupçonne pas et qui fait qu’à eux les romans d’aventure les plus invraisemblables semblent vrais, car dans cette vie romanesque, anachronique, l’ambassadeur est ami du forçat : le prince, avec une certaine liberté d’allures que donne l’éducation aristocratique et qu’un petit bourgeois tremblant n’aurait pas en sortant de chez la duchesse, s’en va conférer avec l’apache ; partie réprouvée de la collectivité humaine, mais partie importante, soupçonnée là où elle n’est pas, étalée, insolente, impunie là où elle n’est pas devinée; comptant des adhérents partout, dans le peuple, dans l’armée, dans le temple, au bagne, sur le trône; vivant enfin, du moins un grand nombre, dans l’intimité caressante et dangereuse avec les hommes de l’autre race, les provoquant, jouant avec eux à parler de son vice comme s’il n’était pas sien, jeu qui est rendu facile par l’aveuglement ou la fausseté des autres, jeu qui peut se prolonger des années jusqu’au jour du scandale où ces dompteurs sont dévorés ; jusque-là obligés de cacher leur vie, de détourner leurs regards d’où ils voudraient se fixer, de les fixer sur ce dont ils voudraient se détourner, de changer le genre de bien des adjectifs dans leur vocabulaire, contrainte sociale, légère auprès de la contrainte intérieure que leur vice, ou ce qu’on nomme improprement ainsi, leur impose non plus à l’égard des autres mais d’eux-mêmes, et de façon qu’à eux-mêmes il ne leur paraisse pas un vice.")

print("Execution time :",time.perf_counter(),"second")