#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "f0100a83-0d96-4747-a4a0-c38d69e96b17")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Dimas1234567")
