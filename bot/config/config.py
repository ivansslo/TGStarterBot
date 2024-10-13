from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    START_MMproBump_bot: bool = True
    START_MMproBump_bot_URL: str = "https://api.mmbump.pro/"
    START_MMproBump_bot_STR: str = "ref_6420382110" #replace your referral id

    START_pixelversexyzbot: bool = True
    START_pixelversexyzbot_URL: str = "https://sexyzbot.pxlvrs.io/"
    START_pixelversexyzbot_STR: str = "6420382110" #replace your referral id

    START_cexio_tap_bot: bool = True
    START_cexio_tap_bot_URL: str = "https://cexp.cex.io/"
    START_cexio_tap_bot_STR: str = "1724139499075599" #replace your referral id

    START_memefi_coin_bot: bool = True
    START_memefi_coin_bot_URL: str = "https://tg-app.memefi.club/"
    START_memefi_coin_bot_STR: str = "r_7163349516" #replace your referral id

    START_dotcoin_bot: bool = True
    START_dotcoin_bot_URL: str = "https://app.dotcoin.bot/"
    START_dotcoin_bot_STR: str = "r_6420382110" #replace your referral id

    START_TimeFarmCryptoBot: bool = True
    START_TimeFarmCryptoBot_URL: str = "https://tg-tap-miniapp.laborx.io/"
    START_TimeFarmCryptoBot_STR: str = "rMT22RcupAXDxspW" #replace your referral id

    START_wormfare_slap_bot: bool = True
    START_wormfare_slap_bot_URL: str = "https://clicker.wormfare.com/?v=1"
    START_wormfare_slap_bot_STR: str = "r_6420382110" #replace your referral id

    START_cedex_tap_bot: bool = True
    START_cedex_tap_bot_URL: str = "https://cdxp.cedex.io/"
    START_cedex_tap_bot_STR: str = "1723979659080210" #replace your referral id

    START_tapswap_bot: bool = True
    START_tapswap_bot_URL: str = "https://app.tapswap.club/"
    START_tapswap_bot_STR: str = "r_6420382110" #replace your referral id

    START_wcoin_tapbot: bool = True
    START_wcoin_tapbot_URL: str = "https://alohomora-bucket-fra1-prod-frontend-static.fra1.cdn.digitaloceanspaces.com/latest/index.html"
    START_wcoin_tapbot_STR: str = "s_17eaf419e" #replace your referral id

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
