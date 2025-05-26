import numpy as np
import pandas as pd

from agents.base import BaseAgent


class ExampleAgent(BaseAgent):
    def __init__(self, config):
        self.config = config
        self.run()

    def run(self):
        self.loggger.info("Running agent " + self.config.name + "...")
