from misoc.cores.liteeth_mini.common import *


def LiteEthPHY(clock_pads, pads, clk_freq=None, **kwargs):
    # Autodetect PHY
    if hasattr(clock_pads, "gtx") and len(pads.tx_data) == 8:
        if hasattr(clock_pads, "tx"):
            # This is a 10/100/1G PHY
            from misoc.cores.liteeth_mini.phy.gmii_mii import LiteEthPHYGMIIMII
            return LiteEthPHYGMIIMII(clock_pads, pads, clk_freq=clk_freq, **kwargs)
        else:
            # This is a pure 1G PHY
            from misoc.cores.liteeth_mini.phy.gmii import LiteEthPHYGMII
            return LiteEthPHYGMII(clock_pads, pads, **kwargs)
    elif len(pads.tx_data) == 4:
        # This is a MII PHY
        from misoc.cores.liteeth_mini.phy.mii import LiteEthPHYMII
        return LiteEthPHYMII(clock_pads, pads, **kwargs)
    else:
        raise ValueError("Unable to autodetect PHY from platform file, use direct instantiation")
