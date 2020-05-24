![Validate](https://github.com/seanblumenfeld/ruuvihub/workflows/Validate/badge.svg)
![Deploy](https://github.com/seanblumenfeld/ruuvihub/workflows/Deploy/badge.svg)

# RuuviHub
A Django API and Admin site for collecting and managing ruuvitag data.

# Ruuvitag sensor broadcast protocols
https://github.com/ruuvi/ruuvi-sensor-protocols/blob/master/broadcast_formats.md

# TODO
- [x] Feature: API Authentication
- [ ] Feature: Ability to move a Ruuvitag sensor to a new location while keeping data for old location unaffected
- [ ] Feature: Set up raspberry pi bluetooth/wifi gateway
- [ ] Feature: Package up watch_sensor_events service to run on raspberry pi
- [ ] Feature: Set up SSL
  - [ ] Task: Set up Heroku app SSL 
  - [ ] Task: update watch_sensor_events service to use https
- [ ] Feature: Integrate raspberry Pi temperature monitor using https://www.raspberrypi.org/forums/viewtopic.php?t=50373
- [ ] Feature: configure sensor recording frequency per sensor

    
