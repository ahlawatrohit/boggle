import random

class GameUtil:

    #
    # Every cell of the 4 by 4 grid would have one character
    # randomly chosen from this set
    #
    cells = [
        "NEEHGW",
        "TMIOUC",
        "YTLETR",
        "NLNHRZ",
        "WTOOAT",
        "IUNEES",
        "HSPACO",
        "SSOIET",
        "BAOBOJ",
        "RYVDEL",
        "QUMHNI",
        "IERLDX",
        "NEEGAA",
        "FPSAKF",
        "STITYP",
        "WRETVH"
    ]

    #
    # Generate game grid with random characters from the above cell list
    #
    def generate_grid(self):
        grid = ""
        for entry in GameUtil.cells:
            grid = grid +  entry[random.randrange(0,6)]
        return grid
