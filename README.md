# cow_006
## **Описание игры**

**Игра "Корова 006"** — это карточная игра, в которой используются карты с номерами от 1 до 104 и количеством штрафных очков на каждой ("коровьи головы" или просто "головы"). В игре участвуют 2-10 игроков.


## **Цель игры**
  
Набрать как можно меньше штрафных очков (ими обладают все карты коров-агентов, но их число на разных картах отличается). 

## **Комплектность игры:**

Карты 5 цветов (зеленый, голубой, желтый, красный, фиолетовый) с номерами от 1 до 104 и количеством штрафных очков на каждой:
+ 76 карт: Зеленые — 1 штрафное очко
+ 9 карт: Голубые — 2 штрафных очка
+ 10 карт: Желтые — 3 штрафных очка
+ 8 карт: Красные — 5 штрафных очков
+ 1 карта: Фиолетовая — 7 штрафных очков
    
## **Раздача карт:**
  Каждому игроку раздается 10 карт в закрытую.
  Из колоды берутся 4 карты, которые кладутся в 4 ряда по одной.

## **Условие поражения:**
  В начале игры каждый игрок имеет 0 штрафных очков. Игрок проигрывает, когда получает 66 и более штрафных очков. 

## **Подготовка к игре:**
+  Карты перетасовываются и раздаются по 10 штук каждому игроку. Остальная колода откладывается до следующей партии.
+ Из колоды берутся 4 карты и кладутся лицевой стороной вверх по одной в ряд (с них будут начинаться 4 рада карт).

## **Ход игры:**
  Игра длится несколько партий. 
+ Игроки не видят карты друг друга. В каждый ход игроки выбирают по 1 карте из своей руки.
+ Выбранные карты сортируются в порядке возрастания и выкладываются на поле по очереди (сначала самая младшая и т.д.).
+ Каждая карта кладется в конец ряда, в котором последняя ранее выложенная карта ближе всего к ней по значению. _!Обязательное условие!_ Выложенная карта должна быть больше карты в ряду (например: последняя карта в ряду имеет номер 6, а среди выложенных четырьмя участниками карт: 4, 10, 56, 77, в данный ряд может встать только карта с номером 10).
+ Если карта по значению оказалась меньше всех последних чисел рядов, то игрок выбирает любой ряд и _забирает_ из него все карты, а свою оставляет, начиная новый ряд.
+ Если карта оказалась **шестой** в ряду - игрок _забирает_ все 5 карт этого ряда, а свою оставляет, начиная новый ряд.
+ Каждый раз, когда игрок _берет_ карты, ему добавляется количество очков, равное количеству голов на взятых картах.
+ Одна партия длится 10 ходов (до тех пор, пока у всех игроков не закончатся карты).

Игра заканчивается, когда по результатам нескольких туров кто-нибудь набирает 66 штрафных очков или больше – он объявляется проигравшим.
  
## **Примечания:**
  Может, эта закономерность поможет лучше ориентироваться в картах:
+ Агенты с номерами кратными 5 (5, 15, 25 и т.д. ) имеют 2-й ранг (голубые карты).
+ Агенты с номерами кратными 10 (10, 20, 30 и т.д.) имеют 3-й ранг (желтые карты).
+ «Двойные агенты», у которых цифры в номере одинаковые (11, 22, 33 и т.д.) имеют 5-й ранг (красные карты).
+ Агент 55 – «суперагент», он имеет номер кратный 5, а также относится к «двойным агентам», поэтому его ранг 7 (фиолетовая карта).
+ У всех остальных агентов 1-й ранг (зеленые карты).


## Пример текстового интерфейста игры
Игроки: Ast and P1. 
```
Master: Игрокам раздаются карты
Ast(0): Ваши карты: [82<1>]  [102<1>]  [35<2>]  [65<2>]  [33<1>]  [66<5>]  [44<5>]  [98<1>]  [97<1>]  [25<2>]
(P1(0): Карты P1: [12<1>]  [71<1>]  [5<1>]  [81<1>]  [49<1>]  [21<1>]  [3<1>]  [85<2>]  [22<5>]  [26<1>])
r1: [39<1>]
r2: [89<1>]
r3: [80<3>]
r4: [77<1>]
Master: Игроки выбирают карту
Ast(0): введите карту, которую играем из руки: [104<1>]
Ast(0): такой карты нет в руке
Ast(0): введите карту, которую играем из руки: [82<1>]
Ast(0): карта выбрана
P1(0): выбирает карту
P1(0): карта выбрана ([85<2>])
Master: открытие карт: [82<1>]  [85<2>]
Master: следующий ход
---
r1: [39<1>]
r2: [89<1>] 
r3: [80<3>]  [82<1>]  [85<2>]
r4: [77<1>]
Ast(0): Ваши карты: [102<1>]  [35<2>]  [65<2>]  [33<1>]  [66<5>]  [44<5>]  [98<1>]  [97<1>]  [25<2>]
(P1(0): Карты P1: [12<1>]  [71<1>]  [5<1>]  [81<1>]  [49<1>]  [21<1>]  [3<1>]  [22<5>]  [26<1>])
Master: Игроки выбирают карту
Ast(0): введите карту, которую играем из руки: [33<1>]
Ast(0): карта выбрана
P1(0): выбирает карту
P1(0): карта выбрана ([49<1>])
Master: открытие карт: [33<5>]  [49<1>]
Ast(0): ваша карта не подходит ни одному ряду! введите ряд, который хотите забрать: 2
Master: игрок Ast забирает ряд 2 
Master: игрок Ast получает штрафные баллы: 1
Master: следующий ход
---
r1: [39<1>] [49<1>]
r2: [33<5>]
r3: [80<3>]  [82<1>]  [85<2>]
r4: [77<1>]
Ast(1): Ваши карты: [102<1>]  [35<2>]  [65<2>]  [66<5>]  [44<5>]  [98<1>]  [97<1>]  [25<2>]
(P1(0): Карты P1: [12<1>]  [71<1>]  [5<1>]  [81<1>]  [21<1>]  [3<1>]  [22<5>]  [26<1>])
Master: Игроки выбирают карту
Ast(1): введите карту, которую играем из руки: [97<1>]
Ast(1): карта выбрана
P1(0): выбирает карту
P1(0): карта выбрана ([81<1>])
Master: открытие карт: [81<1>]  [97<1>]
Master: следующий ход
---
r1: [39<1>] [49<1>]
r2: [33<5>]
r3: [80<3>]  [82<1>]  [85<2>]  [97<1>]
r4: [77<1>] [81<1>]
...
---
r1: [39<1>] [49<1>]
r2: [33<5>]
r3: [80<3>]  [82<1>]  [85<2>]  [97<1>]  [81<1>]
r4: [3<1>]
Ast(..): Ваши карты: [102<1>]  [35<2>]  [65<2>]  [66<5>]  [44<5>]  [25<2>]
(P1(..): Карты А1: [71<1>]  [5<1>]  [81<1>]  [21<1>]  [22<5>]  [26<1>])
Master: Игроки выбирают карту
Ast(..): введите карту, которую играем из руки: [102<1>]
Ast(..): карта выбрана
P1(..): выбирает карту
P1(..): карта выбрана ([5<1>])
Master: открытие карт: [g5<1>]  [102<1>]
Ast(..): ваша карта 6-я в третьем ряду
Master: игрок Ast забирает ряд 3 
Master: игрок Ast получает штрафные баллы: 8
Master: следующий ход
---
r1: [39<1>]  [49<1>]
r2: [33<5>]
r3: [102<1>]
r4: [3<1>]  [5<1>]
...
---
Master: игрок P1 получил 68 штрафных очков!
Master: игра окончена
Master: оглашение результатов игры
Ast: Победитель: 54 штрафных очков
P1: Проигравший: 68 штрафных очков
``` 

## Пример save-файла 
Начало игры.
```json
{
  "row1": "[39<1>]",
  "row2": "[89<1>]",
  "row3": "[80<3>]",
  "row4": "[77<1>]",
  "current_player_index": 0,
  "players": [
    {
      "name": "Ast",
      "hand": "[82<1>]  [102<1>]  [35<2>]  [65<2>]  [33<1>]  [66<5>]  [44<5>]  [98<1>]  [97<1>]  [25<2>]",
      "score": 0,
      "is_human": true
    },
    {
      "name": "P1",
      "hand": "[12<1>]  [71<1>]  [5<1>]  [81<1>]  [49<1>]  [21<1>]  [3<1>]  [85<2>]  [22<5>]  [26<1>]",
      "score": 0,
      "is_human": false
    }
  ]
}
```






















