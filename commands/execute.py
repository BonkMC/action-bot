from attr.filters import exclude
from interactions import slash_command, slash_option, OptionType, SlashContext, Embed, SlashCommandChoice
from utils import colors
import time
from bot_instance import staff_role_check  # Import role_check from bot_instance

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
@staff_role_check(exclude=["Manager", "Admin", "Owner", "Developer"], exclude_acts_as_include=True)
async def handle_execute_command(ctx: SlashContext, command):
    console_channel_id = 1271152792207229081
    console_channel = ctx.guild.get_channel(console_channel_id)
    try:
        await console_channel.send(command)
        await ctx.send(
            embeds=Embed(
                title="Command Executed",
                description=f"The command `{command}` has been executed in console.",
                color=colors.DiscordColors.GREEN
            )
        )
    except:
        await ctx.send(
            embeds=Embed(
                title="Command Failed",
                description=f"The command `{command}` failed to execute in console.",
                color=colors.DiscordColors.RED
            )
        )