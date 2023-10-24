# Exercice 1

## A

>```bsh
>15:48 lasbordes1@IUTINFO-TP-03 ~ $ pwd
>/home/etudiants/lasbordes1
>15:48 lasbordes1@IUTINFO-TP-03 ~ $ date
>mardi 3 octobre 2023, 15:48:46 (UTC+0200)
>15:48 lasbordes1@IUTINFO-TP-03 ~ $ who
>nogueira6 pts/0        2023-10-03 15:46 (164.81.118.73)
>dubrulle3 pts/1        2023-10-03 15:46 (164.81.118.113)
>lajoinie19 pts/2        2023-10-03 15:47 (164.81.118.79)
>ollivier10 pts/3        2023-10-03 15:47 (164.81.118.77)
>anglada2 pts/4        2023-10-03 15:48 (164.81.118.78)
>charpentier55 pts/5        2023-10-03 15:48 (164.81.118.76)
>lasbordes1 pts/6        2023-10-03 15:48 (164.81.118.119)
>15:48 lasbordes1@IUTINFO-TP-03 ~ $ who am i
>lasbordes1 pts/6        2023-10-03 15:48 (164.81.118.119)
>15:49 lasbordes1@IUTINFO-TP-03 ~ $ logname
>lasbordes1
>15:49 lasbordes1@IUTINFO-TP-03 ~ $ tty
>/dev/pts/6
>15:49 lasbordes1@IUTINFO-TP-03 ~ $ id
>uid=245207(lasbordes1) gid=1001 groupes=1001
>15:49 lasbordes1@IUTINFO-TP-03 ~ $ ls
>a.out  exos  Ubox_Perso  Ubox_Travail
>15:49 lasbordes1@IUTINFO-TP-03 ~ $ ls -a
>.  ..  a.out  .bash_logout  .bashrc  exos  .joe_state  .profile  Ubox_Perso  Ubox_Travail  .viminfo
>15:49 lasbordes1@IUTINFO-TP-03 ~ $ ls -al
>total 80
>drwx------   5 lasbordes1 1001  4096 sept. 18 15:20 .
>drwxr-xr-x 477 root       root 16384 sept. 22 16:10 ..
>-rwx------   1 lasbordes1 1001 16712 sept. 18 14:04 a.out
>-rw-------   1 lasbordes1 1001   220 sept. 18 13:54 .bash_logout
>-rw-------   1 lasbordes1 1001  3644 sept. 18 13:54 .bashrc
>drwx------   2 lasbordes1 1001  4096 sept. 18 15:20 exos
>-rw-------   1 lasbordes1 1001   193 sept. 18 13:56 .joe_state
>-rw-------   1 lasbordes1 1001   807 sept. 18 13:54 .profile
>drwxr-xr-x   2 lasbordes1 1001  4096 sept. 14 11:22 Ubox_Perso
>drwxr-xr-x   2 lasbordes1 1001  4096 juil.  7  2022 Ubox_Travail
>-rw-------   1 lasbordes1 1001  9707 sept. 18 15:20 .viminfo
>15:49 lasbordes1@IUTINFO-TP-03 ~ $ cd ..
>15:50 lasbordes1@IUTINFO-TP-03 etudiants $ pwd
>/home/etudiants
>15:50 lasbordes1@IUTINFO-TP-03 etudiants $ ls
>abdellougenes1  blanchard85     chafiq1         dejugnac1       fernandes62     iparraguirre1  lopes31         nguyen-van-gi1  reich2          theodore4
>abraham4        bocquet7        chagnon8        delage98        ferreira42      jacotin1       lopez50         nogueira6       reinert-marti1  thinnes4
>aigueperse3     bodin21         charles48       delanier1       fetter1         jacquemin6     loridan1        nony11          renaud39        tilleul1
>akunzada1       boender1        charpentier51   delayre1        feugere-des-f1  jamaleddine2   mabea2          nouhaud28       renon17         toribio1
>allemand4       boisbaumann1    charpentier55   del-carmen-vi1  fevre4          jandard2       madi29          odabasioglu1    restoin5        touzet8
>almonteringau1  boisseau19      chartrain4      deleest1        fiaudrin1       jarriault2     maguer4         olle1           reymalissein1   tran62
>al-rawahi1      boisserie9      chastenet9      delhomel1       forestier21     jarrige12      maingoutaud3    ollivier10      rezzonico1      trenchs2
>alyaaribi1      bony5           chatain10       delias10        fort12          jarry46        maintenant1     otshudi1        ribes8          triche3
>amal-laoudai1   bordelais1      chatard17       delisle1        fougeret1       jeanjon8       mairia1         ouahby6         richard90       trillard1
>an3             bordes45        chatard18       delobelle4      fougeret2       jehannin2      majchrzak1      paget4          riffaud38       troncherivier1
>anglada2        borger1         chaumeil19      denis77         foulon10        joly31         maly1           pantene2        rigaud25        truong9
>anglade5        borlot-vautri1  chen63          denise1         four6           kaczmarek4     marcuzzi1       papeix2         rigot7          ul_iutinfo_102
>annan1          boucher38       cherif6         de-pellegrin1   frediani2       kermene1       mare2           pareau1         riviere59       ul_iutinfo_30
>antivackis1     boudeville1     chezeaud4       desboudard1     frugier52       kewe1          martip28        parzych1        robinier1       ul_iutinfo_32
>antoine19       bouge2          claux10         descamps7       gaborit5        koulibaly2     marty59         pascaud27       rodet2          ul_iutinfo_33
>arnaud63        boukhari7       clergerie6      deschamps62     gaillard57      krizmanic1     martzolf1       pattyn4         rodrigues45     ul_iutinfo_34
>artaud6         boulkrinat2     cluzeaud8       descoutures2    garcia72        lachaud52      masclet1        pelaudeix3      rodrigues51     ul_iutinfo_35
>audoin18        bounizar1       cochard6        desmartin2      gaudy21         lacour23       massot4         perrier62       romero7         ul_iutinfo_36
>aylal1          bouny10         colasse2        desmedt1        gauthier78      lacroix77      matusiak1       perrot41        root            ul_iutinfo_37
>ayrault3        bourdarie1      colin33         desmond6        gauvain1        ladrat10       maugiv01        petit105        rouffanche9     ul_iutinfo_38
>bachelet6       bourdier19      coly7           deveau3         gendry1         lafarge36      maugrion1       peyrat38        rougier39       ul_iutinfo_39
>badana1         bourg21         combep04        deveze2         gerard18        laffargue6     mauri1          pialleport2     roussarie14     ul_iutinfo_40
>bagolle1        bourgeault3     condat6         dharyf2         gilbert20       lajardie1      mazabraud12     picaud15        rousseau99      uysal2
>banet3          bouroudane1     constans8       dislay1         gimeno2         lajoinie19     mazenoux2       pignol8         rousselet3      van-rijswijk1
>barbe18         branas1         contie7         divry3          gladin1         lajudie6       mechaussie-de2  pinaud29        rousselot2      vedrine5
>baruthel1       braud15         corgnac-segaf1  doublet6        godinat1        landelle3      mehmood1        pineaud1        roux160         verdeyme2
>baulant1        braunau1        costode1        dourdoigne2     gokcen1         lanvin1        menchon1        pinheiro4       sabatier9       vergne81
>bauri1          brehier2        coudert92       dron2           gorce27         laroche28      mendes16        pinheiro7       sacristan2      vernel-wesolo1
>baussian3       breil2          coulaud20       droual1         goupil5         lasbordes1     mercier60       pipi1           saddiki2        vidal-pujol1
>bayart1         bremont4        coulaud24       druineau1       grenouilloux2   lassalle24     mery15          pontais3        salem2          vieira-da-sil2
>bayle40         brochet1        coulombel6      dubrep03        guerin45        laurent105     mesri4          posseme2        salmon17        villanova1
>bec5            brooks4         court4          dubrev01        guery20         laval51        mestries2       posteaux1       samsel1         villevy1
>bellil2         brullon1        courty18        dubrulle3       guillard11      lavauzelle11   metais10        poteau3         sarribouette1   vimbaye1
>berduck1        bussiere11      couvidoux2      duchesne5       guillemeteau1   laville16      metayer10       pouyade9        savary19        vincent133
>berlureau3      cabrera5        couzon1         duchiron13      guillin4        le-caloch1     mignot19        pouzol4         sazerat4        vivenp01
>bernard151      cagnon2         crespin8        ducos4          guillon26       lecompte7      mille3          prevost31       septembre1      vivet3
>berteloot3      cailliaux1      cressenville1   dufosse4        guston1         lefebvre55     misse1          prevot15        simonin9        wang104
>bertucat2       campredon2      dailami1        dufour75        guysoulard1     leger59        mohamed37       prodel4         sip-1           wang106
>bervil1         canaud2         da-mota6        dugaleix1       hajnoczy1       legg2          monedp02        quenette1       smimid1         wang117
>beteau2         cao17           damouh2         dugaleix2       hardouineau1    leguille1      monie1          rajoye1         soudet1         xu24
>beyrand18       capel10         damour6         dumont49        herault16       lepert1        monmont3        ramberg1        soularue9       zani1
>biarneix3       carpentier23    danvin1         duplessy4       herbepin1       lerdung1       mons19          rameau2         soury26         zawodniak1
>bidault17       carpentierber1  darfeuille16    durand181       hermelin1       levarato2      monteiro-ruim1  ranty12         staple1         zoccola1
>bilen1          castanie3       daube1          egea4           herouard1       lezeau1        morinet4        rasschaert2     szyda1
>billetat1       catchirayar2    dedet6          e_vivenp01      hierso3         lhuissier4     mouffron2       ratel4          taconet1
>billonnet3      cavdar2         degroise1       fatmi6          hiez2           limbert2       nadler-campou1  ravaud3         tech
>biston1         cazarres2       deguil1         faucher77       huber5          limousin8      neveu12         raynaud110      teodoro1
>blanc46         cazillac6       dejean11        faure205        hugelp01        loizeau2       nguyen120       raynaud99       tetumu1
>15:50 lasbordes1@IUTINFO-TP-03 etudiants $ cd
>15:50 lasbordes1@IUTINFO-TP-03 ~ $ pwd
>/home/etudiants/lasbordes1
>15:50 lasbordes1@IUTINFO-TP-03 ~ $
>```
> pwd >> Affiche le répertoire courant\
> date >> Affiche la date\
> who >> Affiche tout les utilisateurs présent sur la machine\
> whoami >> Affiche ma session utilisateur\
> logname >> Affiche mon nom utilisateur\
> tty >> Affiche le terminal que j'utilise\
> id >> Affiche mon GUI, UID et mes groupes\
> ls >> Affiche tout les fichiers (sauf les cashés par un point)\
> ls -a >> Affiche tout les fichiers\
> ls -al >> Affiche tout les fichiers et leurs permission\
> cd .. >> Retourne un répertoire en arrière

# B

> C'EST PAS UNE QUESTION

# C

> / >> bin, dev, home\
> /usr >> bin, games, include\
> /user/bin >> '[', ex, libnetcfg\
> /dev >> agpgart, disk, kmsg

# Exercice 2

## A

> `cat` affiche tout le ficher alors que `more` affiche une page que l'on peut continuer 

# Exercice 5

## 1

### A

>abc, aedc, a.out, arthur, bottin, chap11, chap2, chap3, chap4, EXO, p10.c, p1.c, p2.c, p3.c, Ubox_Perso, Ubox_Travail, x.a1, x.a2

### B

>abc, aedc, a.out, arthur

### C

>a.out

### D

>abc, aedc

### E

>abc

### F

>aedc

### G

>ls: impossible d'accéder à 'a???c': Aucun fichier ou dossier de ce type

### H

>chap11, x.a1

### I

>p10.c, p1.c, p2.c, p3.c

### J

>chap2, chap3, chap4

### K

>abc, aedc, a.out, arthur, chap11, chap2, chap3, chap4

### L

>ls: impossible d'accéder à '[a-c]*': Aucun fichier ou dossier de ce type

### M

>p1.c, p2.c, p3.c

### N

>ls: impossible d'accéder à '[abp]?[m-z]': Aucun fichier ou dossier de ce type

## 2

### A

>ls *.c

### C

>ls ???p*

### D

>ls ????

### E

>ls ?[bcde]*

### F

>ls [aeiouy]??*[zrtpqsdfghjklmwxcvbn]

## 3

rm: impossible de supprimer 'pierre/langagec/': est un dossier



