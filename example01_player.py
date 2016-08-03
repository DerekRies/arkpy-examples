from arkpy import ark, utils


def main():
    """
    This example reads an .arkprofile file and prints out some important info
    about the player and character found in that file.
    """
    file_path = 'data/LocalPlayerRosetta.arkprofile'
    file_path = 'data/random.2.arkprofile'
    profile = ark.ArkProfile(file_path)
    print 'Player Steam Name: %s' % profile.player_name.value
    print 'Player Steam ID: %s' % profile.unique_id.value
    # print 'Player Steam ID: %s' % profile.
    print 'Player Character Name: %s' % profile.character.name.value
    in_tribe = (profile.tribe_ID.value)
    if in_tribe:
        print 'Tribe ID: %s' % profile.tribe_ID.value
    print 'Spectator: %s' % str(profile.is_spectator)
    print 'Level: %s' % str(profile.character.level_ups.value + 1)
    print 'Experience: %s' % profile.character.experience.value
    print 'Stats:'
    stats = profile.character.stat_points
    for stat in ark.StatMap:
        print '  %s: +%s' % (stat.name, stats[stat].value)
    print 'Engram Points: %s' % profile.character.engram_points.value
    print 'Engrams:'
    for ind, engram in enumerate(profile.character.engrams.value):
        engram_path = engram.value
        # A simple utility method to get the last section of the path string
        # Containing only the item name.
        print '  %s: %s' % (ind + 1, utils.get_item(engram_path))
    slots = profile.character.default_slots
    print 'Hotbar Slots:'
    for ind, slot in enumerate(slots):
        if slot.value == '':
            slot_item = 'None'
        else:
            slot_item = utils.get_item(slot.value)
        print 'Slot #%s: %s' % (ind, slot_item)

if __name__ == '__main__':
    main()
