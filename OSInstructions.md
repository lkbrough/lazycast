1. Take the SD Card out of the bottom of the Raspberry Pi and insert it into an SD Card reader. It's a microSD card so you might need an adapter.
2. Run Raspberry Pi Imager [Link](https://www.raspberrypi.com/software/) 
![](/images/rpiImager.png)
3. Choose "Raspberry Pi OS (Legacy)" as the OS to install. 
![](/images/other.png) 
![](/images/version.png)
4. Choose the SD Card you want to write to. NOTE: Make sure to select the SD Card! You can badly damage a computer if you select the wrong one! In the example image, I choose Kingston as that is the brand of my SD Card reader. The size of the SD Card is 64 GB if that helps identify the right device. 
![](/images/SDCard.png)
5. Once you are confident in your choices, click write and wait until it finishing writing and verifying.
6. Put the SD Card back in the Raspberry Pi and power it on. Give it a few minutes to power on until it gets to this screen. 
![](/images/raspberryPi.png)
7. Follow the basic setup selecting US, American English, and Chicago timezone. Check off to use English language and US Keyboard. Click next. 
![](/images/countrySetup.png)
8. Set the password to be our usual password. Check with another member of the media team if you are not sure what to set as the usual password. Click next. 
![](/images/passwordSet.png)
9. If the pi shows a black border around the screen (most of the time, it will), check off the box on the next screen. The black border is shown in the first image and the one below. Click next. 
![](/images/blackBorder.png)
10. Ideally, these steps should be done at church, therefore for the internet step, login to the Admin network. If done at a house, login to your personal wifi or plug in an ethernet cable to the raspberry pi. If you have no internet or will let it update at church later, skip this step by pressing skip. To complete it, click next. 
![](/images/internet.png) Once signed in, the raspberry pi will update. It can take a while so it's better to do it on a faster internet connection like the church's. Click next to update it and let it sit while updating. 
![](/images/update.png)
11. Click Restart to restart the Pi. Give it a few moments to restart. 
![](/images/restart.png)
12. Rename the Raspberry Pi so we don't confuse them if we get more RPis in the future. Choose the name based on the usage and location. Ideally, keep Pi in the name so it can be easily identified as a pi. This one is setup as the audience projector Pi so it'll be named appropriately. Under the raspberry pi menu, under preferences, choose Raspberry Pi Configuration. 
![](/images/rpirename.png)
13. Set the hostname to what was decided. 
![](/images/hostname.png)
14. Switch to the display tab and set screen blanking to disable to ensure the Pi does not go to sleep while running. Click OK and choose to reboot the device now. 
![](/images/screenBlankingDisable.png) 
![](/images/restart2.png)
14. Continue with the steps in the setupInstructions.md