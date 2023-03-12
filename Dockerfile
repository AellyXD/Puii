'FROM aellyxd/puii:main

# set timezone

ENV TZ=Asia/Kolkata

# Railway's banned dependency

RUN if [ ! $RAILWAY_STATIC_URL ]; then pip3 install --no-cache-dir yt-dlp; fi

# changing workdir
# changing workdir
# changing workdir
