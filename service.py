# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import xbmcaddon


def main():
    if xbmc.getInfoLabel('Window(10000).Property(script.rrmj.extended.service.started)'):
        # Prevent add-on updates from starting a new version of the addon
        return

    xbmcgui.Window(10000).setProperty('script.rrmj.extended.service.started', '1')

    if xbmcaddon.Addon().getSetting('kiosk.mode') == 'true':
        xbmc.log('script.rrmj.extended: Starting from service (Kiosk Mode)', xbmc.LOGNOTICE)
        xbmc.executebuiltin('RunScript(script.rrmj.extended)')


if __name__ == '__main__':
    main()
