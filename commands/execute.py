from attr.filters import exclude
from interactions import slash_command, slash_option, OptionType, SlashContext, Embed, SlashCommandChoice
from utils import colors
import time
import utils.config
from pydactyl import PterodactylClient
from bot_instance import staff_role_check  # Import role_check from bot_instance

config = utils.config.AppConfig()
key = config.get_bonk_panel_api_key()
api = PterodactylClient('https://bonkpanel.ddns.net:5983', key)

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
    """console_channel_id = 1271152792207229081
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
        )"""
    srv_id = "df4e1f23-2fd0-4568-b655-9c636280e3ac"
    try:
        api.client.servers.send_console_command(srv_id, command)
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

