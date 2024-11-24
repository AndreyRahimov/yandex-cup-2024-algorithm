# A. Два из трёх

|   |   |
|---|---|
|Ограничение времени|1 секунда|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

Древнегреческий философ Пифагор придавал большое значение числам, считая их основой мира. А числам, обладающим теми или иными математическими свойствами, приписывались мистические значения. Например, нечётные числа в пифагорействе считались мужскими, а чётные — женскими. Делимость числа на другие вообще была существенным отличительным признаком для Пифагора. И вот теперь его интересуют числа, которые будут достаточно хорошо делимыми, но не до конца идеальными в этом плане. Для этого он выписал возрастающую последовательность натуральных чисел, делящихся ровно на два числа среди трёх заранее заданных чисел a, b и c. Помогите Пифагору найти n-е число в этой последовательности.

## Формат ввода

Первая строка содержит целые числа a, b, c ($1≤a,b,c≤10^6$), делимость на которые проверяет Пифагор.

Вторая строка содержит целое число n ($1≤n≤10^{18}$) — номер элемента последовательности, который хочет найти Пифагор. Элементы нумеруются, начиная с единицы.

## Формат вывода

Выведите n-е натуральное число, делящееся ровно на два из трёх чисел a, b, c.

Если подходящего числа не существует или оно превышает $10^{18}$, выведите −1.

### Пример 1

| Ввод        | Вывод |
| ----------- | ----- |
| 2 3 5<br>10 | 42    |

### Пример 2

| Ввод             | Вывод    |
| ---------------- | -------- |
| 5 6 7<br>1000000 | 13999986 |

## Примечания

Последовательность натуральных чисел, делящихся ровно на два числа из трёх чисел 2, 3 и 5, выглядит так: 6,10,12,15,18,20,24,36,40,42,45,48,50,…. Десятым членом этой последовательности является 42.

# B. Горки, греки, гэги

|   |   |
|---|---|
|Ограничение времени|1 секунда|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

Как известно, в Древней Греции были положены начала философии, благодаря которой, в частности, удалось формализовать понятие науки. Одной из главных наук того времени считалась математика: Пифагор, Евклид, Архимед — вы точно слышали эти имена! А уж о том, что, в некотором смысле вследствие развития математики этими знаменитыми философами, вы читаете условие этой задачи, говорить не приходится...

Тем не менее, даже таким выдающимся учёным иногда приходится спускаться с небес на землю и просить архитекторов строить здания для своих школ.

Архитекторы — люди инженерного склада, и потому здесь и там у них возникают задачи, связанные с математикой. Вот и на этот раз перед ними встала следующая проблема.

У них есть n строительных блоков, стоящих на одной прямой. Блок с номером i имеет высоту hi; длину и ширину всех блоков будем считать единичными. Назовем горкой непрерывную подпоследовательность с l-го по r-й блок такую, что найдется $m:l<m<r$ и $h_l<h_{l+1}<…<h_m>h_{m+1}>…>h_r$.

Архитекторам потребовалось узнать, сколько существует горок в этой последовательности блоков. Они очень рассчитывают на вашу помощь!

## Формат ввода

Первая строка содержит целое число t(1≤t≤100) — количество наборов входных данных.

Следующие (2⋅t) строк описывают наборы входных данных.

Первая строка каждого набора содержит целое число n($1≤n≤2⋅10^5$) — количество блоков.

Вторая строка каждого набора содержит n целых чисел $h_1,h_2,…,h_n(1≤h_i≤10^9)$ — высоты блоков.

Гарантируется, что $∑n≤2⋅10^5$.

## Формат вывода

Для каждого набора входных данных выведите одно целое число — количество горок в последовательности блоков.

## Пример

| Ввод                                                                                                | Вывод                 |
| --------------------------------------------------------------------------------------------------- | --------------------- |
| 5<br>5<br>1 2 3 2 1<br>1<br>1000000000<br>1<br>1<br>6<br>1 2 3 3 2 1<br>10<br>1 5 8 4 6 3 8 10 14 7 | 4<br>0<br>0<br>0<br>6 |


# C. Древние танцы

|   |   |
|---|---|
|Ограничение времени|1 секунда|
|Ограничение памяти|64Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

Исследователи считают шумерскую цивилизацию одной из первых цивилизаций в истории человечества и приписывают ей множество различных изобретений. Так, например, считается, что шумеры изобрели письменность. Для этого они использовали глиняные таблички, на которых, пока глина не застыла, каким-либо заострённым предметом выдавливали знаки. Этот вид письменности получил название «клинопись». Благодаря относительной долговечности данного материала большое количество образцов добралось до нашего времени в пригодном для расшифровки состоянии.

Но, к сожалению, этого нельзя сказать про образец, который сейчас дешифрует герой нашей истории  — Иван. Ему удалось установить, что на табличке, лежащей перед ним, описан некоторый древний танец. Символ «R» (для вашего удобства мы уже перевели их с шумерского) на ней означает шаг вправо, а символ «L» означает шаг влево. К сожалению, табличка в нескольких местах потерлась, и однозначно установить, какой там был символ, не получается; такие символы мы будем обозначать «?».

Из обычного любопытства и во имя науки Ивану стало интересно, какую максимальную ширину мог бы иметь танец. Шириной танца Иван считает расстояние между самой левой и самой правой точками танца; размером танцующего Иван решил пренебречь. Помогите Ивану подобрать вместо «?» такие символы, что длина полученного танца будет максимальна. Также Иван считает, что в исходной табличке (до того, как она потерлась в нескольких местах) были только символы «L» и «R».

## Формат ввода

Ввод содержит строку S ($1 ≤ |S| ≤ 10^5$), состоящую из символов «L», «R» и «?», — описание танца.

## Формат вывода

Выведите одно целое число — максимально возможную ширину танца.

### Пример 1

| Ввод | Вывод |
| ---- | ----- |
| R??L | 3     |

### Пример 2

| Ввод | Вывод |
| ---- | ----- |
| RLRL | 1     |

# D. Легенда об Икаре

|   |   |
|---|---|
|Ограничение времени|2 секунды|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод|
|Вывод|стандартный вывод|

Это интерактивная задача.  

Для того чтобы спастись с острова Крит и избежать гнева разгневанного Миноса, мастер Дедал изготовил для своего сына Икара крылья, скреплённые воском. Дедал предупредил Икара: «Не поднимайся слишком высоко; солнце растопит воск. Не лети слишком низко; морская вода намочит перья.»

Формально, полёт Икара подчиняется следующим правилам:

1. Если Икар находится на высоте H и H<N, морская вода будет попадать на его крылья;
    
2. Если Икар находится на высоте H и N≤H≤M, морская вода не будет попадать на его крылья, а так же солнце не будет топить воск;
    
3. Если Икар поднимется выше M, воск сразу растопится, и он упадёт, что недопустимо;
    
4. Известно, что (M−N)>N.
    

Ваша задача — помочь Икару найти высоту N — минимальную высоту, на которой морская вода не будет мочить крылья Икара. У Икара есть не более 200 попыток для нахождения высоты N, однако каждая из попыток не должна быть выше M.

Известно, что 1≤N≤M≤$10^{18}$.  
  

Протокол взаимодействия.  
  

Для осуществления запросов программа должна использовать стандартный вывод.

Ваша программа должна выводить запросы — целые числа $h_i(1≤h_i≤10^{18})$ по одному в строке. После вывода каждой строки программа должна выполнить операцию «ﬂush».

Входные данные будут содержать ответы на запросы, то есть строки вида «wet», «ok» или «fail». i-я из этих строк является результатом подъёма Икара на высоту hi.

1. Если $h_i<N$, во входных данных будет строка «wet»;
    
2. Если $N≤h_i≤M$, во входных данных будет строка «ok»;
    
3. Если $h_i>M$ или количество запросов превзошло 200, во входных данных будет строка «fail». После того как программа считала «fail», она должна немедленно завершиться.
    

Когда ваша программа нашла число N, выведите строку вида «! N» (без кавычек), где N — ответ, и завершите работу программы.  
  

Пример  

| стандартный ввод | стандартный вывод |
| ---------------- | ----------------- |
| <br>wet          | 8                 |
|                  | 11                |
| ok               | <br>9             |
| wet              | <br>10            |
| ok               | <br>! 10          |

# E. Двоичные гири майя

|   |   |
|---|---|
|Ограничение времени|2 секунды|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

В одной из пирамид майя находится секретная сокровищница. Вход в неё открывают весы; чтобы попасть в сокровищницу, нужно получить на весах ровно n килограммов.

В зале с весами стоят в ряд мешки с гирями, пронумерованные, начиная с нуля:

- Гири из нулевого мешка весят по 1 килограмму каждая;
    
- Гири из первого мешка весят по 2 килограмма каждая;
    
- Гири из второго мешка весят по 4 килограмма каждая;
    
- ...
    
- Гири из i-го мешка весят по $2_i$ килограммов каждая.
    

Можно считать, что мешков бесконечно много, и в каждом мешке бесконечно много гирь.

На стене зала написаны m магических чисел $a_1, ..., a_m$. Это варианты того, сколько гирь можно брать из каждого мешка.

Чтобы выполнить обряд, жрец майя должен сделать следующее:

- Выбрать, из скольких первых мешков он будет брать гири. Пусть это число равно k;
    
- Взять из каждого мешка с номером от 0 до (k−1) некоторое количество гирь. Для каждого из мешков число взятых гирь должно быть одним из записанных на стене (из разных мешков можно брать одинаковое число гирь, если это число записано на стене);
    
- Сложить все взятые из мешков гири на весы.
    

Например, пусть на весах нужно набрать 8 килограммов, а на стене написаны числа 0, 1 и 2. Тогда можно выполнить обряд следующими способами:

- Взять 2 гири из нулевого мешка, 1 гирю из первого мешка и 1 гирю из второго мешка;
    
- Взять 0 гирь из нулевого мешка, 2 гири из первого мешка и 1 гирю из второго мешка;
    
- Взять 0 гирь из нулевого мешка, 0 гирь из первого мешка и 2 гири из второго мешка;
    
- Взять 0 гирь из нулевого мешка, 0 гирь из первого мешка, 0 гирь из второго мешка и 1 гирю из третьего мешка.
    

Жрец майя хочет узнать, сколько у него есть способов выполнить обряд, получив на весах ровно n килограммов. Два способа считаются различными, если из хотя бы одного мешка в них берётся разное число гирь.

Помогите жрецу найти ответ на его вопрос.

## Формат ввода

Первая строка содержит целое число n ($1≤n≤10^8$) — суммарный вес в килограммах, который нужно получить.

Вторая строка содержит целое число m (1≤m≤10) — количество магических чисел, записанных на стене зала.

Третья строка содержит m различных целых чисел $a_i$ ($0≤a_i≤100$) — магические числа, записанные на стене зала.

## Формат вывода

Выведите одно целое число — количество различных способов получить суммарный вес n, соблюдая правила обряда.

Так как ответ может быть достаточно большим, выведите остаток от его деления на 1000000007 ($10^9+7$).

### Пример 1

| Ввод            | Вывод |
| --------------- | ----- |
| 8<br>3<br>0 1 2 | 4     |

### Пример 2

| Ввод               | Вывод |
| ------------------ | ----- |
| 20<br>4<br>1 3 5 6 | 3     |

# F. Нулевой Рим

|   |   |
|---|---|
|Ограничение времени|1 секунда|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

Это интерактивная задача.

В древнем Египте жил фараон-реформатор Эхнатон. Он хотел изменить религию в стране, и по этому случаю построить новый храм во имя нового бога Атона. Архитектор, который должен был строить храм, забыл узнать количество колонн, которые надо было возвести. К счастью, он мог один раз в письменной форме узнать желаемое количество у фараона, задав ему какое-то количество вопросов. К сожалению, он не знал, на сколько вопросов согласится ответить фараон. Эхнатон любил шутить, и потому мог ответить не более чем на один заданный вопрос неправильно (изменить свой ответ на противоположный). Фараон был немногословен, поэтому отвечал на вопросы только «Да» или «Нет». Он был умен и точно знал, сколько вопросов надо задать, чтобы о чём-то узнать (учитывая своё чувство юмора, разумеется), и потому запросы с большим количеством вопросов оставлял неудовлетворёнными.

Архитектор точно знает, что желаемое количество колонн не превосходит 2024, потому что большие числа ему неизвестны. И, по вполне понятным причинам, он не может построить меньше 0 колонн.

Архитектор решил не злить фараона и задавать ему очень простые вопросы: давать список чисел и спрашивать, есть ли там желаемое. Помогите ему составить список вопросов.  

## Протокол взаимодействия.

Сначала вы должны считать число 1≤t≤100 — количество чисел, загаданных программой жюри.

Ваша программа должна вывести в первой строке целое число k — количество вопросов, которое архитектор должен задать фараону.

В следующих k строках выведите наборы чисел, среди которых фараон будет искать число, соответствующее желаемому количеству колонн в храме.

В ответ программа жюри выведет t строк, на каждой из которых записаны k чисел: ответы программы жюри (0 для ответа «нет» и 1 для ответа «да» соответственно) для числа, соответствующего порядковому номеру набора.

После этого вы должны вывести t строчек, на каждой из которых — ваш ответ — угаданное вами количество колонн (в порядке наборов, данных программой жюри), и корректно завершить работу программы.

Программа, верно работающая для k≤15, получит 2 балла.

Программа, верно работающая для k=16 получит 1 балл.

Если число k больше, чем хочет фараон – он не хочет отвечать на такое количество вопросов, в ответ на ваши запросы программа жюри пришлёт вам число −1. В таком случае вы должны корректно завершить работу программы (чтобы получить корректный вердикт).

## Пример

| Ввод                       | Вывод                                               |
| -------------------------- | --------------------------------------------------- |
| 1<br><br><br><br><br>1 0 1 | <br>3<br>1 2 3 4<br>5 6 7 8<br>9 10 11 12<br><br>10 |
