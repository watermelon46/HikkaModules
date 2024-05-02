# meta developer: @hlnmhikka
# requires: psutil py-cpuinfo uptime
__version__ = (1, 0)

import logging
import asyncio
from .. import loader, utils
import platform 
import psutil
from getpass import getuser
from uptime import uptime
from time import time
import cpuinfo
import socket

logger = logging.getLogger(__name__)

def uptime_parse(): # code from https://github.com/Cairnarvon/uptime/blob/master/src/__main__.py
    up = uptime()

    if up is None:
        return "unable to determine"

    if '-b' not in sys.argv:
        parts = []

        days, up = up // 86400, up % 86400
        if days:
            parts.append('%d day%s' % (days, 's' if days != 1 else ''))

        hours, up = up // 3600, up % 3600
        if hours:
            parts.append('%d hour%s' % (hours, 's' if hours != 1 else ''))

        minutes, up = up // 60, up % 60
        if minutes:
            parts.append('%d minute%s' % (minutes, 's' if minutes != 1 else ''))

        if up or not parts:
            parts.append('%.2f seconds' % up)
            
    return "".join(parts)
@loader.tds
class wmfetch(loader.Module):
    
    __version__ = (1, 1)

    """wmfetch"""

    strings = {
        "name":  "wmfetch"
    }

    async def wmfetchcmd(self, message):
        """
        - get system info
        """
        starttime = time()
        # Fetch2 - getting info from micro
        username = getuser()
        uptime = uptime_parse()
        localip=socket.gethostbyname(socket.gethostname())
        # Fetch1 - getting info from uname()
        sysinfo = platform.uname()
        system = sysinfo[0]
        pcname = sysinfo[1]
        release = sysinfo[2]
        arch = sysinfo[4]
        # Fetch2 - getting info from psutil
        ramraw = psutil.virtual_memory()
        ramtotal = round(ramraw.total/1048576, 2)
        ramused = round(ramraw.used/1048576, 2)
        rampercent = ramraw.percent
        cpucount = psutil.cpu_count()
        cpuload = psutil.cpu_percent()
        # Fetch3 - getting info from cpuinfo
        cpuraw = cpuinfo.get_cpu_info()
        pyver = cpuraw['python_version']
        cpuname = cpuraw['brand_raw']
        cpuhz = cpuraw['hz_advertised_friendly']
        fetchedIn = time() - starttime
        # When everything is fetched, it's time to show output!
        await message.edit(f"""
        <b>🍉 wmfetch4hikka
   
        {username}@{pcname}
        ————————————————
        OS:</b> {system}
        <b>Kernel:</b> {release}
        <b>Uptime:</b> {uptime}
        <b>CPU:</b> ({cpucount}) {cpuname}
        <b>CPU arch:</b> {arch}
        <b>CPU load:</b> {cpuload}%
        <b>RAM:</b> {ramused}MB / {ramtotal}MB ({rampercent})
        <b>Python:</b> {pyver}
        <b>Local IP:</b> {localip}
            
        Fetched in {round(fetchedIn, 5)}s
        """)