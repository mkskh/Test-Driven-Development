#!/usr/bin/env python

from cleaning_robot import CleaningRobot


def main():
    test_failed = False
    # TODO - initiate cleaning robot and test what happens when it encounters
    # an inner door, the main door or a prison guard. Then modify cleaning_robot.py
    # so that it works accordingly.

    cleaning_robot = CleaningRobot(True)

    if not "Door unlocked.\n" in cleaning_robot.when_encounter_inner_door():
        test_failed = True
    
    if not "Door unlocked.\n" in cleaning_robot.when_encounter_outer_door():
        test_failed = True
    
    if "Door locked.\n" in cleaning_robot.when_encounter_inner_door():
        test_failed = True
    
    if "Door locked.\n" in cleaning_robot.when_encounter_outer_door():
        test_failed = True
    
    if not "Door entered.\n" in cleaning_robot.when_encounter_inner_door():
        test_failed = True
    
    if "Door entered.\n" in cleaning_robot.when_encounter_outer_door():
        test_failed = True
    
    if "Turn around.\n" in cleaning_robot.when_encounter_guard():
        test_failed = True
    
    if test_failed:
        print("Unfortunately, one or several tests failed.")
    else:
        print("All tests ran successfully.")


if __name__ == "__main__":
    main()
