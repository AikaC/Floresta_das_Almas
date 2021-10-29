
default escolha = "Cruzeiro do Sul"

label estrelas:

 play music "audio/88795__ethang__kerriflute.wav"
 "Agora sem Maya, e já distante de todo o perigo..."
 "... Nossos pequenos precisam continuar sua fuga."

 show Cpotira
 show idle
 with dissolve

 potira "Precisamos nos localizar."

 hide Cpotira
 hide idle
 show Ccaue at right
 show idle at right
 with dissolve

 caue "Já estamos bem longe da área da aldeia."

 hide Ccaue
 hide idle
 show Cjacira
 show idle
 with dissolve

 jacira "Não faço ideia de onde estamos..."

 hide Cjacira
 hide idle
 show Cpotira at left
 show idle at left
 with dissolve

 potira "Podemos usar as estrelas!"
 potira "Qual constelação seguir?"

 hide rio
 show estrelado
 hide Cpotira
 hide idle
 with dissolve

 window hide

 menu:
  "As Três Marias":
   $escolha = "Três Marias"
   jump seguir_constelacao
  "O Cruzeiro do Sul":
   jump seguir_constelacao
 return

label seguir_constelacao:

 window show

 show Ccaue
 show idle
 with dissolve

 caue "Nós nunca seguimos [escolha] tão longe dos domínios da aldeia."

 hide Ccaue
 hide idle
 show Cpotira at right
 show idle at right
 with dissolve

 potira "Então deveríamos nos dividir."

 hide Cpotira
 hide idle
 show Cjacira
 show idle
 with dissolve

 jacira "Certo eu vou até [escolha] sozinha."

 hide Cjacira
 hide idle
 with dissolve

 "Potira e Cauê seguiram o caminho das estrelas,{w} agora sem Jacira."
 

 play sound "audio/canto da sereia.ogg"

 show Cpotira
 show idle
 with dissolve

 potira "De onde vem esse som?{w=1} Cauê?{w=1} Cauê!"

 hide Cpotira
 hide idle
 with dissolve

 menu:
  "Seguir o som":

   show Cpotira
   show idle
   with dissolve

   potira "Cauê!"

   hide Cpotira
   hide idle
   with dissolve

   jump iara
  "Procurar Cauê":
   jump iara
 return

label iara:

 hide estrelado
 show NOITElago

 play sound "audio/jump-scare.ogg"
 show iara02 at proximo

 window hide
 pause

 window show
 "Potira ficou paralisada ao ver uma das lendas mais terríveis na sua frente."
 "A Iara, com o pequeno Cauê nos braços."

 hide iara02
 show Cpotira
 show susto
 with dissolve

 potira "Por Tupã, {w}o que eu faço agora?"

 hide Cpotira
 hide susto
 with dissolve

 "Num lampejo de ideias, suas opções eram limitadas."
 "O sol já aparecia e logo as criaturas da noite descansariam."
 "Mas para que sua segurança estivesse garantida..."
 show pedra
 show iara01
 "... Potira precisaria atravessar o lago da Iara."
 "Pois ainda era perseguida pela cuca."

 hide iara01
 hide pedra
 with dissolve

 menu:
  "Usar as toras flutuantes":

   hide NOITElago
   show DIAlago
   with dissolve

   "Você sobreviveu a sua primeira noite no halloween nativo."

   hide DIAlago
   return
  "Atravessar nadando":
   show pedra
   show iara01

   "Você morreu como uma verdadeira guerreira."

   hide pedra
   hide iara01
   return