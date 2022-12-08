1. Follow the OS Instructions first to reinstall the Raspberry Pi OS
2. Open a terminal.
3. Clone this repo to the raspberry pi. `git clone https://github.com/lkbrough/lazycast.git`
4. Go into the new 'lazycast directory' `cd lazycast`
5. Run the install.sh script. You will have to type Y for yes a few times to agree to using space on the rpi a few times. `./install.sh`
6. The device will reboot when this script is finished running, let it come up as expected.
![](/images/cloneandinstall.png)
7. Once it comes back up, you'll need to reconnect it to the internet if you're on wifi. Part of the last step installed a new network manager and uninstalled the base one. We'll remove the old icon to make it clear which is the real internet icon. Right click the top bar close to the icons on the right side and choose Add/Remove Panel Items. Remove the Wireless & Wired Network by selecting it and clicking remove.
![](/images/removeNetwork.png)
8. Open up a terminal, go back into lazycast, and run the setup.sh script. 
```
cd lazycast
./setup.sh
```
9. Once it's finished, go back to the home directory and try running the start-windows-projector. `./start-windows-projector` and connect a computer to it to check.