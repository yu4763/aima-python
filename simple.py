from planning import *


def murder():
    return PlanningProblem(
        initial='Want(Alex, elected) & Want(Ben, elected)'
        '&Person(Alex) & Person(Ben) & Weapon(knife) & Weapon(gun) & Object(elected)',
        goals='Die(Alex)',
        actions=[
            Action('win(p)',
                   precond='Want(p, elected)',
                   effect='Win(p)',
                   domain='Person(p) & Object(elected)'),
            Action('hate(p1, p2)',
                   precond='Want(p1, elected) & Want(p2, elected) & Win(p2)',
                   effect='Hate(p1, p2)',
                   domain='Person(p1) & Person(p2)'),
            Action('get(p1, w)',
                   precond='~Have(p1, w)',
                   effect='Have(p1, w)',
                   domain='Person(p1) & Weapon(w)'),
            Action('stab(p1, p2)',
                   precond='Hate(p1, p2) & Have(p1, knife)',
                   effect='Die(p2)',
                   domain='Person(p1) & Person(p2) & Weapon(knife)')],
        domain='Person(Alex) & Person(Ben) & Weapon(knife) & Weapon(gun) & Object(elected)')


st = murder()

pop = PartialOrderPlanner(st)

pop.execute()
