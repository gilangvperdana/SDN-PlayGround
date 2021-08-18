from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        s1 = self.addSwitch( 's1')
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )

        # Add links
        self.addLink( h1,s1 )
        self.addLink( h2,s8 )
        self.addLink( s8,s6 )
        self.addLink( s8,s7 )
        self.addLink( s8,s1 )
        self.addLink( s7,s3 )
        self.addLink( s5,s3 )
        self.addLink( s5,s7 )
        self.addLink( s6,s4 )
        self.addLink( s4,s2 )
        self.addLink( s2,s6 )
        self.addLink( s2,s1 )
        self.addLink( s3,s1 )

topos = { 'topoex1': ( lambda: MyTopo() ) }
