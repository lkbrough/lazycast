#!/usr/bin/env python3

"""
	This software is part of lazycast, a simple wireless display receiver for Raspberry Pi
	Copyright (C) 2018 Hsun-Wei Cho
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import socket
import fcntl, os
import errno
import threading
from threading import Thread
import time
from time import sleep
import sys
import subprocess
import argparse
##################### Settings #####################
player_select = 0
disable_1920_1080_60fps = 1
enable_mouse_keyboard = 1

display_power_management = 0

####################################################

parser = argparse.ArgumentParser()
parser.add_argument('arg1', nargs='?', default='192.168.173.80')
args = parser.parse_args()
sourceip = vars(args)['arg1']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sourceip, 7236)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

connectcounter = 0
while True: 
	try:
		sock.connect(server_address)
	except socket.error as e:
		#connectcounter = connectcounter + 1
		#if connectcounter == 3:
		sock.close()
		sys.exit(1)
	else:
		break

cpuinfo = os.popen('grep Hardware /proc/cpuinfo')
cpustr = cpuinfo.read()
runonpi = 'BCM2835' in cpustr or 'BCM2711' in cpustr
cpuinfo.close()


data = sock.recv(1000)
data = data.decode()
print("M1:")
print(data)
s_data = 'RTSP/1.0 200 OK\r\nCSeq: 1\r\nPublic: org.wfa.wfd1.0, SET_PARAMETER, GET_PARAMETER\r\n\r\n'
print('Response:')
print(s_data)
sock.sendall(s_data.encode())


# M2
s_data = 'OPTIONS * RTSP/1.0\r\nCSeq: 1\r\nRequire: org.wfa.wfd1.0\r\n\r\n'
print("M2:")
print(s_data)
sock.sendall(s_data.encode())

data = sock.recv(1000)
data = data.decode()
print('Response:')
print(data)
m2data = data


# M3
data = sock.recv(1000)
data = data.decode()
print("M3:")
print(data)

msg = 'wfd_client_rtp_ports: RTP/AVP/UDP;unicast 1028 0 mode=play\r\n'
if player_select == 2:
	msg = msg + 'wfd_audio_codecs: LPCM 00000002 00\r\n'
else:
	msg = msg + 'wfd_audio_codecs: AAC 00000001 00\r\n'

if disable_1920_1080_60fps == 1:
	msg = msg + 'wfd_video_formats: 00 00 02 10 0001FEFF 3FFFFFFF 00000FFF 00 0000 0000 00 none none\r\n'
else:
	msg = msg + 'wfd_video_formats: 00 00 02 10 0001FFFF 3FFFFFFF 00000FFF 00 0000 0000 00 none none\r\n'

msg = msg +'wfd_3d_video_formats: none\r\n'\
	+'wfd_coupled_sink: none\r\n'\
	+'wfd_connector_type: 05\r\n'\
	+'wfd_uibc_capability: input_category_list=GENERIC, HIDC;generic_cap_list=Keyboard, Mouse;hidc_cap_list=Keyboard/USB, Mouse/USB;port=none\r\n'\
	+'wfd_standby_resume_capability: none\r\n'\
	+'wfd_content_protection: none\r\n'


# if runonpi and not os.path.exists('edid.txt'):
# 		os.system('tvservice -d edid.txt')

# edidlen = 0
# if os.path.exists('edid.txt'):
# 	edidfile = open('edid.txt','r')
# 	lines = edidfile.readlines()
# 	edidfile.close()
# 	edidstr =''
# 	for line in lines:
# 		edidstr = edidstr + line
# 	edidlen = len(edidstr)

# if 'wfd_display_edid' in data and edidlen != 0:
# 	msg = msg + 'wfd_display_edid: ' + '{:04X}'.format(edidlen/256 + 1) + ' ' + str(edidstr.encode('utf-8').hex())+'\r\n'

# if 'microsoft_latency_management_capability' in data:
# 	msg = msg + 'microsoft-latency-management-capability: supported\r\n'
# if 'microsoft_format_change_capability' in data:
# 	msg = msg + 'microsoft_format_change_capability: supported\r\n'

if 'intel_friendly_name' in data:
	msg = msg + 'intel_friendly_name: raspberrypi\r\n'
if 'intel_sink_manufacturer_name' in data:
	msg = msg + 'intel_sink_manufacturer_name: lazycast\r\n'
if 'intel_sink_model_name' in data:
	msg = msg + 'intel_sink_model_name: lazycast\r\n'
# if 'intel_sink_version' in data:
# 	msg = msg + 'intel_sink_version: 20.4.26\r\n'
if 'intel_sink_device_URL' in data:
	msg = msg + 'intel_sink_device_URL: https://github.com/homeworkc/lazycast\r\n'




m3resp ='RTSP/1.0 200 OK\r\nCSeq: 2\r\n'+'Content-Type: text/parameters\r\nContent-Length: '+str(len(msg))+'\r\n\r\n'+msg
print('Response:')
print(m3resp)
sock.sendall(m3resp.encode())


# M4
data = sock.recv(1000)
data = data.decode()
print('M4')
print(data)

s_data = 'RTSP/1.0 200 OK\r\nCSeq: 3\r\n\r\n'
print(s_data)
sock.sendall(s_data.encode())

# def uibcstart(sock, data):
# 	#print data
# 	data = data.decode()
# 	messagelist=data.split('\r\n\r\n')
# 	for entry in messagelist:
# 		if 'wfd_uibc_capability:' in entry:
# 			entrylist = entry.split(';')
# 			uibcport = entrylist[-1]
# 			uibcport = uibcport.split('\r')
# 			uibcport = uibcport[0]
# 			uibcport = uibcport.split('=')
# 			uibcport = uibcport[1]
# 			print('uibcport:'+uibcport+"\n")
# 			if 'none' not in uibcport and enable_mouse_keyboard == 1:
# 				os.system('pkill control.bin')
# 				os.system('pkill controlhidc.bin')
# 				if('hidc_cap_list=none' not in entry):
# 					os.system('./control/controlhidc.bin '+ uibcport + ' ' + sourceip + ' &')
# 				elif('generic_cap_list=none' not in entry):
# 					os.system('./control/control.bin '+ uibcport + ' &')

# uibcstart(sock,data)

def killall(control):
        os.system('pkill vlc')
        if display_power_management == 1:
                os.system('vcgencmd display_power 0')

# M5
data = sock.recv(1000)
data = data.decode()
print('M5')
print(data)

s_data = 'RTSP/1.0 200 OK\r\nCSeq: 4\r\n\r\n'
print(s_data)
sock.sendall(s_data.encode())


# M6
m6req ='SETUP rtsp://'+sourceip+'/wfd1.0/streamid=0 RTSP/1.0\r\n'\
+'CSeq: 5\r\n'\
+'Transport: RTP/AVP/UDP;unicast;client_port=1028\r\n\r\n'
print('M6')
print(m6req)
sock.sendall(m6req.encode())

data = sock.recv(1000)
data = data.decode()
print(data)

paralist=data.split(';')
print(paralist)
serverport=[x for x in paralist if 'server_port=' in x]
print(serverport)
serverport=serverport[-1]
serverport=serverport[12:17]
print(serverport)

paralist=data.split( )
position=paralist.index('Session:')+1
sessionid=paralist[position]


# M7
m7req ='PLAY rtsp://'+sourceip+'/wfd1.0/streamid=0 RTSP/1.0\r\n'\
+'CSeq: 6\r\n'\
+'Session: '+str(sessionid)+'\r\n\r\n'
print("<---M7---\n" + m7req)
sock.sendall(m7req.encode())

data = sock.recv(1000)
data = data.decode()
print(data)

print("---- Negotiation successful ----")


player_select = 0

def launchplayer(player_select):
	
	#os.system('nc -u -l 1028 > test.ts')
	#os.system('gst-launch-1.0 -v udpsrc port=1028 ! tsdemux name=d !  h264parse ! queue ! v4l2h264dec capture-io-mode=4 ! kmssink d. ! queue ! decodebin ! audioconvert ! audioresample ! alsasink &')
	#os.system('gst-launch-1.0 -v udpsrc port=1028  ! tsparse set-timestamps=true ! tsdemux name=d !  h264parse ! queue ! v4l2h264dec capture-io-mode=4 ! kmssink  &')
	os.system('vlc --fullscreen rtp://0.0.0.0:1028/wfd1.0/streamid=0 --intf dummy --no-ts-trust-pcr --ts-seek-percent --network-caching=100 --no-mouse-events & ')
	# os.system('gst-launch-1.0  -v  playbin   uri=udp://0.0.0.0:1028/wfd1.0/streamid=0  video-sink=autovideosink audio-sink=alsasink sync=false &')
	# # os.system('gst-launch-1.0 -v udpsrc port=1028 ! application/x-rtp,media=video,encoding-name=H264 ! queue ! rtph264depay ! avdec_h264 ! autovideosink &')
	# # os.system('gst-launch-1.0 -v udpsrc port=1028 ! video/mpegts ! tsdemux !  h264parse ! queue ! avdec_h264 ! ximagesink sync=false &')
	# # os.system('gst-launch-1.0  -v  playbin   uri=udp://0.0.0.0:1028/wfd1.0/streamid=0  video-sink=ximagesink audio-sink=alsasink sync=false &')
	# # os.system('gst-launch-1.0  -v  playbin   uri=udp://0.0.0.0:1028/wfd1.0/streamid=0  video-sink=xvimagesink audio-sink=alsasink sync=false &')
	# if True:
	#os.system('gst-launch-1.0  -v  playbin   uri=udp://0.0.0.0:1028/wfd1.0/streamid=0  video-sink=kmssink audio-sink=alsasink sync=true &')
	# else:
	# 	os.system('vlc --fullscreen rtp://0.0.0.0:1028/wfd1.0/streamid=0 --intf dummy --no-ts-trust-pcr --ts-seek-percent --network-caching=300 --no-mouse-events & ')


launchplayer(player_select)



csnum = 102
while True:
	data = sock.recv(1000)
	data = data.decode()
	print(data)
	watchdog = 0
	if len(data)==0 or 'wfd_trigger_method: TEARDOWN' in data:
		killall(True)
		sleep(1)
		break
	elif 'wfd_video_formats' in data:
		launchplayer(player_select)
	messagelist=data.split('\r\n\r\n')
	print(messagelist)
	singlemessagelist=[x for x in messagelist if ('GET_PARAMETER' in x or 'SET_PARAMETER' in x )]
	print(singlemessagelist)
	for singlemessage in singlemessagelist:
		entrylist=singlemessage.split('\r')
		for entry in entrylist:
			if 'CSeq' in entry:
				cseq = entry

		resp='RTSP/1.0 200 OK\r'+cseq+'\r\n\r\n';#cseq contains \n
		print(resp)
		sock.sendall(resp.encode())
	
	# uibcstart(sock,data)


sock.close()



