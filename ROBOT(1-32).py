#EXERCISE1                            
from pyrob.api import *


@task
def task_1_1():
    pass
    move_right(2)
    move_down()


if __name__ == '__main__':
    run_tasks()
	
#EXERCISE2
from pyrob.api import *


@task
def task_1_2():
    pass
    move_down(2)
    move_right(2)
    fill_cell()
    move_right(2)
    move_down()

if __name__ == '__main__':
    run_tasks()

	
#EXERCISE3
from pyrob.api import *


@task
def task_3_1():
    pass
    while wall_is_on_the_right() != True:
        move_right()

if __name__ == '__main__':
    run_tasks()
	
#EXERCISE4
from pyrob.api import *


@task
def task_3_3():
    pass
    if wall_is_above() == False:
        move_up()
    elif wall_is_on_the_right() == False:
        move_right()
    elif wall_is_beneath() == False:
        move_down()
    else:
        move_left()


if __name__ == '__main__':
    run_tasks()
	
#EXERCISE5
from pyrob.api import *


@task
def task_5_2():
    pass
    while wall_is_beneath() == True:
        move_right()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE6
from pyrob.api import *


@task
def task_5_3():
    pass
    while wall_is_beneath() == False:
        move_right()
    while wall_is_beneath() == True:
        move_right()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE7
from pyrob.api import *


@task
def task_5_4():
    pass
    while wall_is_beneath() == False:
        move_down()
    while wall_is_beneath() == True:
        move_right()
    move_down()
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE8
from pyrob.api import *


@task
def task_5_7():
    pass
    while (wall_is_above() == True) or (wall_is_beneath() == True):
        move_right()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE9
from pyrob.api import *


@task
def task_8_2():
    pass
    while wall_is_on_the_right() == False:
        if (wall_is_above() == False) and (wall_is_beneath() == True):
            fill_cell()
        move_right()
        if (wall_is_above() == False) and (wall_is_beneath() == True):
            fill_cell()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE10
from pyrob.api import *


@task
def task_8_3():
    pass
    while wall_is_on_the_right() == False:
        if (wall_is_above() == True) or (wall_is_beneath() == True):
            fill_cell()
        move_right()
        if (wall_is_above() == True) or (wall_is_beneath() == True):
            fill_cell()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE11
from pyrob.api import *


@task
def task_8_4():
    pass
    while wall_is_on_the_right() == False:
        if (wall_is_above() == True) and (wall_is_beneath() == True):
            fill_cell()
        move_right()
        if (wall_is_above() == True) and (wall_is_beneath() == True):
            fill_cell()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE12
from pyrob.api import *


@task
def task_8_6():
    pass
    while wall_is_on_the_right() == False:
        if (wall_is_above() == False) and (wall_is_beneath() == True):
            fill_cell()
        move_right()
        if (wall_is_above() == False) and (wall_is_beneath() == True):
            fill_cell()


if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE13
from pyrob.api import *


@task
def task_8_10():
    pass
    def paint():
        if wall_is_above() == False:
                move_up()
                fill_cell()
                move_down()
        if wall_is_beneath() == False:
                move_down()
                fill_cell()
                move_up()
    while wall_is_on_the_right() == False:
        paint()
        move_right()
    paint()

if __name__ == '__main__':
    run_tasks()

	
#EXERCISE14
from pyrob.api import *


@task
def task_8_11():
    pass
    def paint():
        if wall_is_above() == False:
                move_up()
                fill_cell()
                move_down()
        if wall_is_beneath() == False:
                move_down()
                fill_cell()
                move_up()
        if (wall_is_above() == True) and (wall_is_beneath() == True):
                fill_cell()
    while wall_is_on_the_right() == False:
        paint()
        move_right()
    paint()

if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE15
from pyrob.api import *


@task
def task_8_21():
    pass
    if wall_is_on_the_left() == True:
        if wall_is_above() == True:
            while wall_is_beneath() == False:
                move_down()
        else:
            while wall_is_above() == False:
                move_up()
        while wall_is_on_the_right() == False:
            move_right()
    else:
        if wall_is_above() == True:
            while wall_is_beneath() == False:
                move_down()
        else:
            while wall_is_above() == False:
                move_up()
        while wall_is_on_the_left() == False:
            move_left()
        
        
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE16
from pyrob.api import *


@task
def task_8_22():
    pass
    while wall_is_on_the_left() == wall_is_on_the_right() == True:
        move_up()
    if wall_is_on_the_left() == False:
        while wall_is_on_the_left() == False:
            move_left()
    else:
        while wall_is_on_the_right() == False:
            move_right()
        
        
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE17
from pyrob.api import *


@task
def task_8_27():
    pass
    while cell_is_filled() == False:
        move_up()
    move_right()
    if cell_is_filled() == False:
        move_left(2)
        
        
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE18
from pyrob.api import *


@task
def task_8_28():
    pass
    while (wall_is_above() == True) and (wall_is_on_the_right() == False):
        move_right()
    if (wall_is_above() == False):
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()
    else:
        while (wall_is_above() == True) and (wall_is_on_the_left() == False):
            move_left()
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()
        
        
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE19
from pyrob.api import *


@task
def task_8_29():
    pass
    while wall_is_on_the_left() == False:
        move_left()
    if wall_is_above() == False:
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()
    else:
        while wall_is_on_the_right() == False:
            move_right()
        if wall_is_above() == False:
            while wall_is_above() == False:
                move_up()
            while wall_is_on_the_left() == False:
                move_left()
        
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE20
from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    pass
    move_right()
    for i in range(6):
        for i in range(26):
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        for i in range(26):
            fill_cell()
            move_left()
        fill_cell()
        move_down()



if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE21
from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    pass
    n = 3
    move_right()
    move_down()
    fill_cell()
    move_down()
    for i in range(6):
        for i in range(1, n):
            fill_cell()
            move_right() 
        move_down()
        fill_cell()
        for i in range(1,n):
            fill_cell()
            move_left()
        fill_cell()
        move_down()
        n += 2



if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE22
from pyrob.api import *


@task
def task_5_10():
    pass
    fill_cell()
    while wall_is_beneath() == False:
        while wall_is_on_the_right() == False:
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        while wall_is_on_the_left() == False:
            fill_cell()
            move_left()
        fill_cell()
        if wall_is_beneath() == False:
            move_down()
    if wall_is_beneath() == True:
        fill_cell()
        while wall_is_on_the_right() == False:
            move_right()
            fill_cell()
        while wall_is_on_the_left() == False:
            move_left()
    

if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE23
from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    pass
    while wall_is_on_the_right() == False:
        move_right()
        while wall_is_above() == False:
            move_up()
            fill_cell()
        while wall_is_beneath() == False:
            move_down()
    while (wall_is_above() == True) or (wall_is_beneath() == True):
        move_left()
            
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE24
from pyrob.api import *


@task(delay=0.05)
def task_2_1():
    pass
    def krest():
        move_down()
        fill_cell()
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_right()
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_left()
    move_down()
    move_right()
    krest()
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE25
from pyrob.api import *


@task(delay=0.05)
def task_2_2():
    pass
    def krest():
        move_down()
        fill_cell()
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_right()
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_left()
    move_down()
    for i in range(4):
        krest()
        move_right(4)
    krest()
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE26
from pyrob.api import *


@task(delay=0.01)
def task_2_4():
    pass
    def krest():
        move_down()
        fill_cell()
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_right()
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_left()
    for i in range(2):
        for i in range(9):
            krest()
            move_right(4)
        krest()
        move_down(4)
        for i in range(9):
            krest()
            move_left(4)
        krest()
        move_down(4)
    krest()
    for i in range(9):
        move_right(4)
        krest()
    move_left(36) 
        
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE27
from pyrob.api import *


@task
def task_7_5():
    pass
    n = 0
    i = 0
    move_right()
    fill_cell()
    while wall_is_on_the_right() == False:
        if i == n:
            n += +1
            i = 0
            fill_cell()
        i += 1
        move_right()
        
        
    
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE28
from pyrob.api import *


@task
def task_7_6():
    pass
    i = 0
    while wall_is_on_the_right() == False:
        if cell_is_filled() == True:
            i += 1
        if i == 5:
            break
        move_right()
        
        
    
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE29
from pyrob.api import *


@task
def task_7_7():
    pass
    i = 0
    while wall_is_on_the_right() == False:
        if cell_is_filled() == True:
            i += 1
        else:
            i = 0
        if i == 3:
            break
        move_right()
        
        
    
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE30
from pyrob.api import *


@task
def task_9_3():
    pass
    n = 1
    i = 1
    j = 0
    move_right()
    while wall_is_on_the_right() == False:
        fill_cell()
        move_right()
        i += 1
    while wall_is_beneath() == False:
        move_down()
        for k in range (i):
            if (k != i - n) and (k != n):
                fill_cell()
            move_left()
        fill_cell()
        n += 1
        move_down()
        for k in range (i):
            if (k != i - n) and (k != n):
                fill_cell()
            move_right()
        j += 2
        if j != i:
            fill_cell()
        n += 1
    move_left(i)
                
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE31
from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    pass
    i1 = 0
    i2 = 0
    while wall_is_on_the_left() == False:
        move_left()
        i2 += 1
    while i1 != i2:
        i1 = 0
        while wall_is_beneath() == True:
            move_right()
            i1 += 1
            if i1 == i2:
                move_left(i2)
                fill_cell()
                break
        while wall_is_beneath() == False:
            move_down()
        while wall_is_on_the_left() == False:
            move_left()
            
if __name__ == '__main__':
    run_tasks()
	
	
#EXERCISE32
from pyrob.api import *
​
​
@task(delay=0.01)
def task_8_18():
    pass
    i = 0
    while wall_is_beneath() == True:
        if wall_is_above() == True:
            fill_cell()
        else:
            while wall_is_above() == False:
                move_up()
                if cell_is_filled() == False:
                    fill_cell()
                else:
                    i += 1
            while wall_is_beneath() == False:
                move_down()
        move_right()
    
    mov('ax', i)
            
if __name__ == '__main__':
    run_tasks()