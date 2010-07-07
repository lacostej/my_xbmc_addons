import xbmc, xbmcgui

#get actioncodes from keymap.xml
ACTION_PREVIOUS_MENU = 10

rtmp_url_high = "rtmp://rtmp.infomaniak.ch/shoutcast/start-latina-high.aac"

class LatinaFr(xbmcgui.Window):
  def __init__(self):
    self.strActionInfo = xbmcgui.ControlLabel(400, 400, 400, 200, '', 'font13', '0xFFFF00FF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Push BACK to quit')
    self.button0 = xbmcgui.ControlButton(450, 500, 80, 30, "PLAY")
    self.addControl(self.button0)
    self.button1 = xbmcgui.ControlButton(550, 500, 80, 30, "PAUSE")
    self.addControl(self.button1)
    self.setFocus(self.button0)
    self.button0.controlDown(self.button1)
    self.button1.controlUp(self.button0)
    self.button0.controlRight(self.button1)
    self.button1.controlLeft(self.button0)

    self.player = xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER)
    #self.start()
 
  def onControl(self, control):
    if control == self.button0:
      self.start()
    if control == self.button1:
      self.stop()

  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()

  def message(self, msg):
    dialog = xbmcgui.Dialog()
    dialog.ok("My message title", msg)
    
  def start(self):
    item = xbmcgui.ListItem("Latina.fr")
    swf_url = "http://broadcast.infomaniak.ch/player/player.swf?sLive=start-latina"
    rtmp_url = "rtmp://rtmp.infomaniak.ch/shoutcast/"
    playpath = "start-latina-high.aac"
    #page_url = "http://rtl-now.rtl.de/awz.php"
    item.setProperty("PlayPath", playpath)
    item.setProperty("SWFPlayer", swf_url)
    #item.setProperty("PageURL", page_url)
    self.player.play(rtmp_url, item)

  def stop(self):
    self.player.stop()
  
  def pauseResume(self):
    if self.player.isPlaying():
      self.player.pause()
    else:
      self.player.playselectedl()

mydisplay = LatinaFr()
mydisplay.doModal()
del mydisplay
