class Pers:
    def __init__(self):
        # passive (not using in fighting)
        self.level = 1  # level

        # active (using in fighting)
        self.health_points = 20  # HP. Depends on level, skills
        self.armor_points = 0  # Armor points. Depends on skills, level
        self.damage_points = 5  # Depends on skills, level
        self.hill_points = 2  # Depends on skills, level
        self.cool_down = 0.25  # Depends on skills

    def take_damage(self, damage, skill=None):
        if skill == 'fire':
            damage *= 1.2
        self.health_points -= damage


class Enemy(Pers):
    def __init__(self, name):
        super().__init__()
        self.coins = 15
        self.name = name

    def get_states(self):
        return f'health#{self.health_points}', f'damage#{self.damage_points}', f'protect#{self.armor_points}', \
               f'hill#{self.hill_points}', f'cooldown#{self.cool_down}'

    def take_damage(self, damage, skill=None):
        ...


class Hero(Pers):
    def __init__(self):
        super().__init__()
        self.killed = 0
        self.bag_of_coins = 100
        self.skills_quality = 1  # Quality of different skills. Dep on level
        self.coins = 0
        self.bag = {} # Inventory. Structure: {name}: class_object


    def up_level(self, reason, params):
        self.level += 1
        if reason == 'SKILL':
            # params = [type of skill (attack, protect, hill)]
            if params[0] == 'attack':
                self.damage_points += 3
            elif params[0] == 'protect':
                self.armor_points += 1
            elif params[0] == 'hill':
                self.hill_points += 0.5
        elif reason == 'DAMAGE':
            pass
        self.coins = 0  # coins are spent for upping level,
        self.bag_of_coins += 20  # so bag is growing up

    def hill_myself(self):
        self.health_points += self.hill_points
        # TO DO start cooldown

    def take_treasure(self, args):  # get coins from treasure
        coin, kind = args
        if kind == 'usual':
            pass
        self.coins += coin

    def get_states(self, kind='changing'):
        if kind == 'changing':
            return f'health#{self.health_points}', f'damage#{self.damage_points}', f'protect#{self.armor_points}', \
                   f'hill#{self.hill_points}', f'cooldown#{self.cool_down}'
        elif kind == 'constant':
            return self.level, self.skills_quality
        elif kind == 'all':
            return self.level, self.skills_quality, self.health_points, self.damage_points, self.armor_points, \
                   self.hill_points, self.cool_down

    def attack(self, name, states):
        # enemy_health = states[0].split('#')[1]
        # enemy_damage = states[1].split('#')[1]
        # while self.health_points > 0 and enemy_health > 0:
        #     enemy_health -= self.damage_points
        #     self.health_points -= enemy_damage
        #     time.sleep(self.cool_down)
        ...

    def eat(self, item_object):
        if item_object in self.bag:
            points = item_object.get_params[0]
            self.health_points += points

    def review_items(self):
        return self.bag


    def take_item(self, item):
        self.bag[item.name] = item.get_params()

    def review_item(self, item):
        return self.bag.get(item.name)


class Item:
    def __init__(self, name='Advertisment', hill_points=0, damage_points=0) -> None:
        self.name = name
        self.hillpoints = hill_points
        self.damage_points = damage_points
        self.skills = []

    def get_params(self):
        return [self.hillpoints, self.damage_points, self.skills]


class Kristallik:
    def __init__(self, kind='usual'):
        self.coins = 10
        self.level = 1
        self.kind = kind

    def disappear(self):
        self.coins = 0
        self.kind = None

    def get_coins(self):
        return self.coins, self.kind


class Script:
    def __init__(self, name='', discription='', ways={}, items=None):
        self.discription = discription
        self.ways = ways
        self.name = name
        self.items = items

situations = {}


class Game:
    def __init__(self) -> None:

        lst_of_sits = [
            Script('Старт', '''
            Выберите персонажа:
            2-х миллиметровый крысёныш
                или
            2-х метровая курица
            ''', {'Курица': 'Выбираю курицу', 'Крыс': 'Я за крысу!'}),

            Script('Курица', '''
            Вы - 2-х метровая курица. Жизнь у вас такая себе. 
            Из-за высоких цен, рассчитанных на котов, вы не можете покупать себе достаточно еды.
            *урчание в области живота*''', {'ок': 'ладно...'}),

            Script('Крыс', '''
            Вы - 2-х миллиметровый крысёныш.
            Крыса вы не только как животное, но и по натуре. У вас нет друзей(((
            ''', {"оки": ''}),

            Script('ок', '''Прогуливаясь по улице вы увидели объявление о наборе участников в шоу-конкурс. 
            Постер:
            "Соревнование по поеданию кукурузы! Главный приз – трёшка в Сыратове и 10 центнеров кукурузы!!"
            Жаль, вы - курица и читать можете только важную для курицы информацию. Вы видите:
            "__________ кукурузы! _____________________________________________ кукурузы!!"
            ''', {'Ура!': ' - За кукурузой!!!', 'Игнор': ' - Проигнорить как обычно'}),

            Script('Игнор', 'Ваша жизнь не меняется'),

            Script('Ура!', '''
            Следующий день
            Вы приходите на соревнование. Конкурсантов рассаживают в большие картонные коробки, чтоб не списывали друг у друга.
            ''', {'Не': ' - Это бред какой-то, пойду отсюда, кудку-дах', 'Намана': '- классика, каждый день такое происходит. ква-кудах-тах-тах'}),

            Script('Намана', '''
            Вы заходите со всеми. 
            Вам дают тарелку с 10 кг кукурузы
            3 
            2
            1
            Конкурс начался!!!

            Спустя 2 минуты к вам прогрызается 2-х миллиметровый крысёныш. Он предлагает вам свою порцию кукурузы.
            ''', {'Кудах!': ' - Спасибо, солнышко :>', 'Кудкудах':'- Не, братан, пасиба, я не голодаю из-за нынешней экономики'}),

            Script('Кудах!', '''
            Вы съедаете еще 10 кг кукурузы
            После мероприятия к вам подходит этот же крыс.
            - Ты мне очень помог, так что я хочу подарить тебе еще 9 центнеров кукурузы
            - Кудах!
            Вы принимаете груховик с кукурузой на следующий день. 
            Теперь у вас есть все, и живете вкусно и счастливо :)
            '''),

            Script('Кудкудах', '''
            Вы профукали 9 центнеров кукурузы
            Еф
            '''),

            Script('Не', '''
            В вашу пустую голову приходит мысль уйти с не менее пустым желудком с конкурса с едой. 
            Вы покидаете помещение
            Проходя мимо склада с призовой кукурузой вы улавливаете запах...
            ''', {'Кукуруза': '- Наверняка это кукуруза', 'Шаверма': "я знаю только шавермы"}),

            Script('Кукуруза', '''
            Вы кидаетесь к амбару, проламываете стену и начинаете жадно поедать кукурузу.
            Час спустя
            Вы чилите в полицейском участке
            Конец
            '''),

            Script('Шаверма', """нда.. Бывает
            

            Хотите ответы?""", {'хочу': ' - спойлер', 'не хочу': ' - тоже спойлер'}),


            Script('хочу', '''
            Подсказка:
            Выбирайте нормальные варианты
            '''),

            Script('не хочу', '''
            Ну тогда давайте заново
            '''),

            Script('оки', '''
            Прогуливаясь по улице вы увидели объявление о наборе участников в шоу-конкурс.
            "Соревнование по поеданию кукурузы! Главный приз – трёшка в Сыратове и 10 центнеров кукурузы!!"''', 
            {'участвовать': '- завтра вы пойдете на шоу', 'игнор': ' - как-нибудь потом, никогда'}),

            Script('игнор', '''
            Вы решаете проигнорировать судьбоносное объявление. Ваша жизнь вновь становится однообразной'''),

            Script('участвовать', '''Вы срываете объявление, чтобы больше никто не узнал о соревнованиях''', {'вперед': "следующий день"}, paper),

            Script('вперед', '''
            Следующий день
            Вы приходите на соревнование. Конкурсантов рассаживают в большие картонные коробки, чтоб не списывали друг у друга.''', 
            {'Зайти': '- Вы заходите со всеми', 'Безобразие!!!': '- Вы говорите, что это незаконно и вызываете полицию.'}),

            Script('Безобразие!!!', '''
            Полиция приезжает и находит..
            Контрабанду кукурузы!!!!!
            Полиция благодарит вас за проявленную ответственность и мужество и предлагает 1 кг кукурузы как награду.''', 
            {'Принять': ' - Принять награду', 'Отказаться': ' - Не, спасибо)'}),

            Script('Принять', '''Это была проверка. Вас арестовывают с подозрением на сотрудничество с контрабандистами.'''),


            Script('Отказаться', '''Один из полицейских подходит к вам и хлопает по плечу
            Он передает вам бумажный сверток
            - Позвони мне сегодня вечером'''),


            Script('Зайти', '''
            Вы заходите со всеми. 
            Вам дают тарелку с 10 кг кукурузы и конкурс начинается!
            Вы понимаете, что 10 кг кукурузы вам не съесть
            Вы умная крыса?
            ''', {'Умная': '- Да, и у меня есть план', 'Шаурма':' - хыыы'}),


            Script('Умная', '''
            Вы крыса очень маленькая. Пока вас никто не видит, вы прогрызаете коробку.
            Вы подбегаете к соседней коробке, прогрызаете ее. 
            Там сидит 2-х метровая курица, быстро поедающая свои 10 кг кукурузы.
            ''', {'Поговорить':' - Можно предложить ей сотрудничество','Уйти':' - Оно слишком большое'}),


            Script('Поговорить', '''
            Вы очень умная крыса, поэтому прекрасно знаете о финансовом состоянии куриц в стране.
            - Ты ведь здесь лишь ради еды?
            - Кудку-дах!!! (Испуганный) Кудку-дах-дах-дах (Энергичное "да")
            - Могу дать тебе еще 10 кг кукурузы
            - Кудку-дааах~ (Правда? Спасибо))
            Вы успешно сбагрили свою кукурузу. Вы занимаете первое место и получаете трешку в Сыратове и 10 центнеров кукурузы
            '''),

            Script('Уйти', '''
            вам страшно и вы уходите.
            Вы ничего не выиграли
            Плохая из вас крыса
            '''),

            Script('Шаурма', '''АБ ответ
            ''')]

        self.ways = {}



        for discription in lst_of_sits:
            self.ways[discription.name] = discription
            item = self.ways

    def start(self):
        current_situation = self.ways["Старт"]

        while True:
            print(current_situation.discription)
            if current_situation.items:
                print(current_situation.items.name)
                print('Вы подобрали предмет:', current_situation.items.name)
                racky.take_item(paper)
            print(racky.review_item(paper))
            print(racky.review_items())
            for i, (k, v) in enumerate(current_situation.ways.items()):
                print(i + 1, v)
            choise = list(current_situation.ways.keys())[int(input()) - 1]
            current_situation = self.ways[choise]
            if len(current_situation.ways) == 0:
                break
        print(current_situation.discription)



racky = Hero()
racky.take_damage(10)
print(racky.get_states())

paper = Item()
print(racky.take_item(paper))
print(racky.review_item(paper))
print(racky.review_items())

g = Game()
g.start()

kris = Kristallik()
coins = kris.get_coins()
print(coins)
racky.take_treasure(coins)

monsty = Enemy('IWantSleep')
argg = monsty.get_states()
racky.attack('IWantSleep', argg)

