from utils import config
from interactions import Client, check, SlashContext
import os


AppConfig_obj = config.AppConfig()
token = AppConfig_obj.get_bonk_punisher_key()
bot = Client(token=token, sync_interactions=True)

SR_CHECK_ROLES = [1259606868939247686, 1303524092846145596, 1259605492230000731, 1298484402216501249, 1259874782103605268, 1277325708082806847, 1259605722140774411]



# Role check decorator for role-specific commands
def sr_role_check():
    async def predicate(ctx: SlashContext):
        user_roles = [int(i.id) for i in ctx.author.roles]
        return any(role_id in user_roles for role_id in SR_CHECK_ROLES)
    return check(predicate)

def higherup_role_check():
    async def predicate(ctx: SlashContext):
        user_roles = [int(i.id) for i in ctx.author.roles]
        return any(role_id in user_roles for role_id in SR_CHECK_ROLES)
    return check(predicate)
