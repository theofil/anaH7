# PDG IDs of interesting particles

class myParticle:
    """A simple class storying the name of the particle and it's ID"""

    def __init__(self, name, PID):
	self.name = name
        self.PID  = PID


PoI = [] ### list with particles of interest

PoI += [myParticle("pi+"         ,  211  )]
PoI += [myParticle("K+"          ,  321  )]
PoI += [myParticle("Kshort"      ,  310  )]
PoI += [myParticle("D+"          ,  411  )]
PoI += [myParticle("D0"          ,  421  )]
PoI += [myParticle("D+s"         ,  433  )]
PoI += [myParticle("D*(2010)+"   ,  413  )]
PoI += [myParticle("J/psi"       ,  443  )]
PoI += [myParticle("Lambda0"     ,  3122 )]
PoI += [myParticle("Lambda0c"    ,  4122 )]
PoI += [myParticle("Ksi0c"       ,  4132 )]
PoI += [myParticle("Ksi-"        ,  3312 )]
  

