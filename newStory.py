from planning import *


def murder():
    return PlanningProblem(
        initial='Love(Alex, Diana) & Love(Ben, Diana) & ~Love(Diana, Alex) & ~Love(Diana, Alex)'
                '& ~Love(Alex, Ben) & ~Love(Ben, Alex) & ~Hate(Alex, Diana) & ~Hate(Ben, Diana)'
                '& ~Hate(Diana, Alex) & ~Hate(Diana, Ben) & ~Hate(Alex, Ben) & ~Hate(Ben, Alex)'
                ' & Want(Alex, elected) & Want(Ben, elected)',
        goals='Die(Alex)',
        actions=[
            Action('fall_in_love(p1, p2)',
                   precond='~Love(p1, p2) & ~Hate(p1, p2)',
                   effect='Love(p1, p2)',
                   domain='Person(p1) & Person(p2)'),
            Action('hate(p1, p2)',
                   precond='Love(p1, Diana) & Love(p2, Diana) & love(Diana, p2) & ~love(p1, p2)',
                   effect='Hate(p1, p2)',
                   domain='Person(p1) & Person(p2)  '),
            Action('get(p1, w)',
                   precond='~Have(p1, w)',
                   effect='Have(p1, w)',
                   domain='Person(p1) & Weapon(w)'),
            Action('stab(p1, p2)',
                   precond='Hate(p1, p2) & Have(p1, knife)',
                   effect='Die(p2)',
                   domain='Person(p1) & Person(p2) & Weapon(knife)')],
        domain='Person(Alex) & Person(Diana) & Person(Ben) & Weapon(knife) & Weapon(gun) & Object(elected)')


st = murder()
st.goal_test()

pop = PartialOrderPlanner(st)

pop.execute()
