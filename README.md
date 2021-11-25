# SDN PlayGround

```
This is a repository to store the results of my learning about SDN.
```

# How to Run ?
```
Please visit my medium at [https://gilangvperdana.medium.com/tentang-software-defined-network-82d4edf515e3] for the necessary installation requirements.
If the need is ready, please follow these steps (Execute on mininet Nodes):
$ cd SDN-PlayGround
$ sudo mn --switch ovs,protocols=OpenFlow14 --controller remote,ip=your_controller_ip --custom Topo-example.py --topo topoex1

Change your_controller_ip to your ip of your controller nodes.
You can see the expectation Topology on Final-Topo.png
```

# Need LAB on Container ?
```
If you need simply installation LAB (data & control plane for SDN) you can try with this containerization SDN Envrionment :
https://github.com/gilangvperdana/SDN-Docker
```
