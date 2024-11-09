from interactions import slash_command, slash_option, OptionType, SlashContext, Embed, SlashCommandChoice, Button, ButtonStyle, ActionRow, ComponentContext, StringSelectMenu
from interactions.api.events import Component
import time
from utils import colors
from bot_instance import sr_role_check, bot

@slash_command(
    name="test",
    description="",
)
@sr_role_check()
async def test(ctx):
    channel = ctx
    button = Button(
        custom_id="my_button_id",
        style=ButtonStyle.GREEN,
        label="Click Me",
    )
    message = await channel.send("Look a Button!", components=button)

    # define the check
    async def check(component: Component) -> bool:
        if component.ctx.author.username.startswith("a"):
            return True
        else:
            await component.ctx.send("Your name does not start with an 'a'!", ephemeral=True)

    try:
        # you need to pass the component you want to listen for here
        # you can also pass an ActionRow, or a list of ActionRows. Then a press on any component in there will be listened for
        used_component: Component = await bot.wait_for_component(components=button, check=check, timeout=30)

    except TimeoutError:
        print("Timed Out!")

        button.disabled = True
        await message.edit(components=button)

    else:
        await used_component.ctx.send("Your name starts with 'a'")