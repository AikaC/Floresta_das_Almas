
label rio:

 show rio
 with dissolve

 play music "audio/586933__krypaw__frogs-lake-night-spot-4.wav"

 "Arrastados pela correnteza, deveriam decidir entre continuar no rio ou voltar a terra firme."

 show Cmaya
 show dor
 with dissolve

 maya "A ferida em meu braço dói com a água fria."

 hide Cmaya
 hide dor
 show Cpotira at left
 show preoc at left
 with dissolve

 potira "Aguentem só mais um pouco."

 hide Cpotira
 hide preoc
 show Ccaue
 show dor
 with dissolve

 caue "Não consigo por muito tempo."

 hide Ccaue
 hide dor
 show Cjacira at right
 show idle at right
 with dissolve

 jacira "Vamos para a margem?"

 hide Cjacira
 hide idle
 with dissolve

 menu:
  "Sim":
   "Ao chegar à margem, com a rapidez de uma animal selvagem..." 
   "...A Cuca agarra Maya com suas garras verdes."

   show Cpotira at left
   show susto at left
   with dissolve

   potira "Maya!"

   hide Cpotira
   hide susto
   show Cjacira
   show idle
   with dissolve

   jacira "Não! {w=1}É tarde demais!"
   jacira "Precisamos continuar."

   hide Cjacira
   hide idle
   show Ccaue at right
   show idle at right
   with dissolve

   caue "É mais seguro ficar no meio do rio."

   hide Ccaue
   hide idle
   with dissolve

   jump estrelas
  "Não":
   "A correnteza forte puxa Maya de forma brutal."

   show Cpotira
   show susto
   with dissolve

   potira "Maya!"

   hide Cpotira
   hide susto
   show Cjacira at right
   show idle at right
   with dissolve

   jacira "Não! É tarde demais!"
   jacira "Precisamos continuar."

   hide Cjacira
   hide idle
   with dissolve

   jump estrelas

 return