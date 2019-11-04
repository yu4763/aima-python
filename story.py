from planning import *


def be_robbed():
    return PlanningProblem(
        initial='Rich(Alex) & Poor(Ben)',
        goals='Robbed(Alex)',
        actions=[
            Action('ask_for_help(p1, p2)',
                   precond='Poor(p1)',
                   effect='Asked(p2, p1)'),
            Action('deny(p2, p1)',
                   precond='Asked(p2, p1)',
                   effect='~Asked(p2, p1) & Angry(p1, p2)'),
            Action('accept(p2, p1)',
                   precond='Asked(p2, p1)',
                   effect='~Asked(p2, p1) & ~Rich(p2) & Poor(p2)'),
            Action('rob(p1, p2)',
                   precond='Angry(p1, p2) & Poor(p1)',
                   effect='Poor(p2) & ~Rich(p2) & Robbed(p2) & Rich(p1) & ~Poor(p1)'),

        ])


def find_thief():
    return PlanningProblem(
        initial='Detective(Sherlock) & Suspect(Ben) & Victim(Alex)',
        goals='Find_Criminal(Ben)',
        actions=[
            Action('ask_for_help(p1, p2)',
                   precond='Poor(p1)',
                   effect='Asked(p2, p1)'),
            Action('deny(p2, p1)',
                   precond='Asked(p2, p1)',
                   effect='~Asked(p2, p1) & Angry(p1, p2)'),
            Action('accept(p2, p1)',
                   precond='Asked(p2, p1)',
                   effect='~Asked(p2, p1) & ~Rich(p2) & Poor(p2)'),
            Action('rob(p1, p2)',
                   precond='Angry(p1, p2) & Poor(p1)',
                   effect='Poor(p2) & ~Rich(p2) & Robbed(p2) & Rich(p1) & ~Poor(p1)'),

        ])


st = be_robbed();
st.act(expr('ask_for_help(Ben, Alex)'));
st.act(expr('deny(Alex, Ben)'));
st.act(expr('rob(Ben, Alex)'));

# pop = PartialOrderPlanner(st)
# pop.execute()
