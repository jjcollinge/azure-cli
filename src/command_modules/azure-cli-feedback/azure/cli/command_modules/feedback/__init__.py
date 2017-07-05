# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.sdk.util import CliCommandType

import azure.cli.command_modules.feedback._help  # pylint: disable=unused-import


class FeedbackCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        super(FeedbackCommandsLoader, self).__init__(cli_ctx=cli_ctx)
        self.module_name = __name__

    def load_command_table(self, args):
        if super(FeedbackCommandsLoader, self).load_command_table(args):

            custom_feedback = CliCommandType(operations_tmpl='azure.cli.command_modules.feedback.custom#{}')

            with self.command_group('', custom_feedback) as g:
                g.command('feedback', 'handle_feedback')

            return self.command_table
