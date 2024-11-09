from interactions import slash_command, slash_option, OptionType, SlashContext, Embed, SlashCommandChoice
from utils import colors
import time
from bot_instance import sr_role_check

CONSOLE_CHANNEL_ID = 1271152792207229081

@slash_command(
    name="execute",
    description="Execute a command in the console"
)
@slash_option(
    name="command",
    description="The command you would like to execute",
    required=True,
    opt_type=OptionType.STRING
)
@sr_role_check()