Help on Token object:

class TTookkeenn(builtins.object)
 |  An individual token --- i.e. a word, punctuation symbol, whitespace, etc.
 |  
 |  Methods defined here:
 |  
 |  ____bbyytteess____(...)
 |  
 |  ____eeqq____(self, value, /)
 |      Return self==value.
 |  
 |  ____ggee____(self, value, /)
 |      Return self>=value.
 |  
 |  ____ggtt____(self, value, /)
 |      Return self>value.
 |  
 |  ____hhaasshh____(self, /)
 |      Return hash(self).
 |  
 |  ____llee____(self, value, /)
 |      Return self<=value.
 |  
 |  ____lleenn____(...)
 |      Number of unicode characters in token.text
 |  
 |  ____lltt____(self, value, /)
 |      Return self<value.
 |  
 |  ____nnee____(self, value, /)
 |      Return self!=value.
 |  
 |  ____nneeww____(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ____rreepprr____(self, /)
 |      Return repr(self).
 |  
 |  ____ssttrr____(self, /)
 |      Return str(self).
 |  
 |  ____uunniiccooddee____(...)
 |  
 |  cchheecckk__ffllaagg(...)
 |      Check the value of a boolean flag.
 |      
 |      Arguments:
 |          flag_id (int): The ID of the flag attribute.
 |      Returns:
 |          is_set (bool): Whether the flag is set.
 |  
 |  iiss__aanncceessttoorr(...)
 |      Check whether this token is a parent, grandparent, etc. of another
 |      in the dependency tree.
 |      
 |      Arguments:
 |          descendant (Token): Another token.
 |      Returns:
 |          is_ancestor (bool): Whether this token is the ancestor of the descendant.
 |  
 |  iiss__aanncceessttoorr__ooff(...)
 |  
 |  nnbboorr(...)
 |      Get a neighboring token.
 |      
 |      Arguments:
 |          i (int): The relative position of the token to get. Defaults to 1.
 |      Returns:
 |          neighbor (Token): The token at position self.doc[self.i+i]
 |  
 |  ssiimmiillaarriittyy(...)
 |      Compute a semantic similarity estimate. Defaults to cosine over vectors.
 |      
 |      Arguments:
 |          other:
 |              The object to compare with. By default, accepts Doc, Span,
 |              Token and Lexeme objects.
 |      Returns:
 |          score (float): A scalar similarity score. Higher is more similar.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  aanncceessttoorrss
 |      A sequence of this token's syntactic ancestors.
 |      
 |      Yields: Token A sequence of ancestor tokens such that ancestor.is_ancestor(self)
 |  
 |  cchhiillddrreenn
 |      A sequence of the token's immediate syntactic children.
 |      
 |      Yields: Token A child token such that child.head==self
 |  
 |  cclluusstteerr
 |  
 |  ccoonnjjuunnccttss
 |      A sequence of coordinated tokens, including the token itself.
 |      
 |      Yields: Token A coordinated token
 |  
 |  ddeepp
 |  
 |  ddeepp__
 |  
 |  ddoocc
 |  
 |  eenntt__iidd
 |      An (integer) entity ID. Usually assigned by patterns in the Matcher.
 |  
 |  eenntt__iidd__
 |      A (string) entity ID. Usually assigned by patterns in the Matcher.
 |  
 |  eenntt__iioobb
 |  
 |  eenntt__iioobb__
 |  
 |  eenntt__ttyyppee
 |  
 |  eenntt__ttyyppee__
 |  
 |  hhaass__rreeppvveecc
 |  
 |  hhaass__vveeccttoorr
 |      A boolean value indicating whether a word vector is associated with the object.
 |  
 |  hheeaadd
 |      The syntactic parent, or "governor", of this token.
 |      
 |      Returns: Token
 |  
 |  ii
 |  
 |  iiddxx
 |  
 |  iiss__aallpphhaa
 |  
 |  iiss__aasscciiii
 |  
 |  iiss__bbrraacckkeett
 |  
 |  iiss__ddiiggiitt
 |  
 |  iiss__lleefftt__ppuunncctt
 |  
 |  iiss__lloowweerr
 |  
 |  iiss__oooovv
 |  
 |  iiss__ppuunncctt
 |  
 |  iiss__qquuoottee
 |  
 |  iiss__rriigghhtt__ppuunncctt
 |  
 |  iiss__ssppaaccee
 |  
 |  iiss__ssttoopp
 |  
 |  iiss__ttiittllee
 |  
 |  llaanngg
 |  
 |  llaanngg__
 |  
 |  lleefftt__eeddggee
 |      The leftmost token of this token's syntactic descendents.
 |      
 |      Returns: Token The first token such that self.is_ancestor(token)
 |  
 |  lleeffttss
 |  
 |  lleemmmmaa
 |  
 |  lleemmmmaa__
 |  
 |  lleexx__iidd
 |  
 |  lliikkee__eemmaaiill
 |  
 |  lliikkee__nnuumm
 |  
 |  lliikkee__uurrll
 |  
 |  lloowweerr
 |  
 |  lloowweerr__
 |  
 |  nn__lleeffttss
 |  
 |  nn__rriigghhttss
 |  
 |  nnoorrmm
 |  
 |  nnoorrmm__
 |  
 |  oorrtthh
 |  
 |  oorrtthh__
 |  
 |  ppooss
 |  
 |  ppooss__
 |  
 |  pprreeffiixx
 |  
 |  pprreeffiixx__
 |  
 |  pprroobb
 |  
 |  rraannkk
 |  
 |  rreeppvveecc
 |  
 |  rriigghhtt__eeddggee
 |      The rightmost token of this token's syntactic descendents.
 |      
 |      Returns: Token The last token such that self.is_ancestor(token)
 |  
 |  rriigghhttss
 |  
 |  sseennttiimmeenntt
 |  
 |  sshhaappee
 |  
 |  sshhaappee__
 |  
 |  ssttrriinngg
 |  
 |  ssuubbttrreeee
 |      A sequence of all the token's syntactic descendents.
 |      
 |      Yields: Token A descendent token such that self.is_ancestor(descendent)
 |  
 |  ssuuffffiixx
 |  
 |  ssuuffffiixx__
 |  
 |  ttaagg
 |  
 |  ttaagg__
 |  
 |  tteexxtt
 |  
 |  tteexxtt__wwiitthh__wwss
 |  
 |  vveeccttoorr
 |      A real-valued meaning representation.
 |      
 |      Type: numpy.ndarray[ndim=1, dtype='float32']
 |  
 |  vveeccttoorr__nnoorrmm
 |  
 |  vvooccaabb
 |  
 |  wwhhiitteessppaaccee__
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  ____ppyyxx__vvttaabbllee____ = <capsule object NULL>
