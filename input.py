expand_actions insdie
name: None
had_domain: True
domain-action: fall_in_love(p1, p2)
domain Person(p1) & Person(p2)
precond [NotLove(p1, p2), NotHate(p1, p2), Person(p1), Person(p2)]
domain-action: hate(p1, p2)
domain Person(p1) & Person(p2)  
precond [Love(p1, Diana), Love(p2, Diana), love(Diana, p2), Notlove(p1, p2), Person(p1), Person(p2)]
domain-action: get(p1, w)
domain Person(p1) & Weapon(w)
precond [NotHave(p1, w), Person(p1), Weapon(w)]
domain-action: stab(p1, p2)
domain Person(p1) & Person(p2) & Weapon(knife)
precond [Hate(p1, p2), Have(p1, knife), Person(p1), Person(p2), Weapon(knife)]
objects {knife, Alex, gun, elected, Ben, Diana}
action_list: [fall_in_love(p1, p2), hate(p1, p2), get(p1, w), stab(p1, p2)]
loop start with action: fall_in_love(p1, p2)
bindings: {p1: knife, p2: Alex}
bindings: {p1: knife, p2: gun}
bindings: {p1: knife, p2: elected}
bindings: {p1: knife, p2: Ben}
bindings: {p1: knife, p2: Diana}
bindings: {p1: Alex, p2: knife}
bindings: {p1: Alex, p2: gun}
bindings: {p1: Alex, p2: elected}
bindings: {p1: Alex, p2: Ben}
bindings: {p1: Alex, p2: Diana}
bindings: {p1: gun, p2: knife}
bindings: {p1: gun, p2: Alex}
bindings: {p1: gun, p2: elected}
bindings: {p1: gun, p2: Ben}
bindings: {p1: gun, p2: Diana}
bindings: {p1: elected, p2: knife}
bindings: {p1: elected, p2: Alex}
bindings: {p1: elected, p2: gun}
bindings: {p1: elected, p2: Ben}
bindings: {p1: elected, p2: Diana}
bindings: {p1: Ben, p2: knife}
bindings: {p1: Ben, p2: Alex}
bindings: {p1: Ben, p2: gun}
bindings: {p1: Ben, p2: elected}
bindings: {p1: Ben, p2: Diana}
bindings: {p1: Diana, p2: knife}
bindings: {p1: Diana, p2: Alex}
bindings: {p1: Diana, p2: gun}
bindings: {p1: Diana, p2: elected}
bindings: {p1: Diana, p2: Ben}
loop start with action: hate(p1, p2)
bindings: {p1: knife, p2: Alex}
bindings: {p1: knife, p2: gun}
bindings: {p1: knife, p2: elected}
bindings: {p1: knife, p2: Ben}
bindings: {p1: knife, p2: Diana}
bindings: {p1: Alex, p2: knife}
bindings: {p1: Alex, p2: gun}
bindings: {p1: Alex, p2: elected}
bindings: {p1: Alex, p2: Ben}
bindings: {p1: Alex, p2: Diana}
bindings: {p1: gun, p2: knife}
bindings: {p1: gun, p2: Alex}
bindings: {p1: gun, p2: elected}
bindings: {p1: gun, p2: Ben}
bindings: {p1: gun, p2: Diana}
bindings: {p1: elected, p2: knife}
bindings: {p1: elected, p2: Alex}
bindings: {p1: elected, p2: gun}
bindings: {p1: elected, p2: Ben}
bindings: {p1: elected, p2: Diana}
bindings: {p1: Ben, p2: knife}
bindings: {p1: Ben, p2: Alex}
bindings: {p1: Ben, p2: gun}
bindings: {p1: Ben, p2: elected}
bindings: {p1: Ben, p2: Diana}
bindings: {p1: Diana, p2: knife}
bindings: {p1: Diana, p2: Alex}
bindings: {p1: Diana, p2: gun}
bindings: {p1: Diana, p2: elected}
bindings: {p1: Diana, p2: Ben}
loop start with action: get(p1, w)
bindings: {p1: knife, w: Alex}
bindings: {p1: knife, w: gun}
bindings: {p1: knife, w: elected}
bindings: {p1: knife, w: Ben}
bindings: {p1: knife, w: Diana}
bindings: {p1: Alex, w: knife}
bindings: {p1: Alex, w: gun}
bindings: {p1: Alex, w: elected}
bindings: {p1: Alex, w: Ben}
bindings: {p1: Alex, w: Diana}
bindings: {p1: gun, w: knife}
bindings: {p1: gun, w: Alex}
bindings: {p1: gun, w: elected}
bindings: {p1: gun, w: Ben}
bindings: {p1: gun, w: Diana}
bindings: {p1: elected, w: knife}
bindings: {p1: elected, w: Alex}
bindings: {p1: elected, w: gun}
bindings: {p1: elected, w: Ben}
bindings: {p1: elected, w: Diana}
bindings: {p1: Ben, w: knife}
bindings: {p1: Ben, w: Alex}
bindings: {p1: Ben, w: gun}
bindings: {p1: Ben, w: elected}
bindings: {p1: Ben, w: Diana}
bindings: {p1: Diana, w: knife}
bindings: {p1: Diana, w: Alex}
bindings: {p1: Diana, w: gun}
bindings: {p1: Diana, w: elected}
bindings: {p1: Diana, w: Ben}
loop start with action: stab(p1, p2)
bindings: {p1: knife, p2: Alex}
bindings: {p1: knife, p2: gun}
bindings: {p1: knife, p2: elected}
bindings: {p1: knife, p2: Ben}
bindings: {p1: knife, p2: Diana}
bindings: {p1: Alex, p2: knife}
bindings: {p1: Alex, p2: gun}
bindings: {p1: Alex, p2: elected}
bindings: {p1: Alex, p2: Ben}
bindings: {p1: Alex, p2: Diana}
bindings: {p1: gun, p2: knife}
bindings: {p1: gun, p2: Alex}
bindings: {p1: gun, p2: elected}
bindings: {p1: gun, p2: Ben}
bindings: {p1: gun, p2: Diana}
bindings: {p1: elected, p2: knife}
bindings: {p1: elected, p2: Alex}
bindings: {p1: elected, p2: gun}
bindings: {p1: elected, p2: Ben}
bindings: {p1: elected, p2: Diana}
bindings: {p1: Ben, p2: knife}
bindings: {p1: Ben, p2: Alex}
bindings: {p1: Ben, p2: gun}
bindings: {p1: Ben, p2: elected}
bindings: {p1: Ben, p2: Diana}
bindings: {p1: Diana, p2: knife}
bindings: {p1: Diana, p2: Alex}
bindings: {p1: Diana, p2: gun}
bindings: {p1: Diana, p2: elected}
bindings: {p1: Diana, p2: Ben}
init
actions {Start, Finish}
expanded_actions: [fall_in_love(knife, Alex), fall_in_love(knife, gun), fall_in_love(knife, elected), fall_in_love(knife, Ben), fall_in_love(knife, Diana), fall_in_love(Alex, knife), fall_in_love(Alex, gun), fall_in_love(Alex, elected), fall_in_love(Alex, Ben), fall_in_love(Alex, Diana), fall_in_love(gun, knife), fall_in_love(gun, Alex), fall_in_love(gun, elected), fall_in_love(gun, Ben), fall_in_love(gun, Diana), fall_in_love(elected, knife), fall_in_love(elected, Alex), fall_in_love(elected, gun), fall_in_love(elected, Ben), fall_in_love(elected, Diana), fall_in_love(Ben, knife), fall_in_love(Ben, Alex), fall_in_love(Ben, gun), fall_in_love(Ben, elected), fall_in_love(Ben, Diana), fall_in_love(Diana, knife), fall_in_love(Diana, Alex), fall_in_love(Diana, gun), fall_in_love(Diana, elected), fall_in_love(Diana, Ben), hate(knife, Alex), hate(knife, gun), hate(knife, elected), hate(knife, Ben), hate(knife, Diana), hate(Alex, knife), hate(Alex, gun), hate(Alex, elected), hate(Alex, Ben), hate(Alex, Diana), hate(gun, knife), hate(gun, Alex), hate(gun, elected), hate(gun, Ben), hate(gun, Diana), hate(elected, knife), hate(elected, Alex), hate(elected, gun), hate(elected, Ben), hate(elected, Diana), hate(Ben, knife), hate(Ben, Alex), hate(Ben, gun), hate(Ben, elected), hate(Ben, Diana), hate(Diana, knife), hate(Diana, Alex), hate(Diana, gun), hate(Diana, elected), hate(Diana, Ben), get(knife, Alex), get(knife, gun), get(knife, elected), get(knife, Ben), get(knife, Diana), get(Alex, knife), get(Alex, gun), get(Alex, elected), get(Alex, Ben), get(Alex, Diana), get(gun, knife), get(gun, Alex), get(gun, elected), get(gun, Ben), get(gun, Diana), get(elected, knife), get(elected, Alex), get(elected, gun), get(elected, Ben), get(elected, Diana), get(Ben, knife), get(Ben, Alex), get(Ben, gun), get(Ben, elected), get(Ben, Diana), get(Diana, knife), get(Diana, Alex), get(Diana, gun), get(Diana, elected), get(Diana, Ben), stab(knife, Alex), stab(knife, gun), stab(knife, elected), stab(knife, Ben), stab(knife, Diana), stab(Alex, knife), stab(Alex, gun), stab(Alex, elected), stab(Alex, Ben), stab(Alex, Diana), stab(gun, knife), stab(gun, Alex), stab(gun, elected), stab(gun, Ben), stab(gun, Diana), stab(elected, knife), stab(elected, Alex), stab(elected, gun), stab(elected, Ben), stab(elected, Diana), stab(Ben, knife), stab(Ben, Alex), stab(Ben, gun), stab(Ben, elected), stab(Ben, Diana), stab(Diana, knife), stab(Diana, Alex), stab(Diana, gun), stab(Diana, elected), stab(Diana, Ben)]
agenda: {(Die(Alex), Finish)}
agenda: {(Die(Alex), Finish)}
1
find_open_precondition
open_precondition: Die(Alex)
possible_actions:  [Start, Finish, fall_in_love(knife, Alex), fall_in_love(knife, gun), fall_in_love(knife, elected), fall_in_love(knife, Ben), fall_in_love(knife, Diana), fall_in_love(Alex, knife), fall_in_love(Alex, gun), fall_in_love(Alex, elected), fall_in_love(Alex, Ben), fall_in_love(Alex, Diana), fall_in_love(gun, knife), fall_in_love(gun, Alex), fall_in_love(gun, elected), fall_in_love(gun, Ben), fall_in_love(gun, Diana), fall_in_love(elected, knife), fall_in_love(elected, Alex), fall_in_love(elected, gun), fall_in_love(elected, Ben), fall_in_love(elected, Diana), fall_in_love(Ben, knife), fall_in_love(Ben, Alex), fall_in_love(Ben, gun), fall_in_love(Ben, elected), fall_in_love(Ben, Diana), fall_in_love(Diana, knife), fall_in_love(Diana, Alex), fall_in_love(Diana, gun), fall_in_love(Diana, elected), fall_in_love(Diana, Ben), hate(knife, Alex), hate(knife, gun), hate(knife, elected), hate(knife, Ben), hate(knife, Diana), hate(Alex, knife), hate(Alex, gun), hate(Alex, elected), hate(Alex, Ben), hate(Alex, Diana), hate(gun, knife), hate(gun, Alex), hate(gun, elected), hate(gun, Ben), hate(gun, Diana), hate(elected, knife), hate(elected, Alex), hate(elected, gun), hate(elected, Ben), hate(elected, Diana), hate(Ben, knife), hate(Ben, Alex), hate(Ben, gun), hate(Ben, elected), hate(Ben, Diana), hate(Diana, knife), hate(Diana, Alex), hate(Diana, gun), hate(Diana, elected), hate(Diana, Ben), get(knife, Alex), get(knife, gun), get(knife, elected), get(knife, Ben), get(knife, Diana), get(Alex, knife), get(Alex, gun), get(Alex, elected), get(Alex, Ben), get(Alex, Diana), get(gun, knife), get(gun, Alex), get(gun, elected), get(gun, Ben), get(gun, Diana), get(elected, knife), get(elected, Alex), get(elected, gun), get(elected, Ben), get(elected, Diana), get(Ben, knife), get(Ben, Alex), get(Ben, gun), get(Ben, elected), get(Ben, Diana), get(Diana, knife), get(Diana, Alex), get(Diana, gun), get(Diana, elected), get(Diana, Ben), stab(knife, Alex), stab(knife, gun), stab(knife, elected), stab(knife, Ben), stab(knife, Diana), stab(Alex, knife), stab(Alex, gun), stab(Alex, elected), stab(Alex, Ben), stab(Alex, Diana), stab(gun, knife), stab(gun, Alex), stab(gun, elected), stab(gun, Ben), stab(gun, Diana), stab(elected, knife), stab(elected, Alex), stab(elected, gun), stab(elected, Ben), stab(elected, Diana), stab(Ben, knife), stab(Ben, Alex), stab(Ben, gun), stab(Ben, elected), stab(Ben, Diana), stab(Diana, knife), stab(Diana, Alex), stab(Diana, gun), stab(Diana, elected), stab(Diana, Ben)]
find_open_precondition finished
Causal Links
(stab(knife, Alex), Die(Alex), Finish)

Constraints
Start < stab(knife, Alex)
Start < Finish
stab(knife, Alex) < Finish

Partial Order Plan
[{Start}, {stab(knife, Alex)}, {Finish}]
