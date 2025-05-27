import numpy as np
import pandas as pd
from datetime import datetime
import boto3
from agents.base import BaseAgent


class ExampleAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.run()

    def run(self):
        self.logger.info("Running agent " + self.config.name + "...")
        now = datetime.utcnow().isoformat()
        mystring = f"The time the agent was run was {now}\n"

        localfilename = "output.txt"
        with open(localfilename, "w") as text_file:
            text_file.write(mystring)

        s3 = boto3.client("s3")
        s3.upload_file(localfilename, self.s3config.bucket_name, self.config.object_key)
