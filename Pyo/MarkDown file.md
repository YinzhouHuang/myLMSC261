# MarkDown

- I was stuck installing the poy. I followed the steps Rachel provided until I got to the last step which was "sudo python3 setup.py install --use-coreaudio -debug". But all I get is a big error report. These include the following examples.

src/engine/ad_coreaudio.c:132:21: error: implicit declaration of function 'AudioGetCurrentHostTime' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
    now.mHostTime = AudioGetCurrentHostTime();
    36 warnings and 1 error generated.
    error: command '/usr/bin/gcc' failed with exit code 1

- Then I tried to Google for help, but there was no answer that worked. I also tried re-updating python and the computer system version, but always the same problem. I'm lost and don't know what to do to fix it.
