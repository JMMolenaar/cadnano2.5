#!/usr/bin/env python
# encoding: utf-8
import cadnano.util as util
from .abstractdecoratoritem import AbstractDecoratorItem

class FluorophoreItem(AbstractDecoratorItem):
    def __init__(self, parent):
        """The parent should be a VirtualHelixItem."""
        super(FluorophoreItem, self).__init__(parent)

    ### SIGNALS ###

    ### SLOTS ###

    ### METHODS ###

    ### COMMANDS ###
