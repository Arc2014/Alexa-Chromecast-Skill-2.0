#!/usr/bin/env python3

"""
Required Environment Variables:

AWS_ACCESS_KEY_ID - AWS User Access Key (IAM)
AWS_SECRET_ACCESS_KEY - AWS Secret Access Key (IAM)
AWS_DEFAULT_REGION - AWS Lambda and SNS Region (e.g. eu-west-1)
AWS_SNS_TOPIC_ARN - AWS SNS Topic ARN (e.g. arn:aws:sns:eu-west-1:236205202378:Alexa-Chromecast) 
PORT - Hardcode external port.
CHROMECAST_NAME - name of the Chromecast to send commands to

"""

import os
from local.SkillSubscriber import Subscriber
from local.ChromecastSkill import Skill

PORT = os.getenv('PORT', False)
PORT = 30000

if __name__ == "__main__":
    chromecast_skill = Skill()
    Subscriber({'chromecast': chromecast_skill}, PORT)
