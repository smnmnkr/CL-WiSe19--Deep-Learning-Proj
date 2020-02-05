from config.util import colors

#
#
# bird configuration:
#
bird = {
    #
    # size, position, color:
    'size': (30, 30),  # px
    'startPosition': [120, 160],  # px
    'color': colors['red'],
    #
    # physics:
    'startVelocity': 5.0,
    'maxVelocity': 15.0,
    'lift': 25.0,
    'attraction': 1.35,
}
