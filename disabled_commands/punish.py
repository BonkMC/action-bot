from interactions import slash_command, slash_option, OptionType, SlashContext, Embed, SlashCommandChoice
from utils import colors
import time
from bot_instance import staff_role_check

# Discord channel ID for punishments
CONSOLE_CHANNEL_ID = 1271152792207229081
BAN_LOGS_CHANNEL_ID = 1259602927509835818

# Mapping of reasons to punishment commands
punishment_commands = {
    "Inappropriate-Structures": "tempbanip",
    "Solicitation": "tempbanip",
    "Unfair-Advantage": "tempbanip",
    "Bug-Exploitation": "tempbanip",
    "Chargebacks": "banip",
    "Punishment-Evasion": "banip",
    "Excessive-and-Malicious-Rule-Breaking": "tempbanip",
    "Inappropriate-Usernmame": "tempbanip",
    "Forging-evidence-lying-to-staff": "tempbanip",
    "Inappropriate Item Name": "tempbanip",
    "Player-Disrespect": "tempmuteip",
    "Discrimination": "tempmuteip",
    "Impersonation": "tempmuteip",
    "Minor-Advertising": "tempmuteip",
    "Major-Advertising": "tempmuteip",
    "Inappropriate-Content": "tempmuteip",
    "Spamming": "tempmuteip",
    "Harassment": "tempmuteip",
    "Death-wishes-Suicidal-encouragment": "tempmuteip",
    "Sensitive Topics": "tempmuteip",
    "Admin Discretion": "banip",
    "DDoS Doxxing Swatting - Blacklist - No Appeal": "banip",
    "Blacklist": "banip",
    "IRL-Trading": "banip"
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
@staff_role_check(exclude=["Trainee"])
async def punish(ctx: SlashContext, ign: str, reason: str, proof):
    # Get the punishment command type (e.g., "ban" or "mute") based on reason
    punishment_type = punishment_commands.get(reason)
    if reason == "Irl-Trading":
        reason = "Solicitation"
    command = f"litebans:{punishment_type} {ign} {reason}"
    console_channel = await ctx.bot.fetch_channel(CONSOLE_CHANNEL_ID)
    await console_channel.send(command)

    # Create and send the embedded message to the Discord channel
    author = ctx.author
    embed = Embed(
        title="Punishment Executed",
        description=f"**Action:** {punishment_type.capitalize()}\n**User:** {ign}\n**Punished by:** <@{author.id}>\n**Reason:** {reason}\n**Proof:**",
        color=colors.DiscordColors.RED,
        timestamp=time.time()
    )
    embed.set_footer(text="Punishment System")
    embed.set_image(url=proof.url)
    embed.set_thumbnail(url=f"https://minotar.net/helm/{ign}/100")

    # Send the embed to the punishments channel
    ban_channel = await ctx.bot.fetch_channel(BAN_LOGS_CHANNEL_ID)
    await ban_channel.send(embed=embed)

    # Confirm to the user
    await ctx.send(f"Punishment for {ign} has been issued successfully for `{reason}`.", ephemeral=True)
