label cura:

 show Ccaue
 show idle
 with dissolve

 caue "Essa encosta parece segura, vamos descansar um pouco aqui."

 hide Ccaue
 hide idle
 show Cjacira
 show preoc
 with dissolve

 jacira "Precisamos te curar agora, Maya."

 hide Cjacira
 hide preoc
 show Cmaya
 show idle
 with dissolve

 maya "Obrigada!"

 hide Cmaya
 hide idle
 with dissolve

 jump abrigo
 return

label abrigo:

 play sound "audio/correndo.wav"

 show Cpotira
 show preoc
 with dissolve

 potira "O que foi isso?"

 hide Cpotira
 hide preoc
 show Cmaya at right
 show susto at right
 with dissolve

 maya "É ela!"

 hide Cmaya
 hide susto
 show Cjacira at left
 show susto at left
 with dissolve

 jacira "E o que vamos fazer?"

 hide Cjacira
 hide susto
 show Ccaue at right
 show preoc at right
 with dissolve

 caue "Nossas únicas opções são seguir o rio ou continuar mata a dentro."

 hide Ccaue
 hide preoc
 show Cpotira
 show preoc
 with dissolve

 potira "O que vocês acham?"

 hide Cpotira
 hide preoc
 with dissolve
 
 menu:
  "Seguir o rio":
   hide floresta
   jump rio
  "Ir para a mata":
   hide floresta
   show mata
   show Cpotira
   show preoc
   with dissolve

   potira "Por aí não!"
   potira "Eu acho que acabei de ver a cuca!"

   hide Cpotira
   hide preoc
   show Ccaue at right
   show idle at right
   with dissolve

   caue "Vamos pelo rio, então."

   hide Ccaue
   hide idle
   with dissolve

   jump rio

 return