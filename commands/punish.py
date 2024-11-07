from interactions import slash_command, slash_option, OptionType, SlashContext, Embed, SlashCommandChoice
from utils import colors
import time
from bot_instance import role_check

# Discord channel ID for punishments
CONSOLE_CHANNEL_ID = 1271152792207229081
BAN_LOGS_CHANNEL_ID = 1259602927509835818

# Mapping of reasons to punishment commands
punishment_commands = {
    "Inappropriate-Structures": "tempban",
    "Solicitation": "tempban",
    "Unfair-Advantage": "tempban",
    "Bug-Exploitation": "tempban",
    "Chargebacks": "ban",
    "Punishment-Evasion": "ban",
    "Excessive-and-Malicious-Rule-Breaking": "tempban",
    "Inappropriate-Usernmame": "tempban",
    "Forging-evidence-lying-to-staff": "tempban",
    "Inappropriate Item Name": "tempban",
    "Player-Disrespect": "mute",
    "Discrimination": "mute",
    "Impersonation": "mute",
    "Minor-Advertising": "mute",
    "Major-Advertising": "mute",
    "Inappropriate-Content": "mute",
    "Spamming": "mute",
    "Harassment": "mute",
    "Death-wishes-Suicidal-encouragment": "mute",
    "Sensitive Topics": "mute",
    "Admin Discretion": "ban",
    "DDoS Doxxing Swatting - Blacklist - No Appeal": "ban",
    "Blacklist": "ban",
    "IRL-Trading": "ban"
}

@slash_command(name="punish", description="Punish a user on the server")
@slash_option(
    name="ign",
    description="Which in-game user would you like to punish?",
    required=True,
    opt_type=OptionType.STRING
)
@slash_option(
    name="reason",
    description="Please provide a reason for the punishment.",
    required=True,
    opt_type=OptionType.STRING,
    choices=[SlashCommandChoice(name=key, value=key) for key in punishment_commands.keys()]
)
@slash_option(
    name="proof",
    description="Provide proof of the offense.",
    required=True,
    opt_type=OptionType.ATTACHMENT
)
@role_check()
async def punish(ctx: SlashContext, ign: str, reason: str, proof):
    # Get the punishment command type (e.g., "ban" or "mute") based on reason
    punishment_type = punishment_commands.get(reason)
    if reason == "Irl-Trading":
        reason = "Solicitation"
    command = f"litebans:{punishment_type} {ign} {reason}"

    console_channel = await ctx.bot.fetch_channel(CONSOLE_CHANNEL_ID)
    await console_channel.send(command)

    # Create and send the embedded message to the Discord channel
    embed = Embed(
        title="Punishment Executed",
        description=f"**Action:** {punishment_type.capitalize()}\n**User:** {ign}\n**Reason:** {reason}",
        color=colors.DiscordColors.RED,
        timestamp=time.time()
    )
    embed.set_footer(text="Punishment System")
    embed.set_image(url=proof.url)

    # Send the embed to the punishments channel
    ban_channel = await ctx.bot.fetch_channel(BAN_LOGS_CHANNEL_ID)
    await ban_channel.send(embed=embed)

    # Confirm to the user
    await ctx.send(f"Punishment for {ign} has been issued successfully for `{reason}`.", ephemeral=True)
