
# Submission For Smart India Hackathon (Internal) 

### Table Of Contents:

| Name          | Description                                                                                                                                                                                   |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MotherShip`  | A central drone capable of carrying payloads and independently controlling four mini drones.                                                                                                  |
| `Drones`      | Multiple mini drones deployed to cover larger areas efficiently, reducing overall operation time.                                                                                             |
| `QFH Antenna` | A Quadrifilar Helix (QFH) antenna enabling satellite-based imaging to identify affected regions. The mothership will then deploy mini drones for localized surveillance and victim detection. |


## 1. The MotherShip
The mothership is the central hub of the project, designed to carry and deploy four mini drones into disaster-prone areas. It acts as both a transport and a processing unit, using onboard microcontrollers to handle incoming data from the drones. Once processed, the mothership transmits this data to a QFH antenna using whichever communication protocol provides the most reliable link. Operators can then decode the data and remotely control the mothership, sending it to new areas in need of assessment or monitoring.

## 2. Children drones (Squad of 4)
The mini drones are small, autonomous scouts that can be released from the mothership to survey a designated area. Each drone is equipped with sensors to stay aware of its surroundings and avoid obstacles while collecting critical information. They transmit thermal images, raw image data, and infrared (IR) data back to the mothership using Wi-Fi or Bluetooth Low Energy (BLE), depending on which provides higher bandwidth. This setup ensures that the mothership receives high-quality data for processing before sending it to the operator.

## 3. QFH (Quadrifilar Helix Antenna) antenna
The QFH antenna plays a dual role in this system. It is primarily used to receive signals from the mothership, carrying processed data from the mini drones for operator analysis. In addition, the antenna can also receive weather satellite transmissions, allowing it to contribute to weather prediction tasks. This added capability makes the system more effective in disaster management, as real-time weather data can help operators plan drone deployment more strategically.


### Citation


```bibtex
@misc{lin2015microsoft,
  title={Microsoft COCO: Common Objects in Context},
  author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
  year={2015},
  eprint={1405.0312},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}

