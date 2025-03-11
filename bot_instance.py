from utils import config
from interactions import Client, check, SlashContext
import os
from dotenv import load_dotenv
import json

load_dotenv()

#AppConfig_obj = config.AppConfig()
#token = AppConfig_obj.get_bonk_punisher_key()
token = os.getenv("BOT_TOKEN")
bot = Client(token=token, sync_interactions=True)


# Role check decorator for role-specific commands
def staff_role_check(exclude: list = [], exclude_acts_as_include: bool = False):
    async def predicate(ctx: SlashContext):
        with open('data/roleslist.json') as f:
            roles_dict = json.load(f)
        check_roles = []
        for role, (a, b) in roles_dict.items():
            if not exclude_acts_as_include and role in exclude:
                continue
            check_roles.extend((a, b))
        user_roles = [int(i.id) for i in ctx.author.roles]
        return any(role_id in user_roles for role_id in check_roles)

    return check(predicate)
