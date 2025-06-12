from typing import TYPE_CHECKING
from ballsdex.packages.custom.daily import Daily

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

async def setup(bot: "BallsDexBot"):
    await bot.add_cog(Daily(bot))
