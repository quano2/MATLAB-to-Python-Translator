
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xea\xb20\xa90\xa4h\xfa\xf6\xb8\x1a\x98!\xdfx\xbe'
    
_lr_action_items = {'LBRACE':([0,],[1,]),'TIMES':([0,],[2,]),'DIVEQUAL':([0,],[4,]),'EQUALS':([0,],[5,]),'PLUSPLUS':([0,],[6,]),'LBRACKET':([0,],[7,]),'GREATERTHAN':([0,],[8,]),'SUBEQUAL':([0,],[11,]),'DIV':([0,],[10,]),'TIMESEQUAL':([0,],[9,]),'RBRACKET':([0,],[12,]),'RBRACE':([0,],[14,]),'PLUSEQUAL':([0,],[15,]),'STRING':([0,],[3,]),'PLUS':([0,],[17,]),'LESSEQUAL':([0,],[18,]),'TRANSPOSE':([0,],[20,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,],[-21,-4,-26,-11,-1,-7,-19,-16,-10,-5,-9,-20,-23,-22,-8,-6,-2,-15,0,-27,-3,-25,-17,-12,-13,-14,-18,-24,]),'EQUALTO':([0,],[24,]),'MINUS':([0,],[21,]),'IDENTIFIER':([0,],[22,]),'GREATEREQUAL':([0,],[23,]),'AND':([0,],[16,]),'NOTEQUAL':([0,],[25,]),'LESSTHAN':([0,],[26,]),'NOT':([0,],[27,]),'NUMBER':([0,],[28,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,],[13,]),'expr':([0,],[19,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> EQUALS','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',8),
  ('expr -> PLUS','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',9),
  ('expr -> MINUS','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',10),
  ('expr -> TIMES','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',11),
  ('expr -> DIV','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',12),
  ('expr -> AND','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',13),
  ('expr -> PLUSPLUS','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',14),
  ('expr -> PLUSEQUAL','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',15),
  ('expr -> SUBEQUAL','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',16),
  ('expr -> TIMESEQUAL','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',17),
  ('expr -> DIVEQUAL','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',18),
  ('expr -> EQUALTO','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',19),
  ('expr -> NOTEQUAL','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',20),
  ('expr -> LESSTHAN','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',21),
  ('expr -> LESSEQUAL','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',22),
  ('expr -> GREATERTHAN','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',23),
  ('expr -> GREATEREQUAL','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',24),
  ('expr -> NOT','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',25),
  ('expr -> LBRACKET','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',26),
  ('expr -> RBRACKET','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',27),
  ('expr -> LBRACE','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',28),
  ('expr -> RBRACE','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',29),
  ('expr -> term','expr',1,'p_expr','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',30),
  ('term -> NUMBER','term',1,'p_term','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',35),
  ('term -> IDENTIFIER','term',1,'p_term','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',36),
  ('term -> STRING','term',1,'p_term','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',37),
  ('expr -> TRANSPOSE','expr',1,'p_transpose','F:/Users/Joe/PycharmProjects/MATLAB-to-Python/Parse.py',47),
]
