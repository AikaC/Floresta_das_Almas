# História principal

label start:

 play music "audio/433573__deleted-user-8713024__africa-tribal-drums.wav"

 show aldeia
 window hide
 nvl clear
 nvl show dissolve

 nvle "Durante muito tempo, nossa tribo foi sinônimo de força."
 nvle "Nossos guerreiros eram conhecidos por obter a força de seus oponentes."
 nvle "Hoje,"
 nvle "cansados de tanto correr mata a dentro,"
 nvle "perseguidos por um mal que nunca havia se manidestado antes."
 nvl clear
 nvle "Eu e meus amigos: Maya, Cauê e Jaci;"
 nvle "Estamos perdidos no meio da lendária {i}Floresta das Almas."
 nvle "Nossa aldeia, completamente destruída."
 nvle "O mal,"
 play sound "audio/Risada-Bruxa.ogg"
 nvle "A Cuca."

 nvl hide dissolve
 window show

 hide aldeia
 show floresta
 show Cpotira at left
 show preoc at left
 with dissolve

 potira "Maya! {w}Você está sangrando!"

 hide Cpotira
 hide preoc
 show Cjacira at right
 show preoc at right
 with dissolve

 jacira "Eu tenho algumas ervas."

 hide Cjacira
 hide preoc
 show Cmaya
 show dor
 with dissolve

 maya "Eu me feri em alguns arbustos dessa {i}floresta maldita{/i}."

 hide Cmaya
 hide dor
 show Ccaue
 show preoc
 with dissolve

 caue "Vamos usar as ervas que Jacira possui?"

 hide Ccaue
 hide preoc
 with dissolve

 menu:
  "Usar as ervas":

   show Cjacira at left
   show preoc at left
   with dissolve

   jacira "Não se preocupe Maya,"  
   jacira "As ervas medicinais logo farão efeito."

   hide Cjacira
   hide preoc
   show Cmaya
   show preoc
   with dissolve

   maya "Obrigada."
   maya "Mas acho que devemos encontrar um local seguro logo."

   hide Cmaya
   hide preoc
   show Ccaue at right
   show preoc at right
   with dissolve

   caue "Consegue correr?"

   hide Ccaue
   hide preoc
   show Cmaya at left
   show idle at left
   with dissolve

   maya "Logo atrás de vocês."

   hide Cmaya
   hide idle
   show Cpotira
   show idle
   with dissolve

   potira "Então vamos!"

   hide Cpotira
   hide idle
   with dissolve

   jump abrigo
  "Procurar abrigo":

   show Cmaya at left
   show idle at left
   with dissolve

   maya "Não temos tempo para isso, {w}eles estão atrás da gente!"
   maya "Vamos encontrar um lugar seguro!"

   hide Cmaya
   hide idle
   show Cpotira
   show preoc
   with dissolve

   potira "Tem certeza?"

   hide Cpotira
   hide preoc
   show Cmaya at right
   show idle at right
   with dissolve

   maya "Sim! Rápido!"

   hide Cmaya
   hide idle
   show Cjacira
   show idle
   with dissolve

   jacira "Por aqui!"

   hide Cjacira
   hide idle
   with dissolve

   jump cura
 # This ends the game.
 return