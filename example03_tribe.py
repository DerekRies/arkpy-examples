from arkpy import ark, utils


def main():
    """
    This example reads an .arktribe file and display some important
    information about the tribe found in that file. Then we'll take a look at
    the Tribe Logs, and see how we can parse those out and export the Tribe
    Logs elsewhere
    """
    file_path = 'data/1082816853.arktribe'
    # file_path = 'data/1168672942.arktribe'
    tribe = ark.ArkTribe(file_path)
    print 'Tribe Name: %s' % tribe.name.value
    print 'Members:'
    admin_ids = [n.value for n in tribe.tribe_admins.value]
    for name, mid in tribe.members:
        isadmin = bool(mid.value in admin_ids)
        vals = (name.value, mid.value)
        if mid.value == tribe.owner_id.value:
            print '  [OWNER] Name: %s, ID: %s' % vals
        elif isadmin:
            print '  [ADMIN] Name: %s, ID: %s' % vals
        else:
            print '  [MEMBER] Name: %s, ID: %s' % vals
    alliances = tribe.alliances
    if alliances is not None:
        if len(tribe.alliances.value):
            print 'Alliances'
            for alliance in tribe.alliances.value:
                alliance_name = alliance.data['AllianceName'].value
                print 'Alliance Name: %s' % alliance_name
                for t in alliance.data['MembersTribeName'].value:
                    print '    Tribe Name: %s' % t.value

    print 'Tribe Log'
    if len(tribe.log.value):
        for entry in tribe.log.value:
            print entry.value
    else:
        print 'EMPTY'


if __name__ == '__main__':
    main()