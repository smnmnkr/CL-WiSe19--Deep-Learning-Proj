import torch
import torch.nn as nn


class Brain(nn.Module):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, brain_size):

        super(Brain, self).__init__()

        # save parameters
        self.brain_size = brain_size

        # Linear
        # https://pytorch.org/docs/stable/nn.html#torch.nn.Linear
        self.fc2 = nn.Linear(self.brain_size, 1)

        # Sigmoid
        # https://pytorch.org/docs/stable/nn.html#sigmoid
        self.ac1 = nn.Sigmoid()

    #
    #
    #  -------- Forward -----------
    #
    def forward(self, x):

        # apply Linear:
        x = self.fc2(x)

        # apply Sigmoid:
        x = self.ac1(x)

        return x

    #
    #
    #  -------- Think -----------
    #
    def think(self, data):
        self.zero_grad()

        x1 = torch.FloatTensor([data[0][0]])  # bird Y
        x2 = torch.FloatTensor([data[1][0][0]])  # pipes.index(0) Y
        x3 = torch.FloatTensor([data[1][0][1]])  # pipes.index(0) X

        x = torch.cat((
            x1,
            x2,
            x3,
        ))

        x = self.forward(x)

        if (False):  # x > .5
            return True

        return False
