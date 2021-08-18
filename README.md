# SDN PlayGround

```
This is a repository to store the results of my learning about SDN.
```

# How to Run ?
```
Please visit my medium at [] for the necessary installation requirements.
If the need is ready, please follow these steps (Execute on mininet Nodes):
$ cd SDN-PlayGround
$ sudo mn --switch ovs,protocols=OpenFlow14 --controller remote,ip=your_controller_ip --custom Topo-example.py --topo topoex1

Change your_controller_ip to your ip of your controller nodes.
You can see the expectation Topology on Final-Topo.png
```