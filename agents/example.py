import numpy as np
import pandas as pd
from datetime import datetime
import boto3, botocore
from agents.base import BaseAgent


class ExampleAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.s3 = boto3.client("s3")
        self.run()

    def run(self):
        self.logger.info("Running agent " + self.config.name + "...")
        self.upload()
        self.download()


    def upload(self):
        now = datetime.utcnow().isoformat()
        mystring = f"The time the agent was run was {now}\n"

        localfilename = "output.txt"
        with open(localfilename, "w") as text_file:
            text_file.write(mystring)

        self.s3.upload_file(localfilename, self.config.s3bucket_name, self.config.object_key)
        
    def download(self):
        try:
            # Try to download the file
            self.s3.download_file(self.config.s3bucket_name, "foo.txt", "foo_local.txt")

        except botocore.exceptions.ClientError as e:
            # Check if the error is a 404 (object not found)
            if e.response["Error"]["Code"] == "404":
                print(f"Object does not exist: s3://??")
            else:
                # Re-raise other exceptions
                raise
