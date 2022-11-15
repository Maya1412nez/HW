class Script:
    def __init__(self):
        self.discription = ""
        self.ways = dict()
        self.name = ""

situations = {}
start = Script()
start.discription = 'Выберите персонажа'
start.ways["Крыс"] = '''
О персонаже:
Вы - 2-х миллиметровый крысёныш. 
Крыса вы не только как животное, но и по натуре. У вас нет друзей((('''
start.ways["Курица"] = '''
О персонаже:
Вы – 2-х метровая курица. Жизнь у вас такая себе. 
Из-за высоких цен, рассчитанных на котов, вы не можете покупать себе достаточно еды.
*урчание в области живота*'''
start.name = 'Старт'
situations[start.name] = start


kuriniy_way1 = Script()
kuriniy_way1.name = 'Курица'
kuriniy_way1.discription = '''Прогуливаясь по улице вы увидели объявление о наборе участников в шоу-конкурс. 
Постер:
"Соревнование по поеданию кукурузы! Главный приз – трёшка в Сыратове и 10 центнеров кукурузы!!"
Жаль, вы - курица и читать можете только важную для курицы информацию. Вы видите:
"__________ кукурузы! _____________________________________________ кукурузы!!"
'''
kuriniy_way1.ways['Ура!'] = ' - За кукурузой!!!'
kuriniy_way1.ways['Игнор'] = ' - Проигнорить как обычно'
situations[kuriniy_way1.name] = kuriniy_way1


kuriniy_way11 = Script()
kuriniy_way11.name = 'Игнор'
kuriniy_way11.discription = 'Ваша жизнь не меняется'
situations[kuriniy_way11.name] = kuriniy_way11


kuriniy_way2 = Script()
kuriniy_way2.name = 'Ура!'
kuriniy_way2.discription = '''
Следующий день
Вы приходите на соревнование. Конкурсантов рассаживают в большие картонные коробки, чтоб не списывали друг у друга.
'''
kuriniy_way2.ways['Не'] = ' - Это бред какой-то, пойду отсюда, кудку-дах'
kuriniy_way2.ways['Намана'] = '- классика, каждый день такое происходит. ква-кудах-тах-тах'
situations[kuriniy_way2.name] = kuriniy_way2


kuriniy_way3 = Script()
kuriniy_way3.name = 'Намана'
kuriniy_way3.discription = '''
Вы заходите со всеми. 
Вам дают тарелку с 10 кг кукурузы
3 
2
1
Конкурс начался!!!

Спустя 2 минуты к вам прогрызается 2-х миллиметровый крысёныш. Он предлагает вам свою порцию кукурузы.
'''
kuriniy_way3.ways['Кудах!'] = ' - Спасибо, солнышко :>'
kuriniy_way3.ways['Кудкудах'] = '- Не, братан, пасиба, я не голодаю из-за нынешней экономики'
situations[kuriniy_way3.name] = kuriniy_way3


kuriniy_way31 = Script()
kuriniy_way31.name = 'Кудах!'
kuriniy_way31.discription = '''
Вы съедаете еще 10 кг кукурузы
После мероприятия к вам подходит этот же крыс.
- Ты мне очень помог, так что я хочу подарить тебе еще 9 центнеров кукурузы
- Кудах!
Вы принимаете груховик с кукурузой на следующий день. 
Теперь у вас есть все, и живете вкусно и счастливо :)
'''
situations[kuriniy_way31.name] = kuriniy_way31


kuriniy_way32 = Script()
kuriniy_way32.name = 'Кудкудах'
kuriniy_way32.discription = '''
Вы профукали 9 центнеров кукурузы
Еф
'''
situations[kuriniy_way32.name] = kuriniy_way32


kuriniy_way21 = Script()
kuriniy_way21.name = 'Не'
kuriniy_way21.discription = '''
В вашу пустую голову приходит мысль уйти с не менее пустым желудком с конкурса с едой. 
Вы покидаете помещение
Проходя мимо склада с призовой кукурузой вы улавливаете запах...
'''
kuriniy_way21.ways['Кукуруза..'] = 'Логично ведь'
kuriniy_way21.ways['Шаурма...'] = '....'
situations[kuriniy_way21.name] = kuriniy_way21


kuriniy_way22 = Script()
kuriniy_way22.name = 'Кукуруза..'
kuriniy_way22.discription = '''
Вы кидаетесь к амбару, проламываете стену и начинаете жадно поедать кукурузу.
Час спустя
Вы чилите в полицейском участке
Конец
'''
situations[kuriniy_way22.name] = kuriniy_way22


kuriniy_way23 = Script()
kuriniy_way23.name = 'Шаурма'
kuriniy_way23.discription = '''
Бывает кншн


Хотите ответы?
'''
kuriniy_way23.ways['Хочу'] = 'спойлер'
kuriniy_way23.ways['Не хочу'] = 'тоже спойлер'
situations[kuriniy_way23.name] = kuriniy_way23



kuriniy_way24 = Script()
kuriniy_way24.name = 'Хочу'
kuriniy_way24.discription = '''
Подсказка:
Выбирайте нормальные варианты
'''
situations[kuriniy_way24.name] = kuriniy_way24


kuriniy_way25 = Script()
kuriniy_way25.name = 'Не хочу'
kuriniy_way25.discription = '''
Ну тогда давайте заново
'''
situations[kuriniy_way25.name] = kuriniy_way25


rat_way1 = Script()
rat_way1.name = 'Крыс'
rat_way1.discription = '''
Прогуливаясь по улице вы увидели объявление о наборе участников в шоу-конкурс.
"Соревнование по поеданию кукурузы! Главный приз – трёшка в Сыратове и 10 центнеров кукурузы!!" '''
rat_way1.ways['Участвовать'] = '- завтра вы пойдете на шоу'
rat_way1.ways['Игнор'] = 'как-нибудь потом, никогда'



rat_way2 = Script()
rat_way2.name = 'Участвовать'
rat_way2.discription = '''
Следующий день
Вы приходите на соревнование. Конкурсантов рассаживают в большие картонные коробки, чтоб не списывали друг у друга.'''
rat_way2.ways['Зайти'] = '- Вы заходите со всеми'
rat_way2.ways['Безобразие!!!'] = '- Вы говорите, что это незаконно и вызываете полицию.'
situations[rat_way2.name] = rat_way2


rat_way3 = Script()
rat_way3.name = 'Безобразие!!!'
rat_way3.discription = '''
Полиция приезжает и находит..
Контрабанду кукурузы!!!!!
Полиция благодарит вас за проявленную ответственность и мужество и предлагает 1 кг кукурузы как награду.'''
rat_way3.ways['Принять'] = 'Принять награду'
rat_way3.ways['Отказаться'] = 'Не, спасибо)'
situations[rat_way3.name] = rat_way3


rat_way31 = Script()
rat_way31.name = 'Принять'
rat_way31.discription = '''Это была проверка. Вас арестовывают с подозрением на сотрудничество с контрабандистами.'''
situations[rat_way31.name] = rat_way31



rat_way32 = Script()
rat_way32.name = 'Отказаться'
rat_way32.discription = '''Один из полицейских подходит к вам и хлопает по плечу
Он передает вам бумажный сверток
- Позвони мне сегодня вечером'''
situations[rat_way32.name] = rat_way32



rat_way4 = Script()
rat_way4.name = 'Зайти'
rat_way4.discription = '''
Вы заходите со всеми. 
Вам дают тарелку с 10 кг кукурузы и конкурс начинается!
Вы понимаете, что 10 кг кукурузы вам не съесть
Вы умная крыса?
'''
rat_way4.ways['Умная'] = '- Да, и у меня есть план'
rat_way4.ways['Шаурма'] = 'хыыы'
situations[rat_way4.name] = rat_way4



rat_way41 = Script()
rat_way41.name = 'Умная'
rat_way41.discription = '''
Вы крыса очень маленькая. Пока вас никто не видит, вы прогрызаете коробку.
Вы подбегаете к соседней коробке, прогрызаете ее. 
Там сидит 2-х метровая курица, быстро поедающая свои 10 кг кукурузы.
'''
rat_way41.ways['Поговорить'] = 'Можно предложить ей сотрудничество'
rat_way41.ways['Уйти'] = 'Оно слишком большое'
situations[rat_way41.name] = rat_way41



rat_way411 = Script()
rat_way411.name = 'Поговорить'
rat_way411.discription = '''
Вы очень умная крыса, поэтому прекрасно знаете о финансовом состоянии куриц в стране.
- Ты ведь здесь лишь ради еды?
- Кудку-дах!!! (Испуганный) Кудку-дах-дах-дах (Энергичное "да")
- Могу дать тебе еще 10 кг кукурузы
- Кудку-дааах~ (Правда? Спасибо))
Вы успешно сбагрили свою кукурузу. Вы занимаете первое место и получаете трешку в Сыратове и 10 центнеров кукурузы
'''
situations[rat_way411.name] = rat_way411


rat_way412 = Script()
rat_way412.name = 'Уйти'
rat_way412.discription = '''
вам страшно и вы уходите.
Вы ничего не выиграли
Плохая из вас крыса
'''
situations[rat_way412.name] = rat_way412


rat_way42 = Script()
rat_way42.name = 'Шаурма'
rat_way42.discription = '''АБ ответ
'''
situations[rat_way42.name] = rat_way42



situations[start.name] = start
current_situation = situations["Старт"]

while True:
    print(current_situation.discription)
    for k, v in current_situation.ways.items():
        print(k, v)
    choise = input()
    current_situation = situations[choise]
    if len(current_situation.ways) == 0:
        break
print(current_situation.discription)