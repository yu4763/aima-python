from planning import *


def murder():
    return PlanningProblem(
        initial='Married(Alex) & Married(Ann) & MarryWith(Alex, Ann) & MarryWith(Ann, Alex) '
                '& Single(Diana) & WorkAt(Alex, School) & WorkAt(Diana, School) ',
        goals='plan_to_kill(Alex, Diana)',
        actions=[
            Action('have_an_affair(p1, p2)',
                   precond='Married(p1) & Love(p1, p2) & Love(p2, p1) & Person(p1) & Person(p2)',
                   effect='Affair(p1, p2)',
                   domain='Person(p1) & Person(p2)'
                   ),
            Action('fall_in_love(p1, p2, l)',
                   precond='WorkAt(p1, l) & WorkAt(p2, l) & Person(p1) & Person(p2) & Location(l)',
                   effect='Love(p1, p2) & Love(p2, p1)',
                   domain='Person(p1) & Person(p2) & Location(l)'
                   ),
            Action('want_to_reveal_affair_to(p1, p2, p3)',
                   precond='Affair(p1, p2) & MarryWith(p1, p3)',
                   effect='plan_to_kill(p1, p2)',
                   domain='Person(p1) & Person(p2) & Person(p3)'
                   ),
        ],
        domain='Person(Ann) & Person(Alex) & Person(Diana) & Location(School)'
    )


st = murder()
pop = PartialOrderPlanner(st)
pop.execute()
