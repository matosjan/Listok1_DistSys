# Задача 1
Код в файле rpc_server.py

# Задача 2

### Синхронная модель
Так как рассматриваем синхронный случай, то все 1000 вызовов $`f_B`$ на узле $`A`$ выполняются последовательно, поэтому посчитаем время затрачиваемое на выполнение одного такого вызова. 
1. Из $`A`$ вызывается $`f_B`$
2. На 100-ой мс $`B`$ получает сообщение от $`A`$, и начинает выполняться $`f_B`$
3. Из $`f_B`$ вызываeтся(отправлаeтся сообщениe) на 100-ой мс $`f_D`$(или $`f_C`$)
4. На 200-ой мс $`D`$ получает сообщение о вызове $`f_D`$ из $`B`$, $`f_D`$ выполняется за 0 мс
5. На 200-ой мс из $`D`$ отправляется сообщение в $`B`$ o завершении $`f_D`$
6. На 300-ой мс $`B`$ получает ответное сообщение из $`D`$
7. На 301-ой мс из $`B`$ вызываeтся(отправлаeтся сообщениe) $`f_C`$(или $`f_D`$)
8. На 401-ой мс $`C`$ получает сообщение о вызове $`f_C`$ из $`B`$, $`f_C`$ выполняется за 0 мс
9. На 401-ой мс из $`C`$ отправляется сообщение в $`B`$ o завершении $`f_C`$
10. На 501-ой мс $`B`$ получает ответное сообщение из $`D`$
11. На 501-ой мс завершается $`f_B`$ и отправляется сообщение в $`A`$ о завершении
12. На 601-ой мс ответное сообщение доходит до $`A`$
    
Таким образом, один вызов $`f_B`$ на узле $`A`$ длится 601 мс, следовательно 1000 вызовов длятся 601000 мс = 601 сек   
**Ответ: 601 сек**

### Асинхронная модель
В такой модели можем делать следующий вызов, не дожидаясь завершения предыдущего вызова. Поэтому:
1. В отрезке [0, 1000] мс будут сделаны 1000 вызовов $`f_B`$ на узле $`A`$
2. В отрезке [100, 1100] мс все сообщения о вызовах $`f_B`$ из $`A`$ дойдут до узла $`B`$
3. В мс поступления сообщения из $`A`$ будет вызван $`f_D`$(или $`f_C`$) на узле $`B`$, то есть в отрезке [100, 2100] будут вызваны 1000 раз $`f_D`$, и 1000 раз $`f_C`$ на узле $`B`$
4. В отрезке [200, 2200] в $`D`$ и $`C`$ поступят сообщения из $`B`$ о вызовах соотеветственно $`f_D`$ и $`f_C`$ которые завершаться за 0 мс
5. В отрезке [200, 2200] ответные сообщения о завершении направятся из $`D`$ и $`C`$ в $`B`$
6. В отрезке [300, 2300] эти сообщения поступят в $`B`$
7. В отрезке [300, 2300] из $`B`$ в $`A`$ направятся ответные сообщения
8. В отрезке [400, 2400] эти сообщения поступят в $`A`$

Таким образом, в асинхронной модели 1000 вызовов $`f_B`$ на узле $`A`$ займут 2400 мс   
**Ответ: 2400 сек**
